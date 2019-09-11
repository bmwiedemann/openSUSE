#!/bin/bash
# DOWNLOAD='no' when testing this script or spec.in
DOWNLOAD='yes'
GIT_DIR='dictionaries'
VERBOSE='yes'

DATADIR="/usr/share"
DOCDIR="/usr/share/doc/packages"
DIC_DIR="hunspell"
HYPH_DIR="hyphen"
TH_DIR="mythes"
COMPAT_DIR="myspell"
LO_DIR="%{_libdir}/libreoffice"
LODATA_DIR="$LO_DIR/share"
LOEXT_DIR="$LODATA_DIR/extensions"

declare -A provides_map=(
["myspell-af_ZA"]="myspell-african"
["myspell-ar"]="myspell-arabic"
["myspell-be_BY"]="myspell-belarusian"
["myspell-bg_BG"]="myspell-bulgarian libreoffice-thesaurus-bg"
["myspell-bn_BD"]="myspell-bengali"
["myspell-br_FR"]="myspell-breton"
["myspell-ca"]="myspell-catalan libreoffice-thesaurus-ca"
["myspell-ca_ES_valencia"]="myspell-valencian"
["myspell-cs_CZ"]="myspell-czech libreoffice-thesaurus-cs"
["myspell-da_DK"]="myspell-danish libreoffice-thesaurus-da"
["myspell-de_DE"]="myspell-german"
["myspell-de_AT"]="myspell-austrian"
["myspell-de_CH"]="myspell-nswiss"
["myspell-el_GR"]="myspell-greek libreoffice-thesaurus-el"
["myspell-en_US"]="myspell-american libreoffice-thesaurus-US"
["myspell-en_GB"]="myspell-british libreoffice-thesaurus-en-GB"
["myspell-en_ZA"]="myspell-south-african-english"
["myspell-en_AU"]="myspell-australian libreoffice-thesaurus-en-AU"
["myspell-en_NZ"]="myspell-new-zaeland"
["myspell-en_CA"]="myspell-canadian"
["myspell-es_UY"]="myspell-spanish-uruguayan"
["myspell-es_HN"]="myspell-spanish-honduran"
["myspell-es_GT"]="myspell-spanish-guatemalan"
["myspell-es_CO"]="myspell-spanish-colombian"
["myspell-es_CL"]="myspell-spanish-chilean"
["myspell-es_VE"]="myspell-spanish-venezuelan"
["myspell-es_CR"]="myspell-spanish-costa-rican"
["myspell-es_BO"]="myspell-spanish-bolivian"
["myspell-es_MX"]="myspell-mexican"
["myspell-es_SV"]="myspell-spanish-salvadorean"
["myspell-es_PA"]="myspell-spanish-panamanian"
["myspell-es_PE"]="myspell-spanish-peruvian"
["myspell-es_EC"]="myspell-spanish-ecuadorian"
["myspell-es_DO"]="myspell-spanish-dominican"
["myspell-es_PR"]="myspell-spanish-puerto-rican"
["myspell-es_AR"]="myspell-spanish-argentine"
["myspell-es_NI"]="myspell-spanish-nicaraguan"
["myspell-es_PY"]="myspell-spanish-paraguayan"
["myspell-es_ES"]="myspell-spanish"
["myspell-et_EE"]="myspell-estonian"
["myspell-fr_FR"]="myspell-french libreoffice-thesaurus-fr"
["myspell-gd_GB"]="myspell-gaelic"
["myspell-gl"]="myspell-galician"
["myspell-gu_IN"]="myspell-gujarati"
["myspell-he_IL"]="myspell-hebrew"
["myspell-hi_IN"]="myspell-hindi"
["myspell-hr_HR"]="myspell-croatian"
["myspell-hu_HU"]="myspell-hungarian libreoffice-thesaurus-hu"
["myspell-is"]="myspell-icelandic"
["myspell-it_IT"]="myspell-italian libreoffice-thesaurus-it"
["myspell-lt_LT"]="myspell-lithuanian"
["myspell-lv_LV"]="myspell-latvian"
["myspell-nl_NL"]="myspell-dutch"
["myspell-nb_NO"]="myspell-norsk-bokmaal"
["myspell-nn_NO"]="myspell-norsk-nynorsk"
["myspell-oc_FR"]="myspell-occitan-lengadocian"
["myspell-pl_PL"]="myspell-polish libreoffice-thesaurus-pl"
["myspell-pt_BR"]="myspell-brazilian libreoffice-thesaurus-pt"
["myspell-pt_PT"]="myspell-portuguese"
["myspell-ro"]="myspell-romanian libreoffice-thesaurus-ro"
["myspell-ru_RU"]="myspell-russian libreoffice-thesaurus-ru"
["myspell-si_LK"]="myspell-sinhala"
["myspell-sk_SK"]="myspell-slovak libreoffice-thesaurus-sk"
["myspell-sl_SI"]="myspell-slovene libreoffice-thesaurus-sl"
["myspell-sr"]="myspell-serbian-latin myspell-serbian-cyrillic"
["myspell-sv_SE"]="myspell-swedish libreoffice-thesaurus-sv"
["myspell-sw_TZ"]="myspell-kiswahili"
["myspell-th_TH"]="myspell-thai"
["myspell-uk_UA"]="myspell-ukrainian"
["myspell-vi"]="myspell-vietnamese"
["myspell-zu_ZA"]="myspell-zulu"
)

