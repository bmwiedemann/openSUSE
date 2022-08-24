#
# spec file for package google-noto-fonts
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define hyear     2022
%define hmonth    06
%define hday      07

%define src_name  NotoFonts

# DO NOT EDIT THIS SPECFILE DIRECTLY, edit google-noto-fonts.spec.in and run generate-fonts-and-specfile.sh script

Name:           google-noto-fonts
Version:        %{hyear}%{hmonth}%{hday}
Release:        0
Summary:        Noto Font Families
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/googlefonts/noto-fonts
# Generate Source0 via generate-fonts-and-specfile.sh
Source0:        ttf.tar.gz
Source1:        generate-fonts-and-specfile.sh
Source2:        LICENSE
Source3:        README.FAQ
Patch0:         fix-arimo.patch
BuildRequires:  fontpackages-devel
BuildRequires:  fonttools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Noto's design goal is to achieve visual harmonization (e.g., compatible heights and stroke
thicknesses) across languages.

%package -n noto-fonts
Summary:        All Noto Fonts except CJK and Emoji
Group:          System/X11/Fonts
Requires:       noto-arimo-fonts
Requires:       noto-cousine-fonts
Requires:       noto-kufiarabic-fonts
Requires:       noto-loopedlao-fonts
Requires:       noto-loopedlao-ui-fonts
Requires:       noto-loopedthai-fonts
Requires:       noto-loopedthai-ui-fonts
Requires:       noto-music-fonts
Requires:       noto-naskharabic-fonts
Requires:       noto-naskharabic-ui-fonts
Requires:       noto-nastaliqurdu-fonts
Requires:       noto-rashihebrew-fonts
Requires:       noto-sans-adlam-fonts
Requires:       noto-sans-adlamunjoined-fonts
Requires:       noto-sans-anatolianhieroglyphs-fonts
Requires:       noto-sans-arabic-fonts
Requires:       noto-sans-arabic-ui-fonts
Requires:       noto-sans-armenian-fonts
Requires:       noto-sans-avestan-fonts
Requires:       noto-sans-balinese-fonts
Requires:       noto-sans-bamum-fonts
Requires:       noto-sans-bassavah-fonts
Requires:       noto-sans-batak-fonts
Requires:       noto-sans-bengali-fonts
Requires:       noto-sans-bengali-ui-fonts
Requires:       noto-sans-bhaiksuki-fonts
Requires:       noto-sans-brahmi-fonts
Requires:       noto-sans-buginese-fonts
Requires:       noto-sans-buhid-fonts
Requires:       noto-sans-canadianaboriginal-fonts
Requires:       noto-sans-carian-fonts
Requires:       noto-sans-caucasianalbanian-fonts
Requires:       noto-sans-chakma-fonts
Requires:       noto-sans-cham-fonts
Requires:       noto-sans-cherokee-fonts
Requires:       noto-sans-chorasmian-fonts
Requires:       noto-sans-coptic-fonts
Requires:       noto-sans-cuneiform-fonts
Requires:       noto-sans-cypriot-fonts
Requires:       noto-sans-cyprominoan-fonts
Requires:       noto-sans-deseret-fonts
Requires:       noto-sans-devanagari-fonts
Requires:       noto-sans-devanagari-ui-fonts
Requires:       noto-sans-duployan-fonts
Requires:       noto-sans-egyptianhieroglyphs-fonts
Requires:       noto-sans-elbasan-fonts
Requires:       noto-sans-elymaic-fonts
Requires:       noto-sans-ethiopic-fonts
Requires:       noto-sans-fonts
Requires:       noto-sans-georgian-fonts
Requires:       noto-sans-glagolitic-fonts
Requires:       noto-sans-gothic-fonts
Requires:       noto-sans-grantha-fonts
Requires:       noto-sans-gujarati-fonts
Requires:       noto-sans-gujarati-ui-fonts
Requires:       noto-sans-gunjalagondi-fonts
Requires:       noto-sans-gurmukhi-fonts
Requires:       noto-sans-gurmukhi-ui-fonts
Requires:       noto-sans-hanifirohingya-fonts
Requires:       noto-sans-hanunoo-fonts
Requires:       noto-sans-hatran-fonts
Requires:       noto-sans-hebrew-fonts
Requires:       noto-sans-hebrewdroid-fonts
Requires:       noto-sans-hebrewnew-fonts
Requires:       noto-sans-imperialaramaic-fonts
Requires:       noto-sans-indicsiyaqnumbers-fonts
Requires:       noto-sans-inscriptionalpahlavi-fonts
Requires:       noto-sans-inscriptionalparthian-fonts
Requires:       noto-sans-javanese-fonts
Requires:       noto-sans-kaithi-fonts
Requires:       noto-sans-kannada-fonts
Requires:       noto-sans-kannada-ui-fonts
Requires:       noto-sans-kayahli-fonts
Requires:       noto-sans-kharoshthi-fonts
Requires:       noto-sans-khmer-fonts
Requires:       noto-sans-khmer-ui-fonts
Requires:       noto-sans-khojki-fonts
Requires:       noto-sans-khudawadi-fonts
Requires:       noto-sans-lao-fonts
Requires:       noto-sans-lao-ui-fonts
Requires:       noto-sans-lepcha-fonts
Requires:       noto-sans-limbu-fonts
Requires:       noto-sans-lineara-fonts
Requires:       noto-sans-linearb-fonts
Requires:       noto-sans-lisu-fonts
Requires:       noto-sans-lycian-fonts
Requires:       noto-sans-lydian-fonts
Requires:       noto-sans-mahajani-fonts
Requires:       noto-sans-malayalam-fonts
Requires:       noto-sans-malayalam-ui-fonts
Requires:       noto-sans-mandaic-fonts
Requires:       noto-sans-manichaean-fonts
Requires:       noto-sans-marchen-fonts
Requires:       noto-sans-masaramgondi-fonts
Requires:       noto-sans-math-fonts
Requires:       noto-sans-mayannumerals-fonts
Requires:       noto-sans-medefaidrin-fonts
Requires:       noto-sans-meeteimayek-fonts
Requires:       noto-sans-mendekikakui-fonts
Requires:       noto-sans-meroitic-fonts
Requires:       noto-sans-miao-fonts
Requires:       noto-sans-modi-fonts
Requires:       noto-sans-mongolian-fonts
Requires:       noto-sans-mono-fonts
Requires:       noto-sans-mro-fonts
Requires:       noto-sans-multani-fonts
Requires:       noto-sans-myanmar-fonts
Requires:       noto-sans-myanmar-ui-fonts
Requires:       noto-sans-nabataean-fonts
Requires:       noto-sans-nandinagari-fonts
Requires:       noto-sans-newa-fonts
Requires:       noto-sans-newtailue-fonts
Requires:       noto-sans-nko-fonts
Requires:       noto-sans-nushu-fonts
Requires:       noto-sans-ogham-fonts
Requires:       noto-sans-olchiki-fonts
Requires:       noto-sans-oldhungarian-fonts
Requires:       noto-sans-olditalic-fonts
Requires:       noto-sans-oldnortharabian-fonts
Requires:       noto-sans-oldpermic-fonts
Requires:       noto-sans-oldpersian-fonts
Requires:       noto-sans-oldsogdian-fonts
Requires:       noto-sans-oldsoutharabian-fonts
Requires:       noto-sans-oldturkic-fonts
Requires:       noto-sans-oriya-fonts
Requires:       noto-sans-oriya-ui-fonts
Requires:       noto-sans-osage-fonts
Requires:       noto-sans-osmanya-fonts
Requires:       noto-sans-pahawhhmong-fonts
Requires:       noto-sans-palmyrene-fonts
Requires:       noto-sans-paucinhau-fonts
Requires:       noto-sans-phagspa-fonts
Requires:       noto-sans-phoenician-fonts
Requires:       noto-sans-psalterpahlavi-fonts
Requires:       noto-sans-rejang-fonts
Requires:       noto-sans-runic-fonts
Requires:       noto-sans-samaritan-fonts
Requires:       noto-sans-saurashtra-fonts
Requires:       noto-sans-sharada-fonts
Requires:       noto-sans-shavian-fonts
Requires:       noto-sans-siddham-fonts
Requires:       noto-sans-signwriting-fonts
Requires:       noto-sans-sinhala-fonts
Requires:       noto-sans-sinhala-ui-fonts
Requires:       noto-sans-sogdian-fonts
Requires:       noto-sans-sorasompeng-fonts
Requires:       noto-sans-soyombo-fonts
Requires:       noto-sans-sundanese-fonts
Requires:       noto-sans-sylotinagri-fonts
Requires:       noto-sans-symbols-fonts
Requires:       noto-sans-symbols2-fonts
Requires:       noto-sans-syriac-fonts
Requires:       noto-sans-tagalog-fonts
Requires:       noto-sans-tagbanwa-fonts
Requires:       noto-sans-taile-fonts
Requires:       noto-sans-taitham-fonts
Requires:       noto-sans-taiviet-fonts
Requires:       noto-sans-takri-fonts
Requires:       noto-sans-tamil-fonts
Requires:       noto-sans-tamil-ui-fonts
Requires:       noto-sans-tamilsupplement-fonts
Requires:       noto-sans-tangsa-fonts
Requires:       noto-sans-telugu-fonts
Requires:       noto-sans-telugu-ui-fonts
Requires:       noto-sans-thaana-fonts
Requires:       noto-sans-thai-fonts
Requires:       noto-sans-thai-ui-fonts
Requires:       noto-sans-tifinagh-fonts
Requires:       noto-sans-tifinaghadrar-fonts
Requires:       noto-sans-tifinaghagrawimazighen-fonts
Requires:       noto-sans-tifinaghahaggar-fonts
Requires:       noto-sans-tifinaghair-fonts
Requires:       noto-sans-tifinaghapt-fonts
Requires:       noto-sans-tifinaghazawagh-fonts
Requires:       noto-sans-tifinaghghat-fonts
Requires:       noto-sans-tifinaghhawad-fonts
Requires:       noto-sans-tifinaghrhissaixa-fonts
Requires:       noto-sans-tifinaghsil-fonts
Requires:       noto-sans-tifinaghtawellemmet-fonts
Requires:       noto-sans-tirhuta-fonts
Requires:       noto-sans-ugaritic-fonts
Requires:       noto-sans-vai-fonts
Requires:       noto-sans-vithkuqi-fonts
Requires:       noto-sans-wancho-fonts
Requires:       noto-sans-warangciti-fonts
Requires:       noto-sans-yi-fonts
Requires:       noto-sans-zanabazarsquare-fonts
Requires:       noto-serif-ahom-fonts
Requires:       noto-serif-armenian-fonts
Requires:       noto-serif-balinese-fonts
Requires:       noto-serif-bengali-fonts
Requires:       noto-serif-devanagari-fonts
Requires:       noto-serif-display-fonts
Requires:       noto-serif-divesakuru-fonts
Requires:       noto-serif-dogra-fonts
Requires:       noto-serif-ethiopic-fonts
Requires:       noto-serif-fonts
Requires:       noto-serif-georgian-fonts
Requires:       noto-serif-grantha-fonts
Requires:       noto-serif-gujarati-fonts
Requires:       noto-serif-gurmukhi-fonts
Requires:       noto-serif-hebrew-fonts
Requires:       noto-serif-kannada-fonts
Requires:       noto-serif-khmer-fonts
Requires:       noto-serif-khojki-fonts
Requires:       noto-serif-lao-fonts
Requires:       noto-serif-makasar-fonts
Requires:       noto-serif-malayalam-fonts
Requires:       noto-serif-myanmar-fonts
Requires:       noto-serif-nyiakengpuachuehmong-fonts
Requires:       noto-serif-olduyghur-fonts
Requires:       noto-serif-oriya-fonts
Requires:       noto-serif-sinhala-fonts
Requires:       noto-serif-tamil-fonts
Requires:       noto-serif-tamilslanted-fonts
Requires:       noto-serif-tangut-fonts
Requires:       noto-serif-telugu-fonts
Requires:       noto-serif-thai-fonts
Requires:       noto-serif-tibetan-fonts
Requires:       noto-serif-toto-fonts
Requires:       noto-serif-vithkuqi-fonts
Requires:       noto-serif-yezidi-fonts
Requires:       noto-tinos-fonts
Requires:       noto-traditionalnushu-fonts

