#!/bin/sh
pkg_name="google-noto-fonts"

for a in *.zip; do
	mkdir -p $pkg_name
	unzip -o -d $pkg_name $a
done

rm $pkg_name/LICENSE_OFL.txt
# remove cjk
rm $pkg_name/*CJK*.?tf
# remove emoji
rm $pkg_name/*Emoji*.ttf
# remove README
rm $pkg_name/README

cp -f $pkg_name.spec.in $pkg_name.spec
ls $pkg_name/ | sed -e 's:Noto::' -e 's:-.*\..tf::' -e 's:\..tf::' -e 's:\.ttc::' | sort -f | uniq | while read font; do 
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
  if [ $serif == "Sans" ]; then
    serif_dsc="Sans Serif "
  else
    serif_dsc=""
  fi
  obsoletes=$packagename
  packagename="$packagename-fonts"
  if [ ! -z "$script" ]; then
    summary=`echo "Noto $script ${serif_dsc}Font" | sed 's:\([a-z]\)\([A-Z]\):\1 \2:g'`
  else
    summary=`echo "Noto $serif Font" | sed 's:\([a-z]\)\([A-Z]\):\1 \2:g'`
  fi
  sed -i "s/@SUBPACKAGE_HEADERS@/%package -n $packagename\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
  sed -i "s/@SUBPACKAGE_HEADERS@/Summary:        $summary\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
  sed -i "s;@SUBPACKAGE_HEADERS@;Group:          System/X11/Fonts\n@SUBPACKAGE_HEADERS@;" $pkg_name.spec
  sed -i "s/@SUBPACKAGE_HEADERS@/Recommends:     $pkg_name-doc\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
  for i in $obsoletes ; do
    sed -i "s/@SUBPACKAGE_HEADERS@/Obsoletes:      $i\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
    sed -i "s/@SUBPACKAGE_HEADERS@/Provides:       $i\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
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
  sed -i "s/@SUBPACKAGE_FILELISTS@/%dir %{_ttfontsdir}\n@SUBPACKAGE_FILELISTS@/" $pkg_name.spec
  if [ $serif == "ColorEmoji" ]; then
    sed -i "s:@SUBPACKAGE_FILELISTS@:%{_ttfontsdir}/Noto$serif$script$ui\*.?tf\n@SUBPACKAGE_FILELISTS@:" $pkg_name.spec
  else
    sed -i "s:@SUBPACKAGE_FILELISTS@:%{_ttfontsdir}/Noto$serif$script$ui-\*.?tf\n@SUBPACKAGE_FILELISTS@:" $pkg_name.spec
  fi
  sed -i "s/@SUBPACKAGE_FILELISTS@/\n@SUBPACKAGE_FILELISTS@/" $pkg_name.spec
done

sed -i 's/@SUBPACKAGE_HEADERS@//' $pkg_name.spec
sed -i 's/@SUBPACKAGE_SCRIPTLETS@//' $pkg_name.spec
sed -i 's/@SUBPACKAGE_FILELISTS@//' $pkg_name.spec

rm -r $pkg_name
