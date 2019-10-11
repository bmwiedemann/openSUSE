#!/bin/bash

function print_usage_and_exit() {
  echo "Usage: create-tar.sh tar_stamps"
  echo ""
  echo "Where tar_stamps should look like this:"
  echo ""
  cat << EOF
# Node ID: 64ee63facd4ff96b3e8590cff559d7e97ac6b061
PRODUCT="firefox" # "firefox" or "thunderbird"
CHANNEL="esr60"
VERSION="60.7.0"
VERSION_SUFFIX="esr"
RELEASE_TAG="" # Needs only to be set if no tar-ball can be downloaded
PREV_VERSION="60.6.3" # Prev. version only needed for locales (leave empty to force l10n-generation)
PREV_VERSION_SUFFIX="esr"
#SKIP_LOCALES="" # Uncomment to skip l10n and compare-locales-generation
EOF

exit 1
}

if [ $# -ne 1 ]; then
  print_usage_and_exit
fi

# Sourcing the given tar_stamps-file to have the variables available
source "$1" || print_usage_and_exit

# Internal variables
BRANCH="releases/mozilla-$CHANNEL"
if [ "$PRODUCT" = "firefox" ]; then
  LOCALE_FILE="firefox-$VERSION/browser/locales/l10n-changesets.json"
else
  LOCALE_FILE="thunderbird-$VERSION/comm/mail/locales/l10n-changesets.json"
fi

SOURCE_TARBALL="$PRODUCT-$VERSION$VERSION_SUFFIX.source.tar.xz"
FTP_URL="https://ftp.mozilla.org/pub/$PRODUCT/releases/$VERSION$VERSION_SUFFIX/source"
# Make first letter of PRODCUT upper case
PRODUCT_CAP="${PRODUCT^}"
LOCALES_URL="https://product-details.mozilla.org/1.0/l10n/$PRODUCT_CAP"
# Exit script on CTRL+C
trap "exit" INT

function check_tarball_source () {
  TARBALL=$1
  # Print out what is going to be done:
  if [ -e $TARBALL ]; then
      echo "Reuse existing file"
  elif wget --spider $FTP_URL/$TARBALL 2> /dev/null; then
      echo "Download file"
  else
      echo "Mercurial checkout"
  fi
}

function ask_cont_abort_question() {
  while true; do
    read -p "$1 [(c)ontinue/(a)bort] " ca
    case $ca in
        [Cc]* ) return 0 ;;
        [Aa]* ) return 1 ;;
        * ) echo "Please answer c or a.";;
    esac
  done
}

function check_for_binary() {
  if ! test -x $1; then
    echo "$1 is missing: execute zypper in $2"
    exit 5
  fi
}

function locales_get() {
  TMP_VERSION="$1"
  URL_TO_CHECK="${LOCALES_URL}-${TMP_VERSION}"

  LAST_FOUND=""
  # Unfortunately, locales-files are not associated to releases, but to builds.
  # And since we don't know which build was the final build, we go from 9 downwards
  # try to find the latest one that exists (assuming there are no more than 9 builds).
  # Error only if not even the first one exists
  for BUILD_ID in $(seq 9 -1 0); do
    FINAL_URL="${URL_TO_CHECK}-build${BUILD_ID}.json"
    if wget --quiet --spider "$FINAL_URL"; then
      LAST_FOUND="$FINAL_URL"
      break
    fi
  done

  if [ "$LAST_FOUND" != "" ]; then
    echo "$LAST_FOUND"
    return 0
  else
    echo "Error: Could not find locales-file (json) for Firefox $TMP_VERSION !"  1>&2
    return 1
  fi
}

function locales_parse() {
  URL="$1"
  curl -s "$URL" | python -c "import json; import sys; \
             print('\n'.join(['{} {}'.format(key, value['changeset']) \
                for key, value in sorted(json.load(sys.stdin)['locales'].items())]));"
}

function locales_unchanged() {
  # If no json-file for one of the versions can be found, we say "they changed"
  prev_url=$(locales_get "$PREV_VERSION$PREV_VERSION_SUFFIX") || return 1
  curr_url=$(locales_get "$VERSION$VERSION_SUFFIX")      || return 1

  prev_content=$(locales_parse "$prev_url") || exit 1
  curr_content=$(locales_parse "$curr_url") || exit 1

  diff -y --suppress-common-lines -d <(echo "$prev_content") <(echo "$curr_content")
}

# check required tools
check_for_binary /usr/bin/hg "mercurial"
check_for_binary /usr/bin/jq "jq"
which python > /dev/null || exit 1

# use parallel compression, if available
compression='-J'
pixz -h > /dev/null 2>&1
if (($? != 127)); then
  compression='-Ipixz'
fi

if [ -z ${SKIP_LOCALES+x} ]; then
  # TODO: Thunderbird has usually "default" as locale entry. 
  # There we probably need to double-check Firefox-locals
  # For now, just download every time for Thunderbird
  if [ "$PRODUCT" = "firefox" ] && [ "$PREV_VERSION" != "" ] && locales_unchanged; then
    printf "%-40s: Did not change. Skipping.\n" "locales"
    LOCALES_CHANGED=0
  else
    printf "%-40s: Need to download.\n" "locales"
    LOCALES_CHANGED=1
  fi
else 
  printf "%-40s: User forced skip (SKIP_LOCALES set)\n" "locales"
fi

# Check what is going to be done and ask for consent
for ff in $SOURCE_TARBALL $SOURCE_TARBALL.asc; do
  printf "%-40s: %s\n" $ff "$(check_tarball_source $ff)"
