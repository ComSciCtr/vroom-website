middleman-depends:
   pkg:
      - installed
      - names:
         - build-essential
         - ruby-dev
         - nodejs

middleman:
  gem.installed:
    - require:
       - pkg: middleman-depends

bundler:
  gem.installed