%description -n noto-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
most noto fonts except for CJK and Emoji.

%package -n noto-arimo-fonts
Summary:        Noto Arimo Font
Group:          System/X11/Fonts
Obsoletes:      noto-arimo < %{version}
Provides:       noto-arimo = %{version}
Obsoletes:      google-arimo-fonts < %{version}
Provides:       google-arimo-fonts = %{version}
%reconfigure_fonts_prereq

%description -n noto-arimo-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Arimo font, hinted.

%package -n noto-cousine-fonts
Summary:        Noto Cousine Font
Group:          System/X11/Fonts
Obsoletes:      noto-cousine < %{version}
Provides:       noto-cousine = %{version}
Obsoletes:      google-cousine-fonts < %{version}
Provides:       google-cousine-fonts = %{version}
%reconfigure_fonts_prereq

%description -n noto-cousine-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cousine font, hinted.

%package -n noto-kufiarabic-fonts
Summary:        Noto Kufi Arabic Font
Group:          System/X11/Fonts
Obsoletes:      noto-kufiarabic < %{version}
Provides:       noto-kufiarabic = %{version}
%reconfigure_fonts_prereq

%description -n noto-kufiarabic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
KufiArabic font, hinted.

%package -n noto-loopedlao-fonts
Summary:        Noto Looped Lao Font
Group:          System/X11/Fonts
Obsoletes:      noto-loopedlao < %{version}
Provides:       noto-loopedlao = %{version}
%reconfigure_fonts_prereq

%description -n noto-loopedlao-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
LoopedLao font, hinted.

%package -n noto-loopedlao-ui-fonts
Summary:        Noto Looped Lao Font
Group:          System/X11/Fonts
Obsoletes:      noto-loopedlao-ui < %{version}
Provides:       noto-loopedlao-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-loopedlao-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
LoopedLao font, hinted.

%package -n noto-loopedthai-fonts
Summary:        Noto Looped Thai Font
Group:          System/X11/Fonts
Obsoletes:      noto-loopedthai < %{version}
Provides:       noto-loopedthai = %{version}
%reconfigure_fonts_prereq

%description -n noto-loopedthai-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
LoopedThai font, hinted.

%package -n noto-loopedthai-ui-fonts
Summary:        Noto Looped Thai Font
Group:          System/X11/Fonts
Obsoletes:      noto-loopedthai-ui < %{version}
Provides:       noto-loopedthai-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-loopedthai-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
LoopedThai font, hinted.

%package -n noto-music-fonts
Summary:        Noto Music Font
Group:          System/X11/Fonts
Obsoletes:      noto-music < %{version}
Provides:       noto-music = %{version}
%reconfigure_fonts_prereq

%description -n noto-music-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Music font, hinted.

%package -n noto-naskharabic-fonts
Summary:        Noto Naskh Arabic Font
Group:          System/X11/Fonts
Obsoletes:      noto-naskharabic < %{version}
Provides:       noto-naskharabic = %{version}
%reconfigure_fonts_prereq

%description -n noto-naskharabic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NaskhArabic font, hinted.

%package -n noto-naskharabic-ui-fonts
Summary:        Noto Naskh Arabic Font
Group:          System/X11/Fonts
Obsoletes:      noto-naskharabic-ui < %{version}
Provides:       noto-naskharabic-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-naskharabic-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NaskhArabic font, hinted.

%package -n noto-nastaliqurdu-fonts
Summary:        Noto Nastaliq Urdu Font
Group:          System/X11/Fonts
Obsoletes:      noto-nastaliqurdu < %{version}
Provides:       noto-nastaliqurdu = %{version}
%reconfigure_fonts_prereq

%description -n noto-nastaliqurdu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NastaliqUrdu font, hinted.

%package -n noto-rashihebrew-fonts
Summary:        Noto Rashi Hebrew Font
Group:          System/X11/Fonts
Obsoletes:      noto-rashihebrew < %{version}
Provides:       noto-rashihebrew = %{version}
%reconfigure_fonts_prereq

%description -n noto-rashihebrew-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
RashiHebrew font, hinted.

%package -n noto-sans-fonts
Summary:        Noto Sans Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans < %{version}
Provides:       noto-sans = %{version}
Obsoletes:      noto-sans-display < %{version}
Provides:       noto-sans-display = %{version}
Obsoletes:      noto-sans-display-fonts < %{version}
Provides:       noto-sans-display-fonts = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sans font, hinted.

%package -n noto-sans-adlam-fonts
Summary:        Noto Adlam Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-adlam < %{version}
Provides:       noto-sans-adlam = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-adlam-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Adlam Sans Serif font, hinted.

%package -n noto-sans-adlamunjoined-fonts
Summary:        Noto Adlam Unjoined Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-adlamunjoined < %{version}
Provides:       noto-sans-adlamunjoined = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-adlamunjoined-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
AdlamUnjoined Sans Serif font, hinted.

%package -n noto-sans-anatolianhieroglyphs-fonts
Summary:        Noto Anatolian Hieroglyphs Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-anatolianhieroglyphs < %{version}
Provides:       noto-sans-anatolianhieroglyphs = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-anatolianhieroglyphs-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
AnatolianHieroglyphs Sans Serif font, hinted.

%package -n noto-sans-arabic-fonts
Summary:        Noto Arabic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-arabic < %{version}
Provides:       noto-sans-arabic = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-arabic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Arabic Sans Serif font, hinted.

%package -n noto-sans-arabic-ui-fonts
Summary:        Noto Arabic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-arabic-ui < %{version}
Provides:       noto-sans-arabic-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-arabic-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Arabic Sans Serif font, hinted.

%package -n noto-sans-armenian-fonts
Summary:        Noto Armenian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-armenian < %{version}
Provides:       noto-sans-armenian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-armenian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Armenian Sans Serif font, hinted.

%package -n noto-sans-avestan-fonts
Summary:        Noto Avestan Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-avestan < %{version}
Provides:       noto-sans-avestan = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-avestan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Avestan Sans Serif font, hinted.

%package -n noto-sans-balinese-fonts
Summary:        Noto Balinese Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-balinese < %{version}
Provides:       noto-sans-balinese = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-balinese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Balinese Sans Serif font, hinted.

%package -n noto-sans-bamum-fonts
Summary:        Noto Bamum Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-bamum < %{version}
Provides:       noto-sans-bamum = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-bamum-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bamum Sans Serif font, hinted.

%package -n noto-sans-bassavah-fonts
Summary:        Noto Bassa Vah Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-bassavah < %{version}
Provides:       noto-sans-bassavah = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-bassavah-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
BassaVah Sans Serif font, hinted.

%package -n noto-sans-batak-fonts
Summary:        Noto Batak Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-batak < %{version}
Provides:       noto-sans-batak = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-batak-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Batak Sans Serif font, hinted.

%package -n noto-sans-bengali-fonts
Summary:        Noto Bengali Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-bengali < %{version}
Provides:       noto-sans-bengali = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-bengali-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bengali Sans Serif font, hinted.

%package -n noto-sans-bengali-ui-fonts
Summary:        Noto Bengali Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-bengali-ui < %{version}
Provides:       noto-sans-bengali-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-bengali-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bengali Sans Serif font, hinted.

%package -n noto-sans-bhaiksuki-fonts
Summary:        Noto Bhaiksuki Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-bhaiksuki < %{version}
Provides:       noto-sans-bhaiksuki = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-bhaiksuki-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bhaiksuki Sans Serif font, hinted.

%package -n noto-sans-brahmi-fonts
Summary:        Noto Brahmi Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-brahmi < %{version}
Provides:       noto-sans-brahmi = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-brahmi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Brahmi Sans Serif font, hinted.

%package -n noto-sans-buginese-fonts
Summary:        Noto Buginese Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-buginese < %{version}
Provides:       noto-sans-buginese = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-buginese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Buginese Sans Serif font, hinted.

%package -n noto-sans-buhid-fonts
Summary:        Noto Buhid Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-buhid < %{version}
Provides:       noto-sans-buhid = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-buhid-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Buhid Sans Serif font, hinted.

%package -n noto-sans-canadianaboriginal-fonts
Summary:        Noto Canadian Aboriginal Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-canadianaboriginal < %{version}
Provides:       noto-sans-canadianaboriginal = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-canadianaboriginal-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
CanadianAboriginal Sans Serif font, hinted.

%package -n noto-sans-carian-fonts
Summary:        Noto Carian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-carian < %{version}
Provides:       noto-sans-carian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-carian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Carian Sans Serif font, hinted.

%package -n noto-sans-caucasianalbanian-fonts
Summary:        Noto Caucasian Albanian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-caucasianalbanian < %{version}
Provides:       noto-sans-caucasianalbanian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-caucasianalbanian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
CaucasianAlbanian Sans Serif font, hinted.

%package -n noto-sans-chakma-fonts
Summary:        Noto Chakma Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-chakma < %{version}
Provides:       noto-sans-chakma = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-chakma-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Chakma Sans Serif font, hinted.

%package -n noto-sans-cham-fonts
Summary:        Noto Cham Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-cham < %{version}
Provides:       noto-sans-cham = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-cham-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cham Sans Serif font, hinted.

%package -n noto-sans-cherokee-fonts
Summary:        Noto Cherokee Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-cherokee < %{version}
Provides:       noto-sans-cherokee = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-cherokee-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cherokee Sans Serif font, hinted.

%package -n noto-sans-chorasmian-fonts
Summary:        Noto Chorasmian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-chorasmian < %{version}
Provides:       noto-sans-chorasmian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-chorasmian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Chorasmian Sans Serif font, hinted.

%package -n noto-sans-coptic-fonts
Summary:        Noto Coptic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-coptic < %{version}
Provides:       noto-sans-coptic = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-coptic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Coptic Sans Serif font, hinted.

%package -n noto-sans-cuneiform-fonts
Summary:        Noto Cuneiform Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-cuneiform < %{version}
Provides:       noto-sans-cuneiform = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-cuneiform-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cuneiform Sans Serif font, hinted.

%package -n noto-sans-cypriot-fonts
Summary:        Noto Cypriot Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-cypriot < %{version}
Provides:       noto-sans-cypriot = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-cypriot-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cypriot Sans Serif font, hinted.

%package -n noto-sans-cyprominoan-fonts
Summary:        Noto Cypro Minoan Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-cyprominoan < %{version}
Provides:       noto-sans-cyprominoan = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-cyprominoan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
CyproMinoan Sans Serif font, hinted.

%package -n noto-sans-deseret-fonts
Summary:        Noto Deseret Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-deseret < %{version}
Provides:       noto-sans-deseret = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-deseret-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Deseret Sans Serif font, hinted.

%package -n noto-sans-devanagari-fonts
Summary:        Noto Devanagari Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-devanagari < %{version}
Provides:       noto-sans-devanagari = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-devanagari-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Devanagari Sans Serif font, hinted.

%package -n noto-sans-devanagari-ui-fonts
Summary:        Noto Devanagari Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-devanagari-ui < %{version}
Provides:       noto-sans-devanagari-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-devanagari-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Devanagari Sans Serif font, hinted.

%package -n noto-sans-duployan-fonts
Summary:        Noto Duployan Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-duployan < %{version}
Provides:       noto-sans-duployan = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-duployan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Duployan Sans Serif font, hinted.

