#! /bin/bash

# tg_owt origin
# get it from https://github.com/telegramdesktop/tdesktop/blob/dev/Telegram/build/docker/centos_env/Dockerfile around line 823
tg_owt_origin="afd9d5d31798d3eacf9ed6c30601e91d0f1e4d60"

rm -rf tg_owt \
  && mkdir tg_owt \
  && cd tg_owt \
  && git init tg_owt \
  && cd tg_owt \
  && git remote add origin https://github.com/desktop-app/tg_owt.git \
  && git fetch --depth=1 origin "$tg_owt_origin" \
  && git reset --hard FETCH_HEAD \
  && git submodule update --init --recursive --depth=1 \
  && rm -rf .git \
  && cd .. \
  && mv tg_owt tg_owt-master \
  && zip tg_owt-master.zip -r tg_owt-master -x '*.git*' \
  && mv tg_owt-master.zip ..

cd ..; rm -rf tg_owt
