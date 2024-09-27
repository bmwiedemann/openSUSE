#! /bin/bash

# ada version
# https://github.com/telegramdesktop/tdesktop/blob/dev/Telegram/build/docker/centos_env/Dockerfile#L799
rm -rf ada \
  && git clone -b v2.9.0 --depth=1 https://github.com/ada-url/ada.git \
  && cd ada \
  && rm -rf .git \
  && cd .. \
  && mv ada ada-v2.9.0 \
  && zip ada-v2.9.0.zip -r ada-v2.9.0 -x '*.git*' \

rm -rf ada-v2.9.0
