supergit -- 

````
# what repos are not mine?

mh> supergit notmine
ArduinoNunchuk    remote.origin.url=https://github.com/GabrielBianconi/ArduinoNunchuk.git
arduino-nrf24l01  remote.origin.url=https://github.com/aaronds/arduino-nrf24l01.git
avrlibraries      remote.origin.url=https://github.com/bradquick/avrlibraries.git
aws-cli           remote.origin.url=https://github.com/aws/aws-cli.git
aws-python-sample remote.origin.url=https://github.com/awslabs/aws-python-sample.git
bradwii           remote.origin.url=https://github.com/bradquick/bradwii.git
sphinx_rtd_theme  remote.origin.url=https://github.com/snide/sphinx_rtd_theme.git

# what repos need a push or a pull?

mh@thunderstorm ~ --> supergit needspush
ArduinoNunchuk    Your branch is ahead of 'origin/master' by 1 commit.
mailtools         Your branch is ahead of 'origin/master' by 1 commit.
sundries          Your branch is ahead of 'origin/master' by 1 commit.
testing           Your branch is ahead of 'origin/master' by 2 commits.

# what repos need attention?

$ supergit attention
multiwii_hk328p   =====================================================
sphinx_rtd_theme  =====================================================
sqlminus          =====================================================
sundries           M bin/supergit
sundries          A  bin/README.md
sundries          Your branch is ahead of 'origin/master' by 1 commit.
termtile          =====================================================
testing           =====================================================
testing           Your branch is ahead of 'origin/master' by 2 commits.
tufte-css         =====================================================
wiichuck_adapter  =====================================================

$ supergit attention -q
ArduinoNunchuk    Your branch is ahead of 'origin/master' by 1 commit.
mailtools         Your branch is ahead of 'origin/master' by 1 commit.
private            M paws/src/awsh
private            M paws/src/awshelpers.py
private            M paws/src/instance-watcher
private           ?? paws/src/out
private           Your branch is ahead of 'origin/master' by 2 commits.
sundries           M bin/supergit
sundries          Your branch is ahead of 'origin/master' by 2 commits.
testing           Your branch is ahead of 'origin/master' by 2 commits.
````
