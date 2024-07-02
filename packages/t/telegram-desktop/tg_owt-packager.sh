#! /bin/bash

# tg_owt origin
# get it from https://github.com/telegramdesktop/tdesktop/blob/dev/Telegram/build/docker/centos_env/Dockerfile around line 761
tg_owt_origin="c9cc4390ab951f2cbc103ff783a11f398b27660b"

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
