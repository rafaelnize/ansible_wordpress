#!/bin/bash


sudo apt-get update
sudo apt-get -y install python python-dev python-pip python-software-properties libssl-dev
sudo apt-get -y install httplib2 Jinja2 paramiko
sudo pip install --upgrade ansible