%package -n noto-sans-egyptianhieroglyphs-fonts
Summary:        Noto Egyptian Hieroglyphs Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-egyptianhieroglyphs < %{version}
Provides:       noto-sans-egyptianhieroglyphs = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-egyptianhieroglyphs-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
EgyptianHieroglyphs Sans Serif font, hinted.

%package -n noto-sans-elbasan-fonts
Summary:        Noto Elbasan Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-elbasan < %{version}
Provides:       noto-sans-elbasan = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-elbasan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Elbasan Sans Serif font, hinted.

%package -n noto-sans-elymaic-fonts
Summary:        Noto Elymaic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-elymaic < %{version}
Provides:       noto-sans-elymaic = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-elymaic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Elymaic Sans Serif font, hinted.

%package -n noto-sans-ethiopic-fonts
Summary:        Noto Ethiopic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-ethiopic < %{version}
Provides:       noto-sans-ethiopic = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-ethiopic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ethiopic Sans Serif font, hinted.

%package -n noto-sans-georgian-fonts
Summary:        Noto Georgian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-georgian < %{version}
Provides:       noto-sans-georgian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-georgian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Georgian Sans Serif font, hinted.

%package -n noto-sans-glagolitic-fonts
Summary:        Noto Glagolitic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-glagolitic < %{version}
Provides:       noto-sans-glagolitic = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-glagolitic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Glagolitic Sans Serif font, hinted.

%package -n noto-sans-gothic-fonts
Summary:        Noto Gothic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-gothic < %{version}
Provides:       noto-sans-gothic = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-gothic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gothic Sans Serif font, hinted.

%package -n noto-sans-grantha-fonts
Summary:        Noto Grantha Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-grantha < %{version}
Provides:       noto-sans-grantha = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-grantha-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Grantha Sans Serif font, hinted.

%package -n noto-sans-gujarati-fonts
Summary:        Noto Gujarati Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-gujarati < %{version}
Provides:       noto-sans-gujarati = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-gujarati-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gujarati Sans Serif font, hinted.

%package -n noto-sans-gujarati-ui-fonts
Summary:        Noto Gujarati Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-gujarati-ui < %{version}
Provides:       noto-sans-gujarati-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-gujarati-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gujarati Sans Serif font, hinted.

%package -n noto-sans-gunjalagondi-fonts
Summary:        Noto Gunjala Gondi Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-gunjalagondi < %{version}
Provides:       noto-sans-gunjalagondi = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-gunjalagondi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
GunjalaGondi Sans Serif font, hinted.

%package -n noto-sans-gurmukhi-fonts
Summary:        Noto Gurmukhi Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-gurmukhi < %{version}
Provides:       noto-sans-gurmukhi = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-gurmukhi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gurmukhi Sans Serif font, hinted.

%package -n noto-sans-gurmukhi-ui-fonts
Summary:        Noto Gurmukhi Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-gurmukhi-ui < %{version}
Provides:       noto-sans-gurmukhi-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-gurmukhi-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gurmukhi Sans Serif font, hinted.

%package -n noto-sans-hanifirohingya-fonts
Summary:        Noto Hanifi Rohingya Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-hanifirohingya < %{version}
Provides:       noto-sans-hanifirohingya = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-hanifirohingya-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
HanifiRohingya Sans Serif font, hinted.

%package -n noto-sans-hanunoo-fonts
Summary:        Noto Hanunoo Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-hanunoo < %{version}
Provides:       noto-sans-hanunoo = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-hanunoo-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Hanunoo Sans Serif font, hinted.

%package -n noto-sans-hatran-fonts
Summary:        Noto Hatran Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-hatran < %{version}
Provides:       noto-sans-hatran = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-hatran-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Hatran Sans Serif font, hinted.

%package -n noto-sans-hebrew-fonts
Summary:        Noto Hebrew Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-hebrew < %{version}
Provides:       noto-sans-hebrew = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-hebrew-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Hebrew Sans Serif font, hinted.

%package -n noto-sans-hebrewdroid-fonts
Summary:        Noto Hebrew Droid Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-hebrewdroid < %{version}
Provides:       noto-sans-hebrewdroid = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-hebrewdroid-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
HebrewDroid Sans Serif font, hinted.

%package -n noto-sans-hebrewnew-fonts
Summary:        Noto Hebrew New Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-hebrewnew < %{version}
Provides:       noto-sans-hebrewnew = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-hebrewnew-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
HebrewNew Sans Serif font, hinted.

%package -n noto-sans-imperialaramaic-fonts
Summary:        Noto Imperial Aramaic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-imperialaramaic < %{version}
Provides:       noto-sans-imperialaramaic = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-imperialaramaic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
ImperialAramaic Sans Serif font, hinted.

%package -n noto-sans-indicsiyaqnumbers-fonts
Summary:        Noto Indic Siyaq Numbers Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-indicsiyaqnumbers < %{version}
Provides:       noto-sans-indicsiyaqnumbers = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-indicsiyaqnumbers-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
IndicSiyaqNumbers Sans Serif font, hinted.

%package -n noto-sans-inscriptionalpahlavi-fonts
Summary:        Noto Inscriptional Pahlavi Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-inscriptionalpahlavi < %{version}
Provides:       noto-sans-inscriptionalpahlavi = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-inscriptionalpahlavi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
InscriptionalPahlavi Sans Serif font, hinted.

%package -n noto-sans-inscriptionalparthian-fonts
Summary:        Noto Inscriptional Parthian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-inscriptionalparthian < %{version}
Provides:       noto-sans-inscriptionalparthian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-inscriptionalparthian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
InscriptionalParthian Sans Serif font, hinted.

%package -n noto-sans-javanese-fonts
Summary:        Noto Javanese Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-javanese < %{version}
Provides:       noto-sans-javanese = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-javanese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Javanese Sans Serif font, hinted.

%package -n noto-sans-kaithi-fonts
Summary:        Noto Kaithi Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-kaithi < %{version}
Provides:       noto-sans-kaithi = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-kaithi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kaithi Sans Serif font, hinted.

%package -n noto-sans-kannada-fonts
Summary:        Noto Kannada Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-kannada < %{version}
Provides:       noto-sans-kannada = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-kannada-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kannada Sans Serif font, hinted.

%package -n noto-sans-kannada-ui-fonts
Summary:        Noto Kannada Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-kannada-ui < %{version}
Provides:       noto-sans-kannada-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-kannada-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kannada Sans Serif font, hinted.

%package -n noto-sans-kayahli-fonts
Summary:        Noto Kayah Li Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-kayahli < %{version}
Provides:       noto-sans-kayahli = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-kayahli-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
KayahLi Sans Serif font, hinted.

%package -n noto-sans-kharoshthi-fonts
Summary:        Noto Kharoshthi Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-kharoshthi < %{version}
Provides:       noto-sans-kharoshthi = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-kharoshthi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kharoshthi Sans Serif font, hinted.

%package -n noto-sans-khmer-fonts
Summary:        Noto Khmer Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-khmer < %{version}
Provides:       noto-sans-khmer = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-khmer-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khmer Sans Serif font, hinted.

%package -n noto-sans-khmer-ui-fonts
Summary:        Noto Khmer Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-khmer-ui < %{version}
Provides:       noto-sans-khmer-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-khmer-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khmer Sans Serif font, hinted.

%package -n noto-sans-khojki-fonts
Summary:        Noto Khojki Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-khojki < %{version}
Provides:       noto-sans-khojki = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-khojki-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khojki Sans Serif font, hinted.

%package -n noto-sans-khudawadi-fonts
Summary:        Noto Khudawadi Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-khudawadi < %{version}
Provides:       noto-sans-khudawadi = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-khudawadi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khudawadi Sans Serif font, hinted.

%package -n noto-sans-lao-fonts
Summary:        Noto Lao Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-lao < %{version}
Provides:       noto-sans-lao = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-lao-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lao Sans Serif font, hinted.

%package -n noto-sans-lao-ui-fonts
Summary:        Noto Lao Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-lao-ui < %{version}
Provides:       noto-sans-lao-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-lao-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lao Sans Serif font, hinted.

%package -n noto-sans-lepcha-fonts
Summary:        Noto Lepcha Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-lepcha < %{version}
Provides:       noto-sans-lepcha = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-lepcha-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lepcha Sans Serif font, hinted.

%package -n noto-sans-limbu-fonts
Summary:        Noto Limbu Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-limbu < %{version}
Provides:       noto-sans-limbu = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-limbu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Limbu Sans Serif font, hinted.

%package -n noto-sans-lineara-fonts
Summary:        Noto Linear A Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-lineara < %{version}
Provides:       noto-sans-lineara = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-lineara-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
LinearA Sans Serif font, hinted.

%package -n noto-sans-linearb-fonts
Summary:        Noto Linear B Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-linearb < %{version}
Provides:       noto-sans-linearb = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-linearb-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
LinearB Sans Serif font, hinted.

%package -n noto-sans-lisu-fonts
Summary:        Noto Lisu Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-lisu < %{version}
Provides:       noto-sans-lisu = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-lisu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lisu Sans Serif font, hinted.

%package -n noto-sans-lycian-fonts
Summary:        Noto Lycian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-lycian < %{version}
Provides:       noto-sans-lycian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-lycian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lycian Sans Serif font, hinted.

%package -n noto-sans-lydian-fonts
Summary:        Noto Lydian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-lydian < %{version}
Provides:       noto-sans-lydian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-lydian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lydian Sans Serif font, hinted.

%package -n noto-sans-mahajani-fonts
Summary:        Noto Mahajani Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-mahajani < %{version}
Provides:       noto-sans-mahajani = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-mahajani-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mahajani Sans Serif font, hinted.

%package -n noto-sans-malayalam-fonts
Summary:        Noto Malayalam Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-malayalam < %{version}
Provides:       noto-sans-malayalam = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-malayalam-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Malayalam Sans Serif font, hinted.

%package -n noto-sans-malayalam-ui-fonts
Summary:        Noto Malayalam Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-malayalam-ui < %{version}
Provides:       noto-sans-malayalam-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-malayalam-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Malayalam Sans Serif font, hinted.

%package -n noto-sans-mandaic-fonts
Summary:        Noto Mandaic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-mandaic < %{version}
Provides:       noto-sans-mandaic = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-mandaic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mandaic Sans Serif font, hinted.

%package -n noto-sans-manichaean-fonts
Summary:        Noto Manichaean Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-manichaean < %{version}
Provides:       noto-sans-manichaean = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-manichaean-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Manichaean Sans Serif font, hinted.

%package -n noto-sans-marchen-fonts
Summary:        Noto Marchen Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-marchen < %{version}
Provides:       noto-sans-marchen = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-marchen-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Marchen Sans Serif font, hinted.

%package -n noto-sans-masaramgondi-fonts
Summary:        Noto Masaram Gondi Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-masaramgondi < %{version}
Provides:       noto-sans-masaramgondi = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-masaramgondi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
MasaramGondi Sans Serif font, hinted.

%package -n noto-sans-math-fonts
Summary:        Noto Math Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-math < %{version}
Provides:       noto-sans-math = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-math-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Math Sans Serif font, hinted.

%package -n noto-sans-mayannumerals-fonts
Summary:        Noto Mayan Numerals Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-mayannumerals < %{version}
Provides:       noto-sans-mayannumerals = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-mayannumerals-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
MayanNumerals Sans Serif font, hinted.

%package -n noto-sans-medefaidrin-fonts
Summary:        Noto Medefaidrin Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-medefaidrin < %{version}
Provides:       noto-sans-medefaidrin = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-medefaidrin-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Medefaidrin Sans Serif font, hinted.

%package -n noto-sans-meeteimayek-fonts
Summary:        Noto Meetei Mayek Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-meeteimayek < %{version}
Provides:       noto-sans-meeteimayek = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-meeteimayek-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
MeeteiMayek Sans Serif font, hinted.

