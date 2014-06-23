rvm-depends:
  pkg.installed:
    - names:
      - build-essential
      - curl

ruby-1.9.3:
  rvm.installed:
    - default: True
    - require:
       - pkg: rvm-depends
