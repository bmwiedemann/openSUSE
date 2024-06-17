#!/bin/bash

function main() {
  # Exit script on CTRL+C
  trap "exit" INT

  if [ $# -ne 1 ]; then
    print_usage_and_exit
  fi

  check_required_tools

  # Sourcing the given tar_stamps-file to have the variables available
  TAR_STAMP="$1"
  source "$TAR_STAMP" || print_usage_and_exit

  set_internal_variables

  check_what_to_do_with_source_tarballs
  download_upstream_source_tarballs

  if [ -z ${SKIP_LOCALES+x} ]; then
    check_what_to_do_with_locales_tarballs
    create_locales_tarballs
  else 
    printf "%-40s: User forced skip (SKIP_LOCALES set)\n" "locales"
  fi

  clean_up_old_tarballs
}

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
#SKIP_LOCALES="" # Uncomment to skip l10n-generation
EOF

  exit 1
}

function check_required_tools() {
  # check required tools
  check_for_binary /usr/bin/hg "mercurial"
  check_for_binary /usr/bin/jq "jq"
  which python3 > /dev/null || exit 1

  # use parallel compression, if available
  compression='-J'
  pixz -h > /dev/null 2>&1
  if (($? != 127)); then
    compression='-Ipixz'
  fi
}

function set_internal_variables() {
  # Internal variables
  BRANCH="releases/mozilla-$CHANNEL"
  if [ "$PRODUCT" = "firefox" ]; then
    FF_LOCALE_FILE="firefox-$VERSION/browser/locales/l10n-changesets.json"
  else
    FF_LOCALE_FILE="thunderbird-$VERSION/browser/locales/l10n-changesets.json"
    TB_LOCALE_FILE="thunderbird-$VERSION/comm/mail/locales/l10n-changesets.json"
    FF_PREV_LOCALE_FILE="thunderbird-$PREV_VERSION/browser/locales/l10n-changesets.json"
    TB_PREV_LOCALE_FILE="thunderbird-$PREV_VERSION/comm/mail/locales/l10n-changesets.json"
    L10N_STRING_PATTERNS="thunderbird-$VERSION/comm/python/l10n/tbxchannel/l10n_merge.py"
  fi

  SOURCE_TARBALL="$PRODUCT-$VERSION$VERSION_SUFFIX.source.tar.xz"
  PREV_SOURCE_TARBALL="$PRODUCT-$PREV_VERSION$PREV_VERSION_SUFFIX.source.tar.xz"
  if [ "$PRODUCT" = "thunderbird" ]; then
    TB_LOCALE_TARBALL="$PRODUCT-$VERSION$VERSION_SUFFIX.strings_all.tar.zst"
  fi
  FTP_URL="https://ftp.mozilla.org/pub/$PRODUCT/releases/$VERSION$VERSION_SUFFIX/source"
  FTP_CANDIDATES_BASE_URL="https://ftp.mozilla.org/pub/%s/candidates"
  LOCALES_URL="https://product-details.mozilla.org/1.0/l10n"
  PRODUCT_URL="https://product-details.mozilla.org/1.0"
  ALREADY_EXTRACTED_LOCALES_FILE=0
}

function get_ftp_candidates_url() {
  local CURR_PRODUCT="$1"
  local VERSION_WITH_SUFFIX="$2"
  printf "$FTP_CANDIDATES_BASE_URL/$VERSION_WITH_SUFFIX-candidates" "$CURR_PRODUCT"
}

function check_tarball_source () {
  TARBALL=$1
  # Print out what is going to be done:
  if [ -e "$TARBALL" ]; then
      echo "Reuse existing file"
  elif wget --spider "$FTP_URL/$TARBALL" 2> /dev/null; then
      echo "Download file"
  else 
      local CANDIDATE_TARBALL_LOCATION=""
      CANDIDATE_TARBALL_LOCATION="$(printf "%s/%s/source/%s" "$(get_ftp_candidates_url "$PRODUCT" "$VERSION$VERSION_SUFFIX")" "$BUILD_ID" "$TARBALL" )"
      if wget --spider "$CANDIDATE_TARBALL_LOCATION" 2> /dev/null; then
          echo "Download UNRELEASED candidate ($BUILD_ID)"
      else
          echo "Mercurial checkout"
      fi
  fi
}