done

$(ask_cont_abort_question "Is this ok?") || exit 0

# Try to download tar-ball from officiall mozilla-mirror
if [ ! -e $SOURCE_TARBALL ]; then
  wget https://ftp.mozilla.org/pub/$PRODUCT/releases/$VERSION$VERSION_SUFFIX/source/$SOURCE_TARBALL
fi
# including signature
if [ ! -e $SOURCE_TARBALL.asc ]; then
  wget https://ftp.mozilla.org/pub/$PRODUCT/releases/$VERSION$VERSION_SUFFIX/source/$SOURCE_TARBALL.asc
fi

# we might have an upstream archive already and can skip the checkout
if [ -e $SOURCE_TARBALL ]; then
  if [ -z ${SKIP_LOCALES+x} ] && [ $LOCALES_CHANGED -ne 0 ]; then
    # still need to extract the locale information from the archive
    echo "extract locale changesets"
    tar -xf $SOURCE_TARBALL $LOCALE_FILE
  fi
else
  # We are working on a version that is not yet published on the mozilla mirror
  # so we have to actually check out the repo

  # mozilla
  if [ -d $PRODUCT-$VERSION ]; then
    pushd $PRODUCT-$VERSION || exit 1
    _repourl=$(hg paths)
    case "$_repourl" in
      *$BRANCH*)
        echo "updating previous tree"
        hg pull
        popd || exit 1
        ;;
      * )
        echo "removing obsolete tree"
        popd || exit 1
        rm -rf $PRODUCT-$VERSION
        ;;
    esac
  fi
  if [ ! -d $PRODUCT-$VERSION ]; then
    echo "cloning new $BRANCH..."
    hg clone http://hg.mozilla.org/$BRANCH $PRODUCT-$VERSION
    if [ "$PRODUCT" = "thunderbird" ]; then
      hg clone http://hg.mozilla.org/releases/comm-$CHANNEL $PRODUCT-$VERSION/comm
    fi
  fi
  pushd $PRODUCT-$VERSION || exit 1

  # parse out the Firefox-release tag for this Thunderbird-checkout
  if [ "$PRODUCT" = "thunderbird" ]; then
    FF_RELEASE_TAG=$(grep ^GECKO_HEAD_REV ./comm/.gecko_rev.yml | awk -F ' ' '{print $2}') || exit 1
    echo "Parsed Firefox base ID from .gecko_rev.yml: $FF_RELEASE_TAG"
  else
    FF_RELEASE_TAG="$RELEASE_TAG"
  fi

  hg update --check $FF_RELEASE_TAG
  [ "$FF_RELEASE_TAG" == "default" ] || hg update -r $FF_RELEASE_TAG
  # get repo and source stamp
  echo -n "REV=" > ../source-stamp.txt
  hg -R . parent --template="{node|short}\n" >> ../source-stamp.txt
  echo -n "REPO=" >> ../source-stamp.txt
  hg showconfig paths.default 2>/dev/null | head -n1 | sed -e "s/^ssh:/http:/" >> ../source-stamp.txt

  if [ "$PRODUCT" = "thunderbird" ]; then
    pushd comm || exit 1
    hg update --check $RELEASE_TAG
    popd || exit 1
    rm -rf thunderbird-${VERSION}/{,comm/}other-licenses/7zstub
  fi
  popd || exit 1

  echo "creating archive..."
  tar $compression -cf $PRODUCT-$VERSION$VERSION_SUFFIX.source.tar.xz --exclude=.hgtags --exclude=.hgignore --exclude=.hg --exclude=CVS $PRODUCT-$VERSION
fi

if [ ! -z ${SKIP_LOCALES+x} ]; then
  echo "Skipping locales-creation."
  exit 0
fi

if [ $LOCALES_CHANGED -ne 0 ]; then
  # l10n
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
          if [ -d "l10n/$locale/.hg" ]; then
            pushd "l10n/$locale" || exit 1
            hg pull
            popd || exit 1
          else
            hg clone "http://hg.mozilla.org/l10n-central/$locale" "l10n/$locale"
          fi
          [ "$RELEASE_TAG" == "default" ] || hg -R "l10n/$locale" up -C -r "$changeset"
          ;;
      esac
    done
  echo "creating l10n archive..."
  if [ "$PRODUCT" = "thunderbird" ]; then
    TB_TAR_FLAGS="--exclude=browser --exclude=suite"
  fi
  tar $compression -cf l10n-$VERSION$VERSION_SUFFIX.tar.xz \
  --exclude=.hgtags --exclude=.hgignore --exclude=.hg \
  $TB_TAR_FLAGS \
  l10n
elif [ -f "l10n-$PREV_VERSION$PREV_VERSION_SUFFIX.tar.xz" ]; then
  # Locales did not change, but the old tar-ball is in this directory
  # Simply rename it:
  echo "Moving l10n-$PREV_VERSION$PREV_VERSION_SUFFIX.tar.xz to l10n-$VERSION$VERSION_SUFFIX.tar.xz"
  mv "l10n-$PREV_VERSION$PREV_VERSION_SUFFIX.tar.xz" "l10n-$VERSION$VERSION_SUFFIX.tar.xz"
fi

# compare-locales
echo "creating compare-locales"
if [ -d compare-locales/.hg ]; then
  pushd compare-locales || exit 1
  hg pull
  popd || exit 1
else
  hg clone http://hg.mozilla.org/build/compare-locales
fi
tar $compression -cf compare-locales.tar.xz --exclude=.hgtags --exclude=.hgignore --exclude=.hg compare-locales

