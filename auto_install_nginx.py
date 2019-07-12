#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 此脚本已在CentOS 7 上测试通过
# 作者：H&C

import subprocess

def install_pcre():
    '''
    这是一个安装PCRE的函数
    :return:
    '''
    while 1:
        install_res = subprocess.call('yum install -y pcre pcre-devel',shell=True)
        if install_res == 0:
            break

def install_openssl():
    '''
    这是一个安装OpenSSl的函数
    :return:
    '''
    while 1:
        install_res = subprocess.call('yum install -y openssl openssl-devel',shell=True)
        if install_res == 0:
            break

def install_depended_upon():
    '''
    这是一个安装Nginx依赖的函数
    :return:
    '''
    while 1:
        install_res = subprocess.call('yum install -y gcc gcc-c++ kernel-devel',shell=True)
        if install_res == 0:
            break

def install_Nginx():
    '''
    这是一个安装Nginx的函数
    :return:
    '''
    #指定Nginx的版本
    nginx_version = 'nginx-1.16.0'
    #指定Nginx的安装目录
    nginx_dir = '/opt/Nginx/'

    #下载Nginx安装包
    subprocess.call('wget http://nginx.org/download/{}.tar.gz -P /opt/'.format(nginx_version),shell=True)
    #解压Nginx安装包
    subprocess.call('tar -zxf /opt/{}.tar.gz -C /opt/'.format(nginx_version),shell=True)
    #指定安装路径、用户和所需模块
    subprocess.call('cd /opt/{}/ && ./configure --prefix={} --user=nginx --group=nginx '
                    '--with-http_ssl_module '
                    '--with-http_stub_status_module'.format(nginx_version,nginx_dir),shell=True)
    #创建nginx用户和组
    subprocess.call('useradd nginx -M -s /sbin/nologin',shell=True)
    #编译安装Nginx
    subprocess.call('make -C /opt/{}/ && make install -C /opt/{}/'.format(nginx_version,nginx_version),shell=True)
    #启动Nginx服务
    subprocess.call('{}sbin/nginx'.format(nginx_dir),shell=True)

def open_firewall():
    '''
    这是一个开放防火墙端口的函数
    :return:
    '''
    #开放防火墙80端口
    subprocess.call('firewall-cmd --zone=public --add-port=80/tcp --permanent',shell=True)
    #重启防火墙服务
    subprocess.call('firewall-cmd --reload',shell=True)

if __name__ == '__main__':
    install_pcre()
    install_openssl()
    install_depended_upon()
    install_Nginx()
    open_firewall()
