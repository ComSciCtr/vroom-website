screen:
  pkg.installed

init-app:
  cmd.run:
    - name: bundle install
    - cwd: /vagrant/{{ pillar['site']['root'] }}/
    - require:
      - gem: middleman
      - gem: bundler

start-app:
  cmd.run:
    - name: bash -lc 'screen -dmS newscreen nohup middleman --force-polling'
    - cwd: /vagrant/{{ pillar['site']['root'] }}/
    - require:
      - cmd: init-app
      - pkg: screen
