#!/bin/bash

CHANNEL="esr60"
BRANCH="releases/comm-$CHANNEL"
RELEASE_TAG="ef6b0f0be269d5b7314fe9b359604c9f4f541055"
MOZ_RELEASE_TAG="eb76765892cfd646d3014e5f3b8df8c6753da2d2"
VERSION="60.8.0"
VERSION_SUFFIX=""
LOCALE_FILE="thunderbird-$VERSION/comm/mail/locales/l10n-changesets.json"

# check required tools
test -x /usr/bin/hg || ( echo "hg missing: execute zypper in mercurial"; exit 5 )
test -x /usr/bin/jq || ( echo "jq missing: execute zypper in jq"; exit 5 )

# use parallel compression, if available
compression='-J'
pixz -h > /dev/null 2>&1
if (($? != 127)); then
  compression='-Ipixz'
fi

# we might have an upstream archive already and can skip the checkout
if [ -e thunderbird-$VERSION$VERSION_SUFFIX.source.tar.xz ]; then
  echo "skip thunderbird checkout and use available archive"
  # still need to extract the locale information from the archive
  echo "extract locale list"
  tar -xf thunderbird-$VERSION$VERSION_SUFFIX.source.tar.xz $LOCALE_FILE
  # remove non-free untar licenced code from distributed tarball
  #xz -d -v thunderbird-$VERSION$VERSION_SUFFIX.source.tar.xz && \
  #tar -v --wildcards --delete -f thunderbird-$VERSION$VERSION_SUFFIX.source.tar \
  #	"thunderbird-${VERSION}/comm/other-licenses/7zstub" \
  # 	"thunderbird-${VERSION}/other-licenses/7zstub" \
  #&& \
  #xz -9 -v thunderbird-$VERSION$VERSION_SUFFIX.source.tar
else
  if [ -d thunderbird-$VERSION ]; then
    pushd thunderbird-$VERSION
    _repourl=$(hg paths)
    case "$_repourl" in
      *$BRANCH*)
        echo "updating previous tree"
        hg pull
        popd
        ;;
      * )
        echo "removing obsolete tree"
        popd
        rm -rf thunderbird-$VERSION
        ;;
    esac
  fi
  if [ ! -d thunderbird-$VERSION ]; then
    echo "cloning new $BRANCH..."
    hg clone http://hg.mozilla.org/releases/mozilla-$CHANNEL thunderbird-$VERSION
    hg clone http://hg.mozilla.org/releases/comm-$CHANNEL thunderbird-$VERSION/comm
  fi
  pushd thunderbird-$VERSION
  hg update --check $MOZ_RELEASE_TAG
  pushd comm
  hg update --check $RELEASE_TAG
  popd
  popd
  echo "creating archive..."
  rm -rf thunderbird-${VERSION}/{,comm/}other-licenses/7zstub
  tar $compression -cf thunderbird-$VERSION.source.tar.xz --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=CVS thunderbird-${VERSION}
fi

# l10n
# http://l10n.mozilla.org/dashboard/?tree=tb30x -> shipped-locales
echo "fetching locales..."
test ! -d l10n && mkdir l10n
jq -r 'to_entries[]| "\(.key) \(.value|.revision)"' $LOCALE_FILE | \
  while read locale changeset ; do
  case $locale in
    ja-JP-mac|en-US)
      ;;
    *)
      echo "reading changeset information for $locale"
      echo "fetching $locale changeset $changeset ..."
      #(
      if [ -d l10n/$locale/.hg ]; then
        (cd l10n/$locale; hg pull)
      else
        hg clone http://hg.mozilla.org/l10n-central/$locale l10n/$locale
      fi
      [ "$RELEASE_TAG" == "default" ] || hg -R l10n/$locale up -C -r $changeset
      #) &
      ;;
  esac
done
wait
echo "creating l10n archive..."
tar $compression -cf l10n-$VERSION.tar.xz \
  --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=browser \
  --exclude=suite \
  l10n

# compare-locales
echo "creating compare-locales"
if [ -d compare-locales/.hg ]; then
  (cd compare-locales; hg pull)
else
  hg clone http://hg.mozilla.org/build/compare-locales
fi
tar $compression -cf compare-locales.tar.xz --exclude=.hgtags --exclude=.hgignore --exclude=.hg compare-locales

