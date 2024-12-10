#! /bin/bash

# tg_owt origin
# get it from https://github.com/telegramdesktop/tdesktop/blob/dev/Telegram/build/docker/centos_env/Dockerfile around line 761
tg_owt_origin="8198c4d8b91e22d68eb5c7327fd408e3b6abcc79"

rm -rf tg_owt \
  && mkdir tg_owt \
  && cd tg_owt \
  && git init tg_owt \
  && cd tg_owt \
  && git remote add origin https://github.com/xuzhao9/tg_owt.git \
  && git fetch --depth=1 origin "$tg_owt_origin" \
  && git reset --hard FETCH_HEAD \
  && git submodule update --init --recursive --depth=1 \
  && rm -rf .git \
  && cd .. \
  && mv tg_owt tg_owt-master \
  && zip tg_owt-master.zip -r tg_owt-master -x '*.git*' \
  && mv tg_owt-master.zip ..

cd ..; rm -rf tg_owt
