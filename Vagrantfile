# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
$bootstrap=<<SCRIPT
sudo apt-get update
sudo apt-get -y install python python-dev python-pip python-software-properties libssl-dev
sudo apt-get -y install httplib2 Jinja2 paramiko
sudo pip install --upgrade ansible
SCRIPT


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
config.vm.box = "ubuntu/trusty64"

  if Vagrant.has_plugin?("vagrant-cachier")

   # Configure cached packages to be shared between instances of the same base box.
   # More info on http://fgrehm.viewdocs.io/vagrant-cachier/usage
     config.cache.scope = :box

   # OPTIONAL: If you are using VirtualBox, you might want to use that to enable
   # NFS for shared folders. This is also very useful for vagrant-libvirt if you
   # want bi-directional sync
   config.cache.synced_folder_opts = {
     type: :rsync,
     # The nolock option can be useful for an NFSv3 client that wants to avoid the
     # NLM sideband protocol. Without this option, apt-get might hang if it tries
     # to lock files needed for /var/cache/* operations. All of this can be avoided
     # by using NFSv4 everywhere. Please note that the tcp option is not the default.
     mount_options: ['rw', 'vers=3', 'tcp', 'nolock']
   }
   # For more information please check http://docs.vagrantup.com/v2/synced-folders/basic_usage.html
 end

config.vm.network "private_network", ip: "192.168.33.26"
config.vm.provider "virtualbox" do |vb|
vb.customize ["modifyvm", :id, "--memory", "1024"]
end
#config.vm.provision :shell, inline: "apt-get update"
config.vm.provision :shell, inline: $bootstrap
#config.vm.synced_folder "run/", "/home/vagrant/run/", type: "rsync", create: true
#config.vm.provision "file", source: "run/Dockerfile", destination: "/home/vagrant/run/Dockerfile"
#config.vm.synced_folder "secrets/", "/home/vagrant/secrets/", type: "rsync", create:true
#config.vm.provision :shell, inline: "docker build -t mlgexpress:v01 ."
#config.vm.provision :shell, inline: "docker run -d -p 8080:8080 -t mlgexpress:v01"
end