declare -A recommends_map=(
["myspell-de"]="myspell-de_DE"
["myspell-en"]="myspell-en_US"
["myspell-es"]="myspell-es_ES"
["myspell-ro"]="myspell-ro_RO"
["myspell-no"]="myspell-nb_NO"
["myspell-vi"]="myspell-vi_VN"
)

# directories under $GIT_DIR, which holds dictionaries
function directories()
{
  ls $GIT_DIR/*/dictionaries.xcu | sed -e 's:dictionaries/::' -e 's:/dictionaries.xcu::' | tr '\n' ' '
}

# create central mapping dir <-> locales <-> files
function locale_to_file_map()
{
  cd $GIT_DIR
  rm -f locale_to_file_map.txt
  for dir in $dirs; do
    cat $dir/dictionaries.xcu \
       | grep -v '<!--' \
       | grep -A1 'Locations\|Locales' \
       | grep -v '\-\-\|Locations\|Locales' \
       | sed s:%origin%:$dir:g \
       | sed 's:<it>: :g' \
       | sed 's:</it>: :g' \
       | sed 's:.*<value>\(.*\)</value>.*:\1:' \
       | while read files; do 
           read locs
           locs=`echo $locs | tr '-' '_'`
           echo $dir: $locs @ $files >> locale_to_file_map.txt
         done
  done
  # add idx files for every dat (where doesn't exist)
  # we will generate them
  sed -i '/\.idx/!s/\([^ ]*\)\.dat/\1.dat \1.idx/g' locale_to_file_map.txt
  cd ..
}

# for given dir: which locales provides
function dir_locales()
{
  dir=$1
  grep "^$dir:" $GIT_DIR/locale_to_file_map.txt | sed 's/.*: //' | sed 's/ @.*//' | tr ' ' '\n' | sort -u | tr '\n' ' '
}

# for given dir: which dictionary relevant files (dic, aff, th*, hyph*) provides
function dir_files()
{
  dir=$1
  grep "$dir:" $GIT_DIR/locale_to_file_map.txt  | sed 's:.*@ ::' | tr ' ' '\n' | sort -u | tr '\n' ' '
}

# for given dictionary file: which locales provides
function file_locales()
{
  file=$1
  # there should be only one occurence of a file in locale_to_file_map.txt
  grep $file $GIT_DIR/locale_to_file_map.txt | sed -e 's/.*: //' -e 's/@.*//'
}

# for given dir: description of the dictionary
function description()
{
  dir=$1
  grep  '<name lang="en.*">' dictionaries/$dir/description.xml | sed -e 's:.*<name lang="en.*">::' -e 's:</name>.*::' | tr '\n' ' ' | sed 's:[ \t]*$::'
}

# all thesaurus dat files
function dat_files()
{
  grep '\.dat' $GIT_DIR/locale_to_file_map.txt | sed 's:.* \([^ ]\+\.dat\).*:\1:'
}

