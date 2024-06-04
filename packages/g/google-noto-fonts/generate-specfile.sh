#!/bin/bash
# This script is used to generate all of the many hundreds of font
# subpackages for google-noto-fonts. It generates a subpackage
# description based on each font folder in the tarball.
# Packagers should not change google-noto-fonts.spec directly but
# instead alter this and google-noto-fonts.spec.in to achieve the
# desired result.
# This is so that future packagers can simply run this script and
# get an updated specfile with all of the new subpackages.
# This is a bash script because POSIX-shell does not define
# arrays and they are needed to list the many obsoletes and provides
# that various subpackages need.

# Make new seperate packages for arimo, cousine, and tinos

# https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
set -euo pipefail

pkg_name="google-noto-fonts"
font_dir="notofonts.github.io-noto-monthly-release-24.6.1"

# Used to extract the tarball to generate the specfile.
# You can comment this out while testing out changes to the script,
# just remember to uncomment before commiting!
tar -x -f $font_dir.tar.gz

cp -f $pkg_name.spec.in $pkg_name.spec
ls $font_dir/fonts | sed -e 's:Noto::' -e 's:-.*\..tf::' -e 's:\..tf::' -e 's:\.ttc::' | sort -f | uniq | while read -r font; do

	# DO NOT create font packages out of these folders.
	if [ "$font" == "LICENSE" ] || [ "$font" == "SansTest" ] || [ "$font" == "SerifTest" ] || [ "$font" == "NaskhArabicUI" ]; then
		continue
	fi

	# Generate the noto-* part of the package name.
	serif=$(echo "$font" | sed 's:\(Sans\|Serif\).*:\1:')
	script=$(echo "$font" | sed "s:$serif\(.*\):\1:")
	packagename="noto-$serif"
	if [ -n "$script" ]; then
		packagename="$packagename-$script"
	fi
	packagename=$(echo "$packagename" | tr '[:upper:]' '[:lower:]')
	if [ "$serif" == "Sans" ]; then
		serif_dsc="Sans Serif "
	else
		serif_dsc="Serif "
	fi

	## Deal with all of the obsoletes and provides created by various font
	## renamings, mergers, and splits over the years.
	# This block contains fonts which previously had an noto-*-ui-fonts subpackage
	# but Google placed the UI fonts into the same folder as the noto-*-fonts folder
	# so now they all belong to the same font.
	if [ "$packagename" == "noto-sans-thailooped" ]; then
		OBSOLETES=('noto-loopedthai' 'noto-loopedthai-fonts' 'noto-loopedthai-ui' 'noto-loopedthai-ui-fonts')
	elif [ "$packagename" == "noto-sans-laolooped" ]; then
		OBSOLETES=('noto-loopedlao' 'noto-loopedlao-fonts' 'noto-loopedlao-ui' 'noto-loopedlao-ui-fonts')
	elif [ "$packagename" == "noto-naskharabic" ] || [ "$packagename" == "noto-sans-arabic" ] || [ "$packagename" == "noto-sans-bengali" ] || [ "$packagename" == "noto-sans-devanagari" ] || [ "$packagename" == "noto-sans-gujarati" ] || [ "$packagename" == "noto-sans-gurmukhi" ] || [ "$packagename" == "noto-sans-kannada" ] || [ "$packagename" == "noto-sans-khmer" ] || [ "$packagename" == "noto-sans-lao" ] || [ "$packagename" == "noto-sans-malayalam" ] || [ "$packagename" == "noto-sans-myanmar" ] || [ "$packagename" == "noto-sans-oriya" ] || [ "$packagename" == "noto-sans-sinhala" ] || [ "$packagename" == "noto-sans-tamil" ] || [ "$packagename" == "noto-sans-telugu" ] || [ "$packagename" == "noto-sans-thai" ]; then
		OBSOLETES=("$packagename" "$packagename-fonts" "$packagename-ui" "$packagename-ui-fonts")
	elif [ "$packagename" == "noto-serif-nphmong" ]; then
		OBSOLETES+=('noto-serif-nyiakengpuachuehmong' 'noto-serif-nyiakengpuachuehmong-fonts')
	# This block is for the rest of the fonts...
	else
		OBSOLETES=("$packagename" "$packagename-fonts")
		if [ "$packagename" == "noto-sans" ]; then
			OBSOLETES+=('noto-sans-display' 'noto-sans-display-fonts')
		elif [ "$packagename" == "noto-serif-tibetan" ]; then
			OBSOLETES+=('noto-sans-tibetan' 'noto-sans-tibetan-fonts')
		elif [ "$packagename" == "noto-sans-syriac" ]; then
			OBSOLETES+=('noto-sans-syriacestrangela' 'noto-sans-syriacestrangela-fonts')
		elif [ "$packagename" == "noto-sans-mono" ]; then
			OBSOLETES+=('noto-mono' 'noto-mono-fonts')
		elif [ "$packagename" == "noto-arimo" ] || [ "$packagename" == "noto-cousine" ] || [ "$packagename" == "noto-tinos" ]; then
			OBSOLETES+=("google-$serif-fonts")
		elif [ "$packagename" == "noto-sans-hebrew" ]; then
			OBSOLETES+=('noto-sans-hebrewnew' 'noto-sans-hebrewnew-fonts' 'noto-sans-hebrewdroid' 'noto-sans-hebrewdroid-fonts')
		elif [ "$packagename" == "noto-sans-tifinagh" ]; then
			OBSOLETES+=('noto-sans-tifinaghadrar' 'noto-sans-tifinaghadrar-fonts' 'noto-sans-tifinaghagrawimazighen' 'noto-sans-tifinaghagrawimazighen-fonts' 'noto-sans-tifinaghahaggar' 'noto-sans-tifinaghahaggar-fonts' 'noto-sans-tifinaghair' 'noto-sans-tifinaghair-fonts' 'noto-sans-tifinaghapt' 'noto-sans-tifinaghapt-fonts' 'noto-sans-tifinaghazawagh' 'noto-sans-tifinaghazawagh-fonts' 'noto-sans-tifinaghghat' 'noto-sans-tifinaghghat-fonts' 'noto-sans-tifinaghhawad' 'noto-sans-tifinaghhawad-fonts' 'noto-sans-tifinaghrhissaixa' 'noto-sans-tifinaghrhissaixa-fonts' 'noto-sans-tifinaghsil' 'noto-sans-tifinaghsil-fonts' 'noto-sans-tifinaghtawellemmet' 'noto-sans-tifinaghtawellemmet-fonts')
		fi
	fi

	packagename="google-$packagename-fonts"

	# Create the correct package description for fonts with or without an
	# Sans/Serif in their name.
	if [ -n "$script" ]; then
		summary=$(echo "Noto $script ${serif_dsc}Font" | sed 's:\([a-z]\)\([A-Z]\):\1 \2:g')
	else
		summary=$(echo "Noto $serif Font" | sed 's:\([a-z]\)\([A-Z]\):\1 \2:g')
	fi

	# This chunk of sed commands puts the subpackages into the specfile.
	# Check out google-noto-fonts.spec.in to see where the placeholder @@
	# are placed.
	sed -i "s/@LIST_OF_SUBPACKAGES@/Requires:       $packagename\n@LIST_OF_SUBPACKAGES@/" $pkg_name.spec
	sed -i "s/@SUBPACKAGE_HEADERS@/%package -n $packagename\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
	sed -i "s/@SUBPACKAGE_HEADERS@/Summary:        $summary\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
	for i in "${OBSOLETES[@]}"; do
		sed -i "s/@SUBPACKAGE_HEADERS@/Obsoletes:      $i < %{version}\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
		sed -i "s/@SUBPACKAGE_HEADERS@/Provides:       $i = %{version}\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
	done
	sed -i "s/@SUBPACKAGE_HEADERS@/%reconfigure_fonts_prereq\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
	sed -i "s/@SUBPACKAGE_HEADERS@/\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
	sed -i "s/@SUBPACKAGE_HEADERS@/%description -n $packagename\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
	sed -i "s/@SUBPACKAGE_HEADERS@/Noto's design goal is to achieve visual harmonization (e.g., compatible\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
	sed -i "s/@SUBPACKAGE_HEADERS@/heights and stroke thicknesses) across languages. This package contains\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
	if [ -n "$script" ]; then
		sed -i "s/@SUBPACKAGE_HEADERS@/$script ${serif_dsc}font, hinted.\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
	else
		sed -i "s/@SUBPACKAGE_HEADERS@/$serif font, hinted.\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
	fi
	sed -i "s/@SUBPACKAGE_HEADERS@/\n@SUBPACKAGE_HEADERS@/" $pkg_name.spec
	sed -i "s/@SUBPACKAGE_SCRIPTLETS@/%reconfigure_fonts_scriptlets -n $packagename\n\n@SUBPACKAGE_SCRIPTLETS@/" $pkg_name.spec
	sed -i "s/@SUBPACKAGE_FILELISTS@/%files -n $packagename\n@SUBPACKAGE_FILELISTS@/" $pkg_name.spec
	sed -i "s/@SUBPACKAGE_FILELISTS@/%license LICENSE\n@SUBPACKAGE_FILELISTS@/" $pkg_name.spec
	sed -i "s/@SUBPACKAGE_FILELISTS@/%dir %{_ttfontsdir}\n@SUBPACKAGE_FILELISTS@/" $pkg_name.spec

	# These are exceptions for font files being named differently.
	if [ "$packagename" == "google-noto-naskharabic-fonts" ] || [ "$packagename" == "google-noto-sans-bengali-fonts" ] || [ "$packagename" == "google-noto-sans-devanagari-fonts" ] || [ "$packagename" == "google-noto-sans-gujarati-fonts" ] || [ "$packagename" == "google-noto-sans-gurmukhi-fonts" ] || [ "$packagename" == "google-noto-sans-kannada-fonts" ] || [ "$packagename" == "google-noto-sans-malayalam-fonts" ] || [ "$packagename" == "google-noto-sans-sinhala-fonts" ] || [ "$packagename" == "google-noto-sans-tamil-fonts" ] || [ "$packagename" == "google-noto-sans-telugu-fonts" ]; then
		sed -i "s:@SUBPACKAGE_FILELISTS@:%{_ttfontsdir}/Noto$serif$script-\*.?tf\n%{_ttfontsdir}/Noto$serif${script}UI-\*.?tf\n@SUBPACKAGE_FILELISTS@:" $pkg_name.spec
	elif [ "$packagename" == "google-noto-sans-tifinagh-fonts" ]; then
		sed -i "s:@SUBPACKAGE_FILELISTS@:%{_ttfontsdir}/Noto$serif$script\*.?tf\n@SUBPACKAGE_FILELISTS@:" $pkg_name.spec
	else
		sed -i "s:@SUBPACKAGE_FILELISTS@:%{_ttfontsdir}/Noto$serif$script-\*.?tf\n@SUBPACKAGE_FILELISTS@:" $pkg_name.spec
	fi
	sed -i "s/@SUBPACKAGE_FILELISTS@/\n@SUBPACKAGE_FILELISTS@/" $pkg_name.spec
done

# Remove the @@ placeholders once we are done.
sed -i 's/@LIST_OF_SUBPACKAGES@//' $pkg_name.spec
sed -i 's/@SUBPACKAGE_HEADERS@//' $pkg_name.spec
sed -i 's/@SUBPACKAGE_SCRIPTLETS@//' $pkg_name.spec
sed -i 's/@SUBPACKAGE_FILELISTS@//' $pkg_name.spec
