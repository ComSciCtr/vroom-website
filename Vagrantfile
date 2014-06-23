# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "precise32"

  config.vm.synced_folder "srv/", "/srv/"

  config.vm.provision :salt do |salt|
     salt.minion_config = "srv/minion"
     salt.run_highstate = true
     salt.verbose = true
  end

  config.vm.network :forwarded_port, host: 4567, guest: 4567

end

