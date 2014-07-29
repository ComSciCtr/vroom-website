Documentation website for [vroom][vroom] built using [Middleman][middleman].

[vroom]: https://github.com/comscictr/vroom
[middleman]: http://middlemanapp.com


### Basic Editing

The documentation pages are generated directly from markdown files in
`source/documentation/`. Each markdown file maps directly to an html file on
the website. For example, the website is currently being hosted on 
[github pages][vroom-website], so the documentation for the `cube()` function
([http://comscictr.github.io/vroom/documentation/rendering/cube.html](http://comscictr.github.io/vroom/documentation/rendering/cube.html))
is generated from the file `source/documentation/rendering/cube.html.md.erb`.

For basic modifications to the site content the easiest method is to clone this
repository, edit the markdown file(s), and then make a [pull request][pull-request].
If you want to make more substantial changes to the site see the following 
sections.

[vroom-website]: https://comscictr.github.io/vroom
[pull-request]: https://github.com/vroom-website/pulls


### Setting Up Vagrant

The preferred method for building the website is to use [Vagrant][vagrant]. If
you do not already have Vagrant installed on your computer you can download it
[here][vagrant-downloads]. You will also need to to install a provider
(VirtualBox, VMWare, etc.). If you do not have one already installed do that
now.

```sh
sudo apt-get install virtualbox
```

Once you have vagrant (and a provider) installed, you need to install the base box.

```sh
vagrant box add ubuntu/trusty64
```

Then bring up the virtual machine.

```sh
vagrant up
```

The first time the virtual machine is launched the development environment will
automatically set up. A web server should be running on port `4567`. You can  
verify that everything is running correctly by opening
 [http://localhost:4567](http://localhost:4567) in your web browser.

Once the machine has finished booting you can SSH into it by running `vagrant
ssh`. When you are finished, the machine can be shutdown with `vagrant halt`.
If you no longer need the virtual machine (or want to free up space) you can
delete it with `vagrant destroy`.

See the [Vagrant documentation][vagrant-docs] for more information.

[vagrant]: http://vagrantup.com
[vagrant-downloads]: http://vagrantup.com/downloads.html
[vagrant-providers]: http://docs.vagrantup.com/v2/providers/index.html
[vagrant-docs]: http://docs.vagrantup.com/v2/getting-started/index.html


### Development with Middleman

This section assumes that you are using Vagrant as outlined in the previous
section.

Since Middleman is installed only in the virtual machine we first need to SSH
in and then change to the project directory. Project directories (the ones
with the `Vagrantfile`) are automatically mapped to `/vagrant`.

```sh
vagrant ssh
cd /vagrant
```

Once we are in the project directory on the VM we can use `middleman` to build
the site.

```sh
bundle exec middleman build
```

The site can be deployed in a similar manner. The default deployment is to 
github-pages and requires write access on the [ComSciCtr][comscictr] account.

```sh
bundle exec middleman deplay
```

[comscictr]: https://github.com/comscictr


Calling `bundle exec middleman` with no additional arguments will start a 
preview server on port `4567`.


### Generating Screenshots

The `tools/` directory contains scripts for automatically generating 
screenshots from the code examples in the documentation. The markdown files in
`source/documentation/` are parsed and the code fragments are used to create
valid vroom programs. The programs are then run and a screenshot is taken. The
location of the window can depend on the desktop environment so some variables
in the file may need to be changed depending on your particular setup.

You will of course need vroom installed, as well as some additional utilities.

```sh
sudo apt-get install scrot imagemagick
```

