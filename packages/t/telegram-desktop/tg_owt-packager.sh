#! /bin/bash

# tg_owt origin
# get it from https://github.com/telegramdesktop/tdesktop/blob/dev/Telegram/build/docker/centos_env/Dockerfile around line 761
# tg_owt_origin="4a60ce1ab9fdb962004c6a959f682ace3db50cbd"
# use xuzhao9's fork to workaround the h264 dlopen issue
tg_owt_origin="0342ae21ee2cc6c6052798bc8fa6b737d9a66418"

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
