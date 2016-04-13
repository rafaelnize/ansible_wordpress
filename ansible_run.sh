#!/bin/bash

ansible all -m ping -u root -k
ansible-playbook -i inventory site.yml
