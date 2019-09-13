#!/bin/bash

CHANNEL="esr52"
BRANCH="releases/comm-$CHANNEL"
RELEASE_TAG="SEAMONKEY_2_49_4_RELEASE"
VERSION="2.49.4"

echo "cloning $BRANCH..."
hg clone http://hg.mozilla.org/$BRANCH seamonkey
pushd seamonkey
hg update -r $RELEASE_TAG
echo "running client.py..."
[ "$RELEASE_TAG" == "default" ] || \
  _extra="--comm-rev=$RELEASE_TAG --mozilla-rev=$RELEASE_TAG --inspector-rev=$RELEASE_TAG --venkman-rev=$RELEASE_TAG --chatzilla-rev=$RELEASE_TAG"
python client.py checkout $_extra --mozilla-repo=http://hg.mozilla.org/releases/mozilla-$CHANNEL
popd

# use parallel compression, if available
compression='-J'
pixz -h > /dev/null 2>&1
if (($? != 127)); then
  compression='-Ipixz'
fi

echo "creating archive..."
tar $compression -cf seamonkey-$VERSION-source.tar.xz --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=CVS seamonkey

# l10n
echo "fetching locales..."
if [ -e shipped-locales ]; then
  SHIPPED_LOCALES=shipped-locales
else
  SHIPPED_LOCALES=seamonkey/suite/locales/shipped-locales
fi
test ! -d l10n && mkdir l10n
for locale in $(awk '{ print $1; }' $SHIPPED_LOCALES); do
  case $locale in
    ja-JP-mac|en-US)
      ;;
    *)
      hg clone http://hg.mozilla.org/releases/l10n/mozilla-release/$locale l10n/$locale
      hg -R l10n/$locale up -C $RELEASE_TAG
      ;;
  esac
done
echo "creating l10n archive..."
tar $compression -cf l10n-$VERSION.tar.xz \
  --exclude=.hgtags --exclude=.hgignore --exclude=.hg \
  l10n

# compare-locales
hg clone http://hg.mozilla.org/build/compare-locales
tar $compression -cf compare-locales.tar.xz --exclude=.hgtags --exclude=.hgignore --exclude=.hg compare-locales
