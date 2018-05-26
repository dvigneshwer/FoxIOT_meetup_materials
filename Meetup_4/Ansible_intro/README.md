# Ansible - Introduction

## What is Ansible ?

Ansible is a configuration management tool by redhat.

## What is configuration management ?

* Configuration management (CM) is the detailed recording and updating of information that describes an projects hardware and software.

* Helps the project managers to push new updates to products.

## How does it Work ?

* It uses SSH to connect to servers and run the configured Tasks.

* Ansible uses "Facts", which is system and environment information it gathers ("context") before running Tasks.

## Why do we use Ansible ?

* administering source code
* producing software development builds
* controlling change, and managing software configurations.

For IOT uses cases,

* Adding new machines to Cloud architectures/builds
* Pushing in New features and updates

## Installing Ansible 
~~~~
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
~~~~

## Listing Pi-Board dependencies

* gpio 
* numpy
* beautifulsoup
* Pillow

## Installation of pi modules 
~~~~
# gpio
sudo apt-get install python-rpi.gpio 
or
pip install RPi.GPIO

# numpy
sudo apt-get install python-numpy
or
pip install numpy

# beautifulsoup
apt-get install python-bs4
or 
pip install beautifulsoup4

# Pillow
pip install Pillow

<<<<<<< HEAD
# pyqt
sudo apt-get install python-qt4
or
pip install PyQt

=======
<<<<<<< HEAD
>>>>>>> lokeshwaran97-patch-1
# Panda
apt-get install python-pandas
or
yum install python-pandas
<<<<<<< HEAD
=======
=======
# pyqt
sudo apt-get install python-qt4
or
pip install PyQt
>>>>>>> 0ce39e2e29ef6af620f5c5c02b73e31a2ce7fe75
>>>>>>> lokeshwaran97-patch-1

~~~~

## Pre-requistes

* Editing Ansible configurations
~~~~
sudo mv /etc/ansible/hosts /etc/ansible/hosts.orig
~~~~

* Changes in hosts file
~~~~
[local]
127.0.0.1 ansible_ssh_user=viki
~~~~

* viki is the username with which the ansible ssh to the particular machine

* Check connection
~~~~
ansible -m ping local

# Response 
127.0.0.1 | SUCCESS => {
    "changed": false, 
    "ping": "pong"
}
~~~~

* -m stands for module
* ping is a module to check for connection
* local is the entry of the list of servers names in the hosts file

## Ansible playbooks
~~~~
# create a file pi_dependencies.yml
touch pi_dependencies.yml
~~~~

* Contents of the file
~~~~
---
- hosts: local
  tasks:
   - name: Install Numpy
     apt: pkg=python-numpy state=installed update_cache=true

   - name : Install GPIO
   	 apt: pkg=python-rpi.gpio state=installed update_cache=true
~~~~

## Steps to run playbook ?

* Create password less ssh
~~~~
# Copy the public key to the other machine
ssh-copy-id viki@localhost

# Try ssh - you can access without password
ssh viki@localhost
~~~~

* Run the playbook
~~~~
ansible-playbook -s pi_dependencies.yaml
~~~~
* -s stands for sudo user

## Sample Output

~~~~

~~~~

## Reference Links :

* [Installation](http://docs.ansible.com/ansible/intro_installation.html)
* [Tutorials](https://serversforhackers.com/an-ansible-tutorial)