# for dat file return corresponding idx file name
function idx_file()
{
  dat_file=$1
  grep "$dat_file" $GIT_DIR/locale_to_file_map.txt | sed 's:.* \([^ ]\+\.idx\).*:\1:'
}

# arch package?
function have_lightproof()
{
  dir=$1
  [ -f $GIT_DIR/$dir/Lightproof.py ]
}

# figure out install path for given file name
function install_path()
{
  filename=$1

  install_dir=""
  # *.dic, *.aff
  if [[ $filename =~ \.dic$ ]] || [[ $filename =~ \.aff$ ]]; then
    if [[ $filename =~ ^hyph ]]; then
      install_dir="$DATADIR/$HYPH_DIR"
    else
      install_dir="$DATADIR/$DIC_DIR"
    fi
  fi
  # th*.dat, th*.idx
  if [[ $filename =~ th.*\.dat ]] || [[ $filename =~ th.*\.idx ]]; then
    install_dir="$DATADIR/$TH_DIR"
  fi

  echo "$install_dir/$filename"
}

function install_regular()
{
  src=$1
  dst=$2
  sed -i "s#@INSTALL@#cp -P $src %{buildroot}$dst\n@INSTALL@#" myspell-dictionaries.spec
}

function install_regular_recursive()
{
  src=$1
  dst=$2
  sed -i "s#@INSTALL@#cp -rP $src %{buildroot}$dst\n@INSTALL@#" myspell-dictionaries.spec
}

function install_link()
{
  targ=$1
  name=$2
  sed -i "s#@INSTALL@#ln -s $targ %{buildroot}$name\n@INSTALL@#" myspell-dictionaries.spec
}

function install_dir()
{
  dirname=$1
  sed -i "s#@INSTALL@#mkdir -p %{buildroot}$dirname\n@INSTALL@#" myspell-dictionaries.spec
}

function add_files()
{
  filelist=$1

  sed -i "s#@FILES@#%defattr(-,root,root,-)\n@FILES@#" myspell-dictionaries.spec
  for f in $filelist; do
    f=$(echo $f | sed 's:%dir_:%dir :')
    sed -i "s#@FILES@#$f\n@FILES@#" myspell-dictionaries.spec
  done
}

function package_files()
{
  pname=$1
  filelist=$2

  sed -i "s#@FILES@#%files -n $pname\n@FILES@#" myspell-dictionaries.spec
  add_files "$filelist"
  sed -i "s#@FILES@#\n@FILES@#" myspell-dictionaries.spec
}

function package_metadata()
{
  locale=$1
  dir=$2
  requires=$3

  desc=$(description $dir)
  sum="MySpell $locale Dictionary"
  sed -i "s#@METADATA@#%package -n myspell-$locale\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#Summary:        $sum\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#Group:          Productivity/Text/Spell\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#Requires:       myspell-dictionaries\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#Provides:       myspell-dictionary\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#Provides:       locale(libreoffice:$locale)\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#Provides:       locale(seamonkey-spellchecker:$locale)\n@METADATA@#" myspell-dictionaries.spec
  for p in ${provides_map["myspell-$locale"]}; do
    sed -i "s#@METADATA@#Provides:       $p\n@METADATA@#" myspell-dictionaries.spec
  done
  if [ "$locale" != "$dir" ]; then
    # require main language subpackage; note that e. g. myspell-te_IN is main language package
    # and myspell-te is language subpackage; drawback of splitting
    sed -i "s#@METADATA@#Requires:       myspell-$dir\n@METADATA@#" myspell-dictionaries.spec
  fi
  for req in $requires; do
    sed -i "s#@METADATA@#Requires:       myspell-$req\n@METADATA@#" myspell-dictionaries.spec
  done
  for p in ${recommends_map["myspell-$locale"]}; do
    sed -i "s#@METADATA@#Recommends:       $p\n@METADATA@#" myspell-dictionaries.spec
  done
  sed -i "s#@METADATA@#BuildArch:      noarch\n@METADATA@#" myspell-dictionaries.spec
  if have_lightproof $dir; then
    sed -i "s#@METADATA@#Recommends:     myspell-lightproof-$dir\n@METADATA@#" myspell-dictionaries.spec
  fi
  sed -i "s#@METADATA@#\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#%description -n myspell-$locale\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#$desc.\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#\n@METADATA@#" myspell-dictionaries.spec
}