%package -n noto-sans-mendekikakui-fonts
Summary:        Noto Mende Kikakui Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-mendekikakui < %{version}
Provides:       noto-sans-mendekikakui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-mendekikakui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
MendeKikakui Sans Serif font, hinted.

%package -n noto-sans-meroitic-fonts
Summary:        Noto Meroitic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-meroitic < %{version}
Provides:       noto-sans-meroitic = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-meroitic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Meroitic Sans Serif font, hinted.

%package -n noto-sans-miao-fonts
Summary:        Noto Miao Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-miao < %{version}
Provides:       noto-sans-miao = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-miao-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Miao Sans Serif font, hinted.

%package -n noto-sans-modi-fonts
Summary:        Noto Modi Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-modi < %{version}
Provides:       noto-sans-modi = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-modi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Modi Sans Serif font, hinted.

%package -n noto-sans-mongolian-fonts
Summary:        Noto Mongolian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-mongolian < %{version}
Provides:       noto-sans-mongolian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-mongolian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mongolian Sans Serif font, hinted.

%package -n noto-sans-mono-fonts
Summary:        Noto Mono Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-mono < %{version}
Provides:       noto-sans-mono = %{version}
Obsoletes:      noto-mono < %{version}
Provides:       noto-mono = %{version}
Obsoletes:      noto-mono-fonts < %{version}
Provides:       noto-mono-fonts = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-mono-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mono Sans Serif font, hinted.

%package -n noto-sans-mro-fonts
Summary:        Noto Mro Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-mro < %{version}
Provides:       noto-sans-mro = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-mro-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mro Sans Serif font, hinted.

%package -n noto-sans-multani-fonts
Summary:        Noto Multani Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-multani < %{version}
Provides:       noto-sans-multani = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-multani-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Multani Sans Serif font, hinted.

%package -n noto-sans-myanmar-fonts
Summary:        Noto Myanmar Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-myanmar < %{version}
Provides:       noto-sans-myanmar = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-myanmar-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Myanmar Sans Serif font, hinted.

%package -n noto-sans-myanmar-ui-fonts
Summary:        Noto Myanmar Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-myanmar-ui < %{version}
Provides:       noto-sans-myanmar-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-myanmar-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Myanmar Sans Serif font, hinted.

%package -n noto-sans-nabataean-fonts
Summary:        Noto Nabataean Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-nabataean < %{version}
Provides:       noto-sans-nabataean = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-nabataean-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Nabataean Sans Serif font, hinted.

%package -n noto-sans-nandinagari-fonts
Summary:        Noto Nandinagari Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-nandinagari < %{version}
Provides:       noto-sans-nandinagari = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-nandinagari-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Nandinagari Sans Serif font, hinted.

%package -n noto-sans-newa-fonts
Summary:        Noto Newa Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-newa < %{version}
Provides:       noto-sans-newa = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-newa-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Newa Sans Serif font, hinted.

%package -n noto-sans-newtailue-fonts
Summary:        Noto New Tai Lue Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-newtailue < %{version}
Provides:       noto-sans-newtailue = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-newtailue-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NewTaiLue Sans Serif font, hinted.

%package -n noto-sans-nko-fonts
Summary:        Noto NKo Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-nko < %{version}
Provides:       noto-sans-nko = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-nko-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NKo Sans Serif font, hinted.

%package -n noto-sans-nushu-fonts
Summary:        Noto Nushu Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-nushu < %{version}
Provides:       noto-sans-nushu = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-nushu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Nushu Sans Serif font, hinted.

%package -n noto-sans-ogham-fonts
Summary:        Noto Ogham Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-ogham < %{version}
Provides:       noto-sans-ogham = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-ogham-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ogham Sans Serif font, hinted.

%package -n noto-sans-olchiki-fonts
Summary:        Noto Ol Chiki Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-olchiki < %{version}
Provides:       noto-sans-olchiki = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-olchiki-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OlChiki Sans Serif font, hinted.

%package -n noto-sans-oldhungarian-fonts
Summary:        Noto Old Hungarian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-oldhungarian < %{version}
Provides:       noto-sans-oldhungarian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-oldhungarian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldHungarian Sans Serif font, hinted.

%package -n noto-sans-olditalic-fonts
Summary:        Noto Old Italic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-olditalic < %{version}
Provides:       noto-sans-olditalic = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-olditalic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldItalic Sans Serif font, hinted.

%package -n noto-sans-oldnortharabian-fonts
Summary:        Noto Old North Arabian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-oldnortharabian < %{version}
Provides:       noto-sans-oldnortharabian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-oldnortharabian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldNorthArabian Sans Serif font, hinted.

%package -n noto-sans-oldpermic-fonts
Summary:        Noto Old Permic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-oldpermic < %{version}
Provides:       noto-sans-oldpermic = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-oldpermic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldPermic Sans Serif font, hinted.

%package -n noto-sans-oldpersian-fonts
Summary:        Noto Old Persian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-oldpersian < %{version}
Provides:       noto-sans-oldpersian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-oldpersian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldPersian Sans Serif font, hinted.

%package -n noto-sans-oldsogdian-fonts
Summary:        Noto Old Sogdian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-oldsogdian < %{version}
Provides:       noto-sans-oldsogdian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-oldsogdian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldSogdian Sans Serif font, hinted.

%package -n noto-sans-oldsoutharabian-fonts
Summary:        Noto Old South Arabian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-oldsoutharabian < %{version}
Provides:       noto-sans-oldsoutharabian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-oldsoutharabian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldSouthArabian Sans Serif font, hinted.

%package -n noto-sans-oldturkic-fonts
Summary:        Noto Old Turkic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-oldturkic < %{version}
Provides:       noto-sans-oldturkic = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-oldturkic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldTurkic Sans Serif font, hinted.

%package -n noto-sans-oriya-fonts
Summary:        Noto Oriya Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-oriya < %{version}
Provides:       noto-sans-oriya = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-oriya-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Oriya Sans Serif font, hinted.

%package -n noto-sans-oriya-ui-fonts
Summary:        Noto Oriya Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-oriya-ui < %{version}
Provides:       noto-sans-oriya-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-oriya-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Oriya Sans Serif font, hinted.

%package -n noto-sans-osage-fonts
Summary:        Noto Osage Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-osage < %{version}
Provides:       noto-sans-osage = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-osage-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Osage Sans Serif font, hinted.

%package -n noto-sans-osmanya-fonts
Summary:        Noto Osmanya Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-osmanya < %{version}
Provides:       noto-sans-osmanya = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-osmanya-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Osmanya Sans Serif font, hinted.

%package -n noto-sans-pahawhhmong-fonts
Summary:        Noto Pahawh Hmong Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-pahawhhmong < %{version}
Provides:       noto-sans-pahawhhmong = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-pahawhhmong-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
PahawhHmong Sans Serif font, hinted.

%package -n noto-sans-palmyrene-fonts
Summary:        Noto Palmyrene Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-palmyrene < %{version}
Provides:       noto-sans-palmyrene = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-palmyrene-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Palmyrene Sans Serif font, hinted.

%package -n noto-sans-paucinhau-fonts
Summary:        Noto Pau Cin Hau Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-paucinhau < %{version}
Provides:       noto-sans-paucinhau = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-paucinhau-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
PauCinHau Sans Serif font, hinted.

%package -n noto-sans-phagspa-fonts
Summary:        Noto Phags Pa Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-phagspa < %{version}
Provides:       noto-sans-phagspa = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-phagspa-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
PhagsPa Sans Serif font, hinted.

%package -n noto-sans-phoenician-fonts
Summary:        Noto Phoenician Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-phoenician < %{version}
Provides:       noto-sans-phoenician = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-phoenician-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Phoenician Sans Serif font, hinted.

%package -n noto-sans-psalterpahlavi-fonts
Summary:        Noto Psalter Pahlavi Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-psalterpahlavi < %{version}
Provides:       noto-sans-psalterpahlavi = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-psalterpahlavi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
PsalterPahlavi Sans Serif font, hinted.

%package -n noto-sans-rejang-fonts
Summary:        Noto Rejang Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-rejang < %{version}
Provides:       noto-sans-rejang = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-rejang-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Rejang Sans Serif font, hinted.

%package -n noto-sans-runic-fonts
Summary:        Noto Runic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-runic < %{version}
Provides:       noto-sans-runic = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-runic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Runic Sans Serif font, hinted.

%package -n noto-sans-samaritan-fonts
Summary:        Noto Samaritan Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-samaritan < %{version}
Provides:       noto-sans-samaritan = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-samaritan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Samaritan Sans Serif font, hinted.

%package -n noto-sans-saurashtra-fonts
Summary:        Noto Saurashtra Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-saurashtra < %{version}
Provides:       noto-sans-saurashtra = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-saurashtra-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Saurashtra Sans Serif font, hinted.

%package -n noto-sans-sharada-fonts
Summary:        Noto Sharada Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-sharada < %{version}
Provides:       noto-sans-sharada = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-sharada-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sharada Sans Serif font, hinted.

%package -n noto-sans-shavian-fonts
Summary:        Noto Shavian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-shavian < %{version}
Provides:       noto-sans-shavian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-shavian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Shavian Sans Serif font, hinted.

%package -n noto-sans-siddham-fonts
Summary:        Noto Siddham Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-siddham < %{version}
Provides:       noto-sans-siddham = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-siddham-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Siddham Sans Serif font, hinted.

%package -n noto-sans-signwriting-fonts
Summary:        Noto Sign Writing Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-signwriting < %{version}
Provides:       noto-sans-signwriting = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-signwriting-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SignWriting Sans Serif font, hinted.

%package -n noto-sans-sinhala-fonts
Summary:        Noto Sinhala Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-sinhala < %{version}
Provides:       noto-sans-sinhala = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-sinhala-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sinhala Sans Serif font, hinted.

%package -n noto-sans-sinhala-ui-fonts
Summary:        Noto Sinhala Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-sinhala-ui < %{version}
Provides:       noto-sans-sinhala-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-sinhala-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sinhala Sans Serif font, hinted.

%package -n noto-sans-sogdian-fonts
Summary:        Noto Sogdian Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-sogdian < %{version}
Provides:       noto-sans-sogdian = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-sogdian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sogdian Sans Serif font, hinted.

%package -n noto-sans-sorasompeng-fonts
Summary:        Noto Sora Sompeng Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-sorasompeng < %{version}
Provides:       noto-sans-sorasompeng = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-sorasompeng-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SoraSompeng Sans Serif font, hinted.

%package -n noto-sans-soyombo-fonts
Summary:        Noto Soyombo Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-soyombo < %{version}
Provides:       noto-sans-soyombo = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-soyombo-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Soyombo Sans Serif font, hinted.

%package -n noto-sans-sundanese-fonts
Summary:        Noto Sundanese Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-sundanese < %{version}
Provides:       noto-sans-sundanese = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-sundanese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sundanese Sans Serif font, hinted.

%package -n noto-sans-sylotinagri-fonts
Summary:        Noto Syloti Nagri Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-sylotinagri < %{version}
Provides:       noto-sans-sylotinagri = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-sylotinagri-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SylotiNagri Sans Serif font, hinted.

%package -n noto-sans-symbols-fonts
Summary:        Noto Symbols Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-symbols < %{version}
Provides:       noto-sans-symbols = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-symbols-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Symbols Sans Serif font, hinted.

%package -n noto-sans-symbols2-fonts
Summary:        Noto Symbols2 Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-symbols2 < %{version}
Provides:       noto-sans-symbols2 = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-symbols2-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Symbols2 Sans Serif font, hinted.

