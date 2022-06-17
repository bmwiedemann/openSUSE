#!/bin/bash
pkg_name="google-noto-fonts"
font_dir="ttf"

# Get only the hinted fonts
svn checkout https://github.com/googlefonts/noto-fonts/trunk/hinted/$font_dir
tar -cvzf $font_dir.tar.gz $font_dir/[!\.]*

cp -f $pkg_name.spec.in $pkg_name.spec
ls $font_dir/ | sed -e 's:Noto::' -e 's:-.*\..tf::' -e 's:\..tf::' -e 's:\.ttc::' | sort -f | uniq | while read font; do
  ui=`(echo $font | grep -q UI) && echo UI`
  font=${font%%$ui}
  serif=`echo $font | sed 's:\(Sans\|Serif\).*:\1:'`
  script=`echo $font | sed "s:$serif\(.*\):\1:"`
  packagename="noto-$serif"
  if [ ! -z $script ]; then
    packagename="$packagename-$script"
  fi
  if [ ! -z $ui ]; then
    packagename="$packagename-$ui"
  fi
  packagename=`echo "$packagename" | tr [A-Z] [a-z]`
  # NotoSansDisplay is already provided by NotoSans
  # Also they have inconsistent family names: https://github.com/googlefonts/noto-fonts/issues/2315
  if [ $packagename == "noto-sans-display" ]; then
    continue
  fi
  if [ $serif == "Sans" ]; then
    serif_dsc="Sans Serif "
  else
    serif_dsc=""
  fi
  if [ $packagename == "noto-sans" ]; then
    OBSOLETES=($packagename 'noto-sans-display' 'noto-sans-display-fonts')
  elif [ $packagename == "noto-serif-tibetan" ]; then
    OBSOLETES=($packagename 'noto-sans-tibetan' 'noto-sans-tibetan-fonts')
  elif [ $packagename == "noto-sans-syriac" ]; then
    OBSOLETES=($packagename 'noto-sans-syriacwestern' 'noto-sans-syriacwestern-fonts' 'noto-sans-syriacestrangela' 'noto-sans-syriacestrangela-fonts' 'noto-sans-syriaceastern' 'noto-sans-syriaceastern-fonts')
  elif [ $packagename == "noto-sans-mono" ]; then
    OBSOLETES=($packagename 'noto-mono' 'noto-mono-fonts')
  elif [ $packagename == "noto-arimo" ] || [ $packagename == "noto-cousine" ] || [ $packagename == "noto-tinos" ]; then
    OBSOLETES=($packagename `echo "google-$serif-fonts" | tr [A-Z] [a-z]`)
  else
    OBSOLETES=($packagename)
  fi
  packagename="$packagename-fonts"
  if [ ! -z "$script" ]; then
    summary=`echo "Noto $script ${serif_dsc}Font" | sed 's:\([a-z]\)\([A-Z]\):\1 \2:g'`
  else
    summary=`echo "Noto $serif Font" | sed 's:\([a-z]\)\([A-Z]\):\1 \2:g'`
  fi
  sed -i "s/@LIST_OF_SUBPACKAGES@/Requires:      $packagename\n@LIST_OF_SUBPACKAGES@/" $pkg_name.spec
  sed -i "s/@SUBPACKAGE_HEADERS@/%package -n $packagename\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
  sed -i "s/@SUBPACKAGE_HEADERS@/Summary:        $summary\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
  sed -i "s;@SUBPACKAGE_HEADERS@;Group:          System/X11/Fonts\n@SUBPACKAGE_HEADERS@;" $pkg_name.spec
  for i in "${OBSOLETES[@]}" ; do
    sed -i "s/@SUBPACKAGE_HEADERS@/Obsoletes:      $i < %{version}\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
    sed -i "s/@SUBPACKAGE_HEADERS@/Provides:       $i = %{version}\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
  done
  sed -i "s/@SUBPACKAGE_HEADERS@/%reconfigure_fonts_prereq\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
  sed -i "s/@SUBPACKAGE_HEADERS@/\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
  sed -i "s/@SUBPACKAGE_HEADERS@/%description -n $packagename\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
  sed -i "s/@SUBPACKAGE_HEADERS@/Noto's design goal is to achieve visual harmonization (e.g., compatible\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
  sed -i "s/@SUBPACKAGE_HEADERS@/heights and stroke thicknesses) across languages. This package contains\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
  if [ ! -z "$script" ]; then
    sed -i "s/@SUBPACKAGE_HEADERS@/$script ${serif_dsc}font, hinted.\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
  else
    sed -i "s/@SUBPACKAGE_HEADERS@/$serif font, hinted.\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
  fi
  sed -i "s/@SUBPACKAGE_HEADERS@/\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec

  sed -i "s/@SUBPACKAGE_SCRIPTLETS@/%reconfigure_fonts_scriptlets -n $packagename\n\n@SUBPACKAGE_SCRIPTLETS@/" $pkg_name.spec

  sed -i "s/@SUBPACKAGE_FILELISTS@/%files -n $packagename\n@SUBPACKAGE_FILELISTS@/" $pkg_name.spec
  sed -i "s/@SUBPACKAGE_FILELISTS@/%defattr(0644,root,root,755)\n@SUBPACKAGE_FILELISTS@/" $pkg_name.spec
  sed -i "s/@SUBPACKAGE_FILELISTS@/%license LICENSE\n@SUBPACKAGE_FILELISTS@/" $pkg_name.spec
  sed -i "s/@SUBPACKAGE_FILELISTS@/%dir %{_ttfontsdir}\n@SUBPACKAGE_FILELISTS@/" $pkg_name.spec
  if [ $serif == "Arimo" ] || [ $serif == "Cousine" ] || [ $serif == "Tinos" ]; then
    sed -i "s:@SUBPACKAGE_FILELISTS@:%{_ttfontsdir}/$serif$script$ui-\*.?tf\n@SUBPACKAGE_FILELISTS@:" $pkg_name.spec
  else
    sed -i "s:@SUBPACKAGE_FILELISTS@:%{_ttfontsdir}/Noto$serif$script$ui-\*.?tf\n@SUBPACKAGE_FILELISTS@:" $pkg_name.spec
  fi
  sed -i "s/@SUBPACKAGE_FILELISTS@/\n@SUBPACKAGE_FILELISTS@/" $pkg_name.spec
done

sed -i 's/@LIST_OF_SUBPACKAGES@//' $pkg_name.spec
sed -i 's/@SUBPACKAGE_HEADERS@//' $pkg_name.spec
sed -i 's/@SUBPACKAGE_SCRIPTLETS@//' $pkg_name.spec
sed -i 's/@SUBPACKAGE_FILELISTS@//' $pkg_name.spec