function lightproof_package_metadata()
{
  dir=$1

  sed -i "s#@METADATA@#%package -n myspell-lightproof-$dir\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#Summary:        Lightproof for $dir\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#Group:          Productivity/Text/Spell\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#Requires:       myspell-$dir\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#%description -n myspell-lightproof-$dir\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#Lightproof grammar checker information for $dir.\n@METADATA@#" myspell-dictionaries.spec
  sed -i "s#@METADATA@#\n@METADATA@#" myspell-dictionaries.spec
}

function finish_spec()
{
  sed -i "s:@METADATA@::" myspell-dictionaries.spec
  sed -i "s:@INSTALL@::" myspell-dictionaries.spec
  sed -i "s:@FILES@::" myspell-dictionaries.spec
  [ -x /usr/bin/spec-cleaner ] && spec-cleaner -i myspell-dictionaries.spec
}

#
# prepare 'dictionaries' directory
#

# download present git version, remove .git, unify layout
if [ $DOWNLOAD == "yes" ]; then 
  echo '--- Download current git version'
  rm -rf $GIT_DIR
  git clone --depth 30 git://anongit.freedesktop.org/libreoffice/$GIT_DIR
  pushd $GIT_DIR
  git log > ../REMOVE_GIT_LOG
  popd
  rm -rf $GIT_DIR/.git
  # exceptions >>>>>>>>>>>>>>>>>>>>>
  pushd $GIT_DIR
    for dir in ca gd_GB; do
      pushd $dir
        cp --force dictionaries/* .
        sed -i 's:dictionaries/::' dictionaries.xcu
      popd
    done
    # bug 914911 comment 10 ---
    # - gl: consistent file naming
    pushd gl
      for ext in aff dic; do
        mv gl_ES.$ext gl.$ext
        sed -i "s:gl_ES.$ext:gl.$ext:" dictionaries.xcu
      done
    popd
    # - de: remove _frami from filenames
    pushd de
      for var in AT CH DE; do
        for ext in aff dic; do
          mv de_${var}_frami.$ext de_${var}.$ext
          sed -i "s:de_${var}_frami.$ext:de_${var}.$ext:" dictionaries.xcu
        done
      done
      # remove hyph_de.dic, th_de_v2.dat, th_de_v2.idx links to
      # hyph_de_DE.dic, th_de_DE_v2.dat, th_de_DE_v2.idx
      sed -i 's:>de :>:' dictionaries.xcu
    popd
    # -ca: rename ca-valencia.{aff,dic} to ca_ES_valencia.{aff,dic}
    pushd ca
      for ext in aff dic; do
        mv ca-valencia.$ext ca_ES_valencia.$ext
        sed -i "s:ca-valencia.$ext:ca_ES_valencia.$ext:" dictionaries.xcu
      done
    popd
    # -------------------------
  popd
  # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  date=`date +%Y%m%d`
elif [ ! -e $GIT_DIR ]; then
  echo "ERROR: DOWNLOAD=$DOWNLOAD and '$GIT_DIR' does not exist"
  echo "Run quilt setup or so."
  exit 1
else
  echo "--- Do not download, using '$GIT_DIR'"
  date=`rpmspec -q --qf "%{VERSION}\n" *.spec | head -n 1`
fi

# create dir <-> locales <-> files mapping
# in $GIT_DIR/locale_to_file_map.txt
dirs=$(directories)
[ "$VERBOSE" == "yes" ] && echo directiories: $dirs
locale_to_file_map

# create *.idx files from *.dat files
echo '--- Creating idx files'
if [ ! -x /usr/bin/th_gen_idx.pl ]; then
  echo "ERROR: /usr/bin/th_gen_idx.pl not found"
  echo "Install mythes-devel package."
  exit 1
fi
for datf in $(dat_files); do
  idxf=$(idx_file $datf)
  [ "$VERBOSE" == "yes" ] && echo "th_gen_idx.pl < $GIT_DIR/$datf > $GIT_DIR/$idxf"
  th_gen_idx.pl < $GIT_DIR/$datf > $GIT_DIR/$idxf
  if [ $? -ne 0 ]; then
    echo "ERROR: failed th_gen_idx.pl -o $GIT_DIR/$idxf < $GIT_DIR/$datf"
    exit 1
  fi
done

#
# generate myspell-dictionaries.spec
#
echo '--- Generating spec file'

cp myspell-dictionaries.spec.in myspell-dictionaries.spec

sed -i "s:@DO_NOT_EDIT_COMMENT@:DO NOT EDIT THIS SPEC FILE:" myspell-dictionaries.spec
sed -i "s:@VERSION@:$date:" myspell-dictionaries.spec

# install main directories
dir_filelist=""
for d in $DATADIR/$DIC_DIR $DATADIR/$HYPH_DIR $DATADIR/$TH_DIR \
         $DATADIR/$COMPAT_DIR $LO_DIR $LODATA_DIR $LOEXT_DIR; do
  [ "$VERBOSE" == "yes" ] && echo "installing $DATADIR/$d"
  install_dir $d
  dir_filelist="$dir_filelist %dir_$d"
done
echo $dir_filelist
add_files "$dir_filelist"

# install dictionary files
for dir in $dirs; do
  files=$(dir_files $dir)
  # clear and declare filelist associative array
  unset filelist
  declare -A filelist
  declare -A requires

  [ "$VERBOSE" == "yes" ] && echo "DICTIONARY: $dir ($files)"
  for file in $files; do
    file_into_main_package=1
    fname=`basename $file`
    locales=$(file_locales $file)
    reg_file_locale=""
    [ "$VERBOSE" == "yes" ] && echo " $file: $locales"
    for locale in $locales; do
      # work around which is bug imho in dictionaries.xcu. 
      # It references file that doesn't exist.
      if [ ! -e "$GIT_DIR/$dir/$fname" ]; then
        [ "$VERBOSE" == "yes" ] && echo "WARNING: $GIT_DIR/$dir/$fname doesn't exist"
        continue;
      fi

      prefix=""
      version=""
      if [[ $fname == th* ]]; then
        # nice collision with th_ for thesaurus
        if [ "$fname" != "th_TH.aff" ] && [ "$fname" != "th_TH.dic" ]; then
          prefix="th_"
          # it seems suffix have to be _v2, even if target is named _v3 :)
          version='_v2'
        fi
      fi
      if [[ $fname == hyph* ]]; then
        prefix="hyph_"
      fi
      ext=`echo $fname | sed 's:.*\.::'`
      linkname=$prefix$locale$version.$ext

      [ "$VERBOSE" == "yes" ] && echo -n "  link: $linkname -> $fname .. "

      # regular file for this locale/extension exists yet, 
      # do not create symlink
      if [ -f $GIT_DIR/$dir/$linkname ]; then
        [ "$VERBOSE" == "yes" ] && 
          echo "regular file exists yet, not creating link"
        # should file go to language sub-subpackage?
        # if not, it will be installed later (search for ***)
        if [ "$locale" != "$dir" ]; then
          file_into_main_package=0
          # bug 914911 comment 10
          # the assumption is, that locale for regular file
          # is listed first in <value></value> @ dictionaries.xcu
          reg_file_locale="$locale"
          ipath=$(install_path $linkname)
          [ "$VERBOSE" == "yes" ] && 
            echo " install: $ipath (myspell-dictionaries-$locale)"
          install_regular $dir/$linkname $ipath
          filelist[$locale]="${filelist[$locale]} $ipath"
          compat_link="$DATADIR/$COMPAT_DIR/$linkname"
          [ "$VERBOSE" == "yes" ] && 
            echo " compat link install: $compat_link -> $ipath"
          install_link $ipath $compat_link
          filelist[$locale]="${filelist[$locale]} $compat_link"
        fi
        continue;
      fi

      # regular file $linkname does not exist yet, create symlink
      [ "$VERBOSE" == "yes" ] && echo "created"
      lipath=$(install_path $linkname)
      ripath=$(install_path $fname)
      [ "$VERBOSE" == "yes" ] && 
        echo "  link install: $lipath -> $ripath (myspell-dictionaries-$locale)"
      install_link $ripath $lipath
      # bug 914911 comment 10
      # the assumption is, that locale for regular file
      # is listed first in <value></value> @ dictionaries.xcu
      if [ ! -z "$reg_file_locale" ]; then
        if ! [[ ${requires[$locale]} =~ $reg_file_locale ]]; then
          [ "$VERBOSE" == "yes" ] && 
            echo "  => myspell-$locale depends on myspell-$reg_file_locale"
          requires[$locale]="${requires[$locale]} $reg_file_locale"
        fi
      fi
      filelist[$locale]="${filelist[$locale]} $lipath"
      compat_link=$DATADIR/$COMPAT_DIR/$linkname
      [ "$VERBOSE" == "yes" ] && 
        echo "  compat link install: $compat_link -> $lipath"
      install_link $lipath "$compat_link"
      filelist[$locale]="${filelist[$locale]} $compat_link"
    done

    # regular file to the main language subpackage if it is not in 
    # some its sub-subpackages (search for ***)
    if [ $file_into_main_package -eq 1 ]; then
      ipath=$(install_path $fname)
      [ "$VERBOSE" == "yes" ] && 
        echo " install: $ipath (myspell-dictionaries-$dir)"
      install_regular $file $ipath
      filelist[$dir]="${filelist[$dir]} $ipath"
      compat_link="$DATADIR/$COMPAT_DIR/$fname"
      [ "$VERBOSE" == "yes" ] && 
        echo " compat link install: $compat_link -> $ipath"
      install_link $ipath $compat_link
      filelist[$dir]="${filelist[$dir]} $compat_link"
    fi
  done

  # install lightproof files
  if have_lightproof $dir; then
    lightproof_files=`find $GIT_DIR/$dir -maxdepth 1 -name 'pythonpath' -o -name 'dialog' -o -name 'Lightproof*' -o \
                                                     -name 'Linguistic.xcu' -o -name 'META-INF' -o -name 'icons' -o \
                                                     -name 'description.xml'`
    install_dir "$LOEXT_DIR/lightproof-$dir"
    lightproof_filelist="%dir_$LOEXT_DIR/lightproof-$dir"
    for f in $lightproof_files; do
      ipath="$LOEXT_DIR/lightproof-$dir/`basename $f`"
      install_regular_recursive $dir/`basename $f` $ipath
      lightproof_filelist="$lightproof_filelist $ipath"
    done
  fi

  # install doc files
  doc_files=`find $GIT_DIR/$dir -maxdepth 1 -type f | grep '.txt\|.xcu\|.xml\|.png\|.tex\|^[^.]*$' || true`
  install_dir "$DOCDIR/myspell-$dir"
  filelist[$dir]="${filelist[$dir]} %dir_$DOCDIR/myspell-$dir"
  for f in $doc_files; do
    ipath="$DOCDIR/myspell-$dir/`basename $f`"
    install_regular $dir/`basename $f` $ipath
    filelist[$dir]="${filelist[$dir]} $ipath"
  done

  # write rpm subpackage information
  for pkg in "${!filelist[@]}"; do
    package_metadata $pkg $dir "${requires[$pkg]}"
    package_files myspell-$pkg "${filelist[$pkg]}"
  done
  if have_lightproof $dir; then
    lightproof_package_metadata $dir
    package_files myspell-lightproof-$dir "$lightproof_filelist"
  fi
done

finish_spec

#
# creating source archive
#
if [ $DOWNLOAD == "yes" ]; then
  echo '--- Creating archive'
  tar cJf dictionaries.tar.xz dictionaries
  rm -r dictionaries
fi

echo --- Done

#
# advice at the end ..
#
echo
echo With osc diff, figure out if there is a new package. 
echo If yes, add its license in License: tag of both 
echo *.spec and *.spec.in
echo if this license is not there yet.
echo