%package -n noto-sans-syriac-fonts
Summary:        Noto Syriac Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-syriac < %{version}
Provides:       noto-sans-syriac = %{version}
Obsoletes:      noto-sans-syriacwestern < %{version}
Provides:       noto-sans-syriacwestern = %{version}
Obsoletes:      noto-sans-syriacwestern-fonts < %{version}
Provides:       noto-sans-syriacwestern-fonts = %{version}
Obsoletes:      noto-sans-syriacestrangela < %{version}
Provides:       noto-sans-syriacestrangela = %{version}
Obsoletes:      noto-sans-syriacestrangela-fonts < %{version}
Provides:       noto-sans-syriacestrangela-fonts = %{version}
Obsoletes:      noto-sans-syriaceastern < %{version}
Provides:       noto-sans-syriaceastern = %{version}
Obsoletes:      noto-sans-syriaceastern-fonts < %{version}
Provides:       noto-sans-syriaceastern-fonts = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-syriac-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Syriac Sans Serif font, hinted.

%package -n noto-sans-tagalog-fonts
Summary:        Noto Tagalog Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tagalog < %{version}
Provides:       noto-sans-tagalog = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tagalog-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tagalog Sans Serif font, hinted.

%package -n noto-sans-tagbanwa-fonts
Summary:        Noto Tagbanwa Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tagbanwa < %{version}
Provides:       noto-sans-tagbanwa = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tagbanwa-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tagbanwa Sans Serif font, hinted.

%package -n noto-sans-taile-fonts
Summary:        Noto Tai Le Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-taile < %{version}
Provides:       noto-sans-taile = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-taile-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TaiLe Sans Serif font, hinted.

%package -n noto-sans-taitham-fonts
Summary:        Noto Tai Tham Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-taitham < %{version}
Provides:       noto-sans-taitham = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-taitham-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TaiTham Sans Serif font, hinted.

%package -n noto-sans-taiviet-fonts
Summary:        Noto Tai Viet Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-taiviet < %{version}
Provides:       noto-sans-taiviet = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-taiviet-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TaiViet Sans Serif font, hinted.

%package -n noto-sans-takri-fonts
Summary:        Noto Takri Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-takri < %{version}
Provides:       noto-sans-takri = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-takri-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Takri Sans Serif font, hinted.

%package -n noto-sans-tamil-fonts
Summary:        Noto Tamil Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tamil < %{version}
Provides:       noto-sans-tamil = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tamil-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tamil Sans Serif font, hinted.

%package -n noto-sans-tamilsupplement-fonts
Summary:        Noto Tamil Supplement Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tamilsupplement < %{version}
Provides:       noto-sans-tamilsupplement = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tamilsupplement-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TamilSupplement Sans Serif font, hinted.

%package -n noto-sans-tamil-ui-fonts
Summary:        Noto Tamil Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tamil-ui < %{version}
Provides:       noto-sans-tamil-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tamil-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tamil Sans Serif font, hinted.

%package -n noto-sans-tangsa-fonts
Summary:        Noto Tangsa Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tangsa < %{version}
Provides:       noto-sans-tangsa = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tangsa-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tangsa Sans Serif font, hinted.

%package -n noto-sans-telugu-fonts
Summary:        Noto Telugu Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-telugu < %{version}
Provides:       noto-sans-telugu = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-telugu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Telugu Sans Serif font, hinted.

%package -n noto-sans-telugu-ui-fonts
Summary:        Noto Telugu Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-telugu-ui < %{version}
Provides:       noto-sans-telugu-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-telugu-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Telugu Sans Serif font, hinted.

%package -n noto-sans-thaana-fonts
Summary:        Noto Thaana Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-thaana < %{version}
Provides:       noto-sans-thaana = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-thaana-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Thaana Sans Serif font, hinted.

%package -n noto-sans-thai-fonts
Summary:        Noto Thai Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-thai < %{version}
Provides:       noto-sans-thai = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-thai-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Thai Sans Serif font, hinted.

%package -n noto-sans-thai-ui-fonts
Summary:        Noto Thai Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-thai-ui < %{version}
Provides:       noto-sans-thai-ui = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-thai-ui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Thai Sans Serif font, hinted.

%package -n noto-sans-tifinagh-fonts
Summary:        Noto Tifinagh Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tifinagh < %{version}
Provides:       noto-sans-tifinagh = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tifinagh-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tifinagh Sans Serif font, hinted.

%package -n noto-sans-tifinaghadrar-fonts
Summary:        Noto Tifinagh Adrar Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tifinaghadrar < %{version}
Provides:       noto-sans-tifinaghadrar = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tifinaghadrar-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TifinaghAdrar Sans Serif font, hinted.

%package -n noto-sans-tifinaghagrawimazighen-fonts
Summary:        Noto Tifinagh Agraw Imazighen Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tifinaghagrawimazighen < %{version}
Provides:       noto-sans-tifinaghagrawimazighen = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tifinaghagrawimazighen-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TifinaghAgrawImazighen Sans Serif font, hinted.

%package -n noto-sans-tifinaghahaggar-fonts
Summary:        Noto Tifinagh Ahaggar Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tifinaghahaggar < %{version}
Provides:       noto-sans-tifinaghahaggar = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tifinaghahaggar-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TifinaghAhaggar Sans Serif font, hinted.

%package -n noto-sans-tifinaghair-fonts
Summary:        Noto Tifinagh Air Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tifinaghair < %{version}
Provides:       noto-sans-tifinaghair = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tifinaghair-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TifinaghAir Sans Serif font, hinted.

%package -n noto-sans-tifinaghapt-fonts
Summary:        Noto Tifinagh APT Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tifinaghapt < %{version}
Provides:       noto-sans-tifinaghapt = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tifinaghapt-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TifinaghAPT Sans Serif font, hinted.

%package -n noto-sans-tifinaghazawagh-fonts
Summary:        Noto Tifinagh Azawagh Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tifinaghazawagh < %{version}
Provides:       noto-sans-tifinaghazawagh = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tifinaghazawagh-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TifinaghAzawagh Sans Serif font, hinted.

%package -n noto-sans-tifinaghghat-fonts
Summary:        Noto Tifinagh Ghat Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tifinaghghat < %{version}
Provides:       noto-sans-tifinaghghat = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tifinaghghat-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TifinaghGhat Sans Serif font, hinted.

%package -n noto-sans-tifinaghhawad-fonts
Summary:        Noto Tifinagh Hawad Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tifinaghhawad < %{version}
Provides:       noto-sans-tifinaghhawad = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tifinaghhawad-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TifinaghHawad Sans Serif font, hinted.

%package -n noto-sans-tifinaghrhissaixa-fonts
Summary:        Noto Tifinagh Rhissa Ixa Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tifinaghrhissaixa < %{version}
Provides:       noto-sans-tifinaghrhissaixa = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tifinaghrhissaixa-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TifinaghRhissaIxa Sans Serif font, hinted.

%package -n noto-sans-tifinaghsil-fonts
Summary:        Noto Tifinagh SIL Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tifinaghsil < %{version}
Provides:       noto-sans-tifinaghsil = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tifinaghsil-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TifinaghSIL Sans Serif font, hinted.

%package -n noto-sans-tifinaghtawellemmet-fonts
Summary:        Noto Tifinagh Tawellemmet Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tifinaghtawellemmet < %{version}
Provides:       noto-sans-tifinaghtawellemmet = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tifinaghtawellemmet-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TifinaghTawellemmet Sans Serif font, hinted.

%package -n noto-sans-tirhuta-fonts
Summary:        Noto Tirhuta Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-tirhuta < %{version}
Provides:       noto-sans-tirhuta = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-tirhuta-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tirhuta Sans Serif font, hinted.

%package -n noto-sans-ugaritic-fonts
Summary:        Noto Ugaritic Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-ugaritic < %{version}
Provides:       noto-sans-ugaritic = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-ugaritic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ugaritic Sans Serif font, hinted.

%package -n noto-sans-vai-fonts
Summary:        Noto Vai Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-vai < %{version}
Provides:       noto-sans-vai = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-vai-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Vai Sans Serif font, hinted.

%package -n noto-sans-vithkuqi-fonts
Summary:        Noto Vithkuqi Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-vithkuqi < %{version}
Provides:       noto-sans-vithkuqi = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-vithkuqi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Vithkuqi Sans Serif font, hinted.

%package -n noto-sans-wancho-fonts
Summary:        Noto Wancho Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-wancho < %{version}
Provides:       noto-sans-wancho = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-wancho-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Wancho Sans Serif font, hinted.

%package -n noto-sans-warangciti-fonts
Summary:        Noto Warang Citi Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-warangciti < %{version}
Provides:       noto-sans-warangciti = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-warangciti-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
WarangCiti Sans Serif font, hinted.

%package -n noto-sans-yi-fonts
Summary:        Noto Yi Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-yi < %{version}
Provides:       noto-sans-yi = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-yi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Yi Sans Serif font, hinted.

%package -n noto-sans-zanabazarsquare-fonts
Summary:        Noto Zanabazar Square Sans Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-sans-zanabazarsquare < %{version}
Provides:       noto-sans-zanabazarsquare = %{version}
%reconfigure_fonts_prereq

%description -n noto-sans-zanabazarsquare-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
ZanabazarSquare Sans Serif font, hinted.

%package -n noto-serif-fonts
Summary:        Noto Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif < %{version}
Provides:       noto-serif = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Serif font, hinted.

%package -n noto-serif-ahom-fonts
Summary:        Noto Ahom Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-ahom < %{version}
Provides:       noto-serif-ahom = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-ahom-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ahom Serif font, hinted.

%package -n noto-serif-armenian-fonts
Summary:        Noto Armenian Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-armenian < %{version}
Provides:       noto-serif-armenian = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-armenian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Armenian Serif font, hinted.

%package -n noto-serif-balinese-fonts
Summary:        Noto Balinese Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-balinese < %{version}
Provides:       noto-serif-balinese = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-balinese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Balinese Serif font, hinted.

%package -n noto-serif-bengali-fonts
Summary:        Noto Bengali Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-bengali < %{version}
Provides:       noto-serif-bengali = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-bengali-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bengali Serif font, hinted.

%package -n noto-serif-devanagari-fonts
Summary:        Noto Devanagari Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-devanagari < %{version}
Provides:       noto-serif-devanagari = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-devanagari-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Devanagari Serif font, hinted.

%package -n noto-serif-display-fonts
Summary:        Noto Display Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-display < %{version}
Provides:       noto-serif-display = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-display-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Display Serif font, hinted.

%package -n noto-serif-divesakuru-fonts
Summary:        Noto Dives Akuru Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-divesakuru < %{version}
Provides:       noto-serif-divesakuru = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-divesakuru-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
DivesAkuru Serif font, hinted.

%package -n noto-serif-dogra-fonts
Summary:        Noto Dogra Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-dogra < %{version}
Provides:       noto-serif-dogra = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-dogra-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Dogra Serif font, hinted.

%package -n noto-serif-ethiopic-fonts
Summary:        Noto Ethiopic Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-ethiopic < %{version}
Provides:       noto-serif-ethiopic = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-ethiopic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ethiopic Serif font, hinted.

%package -n noto-serif-georgian-fonts
Summary:        Noto Georgian Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-georgian < %{version}
Provides:       noto-serif-georgian = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-georgian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Georgian Serif font, hinted.

%package -n noto-serif-grantha-fonts
Summary:        Noto Grantha Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-grantha < %{version}
Provides:       noto-serif-grantha = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-grantha-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Grantha Serif font, hinted.

%package -n noto-serif-gujarati-fonts
Summary:        Noto Gujarati Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-gujarati < %{version}
Provides:       noto-serif-gujarati = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-gujarati-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gujarati Serif font, hinted.

%package -n noto-serif-gurmukhi-fonts
Summary:        Noto Gurmukhi Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-gurmukhi < %{version}
Provides:       noto-serif-gurmukhi = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-gurmukhi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gurmukhi Serif font, hinted.