function ask_cont_abort_question() {
  while true; do
    read -r -p "$1 [(c)ontinue/(a)bort] " ca
    case $ca in
        [Cc]* ) return 0 ;;
        [Aa]* ) return 1 ;;
        * ) echo "Please answer c or a.";;
    esac
  done
}

function check_for_binary() {
  if ! test -x "$1"; then
    echo "$1 is missing: execute zypper in $2"
    exit 5
  fi
}

function get_source_stamp() {
  local CURR_BUILD_ID="$1"
  local FTP_CANDIDATES_BASE_URL=$(get_ftp_candidates_url "$PRODUCT" "$VERSION$VERSION_SUFFIX")
  local FTP_CANDIDATES_JSON_SUFFIX="${CURR_BUILD_ID}/linux-x86_64/en-US/$PRODUCT-$VERSION$VERSION_SUFFIX.json"
  local BUILD_JSON=$(curl --silent --fail "$FTP_CANDIDATES_BASE_URL/$FTP_CANDIDATES_JSON_SUFFIX") || return 1;
  local REV=$(echo "$BUILD_JSON" | jq .moz_source_stamp)
  local SOURCE_REPO=$(echo "$BUILD_JSON" | jq .moz_source_repo)
  local TIMESTAMP=$(echo "$BUILD_JSON" | jq .buildid)
  echo "Extending $TAR_STAMP with:"
  echo "RELEASE_REPO=${SOURCE_REPO}"
  echo "RELEASE_TAG=${REV}"
  echo "RELEASE_TIMESTAMP=${TIMESTAMP}"
  # We "remove and add" instead of "replace" in case the entries are not there yet
  # Removing the old RELEASE_-tags
  sed -i "/RELEASE_\(TAG\|REPO\|TIMESTAMP\)=.*/d" "$TAR_STAMP"
  # Appending the new 
  echo "RELEASE_REPO=$SOURCE_REPO" >> "$TAR_STAMP"
  echo "RELEASE_TAG=$REV" >> "$TAR_STAMP"
  echo "RELEASE_TIMESTAMP=$TIMESTAMP" >> "$TAR_STAMP"
}

function get_build_number() {
  local LAST_FOUND=""
  local CURR_PRODUCT="$1"
  local VERSION_WITH_SUFFIX="$2"
  local CURR_BUILD_ID=""
  local CURR_FTP_BASE_URL=""
  CURR_BUILD_ID=$(curl --silent "$PRODUCT_URL/$CURR_PRODUCT.json" | jq -e '.["releases"] | .["'$CURR_PRODUCT-$VERSION_WITH_SUFFIX'"] | .["build_number"]')

  # Slow fall-back
  if [ $? -ne 0 ]; then
      echo "Build number not found in product URL, falling back to slow FTP-parsing." 1>&2
      CURR_FTP_BASE_URL=$(get_ftp_candidates_url "$CURR_PRODUCT" "$VERSION_WITH_SUFFIX")
      # Unfortunately, locales-files are not associated to releases, but to builds.
      # And since we don't know which build was the final build, we grep them all from
      # the candidates-page, sort them and take the last one which should be the oldest
      # Error only if not even the first one exists
      LAST_FOUND=$(curl --silent --fail "$CURR_FTP_BASE_URL/" | grep -o "build[0-9]*/" | sort | uniq | tail -n 1 | cut -d "/" -f 1)
  else
      LAST_FOUND="build$CURR_BUILD_ID"
  fi

  if [ "$LAST_FOUND" != "" ]; then
    echo "$LAST_FOUND"
    return 0
  else
    echo "Error: Could not find build-number for $CURR_PRODUCT $VERSION_WITH_SUFFIX !"  1>&2
    return 1
  fi
}

function locales_get() {
  local CURR_PRODUCT="$1"
  local TMP_VERSION="$2"
  local CURR_BUILD_ID="$3"
  # Make first letter of CURR_PRODUCT upper case
  CURR_PRODUCT_CAP="${CURR_PRODUCT^}"
  URL_TO_CHECK="${LOCALES_URL}/${CURR_PRODUCT_CAP}-${TMP_VERSION}"
  FINAL_URL="${URL_TO_CHECK}-${CURR_BUILD_ID}.json"
  if wget --quiet --spider "$FINAL_URL"; then
    echo "$FINAL_URL"
    return 0
  else
    echo "Error: Could not find locales-file (json) for Firefox $TMP_VERSION !"  1>&2
    return 1
  fi
}

