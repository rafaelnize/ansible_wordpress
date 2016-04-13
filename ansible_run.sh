#!/bin/bash

ansible all -m ping -u root
ansible-playbook -i inventory site.yml
