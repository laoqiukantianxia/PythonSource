import os
import threading
from concurrent.futures import ProcessPoolExecutor, as_completed, wait, ALL_COMPLETED
import time

# 系统启动一个新线程的成本是比较高的，因为它涉及与操作系统的交互。
# 在程序中需要创建大量生存期很短的线程时，使用线程池可以很好的提升性能。

# 此外，使用线程池可以有效地控制系统中并发线程的数量。当系统中包含有大量的并发线程时，会导致系统性能急剧下降，
# 甚至导致 Python 解释器崩溃，而线程池的最大线程数参数可以控制系统中并发线程的数量不超过此数。

# step：
# 1. 实例化ThreadPoolExecutor类创建线程池
# 2. 定义普通函数作为线程任务
# 3. 调用ThreadPoolExecutor的submit()方法提交线程任务
def get_html(times):
    time.sleep(times)
    print('{} get page {}s finished'.format(os.getpid(), times))
    return times

if __name__ == '__main__':
    # max_workers:线程池最大并发线程数,
    # 若参数为空，默认为cpu核数:os.cpu_count()
    executor = ProcessPoolExecutor(max_workers=2)

    # 通过submit函数提交执行的函数到线程池，submit函数立即返回，不阻塞
    task1 = executor.submit(get_html, (3))
    task2 = executor.submit(get_html, (2))

    # done方法判断任务是否完成
    print(task1.done())
    # result方法获取任务执行的结果
    print(task1.result())
    # cancel方法用于取消某个任务,该任务没有放入线程池中才能取消成功
    print(task1.cancel())

    # as_completed:等任务结束后，再去获取结果
    # as_completed()返回一个生成器，任务没有完成时会阻塞；
    # 当某个任务完成时，会yield这个任务，然后继续阻塞住
    urls = [3, 2, 1]

    # 返回结果按照子进程结束的先后顺序，不可控
    all_tasks = [executor.submit(get_html, (url)) for url in urls]

    # 返回结果按照列表顺序
    #all_tasks = [executor.map(get_html, (url)) for url in urls]

    # wait方法：可以让主线程阻塞，直到满足设定的要求
    wait(all_tasks, return_when=ALL_COMPLETED)
    print('main')

    # for future in as_completed(all_tasks):
    #     data = future.result()
    #     print('in main:get page {}s success'.format(data))