%package -n noto-serif-hebrew-fonts
Summary:        Noto Hebrew Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-hebrew < %{version}
Provides:       noto-serif-hebrew = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-hebrew-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Hebrew Serif font, hinted.

%package -n noto-serif-kannada-fonts
Summary:        Noto Kannada Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-kannada < %{version}
Provides:       noto-serif-kannada = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-kannada-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kannada Serif font, hinted.

%package -n noto-serif-khmer-fonts
Summary:        Noto Khmer Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-khmer < %{version}
Provides:       noto-serif-khmer = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-khmer-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khmer Serif font, hinted.

%package -n noto-serif-khojki-fonts
Summary:        Noto Khojki Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-khojki < %{version}
Provides:       noto-serif-khojki = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-khojki-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khojki Serif font, hinted.

%package -n noto-serif-lao-fonts
Summary:        Noto Lao Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-lao < %{version}
Provides:       noto-serif-lao = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-lao-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lao Serif font, hinted.

%package -n noto-serif-makasar-fonts
Summary:        Noto Makasar Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-makasar < %{version}
Provides:       noto-serif-makasar = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-makasar-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Makasar Serif font, hinted.

%package -n noto-serif-malayalam-fonts
Summary:        Noto Malayalam Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-malayalam < %{version}
Provides:       noto-serif-malayalam = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-malayalam-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Malayalam Serif font, hinted.

%package -n noto-serif-myanmar-fonts
Summary:        Noto Myanmar Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-myanmar < %{version}
Provides:       noto-serif-myanmar = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-myanmar-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Myanmar Serif font, hinted.

%package -n noto-serif-nyiakengpuachuehmong-fonts
Summary:        Noto Nyiakeng Puachue Hmong Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-nyiakengpuachuehmong < %{version}
Provides:       noto-serif-nyiakengpuachuehmong = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-nyiakengpuachuehmong-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NyiakengPuachueHmong Serif font, hinted.

%package -n noto-serif-olduyghur-fonts
Summary:        Noto Old Uyghur Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-olduyghur < %{version}
Provides:       noto-serif-olduyghur = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-olduyghur-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldUyghur Serif font, hinted.

%package -n noto-serif-oriya-fonts
Summary:        Noto Oriya Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-oriya < %{version}
Provides:       noto-serif-oriya = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-oriya-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Oriya Serif font, hinted.

%package -n noto-serif-sinhala-fonts
Summary:        Noto Sinhala Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-sinhala < %{version}
Provides:       noto-serif-sinhala = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-sinhala-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sinhala Serif font, hinted.

%package -n noto-serif-tamil-fonts
Summary:        Noto Tamil Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-tamil < %{version}
Provides:       noto-serif-tamil = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-tamil-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tamil Serif font, hinted.

%package -n noto-serif-tamilslanted-fonts
Summary:        Noto Tamil Slanted Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-tamilslanted < %{version}
Provides:       noto-serif-tamilslanted = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-tamilslanted-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TamilSlanted Serif font, hinted.

%package -n noto-serif-tangut-fonts
Summary:        Noto Tangut Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-tangut < %{version}
Provides:       noto-serif-tangut = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-tangut-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tangut Serif font, hinted.

%package -n noto-serif-telugu-fonts
Summary:        Noto Telugu Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-telugu < %{version}
Provides:       noto-serif-telugu = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-telugu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Telugu Serif font, hinted.

%package -n noto-serif-thai-fonts
Summary:        Noto Thai Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-thai < %{version}
Provides:       noto-serif-thai = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-thai-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Thai Serif font, hinted.

%package -n noto-serif-tibetan-fonts
Summary:        Noto Tibetan Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-tibetan < %{version}
Provides:       noto-serif-tibetan = %{version}
Obsoletes:      noto-sans-tibetan < %{version}
Provides:       noto-sans-tibetan = %{version}
Obsoletes:      noto-sans-tibetan-fonts < %{version}
Provides:       noto-sans-tibetan-fonts = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-tibetan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tibetan Serif font, hinted.

%package -n noto-serif-toto-fonts
Summary:        Noto Toto Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-toto < %{version}
Provides:       noto-serif-toto = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-toto-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Toto Serif font, hinted.

%package -n noto-serif-vithkuqi-fonts
Summary:        Noto Vithkuqi Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-vithkuqi < %{version}
Provides:       noto-serif-vithkuqi = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-vithkuqi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Vithkuqi Serif font, hinted.

%package -n noto-serif-yezidi-fonts
Summary:        Noto Yezidi Serif Font
Group:          System/X11/Fonts
Obsoletes:      noto-serif-yezidi < %{version}
Provides:       noto-serif-yezidi = %{version}
%reconfigure_fonts_prereq

%description -n noto-serif-yezidi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Yezidi Serif font, hinted.

%package -n noto-tinos-fonts
Summary:        Noto Tinos Font
Group:          System/X11/Fonts
Obsoletes:      noto-tinos < %{version}
Provides:       noto-tinos = %{version}
Obsoletes:      google-tinos-fonts < %{version}
Provides:       google-tinos-fonts = %{version}
%reconfigure_fonts_prereq

%description -n noto-tinos-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tinos font, hinted.

%package -n noto-traditionalnushu-fonts
Summary:        Noto Traditional Nushu Font
Group:          System/X11/Fonts
Obsoletes:      noto-traditionalnushu < %{version}
Provides:       noto-traditionalnushu = %{version}
%reconfigure_fonts_prereq

%description -n noto-traditionalnushu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TraditionalNushu font, hinted.

%prep
tar -xzf %{SOURCE0} -C .

# Arimo BoldItalic has an extra "Italic" style
# https://bugzilla.suse.com/show_bug.cgi?id=1202279 and https://github.com/notofonts/Arimo/issues/14
# Fix weight too https://github.com/notofonts/Arimo/issues/13
ttx ttf/Arimo/Arimo-BoldItalic.ttf
%patch0
ttx -f ttf/Arimo/Arimo-BoldItalic.ttx
rm ttf/Arimo/Arimo-BoldItalic.ttx

cp %{SOURCE2} .

%build

%install
# Tifinagh fonts have duplicates in NotoSansTifinagh folder
# https://github.com/googlefonts/noto-fonts/issues/2177 and https://github.com/googlefonts/noto-fonts/issues/2326
rm ttf/NotoSansTifinagh/NotoSansTifinagh[!\-]*

# NotoSansDisplay is already provided by NotoSans
# Also they have inconsistent family names: https://github.com/googlefonts/noto-fonts/issues/2315
rm -r ttf/NotoSansDisplay/

