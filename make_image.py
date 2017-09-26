#!/usr/bin/env python3
# coding=utf-8

__author__ = 'chentf'

__version__ = 'v1.0.0'

import sys
import paramiko
import scpclient
from contextlib import closing


def ssh(host, username, private_key_path):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, key_filename=private_key_path)
    return ssh


def scp(ssh, resource, target, floder):
    with closing(scpclient.Write(ssh.get_transport(), floder)) as scp:
        scp.send_file(resource, True, remote_filename=target)


def generate_docker_file(port, jar_name, yml):
    fp = open("Dockerfile", "w")
    fp.write("FROM 192.168.59.163:5000/java" + "\n")
    fp.write("EXPOSE " + port + "\n")
    fp.write("ADD " + jar_name + " /home" + "\n")
    fp.write(
        'CMD ["java", "-jar","/home/eureka-server-1.0.0.jar","--spring.config.location=classpath:' + yml + '"]' + "\n")


def exec_commands(ssh, cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    results = stdout.read()
    print (results)
    return results


if __name__ == '__main__':
    # 获取ssh
    # SSH私钥匙
    private_key_path = sys.argv[1]
    # jar包的位置
    jar_file = sys.argv[2]
    # 目标文件夹 ~目录为基础
    target_floder = sys.argv[3]
    # 目标文件
    target_file = sys.argv[4]
    # 端口
    port = sys.argv[5]
    # 编写docker时候的jar-name
    jar_name = target_file
    # yml路径地址
    yml = sys.argv[6]
    # 镜像名字
    image_name = sys.argv[7]

    # ssh到目标服务
    ssh1 = ssh("192.168.59.163", "root", private_key_path)

    # todo 判断文件夹是否存在

    # scp文件到文件夹
    scp(ssh1, jar_file, target_file, target_floder)

    # 编写docker file
    generate_docker_file(port, jar_name, yml)
    # 把docker file 扔到服务器去
    scp(ssh1, "Dockerfile", "Dockerfile", target_floder)

    # 制作镜像
    exec_commands(ssh1, "docker build -t 192.168.59.163:5000/" + image_name + " " + target_floder)

    # push镜像
    exec_commands(ssh1, "docker push 192.168.59.163:5000/" + image_name)

    ssh1.close()

    # ssh到192.168.59.164上
    ssh2 = ssh("192.168.59.164", "root", private_key_path)

    # 停止容器
    exec_commands(ssh2, "docker stop " + image_name)

    # 删除容器
    exec_commands(ssh2, "docker rm " + image_name)

    # 删除镜像
    exec_commands(ssh2, "docker rmi 192.168.59.163:5000/" + image_name)

    # pull镜像
    exec_commands(ssh2, "docker pull 192.168.59.163:5000/" + image_name)

    # 运行镜像
    exec_commands(ssh2,
                  "docker run -d -p " + port + ":" + port + " --name " + image_name + " 192.168.59.163:5000/" + image_name)

    print ("hello,world")
