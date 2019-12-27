# WebSSH

## 简介
* 项目背景：vpn建立连接后从web页面进行访问时，针对用户进行 `命令权限` 设置
* 源码路径：[WebSSH](https://github.com/huashengdun/webssh)
* command.yaml：输入命令白名单
## 部署：
* docker部署
  * 环境依赖：docker，docker-compose
  * git clone http://git.wiwide.com/udp/web-ssh.git
  * cd web-ssh
  * 编译：docker-compose build
  * 启动：docker-compose up -d
  * 重启：docker-compose restart
  * 临时修改文件后，需要重启编译在重启
  * 部署完成后，页面访问8567端口，
* 常规部署：
  * 代码路径：/home/prod/deploys/webssh
  * 创建虚拟环境：mkvirtualenv webssh
  * 在虚拟环境中，定位到项目目录，执行pip install -r requestments.txt
  * 将webssh.ini 放入 /home/prod/deploys/supervisor.d，执行supervisorctl reload
  * 状态查看：supervisorctl status webssh
  
## vpn测试机：
* 任意安装wget、openvpn的Linux环境下
* wget http://188.131.217.188:4200/188.131.217.188/client.tar
* tar -zxvf client.tar;openvpn client.conf
* 浏览器访问：http://188.131.217.188:8567/，输入主机名、用户名、密码登录