function locales_parse_file() {
  FILE="$1"
  python3 -c "import json; import sys; \
             print('\n'.join(['{} {}'.format(key, value['revision']) \
                for key, value in sorted(json.load(sys.stdin).items())]));" < "$FILE" 
}

function locales_parse_url() {
  URL="$1"
  curl -s "$URL" | python3 -c "import json; import sys; \
             print('\n'.join(['{} {}'.format(key, value['changeset']) \
                for key, value in sorted(json.load(sys.stdin)['locales'].items())]));"
}

function extract_locales_file() {
    if [ $ALREADY_EXTRACTED_LOCALES_FILE -ne 1 ]; then
      # still need to extract the locale information from the archive
      echo "extract locale changesets"
      if [ "$PRODUCT" = "thunderbird" ]; then
        tar -xf "$SOURCE_TARBALL" "$FF_LOCALE_FILE" "$TB_LOCALE_FILE" "$L10N_STRING_PATTERNS"
      else
        tar -xf "$SOURCE_TARBALL" "$FF_LOCALE_FILE"
      fi
      ALREADY_EXTRACTED_LOCALES_FILE=1
    else 
      echo "Skipping locale changeset extraction, as it was already done."
    fi
}

function locales_unchanged() {
  local CURR_PRODUCT="$1"
  local CURR_BUILD_ID="$2"
  local PREV_BUILD_ID=$(get_build_number "$CURR_PRODUCT" "$PREV_VERSION$PREV_VERSION_SUFFIX")
  # If no json-file for one of the versions can be found, we say "they changed"
  prev_url=$(locales_get "$CURR_PRODUCT" "$PREV_VERSION$PREV_VERSION_SUFFIX" "$PREV_BUILD_ID") || return 1
  prev_content=$(locales_parse_url "$prev_url") || exit 1

  curr_url=$(locales_get "$CURR_PRODUCT" "$VERSION$VERSION_SUFFIX" "$CURR_BUILD_ID")
  if [ $? -ne 0 ]; then
    # We did not find a locales file upstream on the servers
    if [ -e "$SOURCE_TARBALL" ]; then
        # We can find out what the locales are, by extracting the json-file from the tar-ball
        # instead of getting it from the server
        extract_locales_file || return 1
        curr_content=$(locales_parse_file "$FF_LOCALE_FILE") || exit 1
      else 
        # We can't know what the locales are in the current version
        return 1
      fi
  else
    curr_content=$(locales_parse_url "$curr_url") || exit 1
  fi

  diff -y --suppress-common-lines -d <(echo "$prev_content") <(echo "$curr_content")
}

function get_locales_directories() {
  pattern="$1"

  # This file contains a list of directories, upstream uses to build locales
  # If it is there, use it. If not, default to all FF + 3 TB-dirs.
  if [ -e "$L10N_STRING_PATTERNS" ]; then
    python3 -c "import os; import sys; \
               sys.path.append(os.path.dirname(\"$L10N_STRING_PATTERNS\")); \
               from l10n_merge import $pattern; \
               print(\" \".join([p.strip('*') for p in $pattern]));"
  else
    if [ "$pattern" = "GECKO_STRINGS_PATTERNS" ]; then
      # Default of Firefox: Take all
      echo "{lang}/"
    else
      # Default of Thunderbird: Take those 3 dirs
      echo "{lang}/calendar/" "{lang}/chat/" "{lang}/mail/"
    fi
  fi
}