install -Dm 644 -t %{buildroot}%{_ttfontsdir} ttf/*/*.ttf

%reconfigure_fonts_scriptlets -n noto-arimo-fonts

%reconfigure_fonts_scriptlets -n noto-cousine-fonts

%reconfigure_fonts_scriptlets -n noto-kufiarabic-fonts

%reconfigure_fonts_scriptlets -n noto-loopedlao-fonts

%reconfigure_fonts_scriptlets -n noto-loopedlao-ui-fonts

%reconfigure_fonts_scriptlets -n noto-loopedthai-fonts

%reconfigure_fonts_scriptlets -n noto-loopedthai-ui-fonts

%reconfigure_fonts_scriptlets -n noto-music-fonts

%reconfigure_fonts_scriptlets -n noto-naskharabic-fonts

%reconfigure_fonts_scriptlets -n noto-naskharabic-ui-fonts

%reconfigure_fonts_scriptlets -n noto-nastaliqurdu-fonts

%reconfigure_fonts_scriptlets -n noto-rashihebrew-fonts

%reconfigure_fonts_scriptlets -n noto-sans-fonts

%reconfigure_fonts_scriptlets -n noto-sans-adlam-fonts

%reconfigure_fonts_scriptlets -n noto-sans-adlamunjoined-fonts

%reconfigure_fonts_scriptlets -n noto-sans-anatolianhieroglyphs-fonts

%reconfigure_fonts_scriptlets -n noto-sans-arabic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-arabic-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-armenian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-avestan-fonts

%reconfigure_fonts_scriptlets -n noto-sans-balinese-fonts

%reconfigure_fonts_scriptlets -n noto-sans-bamum-fonts

%reconfigure_fonts_scriptlets -n noto-sans-bassavah-fonts

%reconfigure_fonts_scriptlets -n noto-sans-batak-fonts

%reconfigure_fonts_scriptlets -n noto-sans-bengali-fonts

%reconfigure_fonts_scriptlets -n noto-sans-bengali-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-bhaiksuki-fonts

%reconfigure_fonts_scriptlets -n noto-sans-brahmi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-buginese-fonts

%reconfigure_fonts_scriptlets -n noto-sans-buhid-fonts

%reconfigure_fonts_scriptlets -n noto-sans-canadianaboriginal-fonts

%reconfigure_fonts_scriptlets -n noto-sans-carian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-caucasianalbanian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-chakma-fonts

%reconfigure_fonts_scriptlets -n noto-sans-cham-fonts

%reconfigure_fonts_scriptlets -n noto-sans-cherokee-fonts

%reconfigure_fonts_scriptlets -n noto-sans-chorasmian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-coptic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-cuneiform-fonts

%reconfigure_fonts_scriptlets -n noto-sans-cypriot-fonts

%reconfigure_fonts_scriptlets -n noto-sans-cyprominoan-fonts

%reconfigure_fonts_scriptlets -n noto-sans-deseret-fonts

%reconfigure_fonts_scriptlets -n noto-sans-devanagari-fonts

%reconfigure_fonts_scriptlets -n noto-sans-devanagari-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-duployan-fonts

%reconfigure_fonts_scriptlets -n noto-sans-egyptianhieroglyphs-fonts

%reconfigure_fonts_scriptlets -n noto-sans-elbasan-fonts

%reconfigure_fonts_scriptlets -n noto-sans-elymaic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-ethiopic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-georgian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-glagolitic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-gothic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-grantha-fonts

%reconfigure_fonts_scriptlets -n noto-sans-gujarati-fonts

%reconfigure_fonts_scriptlets -n noto-sans-gujarati-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-gunjalagondi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-gurmukhi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-gurmukhi-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hanifirohingya-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hanunoo-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hatran-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hebrew-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hebrewdroid-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hebrewnew-fonts

%reconfigure_fonts_scriptlets -n noto-sans-imperialaramaic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-indicsiyaqnumbers-fonts

%reconfigure_fonts_scriptlets -n noto-sans-inscriptionalpahlavi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-inscriptionalparthian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-javanese-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kaithi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kannada-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kannada-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kayahli-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kharoshthi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-khmer-fonts

%reconfigure_fonts_scriptlets -n noto-sans-khmer-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-khojki-fonts

%reconfigure_fonts_scriptlets -n noto-sans-khudawadi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-lao-fonts

%reconfigure_fonts_scriptlets -n noto-sans-lao-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-lepcha-fonts

%reconfigure_fonts_scriptlets -n noto-sans-limbu-fonts

%reconfigure_fonts_scriptlets -n noto-sans-lineara-fonts

%reconfigure_fonts_scriptlets -n noto-sans-linearb-fonts

%reconfigure_fonts_scriptlets -n noto-sans-lisu-fonts

%reconfigure_fonts_scriptlets -n noto-sans-lycian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-lydian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-mahajani-fonts

%reconfigure_fonts_scriptlets -n noto-sans-malayalam-fonts

%reconfigure_fonts_scriptlets -n noto-sans-malayalam-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-mandaic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-manichaean-fonts

%reconfigure_fonts_scriptlets -n noto-sans-marchen-fonts

%reconfigure_fonts_scriptlets -n noto-sans-masaramgondi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-math-fonts

%reconfigure_fonts_scriptlets -n noto-sans-mayannumerals-fonts

%reconfigure_fonts_scriptlets -n noto-sans-medefaidrin-fonts

%reconfigure_fonts_scriptlets -n noto-sans-meeteimayek-fonts

%reconfigure_fonts_scriptlets -n noto-sans-mendekikakui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-meroitic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-miao-fonts

%reconfigure_fonts_scriptlets -n noto-sans-modi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-mongolian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-mono-fonts

%reconfigure_fonts_scriptlets -n noto-sans-mro-fonts

%reconfigure_fonts_scriptlets -n noto-sans-multani-fonts

%reconfigure_fonts_scriptlets -n noto-sans-myanmar-fonts

%reconfigure_fonts_scriptlets -n noto-sans-myanmar-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-nabataean-fonts

%reconfigure_fonts_scriptlets -n noto-sans-nandinagari-fonts

%reconfigure_fonts_scriptlets -n noto-sans-newa-fonts

%reconfigure_fonts_scriptlets -n noto-sans-newtailue-fonts

%reconfigure_fonts_scriptlets -n noto-sans-nko-fonts

%reconfigure_fonts_scriptlets -n noto-sans-nushu-fonts

%reconfigure_fonts_scriptlets -n noto-sans-ogham-fonts

%reconfigure_fonts_scriptlets -n noto-sans-olchiki-fonts

%reconfigure_fonts_scriptlets -n noto-sans-oldhungarian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-olditalic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-oldnortharabian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-oldpermic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-oldpersian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-oldsogdian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-oldsoutharabian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-oldturkic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-oriya-fonts

%reconfigure_fonts_scriptlets -n noto-sans-oriya-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-osage-fonts

%reconfigure_fonts_scriptlets -n noto-sans-osmanya-fonts

%reconfigure_fonts_scriptlets -n noto-sans-pahawhhmong-fonts

%reconfigure_fonts_scriptlets -n noto-sans-palmyrene-fonts

%reconfigure_fonts_scriptlets -n noto-sans-paucinhau-fonts

%reconfigure_fonts_scriptlets -n noto-sans-phagspa-fonts

%reconfigure_fonts_scriptlets -n noto-sans-phoenician-fonts

%reconfigure_fonts_scriptlets -n noto-sans-psalterpahlavi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-rejang-fonts

%reconfigure_fonts_scriptlets -n noto-sans-runic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-samaritan-fonts

%reconfigure_fonts_scriptlets -n noto-sans-saurashtra-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sharada-fonts

%reconfigure_fonts_scriptlets -n noto-sans-shavian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-siddham-fonts

%reconfigure_fonts_scriptlets -n noto-sans-signwriting-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sinhala-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sinhala-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sogdian-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sorasompeng-fonts

%reconfigure_fonts_scriptlets -n noto-sans-soyombo-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sundanese-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sylotinagri-fonts

%reconfigure_fonts_scriptlets -n noto-sans-symbols-fonts

%reconfigure_fonts_scriptlets -n noto-sans-symbols2-fonts

%reconfigure_fonts_scriptlets -n noto-sans-syriac-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tagalog-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tagbanwa-fonts

%reconfigure_fonts_scriptlets -n noto-sans-taile-fonts

%reconfigure_fonts_scriptlets -n noto-sans-taitham-fonts

%reconfigure_fonts_scriptlets -n noto-sans-taiviet-fonts

%reconfigure_fonts_scriptlets -n noto-sans-takri-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tamil-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tamilsupplement-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tamil-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tangsa-fonts

%reconfigure_fonts_scriptlets -n noto-sans-telugu-fonts

%reconfigure_fonts_scriptlets -n noto-sans-telugu-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-thaana-fonts

%reconfigure_fonts_scriptlets -n noto-sans-thai-fonts

%reconfigure_fonts_scriptlets -n noto-sans-thai-ui-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tifinagh-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tifinaghadrar-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tifinaghagrawimazighen-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tifinaghahaggar-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tifinaghair-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tifinaghapt-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tifinaghazawagh-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tifinaghghat-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tifinaghhawad-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tifinaghrhissaixa-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tifinaghsil-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tifinaghtawellemmet-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tirhuta-fonts

%reconfigure_fonts_scriptlets -n noto-sans-ugaritic-fonts

%reconfigure_fonts_scriptlets -n noto-sans-vai-fonts

%reconfigure_fonts_scriptlets -n noto-sans-vithkuqi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-wancho-fonts

%reconfigure_fonts_scriptlets -n noto-sans-warangciti-fonts

%reconfigure_fonts_scriptlets -n noto-sans-yi-fonts

%reconfigure_fonts_scriptlets -n noto-sans-zanabazarsquare-fonts

%reconfigure_fonts_scriptlets -n noto-serif-fonts

%reconfigure_fonts_scriptlets -n noto-serif-ahom-fonts

%reconfigure_fonts_scriptlets -n noto-serif-armenian-fonts

%reconfigure_fonts_scriptlets -n noto-serif-balinese-fonts

%reconfigure_fonts_scriptlets -n noto-serif-bengali-fonts

%reconfigure_fonts_scriptlets -n noto-serif-devanagari-fonts

%reconfigure_fonts_scriptlets -n noto-serif-display-fonts

%reconfigure_fonts_scriptlets -n noto-serif-divesakuru-fonts

%reconfigure_fonts_scriptlets -n noto-serif-dogra-fonts

%reconfigure_fonts_scriptlets -n noto-serif-ethiopic-fonts

%reconfigure_fonts_scriptlets -n noto-serif-georgian-fonts

%reconfigure_fonts_scriptlets -n noto-serif-grantha-fonts

%reconfigure_fonts_scriptlets -n noto-serif-gujarati-fonts

%reconfigure_fonts_scriptlets -n noto-serif-gurmukhi-fonts

%reconfigure_fonts_scriptlets -n noto-serif-hebrew-fonts

%reconfigure_fonts_scriptlets -n noto-serif-kannada-fonts

%reconfigure_fonts_scriptlets -n noto-serif-khmer-fonts

%reconfigure_fonts_scriptlets -n noto-serif-khojki-fonts

%reconfigure_fonts_scriptlets -n noto-serif-lao-fonts

%reconfigure_fonts_scriptlets -n noto-serif-makasar-fonts

%reconfigure_fonts_scriptlets -n noto-serif-malayalam-fonts

%reconfigure_fonts_scriptlets -n noto-serif-myanmar-fonts

%reconfigure_fonts_scriptlets -n noto-serif-nyiakengpuachuehmong-fonts

%reconfigure_fonts_scriptlets -n noto-serif-olduyghur-fonts

%reconfigure_fonts_scriptlets -n noto-serif-oriya-fonts

%reconfigure_fonts_scriptlets -n noto-serif-sinhala-fonts

%reconfigure_fonts_scriptlets -n noto-serif-tamil-fonts

%reconfigure_fonts_scriptlets -n noto-serif-tamilslanted-fonts

%reconfigure_fonts_scriptlets -n noto-serif-tangut-fonts

%reconfigure_fonts_scriptlets -n noto-serif-telugu-fonts

%reconfigure_fonts_scriptlets -n noto-serif-thai-fonts

%reconfigure_fonts_scriptlets -n noto-serif-tibetan-fonts

%reconfigure_fonts_scriptlets -n noto-serif-toto-fonts

%reconfigure_fonts_scriptlets -n noto-serif-vithkuqi-fonts

%reconfigure_fonts_scriptlets -n noto-serif-yezidi-fonts

%reconfigure_fonts_scriptlets -n noto-tinos-fonts

%reconfigure_fonts_scriptlets -n noto-traditionalnushu-fonts

%files -n noto-fonts
%defattr(0644,root,root,755)

%files -n noto-arimo-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/Arimo-*.?tf

%files -n noto-cousine-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/Cousine-*.?tf

%files -n noto-kufiarabic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoKufiArabic-*.?tf

%files -n noto-loopedlao-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoLoopedLao-*.?tf

%files -n noto-loopedlao-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoLoopedLaoUI-*.?tf

%files -n noto-loopedthai-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoLoopedThai-*.?tf

%files -n noto-loopedthai-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoLoopedThaiUI-*.?tf

%files -n noto-music-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoMusic-*.?tf

%files -n noto-naskharabic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoNaskhArabic-*.?tf

%files -n noto-naskharabic-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoNaskhArabicUI-*.?tf

%files -n noto-nastaliqurdu-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoNastaliqUrdu-*.?tf

%files -n noto-rashihebrew-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoRashiHebrew-*.?tf

%files -n noto-sans-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSans-*.?tf

%files -n noto-sans-adlam-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansAdlam-*.?tf

%files -n noto-sans-adlamunjoined-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansAdlamUnjoined-*.?tf

%files -n noto-sans-anatolianhieroglyphs-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansAnatolianHieroglyphs-*.?tf

%files -n noto-sans-arabic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansArabic-*.?tf

%files -n noto-sans-arabic-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansArabicUI-*.?tf

%files -n noto-sans-armenian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansArmenian-*.?tf

%files -n noto-sans-avestan-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansAvestan-*.?tf

%files -n noto-sans-balinese-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBalinese-*.?tf

%files -n noto-sans-bamum-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBamum-*.?tf

%files -n noto-sans-bassavah-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBassaVah-*.?tf

%files -n noto-sans-batak-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBatak-*.?tf

%files -n noto-sans-bengali-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBengali-*.?tf

%files -n noto-sans-bengali-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBengaliUI-*.?tf

%files -n noto-sans-bhaiksuki-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBhaiksuki-*.?tf

%files -n noto-sans-brahmi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBrahmi-*.?tf

%files -n noto-sans-buginese-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBuginese-*.?tf

%files -n noto-sans-buhid-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBuhid-*.?tf

%files -n noto-sans-canadianaboriginal-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCanadianAboriginal-*.?tf

%files -n noto-sans-carian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCarian-*.?tf

%files -n noto-sans-caucasianalbanian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCaucasianAlbanian-*.?tf

%files -n noto-sans-chakma-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansChakma-*.?tf

%files -n noto-sans-cham-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCham-*.?tf

%files -n noto-sans-cherokee-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCherokee-*.?tf

%files -n noto-sans-chorasmian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansChorasmian-*.?tf

%files -n noto-sans-coptic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCoptic-*.?tf

%files -n noto-sans-cuneiform-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCuneiform-*.?tf

%files -n noto-sans-cypriot-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCypriot-*.?tf

%files -n noto-sans-cyprominoan-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCyproMinoan-*.?tf

%files -n noto-sans-deseret-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansDeseret-*.?tf

%files -n noto-sans-devanagari-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansDevanagari-*.?tf

%files -n noto-sans-devanagari-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansDevanagariUI-*.?tf

%files -n noto-sans-duployan-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansDuployan-*.?tf

%files -n noto-sans-egyptianhieroglyphs-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansEgyptianHieroglyphs-*.?tf

%files -n noto-sans-elbasan-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansElbasan-*.?tf

%files -n noto-sans-elymaic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansElymaic-*.?tf

%files -n noto-sans-ethiopic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansEthiopic-*.?tf

%files -n noto-sans-georgian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGeorgian-*.?tf

%files -n noto-sans-glagolitic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGlagolitic-*.?tf

%files -n noto-sans-gothic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGothic-*.?tf

%files -n noto-sans-grantha-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGrantha-*.?tf

%files -n noto-sans-gujarati-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGujarati-*.?tf

%files -n noto-sans-gujarati-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGujaratiUI-*.?tf

%files -n noto-sans-gunjalagondi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGunjalaGondi-*.?tf

%files -n noto-sans-gurmukhi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGurmukhi-*.?tf

%files -n noto-sans-gurmukhi-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGurmukhiUI-*.?tf

%files -n noto-sans-hanifirohingya-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHanifiRohingya-*.?tf

%files -n noto-sans-hanunoo-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHanunoo-*.?tf

%files -n noto-sans-hatran-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHatran-*.?tf

%files -n noto-sans-hebrew-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHebrew-*.?tf

%files -n noto-sans-hebrewdroid-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHebrewDroid-*.?tf

%files -n noto-sans-hebrewnew-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHebrewNew-*.?tf

%files -n noto-sans-imperialaramaic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansImperialAramaic-*.?tf

%files -n noto-sans-indicsiyaqnumbers-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansIndicSiyaqNumbers-*.?tf

%files -n noto-sans-inscriptionalpahlavi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansInscriptionalPahlavi-*.?tf

%files -n noto-sans-inscriptionalparthian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansInscriptionalParthian-*.?tf

%files -n noto-sans-javanese-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansJavanese-*.?tf

%files -n noto-sans-kaithi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKaithi-*.?tf

%files -n noto-sans-kannada-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKannada-*.?tf

%files -n noto-sans-kannada-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKannadaUI-*.?tf

%files -n noto-sans-kayahli-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKayahLi-*.?tf

%files -n noto-sans-kharoshthi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKharoshthi-*.?tf

%files -n noto-sans-khmer-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKhmer-*.?tf

%files -n noto-sans-khmer-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKhmerUI-*.?tf

%files -n noto-sans-khojki-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKhojki-*.?tf

%files -n noto-sans-khudawadi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKhudawadi-*.?tf

%files -n noto-sans-lao-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLao-*.?tf

%files -n noto-sans-lao-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLaoUI-*.?tf

%files -n noto-sans-lepcha-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLepcha-*.?tf

%files -n noto-sans-limbu-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLimbu-*.?tf

%files -n noto-sans-lineara-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLinearA-*.?tf

%files -n noto-sans-linearb-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLinearB-*.?tf

%files -n noto-sans-lisu-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLisu-*.?tf

%files -n noto-sans-lycian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLycian-*.?tf

%files -n noto-sans-lydian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLydian-*.?tf

%files -n noto-sans-mahajani-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMahajani-*.?tf

%files -n noto-sans-malayalam-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMalayalam-*.?tf

%files -n noto-sans-malayalam-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMalayalamUI-*.?tf

%files -n noto-sans-mandaic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMandaic-*.?tf

%files -n noto-sans-manichaean-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansManichaean-*.?tf

%files -n noto-sans-marchen-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMarchen-*.?tf

%files -n noto-sans-masaramgondi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMasaramGondi-*.?tf

%files -n noto-sans-math-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMath-*.?tf

%files -n noto-sans-mayannumerals-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMayanNumerals-*.?tf

%files -n noto-sans-medefaidrin-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMedefaidrin-*.?tf

%files -n noto-sans-meeteimayek-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMeeteiMayek-*.?tf

%files -n noto-sans-mendekikakui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMendeKikakui-*.?tf

%files -n noto-sans-meroitic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMeroitic-*.?tf

%files -n noto-sans-miao-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMiao-*.?tf

%files -n noto-sans-modi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansModi-*.?tf

%files -n noto-sans-mongolian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMongolian-*.?tf

%files -n noto-sans-mono-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMono-*.?tf

%files -n noto-sans-mro-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMro-*.?tf

%files -n noto-sans-multani-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMultani-*.?tf

%files -n noto-sans-myanmar-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMyanmar-*.?tf

%files -n noto-sans-myanmar-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMyanmarUI-*.?tf

%files -n noto-sans-nabataean-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNabataean-*.?tf

%files -n noto-sans-nandinagari-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNandinagari-*.?tf

%files -n noto-sans-newa-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNewa-*.?tf

%files -n noto-sans-newtailue-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNewTaiLue-*.?tf

%files -n noto-sans-nko-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNKo-*.?tf

%files -n noto-sans-nushu-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNushu-*.?tf

%files -n noto-sans-ogham-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOgham-*.?tf

%files -n noto-sans-olchiki-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOlChiki-*.?tf

%files -n noto-sans-oldhungarian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldHungarian-*.?tf

%files -n noto-sans-olditalic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldItalic-*.?tf

%files -n noto-sans-oldnortharabian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldNorthArabian-*.?tf

%files -n noto-sans-oldpermic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldPermic-*.?tf

%files -n noto-sans-oldpersian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldPersian-*.?tf

%files -n noto-sans-oldsogdian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldSogdian-*.?tf

%files -n noto-sans-oldsoutharabian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldSouthArabian-*.?tf

%files -n noto-sans-oldturkic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldTurkic-*.?tf

%files -n noto-sans-oriya-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOriya-*.?tf

%files -n noto-sans-oriya-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOriyaUI-*.?tf

%files -n noto-sans-osage-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOsage-*.?tf

%files -n noto-sans-osmanya-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOsmanya-*.?tf

%files -n noto-sans-pahawhhmong-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPahawhHmong-*.?tf

%files -n noto-sans-palmyrene-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPalmyrene-*.?tf

%files -n noto-sans-paucinhau-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPauCinHau-*.?tf

%files -n noto-sans-phagspa-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPhagsPa-*.?tf

%files -n noto-sans-phoenician-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPhoenician-*.?tf

%files -n noto-sans-psalterpahlavi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPsalterPahlavi-*.?tf

%files -n noto-sans-rejang-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansRejang-*.?tf

%files -n noto-sans-runic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansRunic-*.?tf

%files -n noto-sans-samaritan-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSamaritan-*.?tf

%files -n noto-sans-saurashtra-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSaurashtra-*.?tf

%files -n noto-sans-sharada-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSharada-*.?tf

%files -n noto-sans-shavian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansShavian-*.?tf

%files -n noto-sans-siddham-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSiddham-*.?tf

%files -n noto-sans-signwriting-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSignWriting-*.?tf

%files -n noto-sans-sinhala-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSinhala-*.?tf

%files -n noto-sans-sinhala-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSinhalaUI-*.?tf

%files -n noto-sans-sogdian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSogdian-*.?tf

%files -n noto-sans-sorasompeng-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSoraSompeng-*.?tf

%files -n noto-sans-soyombo-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSoyombo-*.?tf

%files -n noto-sans-sundanese-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSundanese-*.?tf

%files -n noto-sans-sylotinagri-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSylotiNagri-*.?tf

%files -n noto-sans-symbols-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSymbols-*.?tf

%files -n noto-sans-symbols2-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSymbols2-*.?tf

%files -n noto-sans-syriac-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSyriac-*.?tf

%files -n noto-sans-tagalog-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTagalog-*.?tf

%files -n noto-sans-tagbanwa-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTagbanwa-*.?tf

%files -n noto-sans-taile-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTaiLe-*.?tf

%files -n noto-sans-taitham-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTaiTham-*.?tf

%files -n noto-sans-taiviet-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTaiViet-*.?tf

%files -n noto-sans-takri-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTakri-*.?tf

%files -n noto-sans-tamil-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTamil-*.?tf

%files -n noto-sans-tamilsupplement-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTamilSupplement-*.?tf

%files -n noto-sans-tamil-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTamilUI-*.?tf

%files -n noto-sans-tangsa-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTangsa-*.?tf

%files -n noto-sans-telugu-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTelugu-*.?tf

%files -n noto-sans-telugu-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTeluguUI-*.?tf

%files -n noto-sans-thaana-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansThaana-*.?tf

%files -n noto-sans-thai-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansThai-*.?tf

%files -n noto-sans-thai-ui-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansThaiUI-*.?tf

%files -n noto-sans-tifinagh-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinagh-*.?tf

%files -n noto-sans-tifinaghadrar-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinaghAdrar-*.?tf

%files -n noto-sans-tifinaghagrawimazighen-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinaghAgrawImazighen-*.?tf

%files -n noto-sans-tifinaghahaggar-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinaghAhaggar-*.?tf

%files -n noto-sans-tifinaghair-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinaghAir-*.?tf

%files -n noto-sans-tifinaghapt-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinaghAPT-*.?tf

%files -n noto-sans-tifinaghazawagh-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinaghAzawagh-*.?tf

%files -n noto-sans-tifinaghghat-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinaghGhat-*.?tf

%files -n noto-sans-tifinaghhawad-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinaghHawad-*.?tf

%files -n noto-sans-tifinaghrhissaixa-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinaghRhissaIxa-*.?tf

%files -n noto-sans-tifinaghsil-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinaghSIL-*.?tf

%files -n noto-sans-tifinaghtawellemmet-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinaghTawellemmet-*.?tf

%files -n noto-sans-tirhuta-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTirhuta-*.?tf

%files -n noto-sans-ugaritic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansUgaritic-*.?tf

%files -n noto-sans-vai-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansVai-*.?tf

%files -n noto-sans-vithkuqi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansVithkuqi-*.?tf

%files -n noto-sans-wancho-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansWancho-*.?tf

%files -n noto-sans-warangciti-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansWarangCiti-*.?tf

%files -n noto-sans-yi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansYi-*.?tf

%files -n noto-sans-zanabazarsquare-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansZanabazarSquare-*.?tf

%files -n noto-serif-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerif-*.?tf

%files -n noto-serif-ahom-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifAhom-*.?tf

%files -n noto-serif-armenian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifArmenian-*.?tf

%files -n noto-serif-balinese-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifBalinese-*.?tf

%files -n noto-serif-bengali-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifBengali-*.?tf

%files -n noto-serif-devanagari-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifDevanagari-*.?tf

%files -n noto-serif-display-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifDisplay-*.?tf

%files -n noto-serif-divesakuru-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifDivesAkuru-*.?tf

%files -n noto-serif-dogra-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifDogra-*.?tf

%files -n noto-serif-ethiopic-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifEthiopic-*.?tf

%files -n noto-serif-georgian-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifGeorgian-*.?tf

%files -n noto-serif-grantha-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifGrantha-*.?tf

%files -n noto-serif-gujarati-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifGujarati-*.?tf

%files -n noto-serif-gurmukhi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifGurmukhi-*.?tf

%files -n noto-serif-hebrew-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifHebrew-*.?tf

%files -n noto-serif-kannada-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifKannada-*.?tf

%files -n noto-serif-khmer-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifKhmer-*.?tf

%files -n noto-serif-khojki-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifKhojki-*.?tf

%files -n noto-serif-lao-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifLao-*.?tf

%files -n noto-serif-makasar-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifMakasar-*.?tf

%files -n noto-serif-malayalam-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifMalayalam-*.?tf

%files -n noto-serif-myanmar-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifMyanmar-*.?tf

%files -n noto-serif-nyiakengpuachuehmong-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifNyiakengPuachueHmong-*.?tf

%files -n noto-serif-olduyghur-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifOldUyghur-*.?tf

%files -n noto-serif-oriya-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifOriya-*.?tf

%files -n noto-serif-sinhala-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifSinhala-*.?tf

%files -n noto-serif-tamil-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifTamil-*.?tf

%files -n noto-serif-tamilslanted-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifTamilSlanted-*.?tf

%files -n noto-serif-tangut-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifTangut-*.?tf

%files -n noto-serif-telugu-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifTelugu-*.?tf

%files -n noto-serif-thai-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifThai-*.?tf

%files -n noto-serif-tibetan-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifTibetan-*.?tf

%files -n noto-serif-toto-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifToto-*.?tf

%files -n noto-serif-vithkuqi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifVithkuqi-*.?tf

%files -n noto-serif-yezidi-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifYezidi-*.?tf

%files -n noto-tinos-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/Tinos-*.?tf

%files -n noto-traditionalnushu-fonts
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoTraditionalNushu-*.?tf

%changelog
