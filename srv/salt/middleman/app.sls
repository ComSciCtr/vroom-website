screen:
  pkg.installed

init-app:
  cmd.run:
    - name: bash -lc 'rvm 1.9.3 do bundle install'
    - cwd: /vagrant/{{ pillar['site']['root'] }}/
    - require:
      - rvm: ruby-1.9.3
      - gem: middleman
      - gem: bundler

start-app:
  cmd.run:
    - name: bash -lc 'screen -dmS newscreen nohup middleman --force-polling'
    - cwd: /vagrant/{{ pillar['site']['root'] }}/
    - require:
      - cmd.run: init-app
      - pkg: screen