function create_and_copy_locales() {
    locale="$1"
    source_base="$2"
    source_template="$3"
    final_dest="$4"

    # Replace {lang} with the actual language-basedir
    for template in $source_template; do
      locale_source=$(echo "$template" | sed "s|{lang}|./$source_base/$locale|g")
      locale_dest=$(echo "$template" | sed "s|{lang}|./$final_dest/$locale|g")

      # Create intermediary folders
      for destdir in $locale_dest; do
        mkdir -p "$destdir"
      done
    
      # Copy over FF-files
      cp -r "$locale_source"/* "$locale_dest"
    done
}

function check_what_to_do_with_source_tarballs() {
  # Get ID 
  BUILD_ID=$(get_build_number "$PRODUCT" "$VERSION$VERSION_SUFFIX")

  # Check what is going to be done and ask for consent
  for ff in $SOURCE_TARBALL $SOURCE_TARBALL.asc; do
    printf "%-40s: %s\n" "$ff" "$(check_tarball_source $ff)"
  done

  if [ "$PRODUCT" = "thunderbird" ]; then
    printf "%-40s: %s\n" "$TB_LOCALE_TARBALL" "$(check_tarball_source $TB_LOCALE_TARBALL)"
  fi

  ask_cont_abort_question "Is this ok?" || exit 0
}

function check_what_to_do_with_locales_tarballs() {
  if [ -e "$TB_LOCALE_TARBALL" ]; then
    return;
  fi

  LOCALES_CHANGED=1

  extract_locales_file

  if [ "$PREV_VERSION" != "" ]; then
    # If we have a previous version, check either FF or (TB and FF)
    if [ "$PRODUCT" = "firefox" ]; then
      locales_unchanged "$PRODUCT" "$BUILD_ID"
    else
      # Currently, upstream 'forgets' which Firefox-locales get used for which Thunderbird-release upon release
      # so, instead of parsing upstream JSON-files, we rely on the previous tarball being there and comparing
      # the lang-files directly
      # FF_BUILD_ID=$(get_build_number "firefox" "$VERSION$VERSION_SUFFIX")
      # locales_unchanged "$PRODUCT" "$BUILD_ID" && locales_unchanged "firefox" "$FF_BUILD_ID"
      if [ -e "$PREV_SOURCE_TARBALL" ]; then 
        echo "extract previous locale changesets"
        tar -xf "$PREV_SOURCE_TARBALL" "$FF_PREV_LOCALE_FILE" "$TB_PREV_LOCALE_FILE"

        curr_ff_content=$(locales_parse_file "$FF_LOCALE_FILE") || exit 1
        prev_ff_content=$(locales_parse_file "$FF_PREV_LOCALE_FILE") || exit 1
        curr_tb_content=$(locales_parse_file "$TB_LOCALE_FILE") || exit 1
        prev_tb_content=$(locales_parse_file "$TB_PREV_LOCALE_FILE") || exit 1

        diff -y --suppress-common-lines -d <(echo "$prev_ff_content") <(echo "$curr_ff_content") ||
        diff -y --suppress-common-lines -d <(echo "$prev_tb_content") <(echo "$curr_tb_content")
      fi
    fi
    LOCALES_CHANGED=$?
  fi

  # New line for better visibility
  echo ""
  if [ $LOCALES_CHANGED -eq 1 ]; then
    printf "%-40s: Need to download.\n" "locales"
    ask_cont_abort_question "Is this ok?" || exit 0
  else
    printf "%-40s: Did not change. Skipping.\n" "locales"
  fi
}

function download_release_or_candidate_file() {
  local upstream_file="$1"
  if [ -e "$upstream_file" ]; then
    return;
  fi

  if ! wget --quiet --show-progress --progress=bar "$FTP_URL/$upstream_file"; then
      local CANDIDATE_TARBALL_LOCATION=""
      CANDIDATE_TARBALL_LOCATION="$(printf "%s/%s/source/%s" "$(get_ftp_candidates_url "$PRODUCT" "$VERSION$VERSION_SUFFIX")" "$BUILD_ID" "$upstream_file" )"
      wget --quiet --show-progress --progress=bar "$CANDIDATE_TARBALL_LOCATION"
  fi
}

function download_upstream_source_tarballs() {
  # Try to download tar-ball from officiall mozilla-mirror
  download_release_or_candidate_file "$SOURCE_TARBALL"
  download_release_or_candidate_file "$SOURCE_TARBALL.asc"

  if [ "$PRODUCT" = "thunderbird" ]; then
    download_release_or_candidate_file "$TB_LOCALE_TARBALL"
  fi

  # we might have an upstream archive already and can skip the checkout
  if [ -e "$SOURCE_TARBALL" ]; then
    get_source_stamp "$BUILD_ID"
  else
    # We are working on a version that is not yet published on the mozilla mirror
    # so we have to actually check out the repo
    clone_and_repackage_sources
  fi
}

function clone_and_repackage_sources() {
  if [ -d "$PRODUCT-$VERSION" ]; then
    pushd "$PRODUCT-$VERSION" || exit 1
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
        rm -rf "$PRODUCT-$VERSION"
        ;;
    esac
  fi
  if [ ! -d "$PRODUCT-$VERSION" ]; then
    echo "cloning new $BRANCH..."
    hg clone "https://hg.mozilla.org/$BRANCH $PRODUCT-$VERSION"
    if [ "$PRODUCT" = "thunderbird" ]; then
      hg clone "https://hg.mozilla.org/releases/comm-$CHANNEL" "$PRODUCT-$VERSION/comm"
    fi
  fi
  pushd "$PRODUCT-$VERSION" || exit 1

  # parse out the Firefox-release tag for this Thunderbird-checkout
  if [ "$PRODUCT" = "thunderbird" ]; then
    FF_RELEASE_TAG=$(grep ^GECKO_HEAD_REV ./comm/.gecko_rev.yml | awk -F ' ' '{print $2}') || exit 1
    echo "Parsed Firefox base ID from .gecko_rev.yml: $FF_RELEASE_TAG"
  else
    FF_RELEASE_TAG="$RELEASE_TAG"
  fi

  hg update --check "$FF_RELEASE_TAG"
  [ "$FF_RELEASE_TAG" == "default" ] || hg update -r "$FF_RELEASE_TAG"
  # get repo and source stamp
  local REV=$(hg -R . parent --template="{node|short}\n")
  local SOURCE_REPO=$(hg showconfig paths.default 2>/dev/null | head -n1 | sed -e "s/^ssh:/https:/")
  local TIMESTAMP=$(date +%Y%m%d%H%M%S)

  if [ "$PRODUCT" = "thunderbird" ]; then
    pushd comm || exit 1
    hg update --check "$RELEASE_TAG"
    popd || exit 1
    rm -rf thunderbird-"${VERSION}"/{,comm/}other-licenses/7zstub
  fi
  popd || exit 1

  echo "Extending $TAR_STAMP with:"
  echo "RELEASE_REPO=${SOURCE_REPO}"
  echo "RELEASE_TAG=${REV}"
  echo "RELEASE_TIMESTAMP=${TIMESTAMP}"

  # We "remove and add" instead of "replace" in case the entries are not there yet
  # Removing the old RELEASE_-tags
  sed -i "/RELEASE_\(TAG\|REPO\|TIMESTAMP\)=.*/d" "$TAR_STAMP"
  # Appending the new 
  echo "RELEASE_REPO=$SOURCE_REPO" >> "$TAR_STAMP"
  echo "RELEASE_TAG=$REV" >> "$TAR_STAMP"
  echo "RELEASE_TIMESTAMP=$TIMESTAMP" >> "$TAR_STAMP"

  echo "creating archive..."
  tar "$compression" -cf "$PRODUCT-$VERSION$VERSION_SUFFIX.source.tar.xz" --exclude-vcs "$PRODUCT-$VERSION"
  ALREADY_EXTRACTED_LOCALES_FILE=1
}

