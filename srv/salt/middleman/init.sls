nodejs:
  pkg.installed

middleman:
  gem.installed:
    - ruby: 1.9.3
    - require:
      - rvm: ruby-1.9.3
      - pkg: nodejs

bundler:
  gem.installed:
    - ruby: 1.9.3
    - require:
      - rvm: ruby-1.9.3