function create_locales_tarballs() {
  if [ ! -z ${SKIP_LOCALES+x} ]; then
    echo "Skipping locales-creation."
    exit 0
  fi

  if [ -e "$TB_LOCALE_TARBALL" ]; then
    echo "Repackaging upstream lang-tarball."
    zstd -dcf "$TB_LOCALE_TARBALL" | xz > "l10n-$VERSION$VERSION_SUFFIX.tar.xz"
  else 
    if [ "$LOCALES_CHANGED" -ne 0 ]; then
      clone_and_repackage_locales
    elif [ -f "l10n-$PREV_VERSION$PREV_VERSION_SUFFIX.tar.xz" ]; then
      # Locales did not change, but the old tar-ball is in this directory
      # Simply rename it:
      echo "Moving l10n-$PREV_VERSION$PREV_VERSION_SUFFIX.tar.xz to l10n-$VERSION$VERSION_SUFFIX.tar.xz"
      mv "l10n-$PREV_VERSION$PREV_VERSION_SUFFIX.tar.xz" "l10n-$VERSION$VERSION_SUFFIX.tar.xz"
    fi
  fi
}

function clone_and_repackage_locales() {
  # l10n
  FINAL_L10N_BASE="l10n"
  FF_L10N_BASE="l10n" # Only change this in TB-builds to a separate dir
  TB_L10N_BASE="l10n_tb"

  # If we are doing Thunderbird, we'll have to checkout both TB and FF l10n-repos
  # Thunderbird has one single mono-repo, FF has one for each language
  if [ "$PRODUCT" = "thunderbird" ]; then
    echo "Fetching Thunderbird locales..."
    if [ -d "$TB_L10N_BASE/.hg" ]; then
      pushd "$TB_L10N_BASE/" || exit 1
      hg pull || exit 1
      popd || exit 1
    else
      hg clone "https://hg.mozilla.org/projects/comm-l10n/" "$TB_L10N_BASE/" || exit 1
    fi
    # Just using the first entry here, as all languages have the same changeset
    tb_changeset=$(jq -r 'to_entries[0]| "\(.key) \(.value|.revision)"' "$TB_LOCALE_FILE" | cut -d " " -f 2)
    [ "$RELEASE_TAG" == "default" ] || hg -R "$TB_L10N_BASE/" up -C -r "$tb_changeset" || exit 1
    FF_L10N_BASE="l10n_ff"
  fi

  test ! -d $FF_L10N_BASE && mkdir $FF_L10N_BASE
  # No-op, if we are building FF:
  test ! -d $FINAL_L10N_BASE && mkdir $FINAL_L10N_BASE

  # This is only relevant for Thunderbird-builds
  # Here, the relevant directories we need to copy from FF and from TB
  # are specified in a python-file in the tarball
  # Is of form '{lang}/Foo/bar/ {lang}/Baz/bar/ ..'
  ff_locale_template=$(get_locales_directories "GECKO_STRINGS_PATTERNS")
  tb_locale_template=$(get_locales_directories "COMM_STRINGS_PATTERNS")

  echo "Fetching Browser locales..."
  jq -r 'to_entries[]| "\(.key) \(.value|.revision)"' "$FF_LOCALE_FILE" | \
    while read -r locale changeset ; do
      case $locale in
        ja-JP-mac|en-US)
          ;;
        *)
          echo "reading changeset information for $locale"
          echo "fetching $locale changeset $changeset ..."
          if [ -d "$FF_L10N_BASE/$locale/.hg" ]; then
            pushd "$FF_L10N_BASE/$locale" || exit 1
            hg pull || exit 1
            popd || exit 1
          else
            hg clone "https://hg.mozilla.org/l10n-central/$locale" "$FF_L10N_BASE/$locale" || exit 1
          fi
          [ "$RELEASE_TAG" == "default" ] || hg -R "$FF_L10N_BASE/$locale" up -C -r "$changeset" || exit 1

          # If we are doing TB, we have to merge both l10n-repos
          if [ "$PRODUCT" = "thunderbird" ] && test -d "$TB_L10N_BASE/$locale/" ; then
            create_and_copy_locales "$locale" "$FF_L10N_BASE" "$ff_locale_template" "$FINAL_L10N_BASE"
            create_and_copy_locales "$locale" "$TB_L10N_BASE" "$tb_locale_template" "$FINAL_L10N_BASE"
          fi
          ;;
      esac
    done
  echo "creating l10n archive..."
  local TAR_FLAGS="--exclude-vcs"
  if [ "$PRODUCT" = "thunderbird" ]; then
    TAR_FLAGS="$TAR_FLAGS --exclude=suite"
  fi
  tar "$compression" -cf "l10n-$VERSION$VERSION_SUFFIX.tar.xz" $TAR_FLAGS "$FINAL_L10N_BASE"
}

function clean_up_old_tarballs() {
  if [ -e "$PREV_SOURCE_TARBALL" ]; then
      echo ""
      echo "Deleting old sources tarball $PREV_SOURCE_TARBALL"
      ask_cont_abort_question "Is this ok?" || exit 0
      rm "$PREV_SOURCE_TARBALL"
      rm "$PREV_SOURCE_TARBALL.asc"
      # if old and new lang-tarball are there, delete the old one
      if [ -f "l10n-$PREV_VERSION$PREV_VERSION_SUFFIX.tar.xz" ] && [ -f "l10n-$VERSION$VERSION_SUFFIX.tar.xz" ]; then
          rm "l10n-$PREV_VERSION$PREV_VERSION_SUFFIX.tar.xz"
      fi
  fi
  # If we downloaded the upstream zstd-tarball and repackaged it, remove it now
  if [ -f "$TB_LOCALE_TARBALL" ] && [ -f "l10n-$VERSION$VERSION_SUFFIX.tar.xz" ]; then 
      echo ""
      echo "Deleting old sources tarball $TB_LOCALE_TARBALL"
      ask_cont_abort_question "Is this ok?" || exit 0
      rm "$TB_LOCALE_TARBALL"
  fi
}

main "$@"
