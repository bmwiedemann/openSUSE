#
# spec file for package google-noto-fonts
#
# Copyright (c) 2024 SUSE LLC
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


%define hyear     2024
%define hmonth    06
%define hday      01

%define src_name  NotoFonts

# DO NOT EDIT THIS SPECFILE DIRECTLY, edit google-noto-fonts.spec.in and run generate-specfile.sh script

Name:           google-noto-fonts
Version:        %{hyear}%{hmonth}%{hday}
Release:        0
Summary:        All Noto Fonts except CJK and Emoji
License:        OFL-1.1
URL:            https://notofonts.github.io/
# https://github.com/notofonts/notofonts.github.io/archive/refs/tags/noto-monthly-release-24.6.1.tar.gz
Source0:        notofonts.github.io-noto-monthly-release-24.6.1.tar.gz
Source1:        generate-specfile.sh
Source2:        README.FAQ
Source3:        README.maintain
BuildRequires:  fontpackages-devel
BuildArch:      noarch
Obsoletes:      noto-fonts < %{version}
Provides:       noto-fonts = %{version}
Requires:       google-noto-fangsongkssrotated-fonts
Requires:       google-noto-fangsongkssvertical-fonts
Requires:       google-noto-kufiarabic-fonts
Requires:       google-noto-music-fonts
Requires:       google-noto-naskharabic-fonts
Requires:       google-noto-nastaliqurdu-fonts
Requires:       google-noto-rashihebrew-fonts
Requires:       google-noto-sans-adlam-fonts
Requires:       google-noto-sans-adlamunjoined-fonts
Requires:       google-noto-sans-anatolianhieroglyphs-fonts
Requires:       google-noto-sans-arabic-fonts
Requires:       google-noto-sans-armenian-fonts
Requires:       google-noto-sans-avestan-fonts
Requires:       google-noto-sans-balinese-fonts
Requires:       google-noto-sans-bamum-fonts
Requires:       google-noto-sans-bassavah-fonts
Requires:       google-noto-sans-batak-fonts
Requires:       google-noto-sans-bengali-fonts
Requires:       google-noto-sans-bhaiksuki-fonts
Requires:       google-noto-sans-brahmi-fonts
Requires:       google-noto-sans-buginese-fonts
Requires:       google-noto-sans-buhid-fonts
Requires:       google-noto-sans-canadianaboriginal-fonts
Requires:       google-noto-sans-carian-fonts
Requires:       google-noto-sans-caucasianalbanian-fonts
Requires:       google-noto-sans-chakma-fonts
Requires:       google-noto-sans-cham-fonts
Requires:       google-noto-sans-cherokee-fonts
Requires:       google-noto-sans-chorasmian-fonts
Requires:       google-noto-sans-coptic-fonts
Requires:       google-noto-sans-cuneiform-fonts
Requires:       google-noto-sans-cypriot-fonts
Requires:       google-noto-sans-cyprominoan-fonts
Requires:       google-noto-sans-deseret-fonts
Requires:       google-noto-sans-devanagari-fonts
Requires:       google-noto-sans-duployan-fonts
Requires:       google-noto-sans-egyptianhieroglyphs-fonts
Requires:       google-noto-sans-elbasan-fonts
Requires:       google-noto-sans-elymaic-fonts
Requires:       google-noto-sans-ethiopic-fonts
Requires:       google-noto-sans-fonts
Requires:       google-noto-sans-georgian-fonts
Requires:       google-noto-sans-glagolitic-fonts
Requires:       google-noto-sans-gothic-fonts
Requires:       google-noto-sans-grantha-fonts
Requires:       google-noto-sans-gujarati-fonts
Requires:       google-noto-sans-gunjalagondi-fonts
Requires:       google-noto-sans-gurmukhi-fonts
Requires:       google-noto-sans-hanifirohingya-fonts
Requires:       google-noto-sans-hanunoo-fonts
Requires:       google-noto-sans-hatran-fonts
Requires:       google-noto-sans-hebrew-fonts
Requires:       google-noto-sans-imperialaramaic-fonts
Requires:       google-noto-sans-indicsiyaqnumbers-fonts
Requires:       google-noto-sans-inscriptionalpahlavi-fonts
Requires:       google-noto-sans-inscriptionalparthian-fonts
Requires:       google-noto-sans-javanese-fonts
Requires:       google-noto-sans-kaithi-fonts
Requires:       google-noto-sans-kannada-fonts
Requires:       google-noto-sans-kawi-fonts
Requires:       google-noto-sans-kayahli-fonts
Requires:       google-noto-sans-kharoshthi-fonts
Requires:       google-noto-sans-khmer-fonts
Requires:       google-noto-sans-khojki-fonts
Requires:       google-noto-sans-khudawadi-fonts
Requires:       google-noto-sans-lao-fonts
Requires:       google-noto-sans-laolooped-fonts
Requires:       google-noto-sans-lepcha-fonts
Requires:       google-noto-sans-limbu-fonts
Requires:       google-noto-sans-lineara-fonts
Requires:       google-noto-sans-linearb-fonts
Requires:       google-noto-sans-lisu-fonts
Requires:       google-noto-sans-lycian-fonts
Requires:       google-noto-sans-lydian-fonts
Requires:       google-noto-sans-mahajani-fonts
Requires:       google-noto-sans-malayalam-fonts
Requires:       google-noto-sans-mandaic-fonts
Requires:       google-noto-sans-manichaean-fonts
Requires:       google-noto-sans-marchen-fonts
Requires:       google-noto-sans-masaramgondi-fonts
Requires:       google-noto-sans-math-fonts
Requires:       google-noto-sans-mayannumerals-fonts
Requires:       google-noto-sans-medefaidrin-fonts
Requires:       google-noto-sans-meeteimayek-fonts
Requires:       google-noto-sans-mendekikakui-fonts
Requires:       google-noto-sans-meroitic-fonts
Requires:       google-noto-sans-miao-fonts
Requires:       google-noto-sans-modi-fonts
Requires:       google-noto-sans-mongolian-fonts
Requires:       google-noto-sans-mono-fonts
Requires:       google-noto-sans-mro-fonts
Requires:       google-noto-sans-multani-fonts
Requires:       google-noto-sans-myanmar-fonts
Requires:       google-noto-sans-nabataean-fonts
Requires:       google-noto-sans-nagmundari-fonts
Requires:       google-noto-sans-nandinagari-fonts
Requires:       google-noto-sans-newa-fonts
Requires:       google-noto-sans-newtailue-fonts
Requires:       google-noto-sans-nko-fonts
Requires:       google-noto-sans-nkounjoined-fonts
Requires:       google-noto-sans-nushu-fonts
Requires:       google-noto-sans-ogham-fonts
Requires:       google-noto-sans-olchiki-fonts
Requires:       google-noto-sans-oldhungarian-fonts
Requires:       google-noto-sans-olditalic-fonts
Requires:       google-noto-sans-oldnortharabian-fonts
Requires:       google-noto-sans-oldpermic-fonts
Requires:       google-noto-sans-oldpersian-fonts
Requires:       google-noto-sans-oldsogdian-fonts
Requires:       google-noto-sans-oldsoutharabian-fonts
Requires:       google-noto-sans-oldturkic-fonts
Requires:       google-noto-sans-oriya-fonts
Requires:       google-noto-sans-osage-fonts
Requires:       google-noto-sans-osmanya-fonts
Requires:       google-noto-sans-pahawhhmong-fonts
Requires:       google-noto-sans-palmyrene-fonts
Requires:       google-noto-sans-paucinhau-fonts
Requires:       google-noto-sans-phagspa-fonts
Requires:       google-noto-sans-phoenician-fonts
Requires:       google-noto-sans-psalterpahlavi-fonts
Requires:       google-noto-sans-rejang-fonts
Requires:       google-noto-sans-runic-fonts
Requires:       google-noto-sans-samaritan-fonts
Requires:       google-noto-sans-saurashtra-fonts
Requires:       google-noto-sans-sharada-fonts
Requires:       google-noto-sans-shavian-fonts
Requires:       google-noto-sans-siddham-fonts
Requires:       google-noto-sans-signwriting-fonts
Requires:       google-noto-sans-sinhala-fonts
Requires:       google-noto-sans-sogdian-fonts
Requires:       google-noto-sans-sorasompeng-fonts
Requires:       google-noto-sans-soyombo-fonts
Requires:       google-noto-sans-sundanese-fonts
Requires:       google-noto-sans-sylotinagri-fonts
Requires:       google-noto-sans-symbols-fonts
Requires:       google-noto-sans-symbols2-fonts
Requires:       google-noto-sans-syriac-fonts
Requires:       google-noto-sans-syriaceastern-fonts
Requires:       google-noto-sans-syriacwestern-fonts
Requires:       google-noto-sans-tagalog-fonts
Requires:       google-noto-sans-tagbanwa-fonts
Requires:       google-noto-sans-taile-fonts
Requires:       google-noto-sans-taitham-fonts
Requires:       google-noto-sans-taiviet-fonts
Requires:       google-noto-sans-takri-fonts
Requires:       google-noto-sans-tamil-fonts
Requires:       google-noto-sans-tamilsupplement-fonts
Requires:       google-noto-sans-tangsa-fonts
Requires:       google-noto-sans-telugu-fonts
Requires:       google-noto-sans-thaana-fonts
Requires:       google-noto-sans-thai-fonts
Requires:       google-noto-sans-thailooped-fonts
Requires:       google-noto-sans-tifinagh-fonts
Requires:       google-noto-sans-tirhuta-fonts
Requires:       google-noto-sans-ugaritic-fonts
Requires:       google-noto-sans-vai-fonts
Requires:       google-noto-sans-vithkuqi-fonts
Requires:       google-noto-sans-wancho-fonts
Requires:       google-noto-sans-warangciti-fonts
Requires:       google-noto-sans-yi-fonts
Requires:       google-noto-sans-zanabazarsquare-fonts
Requires:       google-noto-serif-ahom-fonts
Requires:       google-noto-serif-armenian-fonts
Requires:       google-noto-serif-balinese-fonts
Requires:       google-noto-serif-bengali-fonts
Requires:       google-noto-serif-devanagari-fonts
Requires:       google-noto-serif-display-fonts
Requires:       google-noto-serif-divesakuru-fonts
Requires:       google-noto-serif-dogra-fonts
Requires:       google-noto-serif-ethiopic-fonts
Requires:       google-noto-serif-fonts
Requires:       google-noto-serif-georgian-fonts
Requires:       google-noto-serif-grantha-fonts
Requires:       google-noto-serif-gujarati-fonts
Requires:       google-noto-serif-gurmukhi-fonts
Requires:       google-noto-serif-hebrew-fonts
Requires:       google-noto-serif-kannada-fonts
Requires:       google-noto-serif-khitansmallscript-fonts
Requires:       google-noto-serif-khmer-fonts
Requires:       google-noto-serif-khojki-fonts
Requires:       google-noto-serif-lao-fonts
Requires:       google-noto-serif-makasar-fonts
Requires:       google-noto-serif-malayalam-fonts
Requires:       google-noto-serif-myanmar-fonts
Requires:       google-noto-serif-nphmong-fonts
Requires:       google-noto-serif-olduyghur-fonts
Requires:       google-noto-serif-oriya-fonts
Requires:       google-noto-serif-ottomansiyaq-fonts
Requires:       google-noto-serif-sinhala-fonts
Requires:       google-noto-serif-tamil-fonts
Requires:       google-noto-serif-tangut-fonts
Requires:       google-noto-serif-telugu-fonts
Requires:       google-noto-serif-thai-fonts
Requires:       google-noto-serif-tibetan-fonts
Requires:       google-noto-serif-toto-fonts
Requires:       google-noto-serif-vithkuqi-fonts
Requires:       google-noto-serif-yezidi-fonts
Requires:       google-noto-traditionalnushu-fonts
Requires:       google-noto-znamennymusicalnotation-fonts

%description
Noto's design goal is to achieve visual harmonization (e.g., compatible heights and stroke
thicknesses) across languages. This package contains most noto fonts except for CJK and Emoji.

%package -n google-noto-fangsongkssrotated-fonts
Summary:        Noto Fangsong KSSRotated Font
Obsoletes:      noto-fangsongkssrotated < %{version}
Provides:       noto-fangsongkssrotated = %{version}
Obsoletes:      noto-fangsongkssrotated-fonts < %{version}
Provides:       noto-fangsongkssrotated-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-fangsongkssrotated-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
FangsongKSSRotated font, hinted.

%package -n google-noto-fangsongkssvertical-fonts
Summary:        Noto Fangsong KSSVertical Font
Obsoletes:      noto-fangsongkssvertical < %{version}
Provides:       noto-fangsongkssvertical = %{version}
Obsoletes:      noto-fangsongkssvertical-fonts < %{version}
Provides:       noto-fangsongkssvertical-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-fangsongkssvertical-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
FangsongKSSVertical font, hinted.

%package -n google-noto-kufiarabic-fonts
Summary:        Noto Kufi Arabic Font
Obsoletes:      noto-kufiarabic < %{version}
Provides:       noto-kufiarabic = %{version}
Obsoletes:      noto-kufiarabic-fonts < %{version}
Provides:       noto-kufiarabic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-kufiarabic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
KufiArabic font, hinted.

%package -n google-noto-music-fonts
Summary:        Noto Music Font
Obsoletes:      noto-music < %{version}
Provides:       noto-music = %{version}
Obsoletes:      noto-music-fonts < %{version}
Provides:       noto-music-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-music-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Music font, hinted.

%package -n google-noto-naskharabic-fonts
Summary:        Noto Naskh Arabic Font
Obsoletes:      noto-naskharabic < %{version}
Provides:       noto-naskharabic = %{version}
Obsoletes:      noto-naskharabic-fonts < %{version}
Provides:       noto-naskharabic-fonts = %{version}
Obsoletes:      noto-naskharabic-ui < %{version}
Provides:       noto-naskharabic-ui = %{version}
Obsoletes:      noto-naskharabic-ui-fonts < %{version}
Provides:       noto-naskharabic-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-naskharabic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NaskhArabic font, hinted.

%package -n google-noto-nastaliqurdu-fonts
Summary:        Noto Nastaliq Urdu Font
Obsoletes:      noto-nastaliqurdu < %{version}
Provides:       noto-nastaliqurdu = %{version}
Obsoletes:      noto-nastaliqurdu-fonts < %{version}
Provides:       noto-nastaliqurdu-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-nastaliqurdu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NastaliqUrdu font, hinted.

%package -n google-noto-rashihebrew-fonts
Summary:        Noto Rashi Hebrew Font
Obsoletes:      noto-rashihebrew < %{version}
Provides:       noto-rashihebrew = %{version}
Obsoletes:      noto-rashihebrew-fonts < %{version}
Provides:       noto-rashihebrew-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-rashihebrew-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
RashiHebrew font, hinted.

%package -n google-noto-sans-fonts
Summary:        Noto Sans Font
Obsoletes:      noto-sans < %{version}
Provides:       noto-sans = %{version}
Obsoletes:      noto-sans-fonts < %{version}
Provides:       noto-sans-fonts = %{version}
Obsoletes:      noto-sans-display < %{version}
Provides:       noto-sans-display = %{version}
Obsoletes:      noto-sans-display-fonts < %{version}
Provides:       noto-sans-display-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sans font, hinted.

%package -n google-noto-sans-adlam-fonts
Summary:        Noto Adlam Sans Serif Font
Obsoletes:      noto-sans-adlam < %{version}
Provides:       noto-sans-adlam = %{version}
Obsoletes:      noto-sans-adlam-fonts < %{version}
Provides:       noto-sans-adlam-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-adlam-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Adlam Sans Serif font, hinted.

%package -n google-noto-sans-adlamunjoined-fonts
Summary:        Noto Adlam Unjoined Sans Serif Font
Obsoletes:      noto-sans-adlamunjoined < %{version}
Provides:       noto-sans-adlamunjoined = %{version}
Obsoletes:      noto-sans-adlamunjoined-fonts < %{version}
Provides:       noto-sans-adlamunjoined-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-adlamunjoined-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
AdlamUnjoined Sans Serif font, hinted.

%package -n google-noto-sans-anatolianhieroglyphs-fonts
Summary:        Noto Anatolian Hieroglyphs Sans Serif Font
Obsoletes:      noto-sans-anatolianhieroglyphs < %{version}
Provides:       noto-sans-anatolianhieroglyphs = %{version}
Obsoletes:      noto-sans-anatolianhieroglyphs-fonts < %{version}
Provides:       noto-sans-anatolianhieroglyphs-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-anatolianhieroglyphs-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
AnatolianHieroglyphs Sans Serif font, hinted.

%package -n google-noto-sans-arabic-fonts
Summary:        Noto Arabic Sans Serif Font
Obsoletes:      noto-sans-arabic < %{version}
Provides:       noto-sans-arabic = %{version}
Obsoletes:      noto-sans-arabic-fonts < %{version}
Provides:       noto-sans-arabic-fonts = %{version}
Obsoletes:      noto-sans-arabic-ui < %{version}
Provides:       noto-sans-arabic-ui = %{version}
Obsoletes:      noto-sans-arabic-ui-fonts < %{version}
Provides:       noto-sans-arabic-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-arabic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Arabic Sans Serif font, hinted.

%package -n google-noto-sans-armenian-fonts
Summary:        Noto Armenian Sans Serif Font
Obsoletes:      noto-sans-armenian < %{version}
Provides:       noto-sans-armenian = %{version}
Obsoletes:      noto-sans-armenian-fonts < %{version}
Provides:       noto-sans-armenian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-armenian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Armenian Sans Serif font, hinted.

%package -n google-noto-sans-avestan-fonts
Summary:        Noto Avestan Sans Serif Font
Obsoletes:      noto-sans-avestan < %{version}
Provides:       noto-sans-avestan = %{version}
Obsoletes:      noto-sans-avestan-fonts < %{version}
Provides:       noto-sans-avestan-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-avestan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Avestan Sans Serif font, hinted.

%package -n google-noto-sans-balinese-fonts
Summary:        Noto Balinese Sans Serif Font
Obsoletes:      noto-sans-balinese < %{version}
Provides:       noto-sans-balinese = %{version}
Obsoletes:      noto-sans-balinese-fonts < %{version}
Provides:       noto-sans-balinese-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-balinese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Balinese Sans Serif font, hinted.

%package -n google-noto-sans-bamum-fonts
Summary:        Noto Bamum Sans Serif Font
Obsoletes:      noto-sans-bamum < %{version}
Provides:       noto-sans-bamum = %{version}
Obsoletes:      noto-sans-bamum-fonts < %{version}
Provides:       noto-sans-bamum-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-bamum-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bamum Sans Serif font, hinted.

%package -n google-noto-sans-bassavah-fonts
Summary:        Noto Bassa Vah Sans Serif Font
Obsoletes:      noto-sans-bassavah < %{version}
Provides:       noto-sans-bassavah = %{version}
Obsoletes:      noto-sans-bassavah-fonts < %{version}
Provides:       noto-sans-bassavah-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-bassavah-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
BassaVah Sans Serif font, hinted.

%package -n google-noto-sans-batak-fonts
Summary:        Noto Batak Sans Serif Font
Obsoletes:      noto-sans-batak < %{version}
Provides:       noto-sans-batak = %{version}
Obsoletes:      noto-sans-batak-fonts < %{version}
Provides:       noto-sans-batak-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-batak-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Batak Sans Serif font, hinted.

%package -n google-noto-sans-bengali-fonts
Summary:        Noto Bengali Sans Serif Font
Obsoletes:      noto-sans-bengali < %{version}
Provides:       noto-sans-bengali = %{version}
Obsoletes:      noto-sans-bengali-fonts < %{version}
Provides:       noto-sans-bengali-fonts = %{version}
Obsoletes:      noto-sans-bengali-ui < %{version}
Provides:       noto-sans-bengali-ui = %{version}
Obsoletes:      noto-sans-bengali-ui-fonts < %{version}
Provides:       noto-sans-bengali-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-bengali-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bengali Sans Serif font, hinted.

%package -n google-noto-sans-bhaiksuki-fonts
Summary:        Noto Bhaiksuki Sans Serif Font
Obsoletes:      noto-sans-bhaiksuki < %{version}
Provides:       noto-sans-bhaiksuki = %{version}
Obsoletes:      noto-sans-bhaiksuki-fonts < %{version}
Provides:       noto-sans-bhaiksuki-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-bhaiksuki-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bhaiksuki Sans Serif font, hinted.

%package -n google-noto-sans-brahmi-fonts
Summary:        Noto Brahmi Sans Serif Font
Obsoletes:      noto-sans-brahmi < %{version}
Provides:       noto-sans-brahmi = %{version}
Obsoletes:      noto-sans-brahmi-fonts < %{version}
Provides:       noto-sans-brahmi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-brahmi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Brahmi Sans Serif font, hinted.

%package -n google-noto-sans-buginese-fonts
Summary:        Noto Buginese Sans Serif Font
Obsoletes:      noto-sans-buginese < %{version}
Provides:       noto-sans-buginese = %{version}
Obsoletes:      noto-sans-buginese-fonts < %{version}
Provides:       noto-sans-buginese-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-buginese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Buginese Sans Serif font, hinted.

%package -n google-noto-sans-buhid-fonts
Summary:        Noto Buhid Sans Serif Font
Obsoletes:      noto-sans-buhid < %{version}
Provides:       noto-sans-buhid = %{version}
Obsoletes:      noto-sans-buhid-fonts < %{version}
Provides:       noto-sans-buhid-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-buhid-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Buhid Sans Serif font, hinted.

%package -n google-noto-sans-canadianaboriginal-fonts
Summary:        Noto Canadian Aboriginal Sans Serif Font
Obsoletes:      noto-sans-canadianaboriginal < %{version}
Provides:       noto-sans-canadianaboriginal = %{version}
Obsoletes:      noto-sans-canadianaboriginal-fonts < %{version}
Provides:       noto-sans-canadianaboriginal-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-canadianaboriginal-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
CanadianAboriginal Sans Serif font, hinted.

%package -n google-noto-sans-carian-fonts
Summary:        Noto Carian Sans Serif Font
Obsoletes:      noto-sans-carian < %{version}
Provides:       noto-sans-carian = %{version}
Obsoletes:      noto-sans-carian-fonts < %{version}
Provides:       noto-sans-carian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-carian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Carian Sans Serif font, hinted.

%package -n google-noto-sans-caucasianalbanian-fonts
Summary:        Noto Caucasian Albanian Sans Serif Font
Obsoletes:      noto-sans-caucasianalbanian < %{version}
Provides:       noto-sans-caucasianalbanian = %{version}
Obsoletes:      noto-sans-caucasianalbanian-fonts < %{version}
Provides:       noto-sans-caucasianalbanian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-caucasianalbanian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
CaucasianAlbanian Sans Serif font, hinted.

%package -n google-noto-sans-chakma-fonts
Summary:        Noto Chakma Sans Serif Font
Obsoletes:      noto-sans-chakma < %{version}
Provides:       noto-sans-chakma = %{version}
Obsoletes:      noto-sans-chakma-fonts < %{version}
Provides:       noto-sans-chakma-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-chakma-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Chakma Sans Serif font, hinted.

%package -n google-noto-sans-cham-fonts
Summary:        Noto Cham Sans Serif Font
Obsoletes:      noto-sans-cham < %{version}
Provides:       noto-sans-cham = %{version}
Obsoletes:      noto-sans-cham-fonts < %{version}
Provides:       noto-sans-cham-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-cham-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cham Sans Serif font, hinted.

%package -n google-noto-sans-cherokee-fonts
Summary:        Noto Cherokee Sans Serif Font
Obsoletes:      noto-sans-cherokee < %{version}
Provides:       noto-sans-cherokee = %{version}
Obsoletes:      noto-sans-cherokee-fonts < %{version}
Provides:       noto-sans-cherokee-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-cherokee-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cherokee Sans Serif font, hinted.

%package -n google-noto-sans-chorasmian-fonts
Summary:        Noto Chorasmian Sans Serif Font
Obsoletes:      noto-sans-chorasmian < %{version}
Provides:       noto-sans-chorasmian = %{version}
Obsoletes:      noto-sans-chorasmian-fonts < %{version}
Provides:       noto-sans-chorasmian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-chorasmian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Chorasmian Sans Serif font, hinted.

%package -n google-noto-sans-coptic-fonts
Summary:        Noto Coptic Sans Serif Font
Obsoletes:      noto-sans-coptic < %{version}
Provides:       noto-sans-coptic = %{version}
Obsoletes:      noto-sans-coptic-fonts < %{version}
Provides:       noto-sans-coptic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-coptic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Coptic Sans Serif font, hinted.

%package -n google-noto-sans-cuneiform-fonts
Summary:        Noto Cuneiform Sans Serif Font
Obsoletes:      noto-sans-cuneiform < %{version}
Provides:       noto-sans-cuneiform = %{version}
Obsoletes:      noto-sans-cuneiform-fonts < %{version}
Provides:       noto-sans-cuneiform-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-cuneiform-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cuneiform Sans Serif font, hinted.

%package -n google-noto-sans-cypriot-fonts
Summary:        Noto Cypriot Sans Serif Font
Obsoletes:      noto-sans-cypriot < %{version}
Provides:       noto-sans-cypriot = %{version}
Obsoletes:      noto-sans-cypriot-fonts < %{version}
Provides:       noto-sans-cypriot-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-cypriot-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Cypriot Sans Serif font, hinted.

%package -n google-noto-sans-cyprominoan-fonts
Summary:        Noto Cypro Minoan Sans Serif Font
Obsoletes:      noto-sans-cyprominoan < %{version}
Provides:       noto-sans-cyprominoan = %{version}
Obsoletes:      noto-sans-cyprominoan-fonts < %{version}
Provides:       noto-sans-cyprominoan-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-cyprominoan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
CyproMinoan Sans Serif font, hinted.

%package -n google-noto-sans-deseret-fonts
Summary:        Noto Deseret Sans Serif Font
Obsoletes:      noto-sans-deseret < %{version}
Provides:       noto-sans-deseret = %{version}
Obsoletes:      noto-sans-deseret-fonts < %{version}
Provides:       noto-sans-deseret-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-deseret-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Deseret Sans Serif font, hinted.

%package -n google-noto-sans-devanagari-fonts
Summary:        Noto Devanagari Sans Serif Font
Obsoletes:      noto-sans-devanagari < %{version}
Provides:       noto-sans-devanagari = %{version}
Obsoletes:      noto-sans-devanagari-fonts < %{version}
Provides:       noto-sans-devanagari-fonts = %{version}
Obsoletes:      noto-sans-devanagari-ui < %{version}
Provides:       noto-sans-devanagari-ui = %{version}
Obsoletes:      noto-sans-devanagari-ui-fonts < %{version}
Provides:       noto-sans-devanagari-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-devanagari-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Devanagari Sans Serif font, hinted.

%package -n google-noto-sans-duployan-fonts
Summary:        Noto Duployan Sans Serif Font
Obsoletes:      noto-sans-duployan < %{version}
Provides:       noto-sans-duployan = %{version}
Obsoletes:      noto-sans-duployan-fonts < %{version}
Provides:       noto-sans-duployan-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-duployan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Duployan Sans Serif font, hinted.

%package -n google-noto-sans-egyptianhieroglyphs-fonts
Summary:        Noto Egyptian Hieroglyphs Sans Serif Font
Obsoletes:      noto-sans-egyptianhieroglyphs < %{version}
Provides:       noto-sans-egyptianhieroglyphs = %{version}
Obsoletes:      noto-sans-egyptianhieroglyphs-fonts < %{version}
Provides:       noto-sans-egyptianhieroglyphs-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-egyptianhieroglyphs-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
EgyptianHieroglyphs Sans Serif font, hinted.

%package -n google-noto-sans-elbasan-fonts
Summary:        Noto Elbasan Sans Serif Font
Obsoletes:      noto-sans-elbasan < %{version}
Provides:       noto-sans-elbasan = %{version}
Obsoletes:      noto-sans-elbasan-fonts < %{version}
Provides:       noto-sans-elbasan-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-elbasan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Elbasan Sans Serif font, hinted.

%package -n google-noto-sans-elymaic-fonts
Summary:        Noto Elymaic Sans Serif Font
Obsoletes:      noto-sans-elymaic < %{version}
Provides:       noto-sans-elymaic = %{version}
Obsoletes:      noto-sans-elymaic-fonts < %{version}
Provides:       noto-sans-elymaic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-elymaic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Elymaic Sans Serif font, hinted.

%package -n google-noto-sans-ethiopic-fonts
Summary:        Noto Ethiopic Sans Serif Font
Obsoletes:      noto-sans-ethiopic < %{version}
Provides:       noto-sans-ethiopic = %{version}
Obsoletes:      noto-sans-ethiopic-fonts < %{version}
Provides:       noto-sans-ethiopic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-ethiopic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ethiopic Sans Serif font, hinted.

%package -n google-noto-sans-georgian-fonts
Summary:        Noto Georgian Sans Serif Font
Obsoletes:      noto-sans-georgian < %{version}
Provides:       noto-sans-georgian = %{version}
Obsoletes:      noto-sans-georgian-fonts < %{version}
Provides:       noto-sans-georgian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-georgian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Georgian Sans Serif font, hinted.

%package -n google-noto-sans-glagolitic-fonts
Summary:        Noto Glagolitic Sans Serif Font
Obsoletes:      noto-sans-glagolitic < %{version}
Provides:       noto-sans-glagolitic = %{version}
Obsoletes:      noto-sans-glagolitic-fonts < %{version}
Provides:       noto-sans-glagolitic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-glagolitic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Glagolitic Sans Serif font, hinted.

%package -n google-noto-sans-gothic-fonts
Summary:        Noto Gothic Sans Serif Font
Obsoletes:      noto-sans-gothic < %{version}
Provides:       noto-sans-gothic = %{version}
Obsoletes:      noto-sans-gothic-fonts < %{version}
Provides:       noto-sans-gothic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-gothic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gothic Sans Serif font, hinted.

%package -n google-noto-sans-grantha-fonts
Summary:        Noto Grantha Sans Serif Font
Obsoletes:      noto-sans-grantha < %{version}
Provides:       noto-sans-grantha = %{version}
Obsoletes:      noto-sans-grantha-fonts < %{version}
Provides:       noto-sans-grantha-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-grantha-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Grantha Sans Serif font, hinted.

%package -n google-noto-sans-gujarati-fonts
Summary:        Noto Gujarati Sans Serif Font
Obsoletes:      noto-sans-gujarati < %{version}
Provides:       noto-sans-gujarati = %{version}
Obsoletes:      noto-sans-gujarati-fonts < %{version}
Provides:       noto-sans-gujarati-fonts = %{version}
Obsoletes:      noto-sans-gujarati-ui < %{version}
Provides:       noto-sans-gujarati-ui = %{version}
Obsoletes:      noto-sans-gujarati-ui-fonts < %{version}
Provides:       noto-sans-gujarati-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-gujarati-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gujarati Sans Serif font, hinted.

%package -n google-noto-sans-gunjalagondi-fonts
Summary:        Noto Gunjala Gondi Sans Serif Font
Obsoletes:      noto-sans-gunjalagondi < %{version}
Provides:       noto-sans-gunjalagondi = %{version}
Obsoletes:      noto-sans-gunjalagondi-fonts < %{version}
Provides:       noto-sans-gunjalagondi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-gunjalagondi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
GunjalaGondi Sans Serif font, hinted.

%package -n google-noto-sans-gurmukhi-fonts
Summary:        Noto Gurmukhi Sans Serif Font
Obsoletes:      noto-sans-gurmukhi < %{version}
Provides:       noto-sans-gurmukhi = %{version}
Obsoletes:      noto-sans-gurmukhi-fonts < %{version}
Provides:       noto-sans-gurmukhi-fonts = %{version}
Obsoletes:      noto-sans-gurmukhi-ui < %{version}
Provides:       noto-sans-gurmukhi-ui = %{version}
Obsoletes:      noto-sans-gurmukhi-ui-fonts < %{version}
Provides:       noto-sans-gurmukhi-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-gurmukhi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gurmukhi Sans Serif font, hinted.

%package -n google-noto-sans-hanifirohingya-fonts
Summary:        Noto Hanifi Rohingya Sans Serif Font
Obsoletes:      noto-sans-hanifirohingya < %{version}
Provides:       noto-sans-hanifirohingya = %{version}
Obsoletes:      noto-sans-hanifirohingya-fonts < %{version}
Provides:       noto-sans-hanifirohingya-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-hanifirohingya-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
HanifiRohingya Sans Serif font, hinted.

%package -n google-noto-sans-hanunoo-fonts
Summary:        Noto Hanunoo Sans Serif Font
Obsoletes:      noto-sans-hanunoo < %{version}
Provides:       noto-sans-hanunoo = %{version}
Obsoletes:      noto-sans-hanunoo-fonts < %{version}
Provides:       noto-sans-hanunoo-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-hanunoo-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Hanunoo Sans Serif font, hinted.

%package -n google-noto-sans-hatran-fonts
Summary:        Noto Hatran Sans Serif Font
Obsoletes:      noto-sans-hatran < %{version}
Provides:       noto-sans-hatran = %{version}
Obsoletes:      noto-sans-hatran-fonts < %{version}
Provides:       noto-sans-hatran-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-hatran-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Hatran Sans Serif font, hinted.

%package -n google-noto-sans-hebrew-fonts
Summary:        Noto Hebrew Sans Serif Font
Obsoletes:      noto-sans-hebrew < %{version}
Provides:       noto-sans-hebrew = %{version}
Obsoletes:      noto-sans-hebrew-fonts < %{version}
Provides:       noto-sans-hebrew-fonts = %{version}
Obsoletes:      noto-sans-hebrewnew < %{version}
Provides:       noto-sans-hebrewnew = %{version}
Obsoletes:      noto-sans-hebrewnew-fonts < %{version}
Provides:       noto-sans-hebrewnew-fonts = %{version}
Obsoletes:      noto-sans-hebrewdroid < %{version}
Provides:       noto-sans-hebrewdroid = %{version}
Obsoletes:      noto-sans-hebrewdroid-fonts < %{version}
Provides:       noto-sans-hebrewdroid-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-hebrew-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Hebrew Sans Serif font, hinted.

%package -n google-noto-sans-imperialaramaic-fonts
Summary:        Noto Imperial Aramaic Sans Serif Font
Obsoletes:      noto-sans-imperialaramaic < %{version}
Provides:       noto-sans-imperialaramaic = %{version}
Obsoletes:      noto-sans-imperialaramaic-fonts < %{version}
Provides:       noto-sans-imperialaramaic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-imperialaramaic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
ImperialAramaic Sans Serif font, hinted.

%package -n google-noto-sans-indicsiyaqnumbers-fonts
Summary:        Noto Indic Siyaq Numbers Sans Serif Font
Obsoletes:      noto-sans-indicsiyaqnumbers < %{version}
Provides:       noto-sans-indicsiyaqnumbers = %{version}
Obsoletes:      noto-sans-indicsiyaqnumbers-fonts < %{version}
Provides:       noto-sans-indicsiyaqnumbers-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-indicsiyaqnumbers-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
IndicSiyaqNumbers Sans Serif font, hinted.

%package -n google-noto-sans-inscriptionalpahlavi-fonts
Summary:        Noto Inscriptional Pahlavi Sans Serif Font
Obsoletes:      noto-sans-inscriptionalpahlavi < %{version}
Provides:       noto-sans-inscriptionalpahlavi = %{version}
Obsoletes:      noto-sans-inscriptionalpahlavi-fonts < %{version}
Provides:       noto-sans-inscriptionalpahlavi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-inscriptionalpahlavi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
InscriptionalPahlavi Sans Serif font, hinted.

%package -n google-noto-sans-inscriptionalparthian-fonts
Summary:        Noto Inscriptional Parthian Sans Serif Font
Obsoletes:      noto-sans-inscriptionalparthian < %{version}
Provides:       noto-sans-inscriptionalparthian = %{version}
Obsoletes:      noto-sans-inscriptionalparthian-fonts < %{version}
Provides:       noto-sans-inscriptionalparthian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-inscriptionalparthian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
InscriptionalParthian Sans Serif font, hinted.

%package -n google-noto-sans-javanese-fonts
Summary:        Noto Javanese Sans Serif Font
Obsoletes:      noto-sans-javanese < %{version}
Provides:       noto-sans-javanese = %{version}
Obsoletes:      noto-sans-javanese-fonts < %{version}
Provides:       noto-sans-javanese-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-javanese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Javanese Sans Serif font, hinted.

%package -n google-noto-sans-kaithi-fonts
Summary:        Noto Kaithi Sans Serif Font
Obsoletes:      noto-sans-kaithi < %{version}
Provides:       noto-sans-kaithi = %{version}
Obsoletes:      noto-sans-kaithi-fonts < %{version}
Provides:       noto-sans-kaithi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-kaithi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kaithi Sans Serif font, hinted.

%package -n google-noto-sans-kannada-fonts
Summary:        Noto Kannada Sans Serif Font
Obsoletes:      noto-sans-kannada < %{version}
Provides:       noto-sans-kannada = %{version}
Obsoletes:      noto-sans-kannada-fonts < %{version}
Provides:       noto-sans-kannada-fonts = %{version}
Obsoletes:      noto-sans-kannada-ui < %{version}
Provides:       noto-sans-kannada-ui = %{version}
Obsoletes:      noto-sans-kannada-ui-fonts < %{version}
Provides:       noto-sans-kannada-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-kannada-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kannada Sans Serif font, hinted.

%package -n google-noto-sans-kawi-fonts
Summary:        Noto Kawi Sans Serif Font
Obsoletes:      noto-sans-kawi < %{version}
Provides:       noto-sans-kawi = %{version}
Obsoletes:      noto-sans-kawi-fonts < %{version}
Provides:       noto-sans-kawi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-kawi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kawi Sans Serif font, hinted.

%package -n google-noto-sans-kayahli-fonts
Summary:        Noto Kayah Li Sans Serif Font
Obsoletes:      noto-sans-kayahli < %{version}
Provides:       noto-sans-kayahli = %{version}
Obsoletes:      noto-sans-kayahli-fonts < %{version}
Provides:       noto-sans-kayahli-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-kayahli-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
KayahLi Sans Serif font, hinted.

%package -n google-noto-sans-kharoshthi-fonts
Summary:        Noto Kharoshthi Sans Serif Font
Obsoletes:      noto-sans-kharoshthi < %{version}
Provides:       noto-sans-kharoshthi = %{version}
Obsoletes:      noto-sans-kharoshthi-fonts < %{version}
Provides:       noto-sans-kharoshthi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-kharoshthi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kharoshthi Sans Serif font, hinted.

%package -n google-noto-sans-khmer-fonts
Summary:        Noto Khmer Sans Serif Font
Obsoletes:      noto-sans-khmer < %{version}
Provides:       noto-sans-khmer = %{version}
Obsoletes:      noto-sans-khmer-fonts < %{version}
Provides:       noto-sans-khmer-fonts = %{version}
Obsoletes:      noto-sans-khmer-ui < %{version}
Provides:       noto-sans-khmer-ui = %{version}
Obsoletes:      noto-sans-khmer-ui-fonts < %{version}
Provides:       noto-sans-khmer-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-khmer-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khmer Sans Serif font, hinted.

%package -n google-noto-sans-khojki-fonts
Summary:        Noto Khojki Sans Serif Font
Obsoletes:      noto-sans-khojki < %{version}
Provides:       noto-sans-khojki = %{version}
Obsoletes:      noto-sans-khojki-fonts < %{version}
Provides:       noto-sans-khojki-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-khojki-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khojki Sans Serif font, hinted.

%package -n google-noto-sans-khudawadi-fonts
Summary:        Noto Khudawadi Sans Serif Font
Obsoletes:      noto-sans-khudawadi < %{version}
Provides:       noto-sans-khudawadi = %{version}
Obsoletes:      noto-sans-khudawadi-fonts < %{version}
Provides:       noto-sans-khudawadi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-khudawadi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khudawadi Sans Serif font, hinted.

%package -n google-noto-sans-lao-fonts
Summary:        Noto Lao Sans Serif Font
Obsoletes:      noto-sans-lao < %{version}
Provides:       noto-sans-lao = %{version}
Obsoletes:      noto-sans-lao-fonts < %{version}
Provides:       noto-sans-lao-fonts = %{version}
Obsoletes:      noto-sans-lao-ui < %{version}
Provides:       noto-sans-lao-ui = %{version}
Obsoletes:      noto-sans-lao-ui-fonts < %{version}
Provides:       noto-sans-lao-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-lao-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lao Sans Serif font, hinted.

%package -n google-noto-sans-laolooped-fonts
Summary:        Noto Lao Looped Sans Serif Font
Obsoletes:      noto-loopedlao < %{version}
Provides:       noto-loopedlao = %{version}
Obsoletes:      noto-loopedlao-fonts < %{version}
Provides:       noto-loopedlao-fonts = %{version}
Obsoletes:      noto-loopedlao-ui < %{version}
Provides:       noto-loopedlao-ui = %{version}
Obsoletes:      noto-loopedlao-ui-fonts < %{version}
Provides:       noto-loopedlao-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-laolooped-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
LaoLooped Sans Serif font, hinted.

%package -n google-noto-sans-lepcha-fonts
Summary:        Noto Lepcha Sans Serif Font
Obsoletes:      noto-sans-lepcha < %{version}
Provides:       noto-sans-lepcha = %{version}
Obsoletes:      noto-sans-lepcha-fonts < %{version}
Provides:       noto-sans-lepcha-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-lepcha-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lepcha Sans Serif font, hinted.

%package -n google-noto-sans-limbu-fonts
Summary:        Noto Limbu Sans Serif Font
Obsoletes:      noto-sans-limbu < %{version}
Provides:       noto-sans-limbu = %{version}
Obsoletes:      noto-sans-limbu-fonts < %{version}
Provides:       noto-sans-limbu-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-limbu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Limbu Sans Serif font, hinted.

%package -n google-noto-sans-lineara-fonts
Summary:        Noto Linear A Sans Serif Font
Obsoletes:      noto-sans-lineara < %{version}
Provides:       noto-sans-lineara = %{version}
Obsoletes:      noto-sans-lineara-fonts < %{version}
Provides:       noto-sans-lineara-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-lineara-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
LinearA Sans Serif font, hinted.

%package -n google-noto-sans-linearb-fonts
Summary:        Noto Linear B Sans Serif Font
Obsoletes:      noto-sans-linearb < %{version}
Provides:       noto-sans-linearb = %{version}
Obsoletes:      noto-sans-linearb-fonts < %{version}
Provides:       noto-sans-linearb-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-linearb-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
LinearB Sans Serif font, hinted.

%package -n google-noto-sans-lisu-fonts
Summary:        Noto Lisu Sans Serif Font
Obsoletes:      noto-sans-lisu < %{version}
Provides:       noto-sans-lisu = %{version}
Obsoletes:      noto-sans-lisu-fonts < %{version}
Provides:       noto-sans-lisu-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-lisu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lisu Sans Serif font, hinted.

%package -n google-noto-sans-lycian-fonts
Summary:        Noto Lycian Sans Serif Font
Obsoletes:      noto-sans-lycian < %{version}
Provides:       noto-sans-lycian = %{version}
Obsoletes:      noto-sans-lycian-fonts < %{version}
Provides:       noto-sans-lycian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-lycian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lycian Sans Serif font, hinted.

%package -n google-noto-sans-lydian-fonts
Summary:        Noto Lydian Sans Serif Font
Obsoletes:      noto-sans-lydian < %{version}
Provides:       noto-sans-lydian = %{version}
Obsoletes:      noto-sans-lydian-fonts < %{version}
Provides:       noto-sans-lydian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-lydian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lydian Sans Serif font, hinted.

%package -n google-noto-sans-mahajani-fonts
Summary:        Noto Mahajani Sans Serif Font
Obsoletes:      noto-sans-mahajani < %{version}
Provides:       noto-sans-mahajani = %{version}
Obsoletes:      noto-sans-mahajani-fonts < %{version}
Provides:       noto-sans-mahajani-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-mahajani-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mahajani Sans Serif font, hinted.

%package -n google-noto-sans-malayalam-fonts
Summary:        Noto Malayalam Sans Serif Font
Obsoletes:      noto-sans-malayalam < %{version}
Provides:       noto-sans-malayalam = %{version}
Obsoletes:      noto-sans-malayalam-fonts < %{version}
Provides:       noto-sans-malayalam-fonts = %{version}
Obsoletes:      noto-sans-malayalam-ui < %{version}
Provides:       noto-sans-malayalam-ui = %{version}
Obsoletes:      noto-sans-malayalam-ui-fonts < %{version}
Provides:       noto-sans-malayalam-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-malayalam-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Malayalam Sans Serif font, hinted.

%package -n google-noto-sans-mandaic-fonts
Summary:        Noto Mandaic Sans Serif Font
Obsoletes:      noto-sans-mandaic < %{version}
Provides:       noto-sans-mandaic = %{version}
Obsoletes:      noto-sans-mandaic-fonts < %{version}
Provides:       noto-sans-mandaic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-mandaic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mandaic Sans Serif font, hinted.

%package -n google-noto-sans-manichaean-fonts
Summary:        Noto Manichaean Sans Serif Font
Obsoletes:      noto-sans-manichaean < %{version}
Provides:       noto-sans-manichaean = %{version}
Obsoletes:      noto-sans-manichaean-fonts < %{version}
Provides:       noto-sans-manichaean-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-manichaean-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Manichaean Sans Serif font, hinted.

%package -n google-noto-sans-marchen-fonts
Summary:        Noto Marchen Sans Serif Font
Obsoletes:      noto-sans-marchen < %{version}
Provides:       noto-sans-marchen = %{version}
Obsoletes:      noto-sans-marchen-fonts < %{version}
Provides:       noto-sans-marchen-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-marchen-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Marchen Sans Serif font, hinted.

%package -n google-noto-sans-masaramgondi-fonts
Summary:        Noto Masaram Gondi Sans Serif Font
Obsoletes:      noto-sans-masaramgondi < %{version}
Provides:       noto-sans-masaramgondi = %{version}
Obsoletes:      noto-sans-masaramgondi-fonts < %{version}
Provides:       noto-sans-masaramgondi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-masaramgondi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
MasaramGondi Sans Serif font, hinted.

%package -n google-noto-sans-math-fonts
Summary:        Noto Math Sans Serif Font
Obsoletes:      noto-sans-math < %{version}
Provides:       noto-sans-math = %{version}
Obsoletes:      noto-sans-math-fonts < %{version}
Provides:       noto-sans-math-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-math-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Math Sans Serif font, hinted.

%package -n google-noto-sans-mayannumerals-fonts
Summary:        Noto Mayan Numerals Sans Serif Font
Obsoletes:      noto-sans-mayannumerals < %{version}
Provides:       noto-sans-mayannumerals = %{version}
Obsoletes:      noto-sans-mayannumerals-fonts < %{version}
Provides:       noto-sans-mayannumerals-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-mayannumerals-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
MayanNumerals Sans Serif font, hinted.

%package -n google-noto-sans-medefaidrin-fonts
Summary:        Noto Medefaidrin Sans Serif Font
Obsoletes:      noto-sans-medefaidrin < %{version}
Provides:       noto-sans-medefaidrin = %{version}
Obsoletes:      noto-sans-medefaidrin-fonts < %{version}
Provides:       noto-sans-medefaidrin-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-medefaidrin-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Medefaidrin Sans Serif font, hinted.

%package -n google-noto-sans-meeteimayek-fonts
Summary:        Noto Meetei Mayek Sans Serif Font
Obsoletes:      noto-sans-meeteimayek < %{version}
Provides:       noto-sans-meeteimayek = %{version}
Obsoletes:      noto-sans-meeteimayek-fonts < %{version}
Provides:       noto-sans-meeteimayek-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-meeteimayek-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
MeeteiMayek Sans Serif font, hinted.

%package -n google-noto-sans-mendekikakui-fonts
Summary:        Noto Mende Kikakui Sans Serif Font
Obsoletes:      noto-sans-mendekikakui < %{version}
Provides:       noto-sans-mendekikakui = %{version}
Obsoletes:      noto-sans-mendekikakui-fonts < %{version}
Provides:       noto-sans-mendekikakui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-mendekikakui-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
MendeKikakui Sans Serif font, hinted.

%package -n google-noto-sans-meroitic-fonts
Summary:        Noto Meroitic Sans Serif Font
Obsoletes:      noto-sans-meroitic < %{version}
Provides:       noto-sans-meroitic = %{version}
Obsoletes:      noto-sans-meroitic-fonts < %{version}
Provides:       noto-sans-meroitic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-meroitic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Meroitic Sans Serif font, hinted.

%package -n google-noto-sans-miao-fonts
Summary:        Noto Miao Sans Serif Font
Obsoletes:      noto-sans-miao < %{version}
Provides:       noto-sans-miao = %{version}
Obsoletes:      noto-sans-miao-fonts < %{version}
Provides:       noto-sans-miao-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-miao-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Miao Sans Serif font, hinted.

%package -n google-noto-sans-modi-fonts
Summary:        Noto Modi Sans Serif Font
Obsoletes:      noto-sans-modi < %{version}
Provides:       noto-sans-modi = %{version}
Obsoletes:      noto-sans-modi-fonts < %{version}
Provides:       noto-sans-modi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-modi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Modi Sans Serif font, hinted.

%package -n google-noto-sans-mongolian-fonts
Summary:        Noto Mongolian Sans Serif Font
Obsoletes:      noto-sans-mongolian < %{version}
Provides:       noto-sans-mongolian = %{version}
Obsoletes:      noto-sans-mongolian-fonts < %{version}
Provides:       noto-sans-mongolian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-mongolian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mongolian Sans Serif font, hinted.

%package -n google-noto-sans-mono-fonts
Summary:        Noto Mono Sans Serif Font
Obsoletes:      noto-sans-mono < %{version}
Provides:       noto-sans-mono = %{version}
Obsoletes:      noto-sans-mono-fonts < %{version}
Provides:       noto-sans-mono-fonts = %{version}
Obsoletes:      noto-mono < %{version}
Provides:       noto-mono = %{version}
Obsoletes:      noto-mono-fonts < %{version}
Provides:       noto-mono-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-mono-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mono Sans Serif font, hinted.

%package -n google-noto-sans-mro-fonts
Summary:        Noto Mro Sans Serif Font
Obsoletes:      noto-sans-mro < %{version}
Provides:       noto-sans-mro = %{version}
Obsoletes:      noto-sans-mro-fonts < %{version}
Provides:       noto-sans-mro-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-mro-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Mro Sans Serif font, hinted.

%package -n google-noto-sans-multani-fonts
Summary:        Noto Multani Sans Serif Font
Obsoletes:      noto-sans-multani < %{version}
Provides:       noto-sans-multani = %{version}
Obsoletes:      noto-sans-multani-fonts < %{version}
Provides:       noto-sans-multani-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-multani-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Multani Sans Serif font, hinted.

%package -n google-noto-sans-myanmar-fonts
Summary:        Noto Myanmar Sans Serif Font
Obsoletes:      noto-sans-myanmar < %{version}
Provides:       noto-sans-myanmar = %{version}
Obsoletes:      noto-sans-myanmar-fonts < %{version}
Provides:       noto-sans-myanmar-fonts = %{version}
Obsoletes:      noto-sans-myanmar-ui < %{version}
Provides:       noto-sans-myanmar-ui = %{version}
Obsoletes:      noto-sans-myanmar-ui-fonts < %{version}
Provides:       noto-sans-myanmar-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-myanmar-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Myanmar Sans Serif font, hinted.

%package -n google-noto-sans-nabataean-fonts
Summary:        Noto Nabataean Sans Serif Font
Obsoletes:      noto-sans-nabataean < %{version}
Provides:       noto-sans-nabataean = %{version}
Obsoletes:      noto-sans-nabataean-fonts < %{version}
Provides:       noto-sans-nabataean-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-nabataean-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Nabataean Sans Serif font, hinted.

%package -n google-noto-sans-nagmundari-fonts
Summary:        Noto Nag Mundari Sans Serif Font
Obsoletes:      noto-sans-nagmundari < %{version}
Provides:       noto-sans-nagmundari = %{version}
Obsoletes:      noto-sans-nagmundari-fonts < %{version}
Provides:       noto-sans-nagmundari-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-nagmundari-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NagMundari Sans Serif font, hinted.

%package -n google-noto-sans-nandinagari-fonts
Summary:        Noto Nandinagari Sans Serif Font
Obsoletes:      noto-sans-nandinagari < %{version}
Provides:       noto-sans-nandinagari = %{version}
Obsoletes:      noto-sans-nandinagari-fonts < %{version}
Provides:       noto-sans-nandinagari-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-nandinagari-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Nandinagari Sans Serif font, hinted.

%package -n google-noto-sans-newa-fonts
Summary:        Noto Newa Sans Serif Font
Obsoletes:      noto-sans-newa < %{version}
Provides:       noto-sans-newa = %{version}
Obsoletes:      noto-sans-newa-fonts < %{version}
Provides:       noto-sans-newa-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-newa-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Newa Sans Serif font, hinted.

%package -n google-noto-sans-newtailue-fonts
Summary:        Noto New Tai Lue Sans Serif Font
Obsoletes:      noto-sans-newtailue < %{version}
Provides:       noto-sans-newtailue = %{version}
Obsoletes:      noto-sans-newtailue-fonts < %{version}
Provides:       noto-sans-newtailue-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-newtailue-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NewTaiLue Sans Serif font, hinted.

%package -n google-noto-sans-nko-fonts
Summary:        Noto NKo Sans Serif Font
Obsoletes:      noto-sans-nko < %{version}
Provides:       noto-sans-nko = %{version}
Obsoletes:      noto-sans-nko-fonts < %{version}
Provides:       noto-sans-nko-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-nko-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NKo Sans Serif font, hinted.

%package -n google-noto-sans-nkounjoined-fonts
Summary:        Noto NKo Unjoined Sans Serif Font
Obsoletes:      noto-sans-nkounjoined < %{version}
Provides:       noto-sans-nkounjoined = %{version}
Obsoletes:      noto-sans-nkounjoined-fonts < %{version}
Provides:       noto-sans-nkounjoined-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-nkounjoined-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NKoUnjoined Sans Serif font, hinted.

%package -n google-noto-sans-nushu-fonts
Summary:        Noto Nushu Sans Serif Font
Obsoletes:      noto-sans-nushu < %{version}
Provides:       noto-sans-nushu = %{version}
Obsoletes:      noto-sans-nushu-fonts < %{version}
Provides:       noto-sans-nushu-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-nushu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Nushu Sans Serif font, hinted.

%package -n google-noto-sans-ogham-fonts
Summary:        Noto Ogham Sans Serif Font
Obsoletes:      noto-sans-ogham < %{version}
Provides:       noto-sans-ogham = %{version}
Obsoletes:      noto-sans-ogham-fonts < %{version}
Provides:       noto-sans-ogham-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-ogham-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ogham Sans Serif font, hinted.

%package -n google-noto-sans-olchiki-fonts
Summary:        Noto Ol Chiki Sans Serif Font
Obsoletes:      noto-sans-olchiki < %{version}
Provides:       noto-sans-olchiki = %{version}
Obsoletes:      noto-sans-olchiki-fonts < %{version}
Provides:       noto-sans-olchiki-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-olchiki-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OlChiki Sans Serif font, hinted.

%package -n google-noto-sans-oldhungarian-fonts
Summary:        Noto Old Hungarian Sans Serif Font
Obsoletes:      noto-sans-oldhungarian < %{version}
Provides:       noto-sans-oldhungarian = %{version}
Obsoletes:      noto-sans-oldhungarian-fonts < %{version}
Provides:       noto-sans-oldhungarian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-oldhungarian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldHungarian Sans Serif font, hinted.

%package -n google-noto-sans-olditalic-fonts
Summary:        Noto Old Italic Sans Serif Font
Obsoletes:      noto-sans-olditalic < %{version}
Provides:       noto-sans-olditalic = %{version}
Obsoletes:      noto-sans-olditalic-fonts < %{version}
Provides:       noto-sans-olditalic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-olditalic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldItalic Sans Serif font, hinted.

%package -n google-noto-sans-oldnortharabian-fonts
Summary:        Noto Old North Arabian Sans Serif Font
Obsoletes:      noto-sans-oldnortharabian < %{version}
Provides:       noto-sans-oldnortharabian = %{version}
Obsoletes:      noto-sans-oldnortharabian-fonts < %{version}
Provides:       noto-sans-oldnortharabian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-oldnortharabian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldNorthArabian Sans Serif font, hinted.

%package -n google-noto-sans-oldpermic-fonts
Summary:        Noto Old Permic Sans Serif Font
Obsoletes:      noto-sans-oldpermic < %{version}
Provides:       noto-sans-oldpermic = %{version}
Obsoletes:      noto-sans-oldpermic-fonts < %{version}
Provides:       noto-sans-oldpermic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-oldpermic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldPermic Sans Serif font, hinted.

%package -n google-noto-sans-oldpersian-fonts
Summary:        Noto Old Persian Sans Serif Font
Obsoletes:      noto-sans-oldpersian < %{version}
Provides:       noto-sans-oldpersian = %{version}
Obsoletes:      noto-sans-oldpersian-fonts < %{version}
Provides:       noto-sans-oldpersian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-oldpersian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldPersian Sans Serif font, hinted.

%package -n google-noto-sans-oldsogdian-fonts
Summary:        Noto Old Sogdian Sans Serif Font
Obsoletes:      noto-sans-oldsogdian < %{version}
Provides:       noto-sans-oldsogdian = %{version}
Obsoletes:      noto-sans-oldsogdian-fonts < %{version}
Provides:       noto-sans-oldsogdian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-oldsogdian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldSogdian Sans Serif font, hinted.

%package -n google-noto-sans-oldsoutharabian-fonts
Summary:        Noto Old South Arabian Sans Serif Font
Obsoletes:      noto-sans-oldsoutharabian < %{version}
Provides:       noto-sans-oldsoutharabian = %{version}
Obsoletes:      noto-sans-oldsoutharabian-fonts < %{version}
Provides:       noto-sans-oldsoutharabian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-oldsoutharabian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldSouthArabian Sans Serif font, hinted.

%package -n google-noto-sans-oldturkic-fonts
Summary:        Noto Old Turkic Sans Serif Font
Obsoletes:      noto-sans-oldturkic < %{version}
Provides:       noto-sans-oldturkic = %{version}
Obsoletes:      noto-sans-oldturkic-fonts < %{version}
Provides:       noto-sans-oldturkic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-oldturkic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldTurkic Sans Serif font, hinted.

%package -n google-noto-sans-oriya-fonts
Summary:        Noto Oriya Sans Serif Font
Obsoletes:      noto-sans-oriya < %{version}
Provides:       noto-sans-oriya = %{version}
Obsoletes:      noto-sans-oriya-fonts < %{version}
Provides:       noto-sans-oriya-fonts = %{version}
Obsoletes:      noto-sans-oriya-ui < %{version}
Provides:       noto-sans-oriya-ui = %{version}
Obsoletes:      noto-sans-oriya-ui-fonts < %{version}
Provides:       noto-sans-oriya-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-oriya-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Oriya Sans Serif font, hinted.

%package -n google-noto-sans-osage-fonts
Summary:        Noto Osage Sans Serif Font
Obsoletes:      noto-sans-osage < %{version}
Provides:       noto-sans-osage = %{version}
Obsoletes:      noto-sans-osage-fonts < %{version}
Provides:       noto-sans-osage-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-osage-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Osage Sans Serif font, hinted.

%package -n google-noto-sans-osmanya-fonts
Summary:        Noto Osmanya Sans Serif Font
Obsoletes:      noto-sans-osmanya < %{version}
Provides:       noto-sans-osmanya = %{version}
Obsoletes:      noto-sans-osmanya-fonts < %{version}
Provides:       noto-sans-osmanya-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-osmanya-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Osmanya Sans Serif font, hinted.

%package -n google-noto-sans-pahawhhmong-fonts
Summary:        Noto Pahawh Hmong Sans Serif Font
Obsoletes:      noto-sans-pahawhhmong < %{version}
Provides:       noto-sans-pahawhhmong = %{version}
Obsoletes:      noto-sans-pahawhhmong-fonts < %{version}
Provides:       noto-sans-pahawhhmong-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-pahawhhmong-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
PahawhHmong Sans Serif font, hinted.

%package -n google-noto-sans-palmyrene-fonts
Summary:        Noto Palmyrene Sans Serif Font
Obsoletes:      noto-sans-palmyrene < %{version}
Provides:       noto-sans-palmyrene = %{version}
Obsoletes:      noto-sans-palmyrene-fonts < %{version}
Provides:       noto-sans-palmyrene-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-palmyrene-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Palmyrene Sans Serif font, hinted.

%package -n google-noto-sans-paucinhau-fonts
Summary:        Noto Pau Cin Hau Sans Serif Font
Obsoletes:      noto-sans-paucinhau < %{version}
Provides:       noto-sans-paucinhau = %{version}
Obsoletes:      noto-sans-paucinhau-fonts < %{version}
Provides:       noto-sans-paucinhau-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-paucinhau-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
PauCinHau Sans Serif font, hinted.

%package -n google-noto-sans-phagspa-fonts
Summary:        Noto Phags Pa Sans Serif Font
Obsoletes:      noto-sans-phagspa < %{version}
Provides:       noto-sans-phagspa = %{version}
Obsoletes:      noto-sans-phagspa-fonts < %{version}
Provides:       noto-sans-phagspa-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-phagspa-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
PhagsPa Sans Serif font, hinted.

%package -n google-noto-sans-phoenician-fonts
Summary:        Noto Phoenician Sans Serif Font
Obsoletes:      noto-sans-phoenician < %{version}
Provides:       noto-sans-phoenician = %{version}
Obsoletes:      noto-sans-phoenician-fonts < %{version}
Provides:       noto-sans-phoenician-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-phoenician-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Phoenician Sans Serif font, hinted.

%package -n google-noto-sans-psalterpahlavi-fonts
Summary:        Noto Psalter Pahlavi Sans Serif Font
Obsoletes:      noto-sans-psalterpahlavi < %{version}
Provides:       noto-sans-psalterpahlavi = %{version}
Obsoletes:      noto-sans-psalterpahlavi-fonts < %{version}
Provides:       noto-sans-psalterpahlavi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-psalterpahlavi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
PsalterPahlavi Sans Serif font, hinted.

%package -n google-noto-sans-rejang-fonts
Summary:        Noto Rejang Sans Serif Font
Obsoletes:      noto-sans-rejang < %{version}
Provides:       noto-sans-rejang = %{version}
Obsoletes:      noto-sans-rejang-fonts < %{version}
Provides:       noto-sans-rejang-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-rejang-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Rejang Sans Serif font, hinted.

%package -n google-noto-sans-runic-fonts
Summary:        Noto Runic Sans Serif Font
Obsoletes:      noto-sans-runic < %{version}
Provides:       noto-sans-runic = %{version}
Obsoletes:      noto-sans-runic-fonts < %{version}
Provides:       noto-sans-runic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-runic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Runic Sans Serif font, hinted.

%package -n google-noto-sans-samaritan-fonts
Summary:        Noto Samaritan Sans Serif Font
Obsoletes:      noto-sans-samaritan < %{version}
Provides:       noto-sans-samaritan = %{version}
Obsoletes:      noto-sans-samaritan-fonts < %{version}
Provides:       noto-sans-samaritan-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-samaritan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Samaritan Sans Serif font, hinted.

%package -n google-noto-sans-saurashtra-fonts
Summary:        Noto Saurashtra Sans Serif Font
Obsoletes:      noto-sans-saurashtra < %{version}
Provides:       noto-sans-saurashtra = %{version}
Obsoletes:      noto-sans-saurashtra-fonts < %{version}
Provides:       noto-sans-saurashtra-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-saurashtra-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Saurashtra Sans Serif font, hinted.

%package -n google-noto-sans-sharada-fonts
Summary:        Noto Sharada Sans Serif Font
Obsoletes:      noto-sans-sharada < %{version}
Provides:       noto-sans-sharada = %{version}
Obsoletes:      noto-sans-sharada-fonts < %{version}
Provides:       noto-sans-sharada-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-sharada-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sharada Sans Serif font, hinted.

%package -n google-noto-sans-shavian-fonts
Summary:        Noto Shavian Sans Serif Font
Obsoletes:      noto-sans-shavian < %{version}
Provides:       noto-sans-shavian = %{version}
Obsoletes:      noto-sans-shavian-fonts < %{version}
Provides:       noto-sans-shavian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-shavian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Shavian Sans Serif font, hinted.

%package -n google-noto-sans-siddham-fonts
Summary:        Noto Siddham Sans Serif Font
Obsoletes:      noto-sans-siddham < %{version}
Provides:       noto-sans-siddham = %{version}
Obsoletes:      noto-sans-siddham-fonts < %{version}
Provides:       noto-sans-siddham-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-siddham-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Siddham Sans Serif font, hinted.

%package -n google-noto-sans-signwriting-fonts
Summary:        Noto Sign Writing Sans Serif Font
Obsoletes:      noto-sans-signwriting < %{version}
Provides:       noto-sans-signwriting = %{version}
Obsoletes:      noto-sans-signwriting-fonts < %{version}
Provides:       noto-sans-signwriting-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-signwriting-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SignWriting Sans Serif font, hinted.

%package -n google-noto-sans-sinhala-fonts
Summary:        Noto Sinhala Sans Serif Font
Obsoletes:      noto-sans-sinhala < %{version}
Provides:       noto-sans-sinhala = %{version}
Obsoletes:      noto-sans-sinhala-fonts < %{version}
Provides:       noto-sans-sinhala-fonts = %{version}
Obsoletes:      noto-sans-sinhala-ui < %{version}
Provides:       noto-sans-sinhala-ui = %{version}
Obsoletes:      noto-sans-sinhala-ui-fonts < %{version}
Provides:       noto-sans-sinhala-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-sinhala-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sinhala Sans Serif font, hinted.

%package -n google-noto-sans-sogdian-fonts
Summary:        Noto Sogdian Sans Serif Font
Obsoletes:      noto-sans-sogdian < %{version}
Provides:       noto-sans-sogdian = %{version}
Obsoletes:      noto-sans-sogdian-fonts < %{version}
Provides:       noto-sans-sogdian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-sogdian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sogdian Sans Serif font, hinted.

%package -n google-noto-sans-sorasompeng-fonts
Summary:        Noto Sora Sompeng Sans Serif Font
Obsoletes:      noto-sans-sorasompeng < %{version}
Provides:       noto-sans-sorasompeng = %{version}
Obsoletes:      noto-sans-sorasompeng-fonts < %{version}
Provides:       noto-sans-sorasompeng-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-sorasompeng-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SoraSompeng Sans Serif font, hinted.

%package -n google-noto-sans-soyombo-fonts
Summary:        Noto Soyombo Sans Serif Font
Obsoletes:      noto-sans-soyombo < %{version}
Provides:       noto-sans-soyombo = %{version}
Obsoletes:      noto-sans-soyombo-fonts < %{version}
Provides:       noto-sans-soyombo-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-soyombo-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Soyombo Sans Serif font, hinted.

%package -n google-noto-sans-sundanese-fonts
Summary:        Noto Sundanese Sans Serif Font
Obsoletes:      noto-sans-sundanese < %{version}
Provides:       noto-sans-sundanese = %{version}
Obsoletes:      noto-sans-sundanese-fonts < %{version}
Provides:       noto-sans-sundanese-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-sundanese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sundanese Sans Serif font, hinted.

%package -n google-noto-sans-sylotinagri-fonts
Summary:        Noto Syloti Nagri Sans Serif Font
Obsoletes:      noto-sans-sylotinagri < %{version}
Provides:       noto-sans-sylotinagri = %{version}
Obsoletes:      noto-sans-sylotinagri-fonts < %{version}
Provides:       noto-sans-sylotinagri-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-sylotinagri-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SylotiNagri Sans Serif font, hinted.

%package -n google-noto-sans-symbols-fonts
Summary:        Noto Symbols Sans Serif Font
Obsoletes:      noto-sans-symbols < %{version}
Provides:       noto-sans-symbols = %{version}
Obsoletes:      noto-sans-symbols-fonts < %{version}
Provides:       noto-sans-symbols-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-symbols-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Symbols Sans Serif font, hinted.

%package -n google-noto-sans-symbols2-fonts
Summary:        Noto Symbols2 Sans Serif Font
Obsoletes:      noto-sans-symbols2 < %{version}
Provides:       noto-sans-symbols2 = %{version}
Obsoletes:      noto-sans-symbols2-fonts < %{version}
Provides:       noto-sans-symbols2-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-symbols2-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Symbols2 Sans Serif font, hinted.

%package -n google-noto-sans-syriac-fonts
Summary:        Noto Syriac Sans Serif Font
Obsoletes:      noto-sans-syriac < %{version}
Provides:       noto-sans-syriac = %{version}
Obsoletes:      noto-sans-syriac-fonts < %{version}
Provides:       noto-sans-syriac-fonts = %{version}
Obsoletes:      noto-sans-syriacestrangela < %{version}
Provides:       noto-sans-syriacestrangela = %{version}
Obsoletes:      noto-sans-syriacestrangela-fonts < %{version}
Provides:       noto-sans-syriacestrangela-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-syriac-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Syriac Sans Serif font, hinted.

%package -n google-noto-sans-syriaceastern-fonts
Summary:        Noto Syriac Eastern Sans Serif Font
Obsoletes:      noto-sans-syriaceastern < %{version}
Provides:       noto-sans-syriaceastern = %{version}
Obsoletes:      noto-sans-syriaceastern-fonts < %{version}
Provides:       noto-sans-syriaceastern-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-syriaceastern-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SyriacEastern Sans Serif font, hinted.

%package -n google-noto-sans-syriacwestern-fonts
Summary:        Noto Syriac Western Sans Serif Font
Obsoletes:      noto-sans-syriacwestern < %{version}
Provides:       noto-sans-syriacwestern = %{version}
Obsoletes:      noto-sans-syriacwestern-fonts < %{version}
Provides:       noto-sans-syriacwestern-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-syriacwestern-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SyriacWestern Sans Serif font, hinted.

%package -n google-noto-sans-tagalog-fonts
Summary:        Noto Tagalog Sans Serif Font
Obsoletes:      noto-sans-tagalog < %{version}
Provides:       noto-sans-tagalog = %{version}
Obsoletes:      noto-sans-tagalog-fonts < %{version}
Provides:       noto-sans-tagalog-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tagalog-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tagalog Sans Serif font, hinted.

%package -n google-noto-sans-tagbanwa-fonts
Summary:        Noto Tagbanwa Sans Serif Font
Obsoletes:      noto-sans-tagbanwa < %{version}
Provides:       noto-sans-tagbanwa = %{version}
Obsoletes:      noto-sans-tagbanwa-fonts < %{version}
Provides:       noto-sans-tagbanwa-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tagbanwa-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tagbanwa Sans Serif font, hinted.

%package -n google-noto-sans-taile-fonts
Summary:        Noto Tai Le Sans Serif Font
Obsoletes:      noto-sans-taile < %{version}
Provides:       noto-sans-taile = %{version}
Obsoletes:      noto-sans-taile-fonts < %{version}
Provides:       noto-sans-taile-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-taile-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TaiLe Sans Serif font, hinted.

%package -n google-noto-sans-taitham-fonts
Summary:        Noto Tai Tham Sans Serif Font
Obsoletes:      noto-sans-taitham < %{version}
Provides:       noto-sans-taitham = %{version}
Obsoletes:      noto-sans-taitham-fonts < %{version}
Provides:       noto-sans-taitham-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-taitham-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TaiTham Sans Serif font, hinted.

%package -n google-noto-sans-taiviet-fonts
Summary:        Noto Tai Viet Sans Serif Font
Obsoletes:      noto-sans-taiviet < %{version}
Provides:       noto-sans-taiviet = %{version}
Obsoletes:      noto-sans-taiviet-fonts < %{version}
Provides:       noto-sans-taiviet-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-taiviet-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TaiViet Sans Serif font, hinted.

%package -n google-noto-sans-takri-fonts
Summary:        Noto Takri Sans Serif Font
Obsoletes:      noto-sans-takri < %{version}
Provides:       noto-sans-takri = %{version}
Obsoletes:      noto-sans-takri-fonts < %{version}
Provides:       noto-sans-takri-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-takri-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Takri Sans Serif font, hinted.

%package -n google-noto-sans-tamil-fonts
Summary:        Noto Tamil Sans Serif Font
Obsoletes:      noto-sans-tamil < %{version}
Provides:       noto-sans-tamil = %{version}
Obsoletes:      noto-sans-tamil-fonts < %{version}
Provides:       noto-sans-tamil-fonts = %{version}
Obsoletes:      noto-sans-tamil-ui < %{version}
Provides:       noto-sans-tamil-ui = %{version}
Obsoletes:      noto-sans-tamil-ui-fonts < %{version}
Provides:       noto-sans-tamil-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tamil-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tamil Sans Serif font, hinted.

%package -n google-noto-sans-tamilsupplement-fonts
Summary:        Noto Tamil Supplement Sans Serif Font
Obsoletes:      noto-sans-tamilsupplement < %{version}
Provides:       noto-sans-tamilsupplement = %{version}
Obsoletes:      noto-sans-tamilsupplement-fonts < %{version}
Provides:       noto-sans-tamilsupplement-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tamilsupplement-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TamilSupplement Sans Serif font, hinted.

%package -n google-noto-sans-tangsa-fonts
Summary:        Noto Tangsa Sans Serif Font
Obsoletes:      noto-sans-tangsa < %{version}
Provides:       noto-sans-tangsa = %{version}
Obsoletes:      noto-sans-tangsa-fonts < %{version}
Provides:       noto-sans-tangsa-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tangsa-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tangsa Sans Serif font, hinted.

%package -n google-noto-sans-telugu-fonts
Summary:        Noto Telugu Sans Serif Font
Obsoletes:      noto-sans-telugu < %{version}
Provides:       noto-sans-telugu = %{version}
Obsoletes:      noto-sans-telugu-fonts < %{version}
Provides:       noto-sans-telugu-fonts = %{version}
Obsoletes:      noto-sans-telugu-ui < %{version}
Provides:       noto-sans-telugu-ui = %{version}
Obsoletes:      noto-sans-telugu-ui-fonts < %{version}
Provides:       noto-sans-telugu-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-telugu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Telugu Sans Serif font, hinted.

%package -n google-noto-sans-thaana-fonts
Summary:        Noto Thaana Sans Serif Font
Obsoletes:      noto-sans-thaana < %{version}
Provides:       noto-sans-thaana = %{version}
Obsoletes:      noto-sans-thaana-fonts < %{version}
Provides:       noto-sans-thaana-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-thaana-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Thaana Sans Serif font, hinted.

%package -n google-noto-sans-thai-fonts
Summary:        Noto Thai Sans Serif Font
Obsoletes:      noto-sans-thai < %{version}
Provides:       noto-sans-thai = %{version}
Obsoletes:      noto-sans-thai-fonts < %{version}
Provides:       noto-sans-thai-fonts = %{version}
Obsoletes:      noto-sans-thai-ui < %{version}
Provides:       noto-sans-thai-ui = %{version}
Obsoletes:      noto-sans-thai-ui-fonts < %{version}
Provides:       noto-sans-thai-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-thai-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Thai Sans Serif font, hinted.

%package -n google-noto-sans-thailooped-fonts
Summary:        Noto Thai Looped Sans Serif Font
Obsoletes:      noto-loopedthai < %{version}
Provides:       noto-loopedthai = %{version}
Obsoletes:      noto-loopedthai-fonts < %{version}
Provides:       noto-loopedthai-fonts = %{version}
Obsoletes:      noto-loopedthai-ui < %{version}
Provides:       noto-loopedthai-ui = %{version}
Obsoletes:      noto-loopedthai-ui-fonts < %{version}
Provides:       noto-loopedthai-ui-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-thailooped-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
ThaiLooped Sans Serif font, hinted.

%package -n google-noto-sans-tifinagh-fonts
Summary:        Noto Tifinagh Sans Serif Font
Obsoletes:      noto-sans-tifinagh < %{version}
Provides:       noto-sans-tifinagh = %{version}
Obsoletes:      noto-sans-tifinagh-fonts < %{version}
Provides:       noto-sans-tifinagh-fonts = %{version}
Obsoletes:      noto-sans-tifinaghadrar < %{version}
Provides:       noto-sans-tifinaghadrar = %{version}
Obsoletes:      noto-sans-tifinaghadrar-fonts < %{version}
Provides:       noto-sans-tifinaghadrar-fonts = %{version}
Obsoletes:      noto-sans-tifinaghagrawimazighen < %{version}
Provides:       noto-sans-tifinaghagrawimazighen = %{version}
Obsoletes:      noto-sans-tifinaghagrawimazighen-fonts < %{version}
Provides:       noto-sans-tifinaghagrawimazighen-fonts = %{version}
Obsoletes:      noto-sans-tifinaghahaggar < %{version}
Provides:       noto-sans-tifinaghahaggar = %{version}
Obsoletes:      noto-sans-tifinaghahaggar-fonts < %{version}
Provides:       noto-sans-tifinaghahaggar-fonts = %{version}
Obsoletes:      noto-sans-tifinaghair < %{version}
Provides:       noto-sans-tifinaghair = %{version}
Obsoletes:      noto-sans-tifinaghair-fonts < %{version}
Provides:       noto-sans-tifinaghair-fonts = %{version}
Obsoletes:      noto-sans-tifinaghapt < %{version}
Provides:       noto-sans-tifinaghapt = %{version}
Obsoletes:      noto-sans-tifinaghapt-fonts < %{version}
Provides:       noto-sans-tifinaghapt-fonts = %{version}
Obsoletes:      noto-sans-tifinaghazawagh < %{version}
Provides:       noto-sans-tifinaghazawagh = %{version}
Obsoletes:      noto-sans-tifinaghazawagh-fonts < %{version}
Provides:       noto-sans-tifinaghazawagh-fonts = %{version}
Obsoletes:      noto-sans-tifinaghghat < %{version}
Provides:       noto-sans-tifinaghghat = %{version}
Obsoletes:      noto-sans-tifinaghghat-fonts < %{version}
Provides:       noto-sans-tifinaghghat-fonts = %{version}
Obsoletes:      noto-sans-tifinaghhawad < %{version}
Provides:       noto-sans-tifinaghhawad = %{version}
Obsoletes:      noto-sans-tifinaghhawad-fonts < %{version}
Provides:       noto-sans-tifinaghhawad-fonts = %{version}
Obsoletes:      noto-sans-tifinaghrhissaixa < %{version}
Provides:       noto-sans-tifinaghrhissaixa = %{version}
Obsoletes:      noto-sans-tifinaghrhissaixa-fonts < %{version}
Provides:       noto-sans-tifinaghrhissaixa-fonts = %{version}
Obsoletes:      noto-sans-tifinaghsil < %{version}
Provides:       noto-sans-tifinaghsil = %{version}
Obsoletes:      noto-sans-tifinaghsil-fonts < %{version}
Provides:       noto-sans-tifinaghsil-fonts = %{version}
Obsoletes:      noto-sans-tifinaghtawellemmet < %{version}
Provides:       noto-sans-tifinaghtawellemmet = %{version}
Obsoletes:      noto-sans-tifinaghtawellemmet-fonts < %{version}
Provides:       noto-sans-tifinaghtawellemmet-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tifinagh-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tifinagh Sans Serif font, hinted.

%package -n google-noto-sans-tirhuta-fonts
Summary:        Noto Tirhuta Sans Serif Font
Obsoletes:      noto-sans-tirhuta < %{version}
Provides:       noto-sans-tirhuta = %{version}
Obsoletes:      noto-sans-tirhuta-fonts < %{version}
Provides:       noto-sans-tirhuta-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tirhuta-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tirhuta Sans Serif font, hinted.

%package -n google-noto-sans-ugaritic-fonts
Summary:        Noto Ugaritic Sans Serif Font
Obsoletes:      noto-sans-ugaritic < %{version}
Provides:       noto-sans-ugaritic = %{version}
Obsoletes:      noto-sans-ugaritic-fonts < %{version}
Provides:       noto-sans-ugaritic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-ugaritic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ugaritic Sans Serif font, hinted.

%package -n google-noto-sans-vai-fonts
Summary:        Noto Vai Sans Serif Font
Obsoletes:      noto-sans-vai < %{version}
Provides:       noto-sans-vai = %{version}
Obsoletes:      noto-sans-vai-fonts < %{version}
Provides:       noto-sans-vai-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-vai-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Vai Sans Serif font, hinted.

%package -n google-noto-sans-vithkuqi-fonts
Summary:        Noto Vithkuqi Sans Serif Font
Obsoletes:      noto-sans-vithkuqi < %{version}
Provides:       noto-sans-vithkuqi = %{version}
Obsoletes:      noto-sans-vithkuqi-fonts < %{version}
Provides:       noto-sans-vithkuqi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-vithkuqi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Vithkuqi Sans Serif font, hinted.

%package -n google-noto-sans-wancho-fonts
Summary:        Noto Wancho Sans Serif Font
Obsoletes:      noto-sans-wancho < %{version}
Provides:       noto-sans-wancho = %{version}
Obsoletes:      noto-sans-wancho-fonts < %{version}
Provides:       noto-sans-wancho-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-wancho-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Wancho Sans Serif font, hinted.

%package -n google-noto-sans-warangciti-fonts
Summary:        Noto Warang Citi Sans Serif Font
Obsoletes:      noto-sans-warangciti < %{version}
Provides:       noto-sans-warangciti = %{version}
Obsoletes:      noto-sans-warangciti-fonts < %{version}
Provides:       noto-sans-warangciti-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-warangciti-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
WarangCiti Sans Serif font, hinted.

%package -n google-noto-sans-yi-fonts
Summary:        Noto Yi Sans Serif Font
Obsoletes:      noto-sans-yi < %{version}
Provides:       noto-sans-yi = %{version}
Obsoletes:      noto-sans-yi-fonts < %{version}
Provides:       noto-sans-yi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-yi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Yi Sans Serif font, hinted.

%package -n google-noto-sans-zanabazarsquare-fonts
Summary:        Noto Zanabazar Square Sans Serif Font
Obsoletes:      noto-sans-zanabazarsquare < %{version}
Provides:       noto-sans-zanabazarsquare = %{version}
Obsoletes:      noto-sans-zanabazarsquare-fonts < %{version}
Provides:       noto-sans-zanabazarsquare-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-zanabazarsquare-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
ZanabazarSquare Sans Serif font, hinted.

%package -n google-noto-serif-fonts
Summary:        Noto Serif Font
Obsoletes:      noto-serif < %{version}
Provides:       noto-serif = %{version}
Obsoletes:      noto-serif-fonts < %{version}
Provides:       noto-serif-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Serif font, hinted.

%package -n google-noto-serif-ahom-fonts
Summary:        Noto Ahom Serif Font
Obsoletes:      noto-serif-ahom < %{version}
Provides:       noto-serif-ahom = %{version}
Obsoletes:      noto-serif-ahom-fonts < %{version}
Provides:       noto-serif-ahom-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-ahom-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ahom Serif font, hinted.

%package -n google-noto-serif-armenian-fonts
Summary:        Noto Armenian Serif Font
Obsoletes:      noto-serif-armenian < %{version}
Provides:       noto-serif-armenian = %{version}
Obsoletes:      noto-serif-armenian-fonts < %{version}
Provides:       noto-serif-armenian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-armenian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Armenian Serif font, hinted.

%package -n google-noto-serif-balinese-fonts
Summary:        Noto Balinese Serif Font
Obsoletes:      noto-serif-balinese < %{version}
Provides:       noto-serif-balinese = %{version}
Obsoletes:      noto-serif-balinese-fonts < %{version}
Provides:       noto-serif-balinese-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-balinese-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Balinese Serif font, hinted.

%package -n google-noto-serif-bengali-fonts
Summary:        Noto Bengali Serif Font
Obsoletes:      noto-serif-bengali < %{version}
Provides:       noto-serif-bengali = %{version}
Obsoletes:      noto-serif-bengali-fonts < %{version}
Provides:       noto-serif-bengali-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-bengali-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bengali Serif font, hinted.

%package -n google-noto-serif-devanagari-fonts
Summary:        Noto Devanagari Serif Font
Obsoletes:      noto-serif-devanagari < %{version}
Provides:       noto-serif-devanagari = %{version}
Obsoletes:      noto-serif-devanagari-fonts < %{version}
Provides:       noto-serif-devanagari-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-devanagari-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Devanagari Serif font, hinted.

%package -n google-noto-serif-display-fonts
Summary:        Noto Display Serif Font
Obsoletes:      noto-serif-display < %{version}
Provides:       noto-serif-display = %{version}
Obsoletes:      noto-serif-display-fonts < %{version}
Provides:       noto-serif-display-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-display-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Display Serif font, hinted.

%package -n google-noto-serif-divesakuru-fonts
Summary:        Noto Dives Akuru Serif Font
Obsoletes:      noto-serif-divesakuru < %{version}
Provides:       noto-serif-divesakuru = %{version}
Obsoletes:      noto-serif-divesakuru-fonts < %{version}
Provides:       noto-serif-divesakuru-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-divesakuru-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
DivesAkuru Serif font, hinted.

%package -n google-noto-serif-dogra-fonts
Summary:        Noto Dogra Serif Font
Obsoletes:      noto-serif-dogra < %{version}
Provides:       noto-serif-dogra = %{version}
Obsoletes:      noto-serif-dogra-fonts < %{version}
Provides:       noto-serif-dogra-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-dogra-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Dogra Serif font, hinted.

%package -n google-noto-serif-ethiopic-fonts
Summary:        Noto Ethiopic Serif Font
Obsoletes:      noto-serif-ethiopic < %{version}
Provides:       noto-serif-ethiopic = %{version}
Obsoletes:      noto-serif-ethiopic-fonts < %{version}
Provides:       noto-serif-ethiopic-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-ethiopic-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Ethiopic Serif font, hinted.

%package -n google-noto-serif-georgian-fonts
Summary:        Noto Georgian Serif Font
Obsoletes:      noto-serif-georgian < %{version}
Provides:       noto-serif-georgian = %{version}
Obsoletes:      noto-serif-georgian-fonts < %{version}
Provides:       noto-serif-georgian-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-georgian-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Georgian Serif font, hinted.

%package -n google-noto-serif-grantha-fonts
Summary:        Noto Grantha Serif Font
Obsoletes:      noto-serif-grantha < %{version}
Provides:       noto-serif-grantha = %{version}
Obsoletes:      noto-serif-grantha-fonts < %{version}
Provides:       noto-serif-grantha-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-grantha-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Grantha Serif font, hinted.

%package -n google-noto-serif-gujarati-fonts
Summary:        Noto Gujarati Serif Font
Obsoletes:      noto-serif-gujarati < %{version}
Provides:       noto-serif-gujarati = %{version}
Obsoletes:      noto-serif-gujarati-fonts < %{version}
Provides:       noto-serif-gujarati-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-gujarati-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gujarati Serif font, hinted.

%package -n google-noto-serif-gurmukhi-fonts
Summary:        Noto Gurmukhi Serif Font
Obsoletes:      noto-serif-gurmukhi < %{version}
Provides:       noto-serif-gurmukhi = %{version}
Obsoletes:      noto-serif-gurmukhi-fonts < %{version}
Provides:       noto-serif-gurmukhi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-gurmukhi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Gurmukhi Serif font, hinted.

%package -n google-noto-serif-hebrew-fonts
Summary:        Noto Hebrew Serif Font
Obsoletes:      noto-serif-hebrew < %{version}
Provides:       noto-serif-hebrew = %{version}
Obsoletes:      noto-serif-hebrew-fonts < %{version}
Provides:       noto-serif-hebrew-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-hebrew-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Hebrew Serif font, hinted.

%package -n google-noto-serif-kannada-fonts
Summary:        Noto Kannada Serif Font
Obsoletes:      noto-serif-kannada < %{version}
Provides:       noto-serif-kannada = %{version}
Obsoletes:      noto-serif-kannada-fonts < %{version}
Provides:       noto-serif-kannada-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-kannada-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Kannada Serif font, hinted.

%package -n google-noto-serif-khitansmallscript-fonts
Summary:        Noto Khitan Small Script Serif Font
Obsoletes:      noto-serif-khitansmallscript < %{version}
Provides:       noto-serif-khitansmallscript = %{version}
Obsoletes:      noto-serif-khitansmallscript-fonts < %{version}
Provides:       noto-serif-khitansmallscript-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-khitansmallscript-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
KhitanSmallScript Serif font, hinted.

%package -n google-noto-serif-khmer-fonts
Summary:        Noto Khmer Serif Font
Obsoletes:      noto-serif-khmer < %{version}
Provides:       noto-serif-khmer = %{version}
Obsoletes:      noto-serif-khmer-fonts < %{version}
Provides:       noto-serif-khmer-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-khmer-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khmer Serif font, hinted.

%package -n google-noto-serif-khojki-fonts
Summary:        Noto Khojki Serif Font
Obsoletes:      noto-serif-khojki < %{version}
Provides:       noto-serif-khojki = %{version}
Obsoletes:      noto-serif-khojki-fonts < %{version}
Provides:       noto-serif-khojki-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-khojki-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Khojki Serif font, hinted.

%package -n google-noto-serif-lao-fonts
Summary:        Noto Lao Serif Font
Obsoletes:      noto-serif-lao < %{version}
Provides:       noto-serif-lao = %{version}
Obsoletes:      noto-serif-lao-fonts < %{version}
Provides:       noto-serif-lao-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-lao-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Lao Serif font, hinted.

%package -n google-noto-serif-makasar-fonts
Summary:        Noto Makasar Serif Font
Obsoletes:      noto-serif-makasar < %{version}
Provides:       noto-serif-makasar = %{version}
Obsoletes:      noto-serif-makasar-fonts < %{version}
Provides:       noto-serif-makasar-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-makasar-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Makasar Serif font, hinted.

%package -n google-noto-serif-malayalam-fonts
Summary:        Noto Malayalam Serif Font
Obsoletes:      noto-serif-malayalam < %{version}
Provides:       noto-serif-malayalam = %{version}
Obsoletes:      noto-serif-malayalam-fonts < %{version}
Provides:       noto-serif-malayalam-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-malayalam-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Malayalam Serif font, hinted.

%package -n google-noto-serif-myanmar-fonts
Summary:        Noto Myanmar Serif Font
Obsoletes:      noto-serif-myanmar < %{version}
Provides:       noto-serif-myanmar = %{version}
Obsoletes:      noto-serif-myanmar-fonts < %{version}
Provides:       noto-serif-myanmar-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-myanmar-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Myanmar Serif font, hinted.

%package -n google-noto-serif-nphmong-fonts
Summary:        Noto NPHmong Serif Font
Obsoletes:      noto-serif-myanmar < %{version}
Provides:       noto-serif-myanmar = %{version}
Obsoletes:      noto-serif-myanmar-fonts < %{version}
Provides:       noto-serif-myanmar-fonts = %{version}
Obsoletes:      noto-serif-nyiakengpuachuehmong < %{version}
Provides:       noto-serif-nyiakengpuachuehmong = %{version}
Obsoletes:      noto-serif-nyiakengpuachuehmong-fonts < %{version}
Provides:       noto-serif-nyiakengpuachuehmong-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-nphmong-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
NPHmong Serif font, hinted.

%package -n google-noto-serif-olduyghur-fonts
Summary:        Noto Old Uyghur Serif Font
Obsoletes:      noto-serif-olduyghur < %{version}
Provides:       noto-serif-olduyghur = %{version}
Obsoletes:      noto-serif-olduyghur-fonts < %{version}
Provides:       noto-serif-olduyghur-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-olduyghur-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OldUyghur Serif font, hinted.

%package -n google-noto-serif-oriya-fonts
Summary:        Noto Oriya Serif Font
Obsoletes:      noto-serif-oriya < %{version}
Provides:       noto-serif-oriya = %{version}
Obsoletes:      noto-serif-oriya-fonts < %{version}
Provides:       noto-serif-oriya-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-oriya-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Oriya Serif font, hinted.

%package -n google-noto-serif-ottomansiyaq-fonts
Summary:        Noto Ottoman Siyaq Serif Font
Obsoletes:      noto-serif-ottomansiyaq < %{version}
Provides:       noto-serif-ottomansiyaq = %{version}
Obsoletes:      noto-serif-ottomansiyaq-fonts < %{version}
Provides:       noto-serif-ottomansiyaq-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-ottomansiyaq-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
OttomanSiyaq Serif font, hinted.

%package -n google-noto-serif-sinhala-fonts
Summary:        Noto Sinhala Serif Font
Obsoletes:      noto-serif-sinhala < %{version}
Provides:       noto-serif-sinhala = %{version}
Obsoletes:      noto-serif-sinhala-fonts < %{version}
Provides:       noto-serif-sinhala-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-sinhala-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Sinhala Serif font, hinted.

%package -n google-noto-serif-tamil-fonts
Summary:        Noto Tamil Serif Font
Obsoletes:      noto-serif-tamil < %{version}
Provides:       noto-serif-tamil = %{version}
Obsoletes:      noto-serif-tamil-fonts < %{version}
Provides:       noto-serif-tamil-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-tamil-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tamil Serif font, hinted.

%package -n google-noto-serif-tangut-fonts
Summary:        Noto Tangut Serif Font
Obsoletes:      noto-serif-tangut < %{version}
Provides:       noto-serif-tangut = %{version}
Obsoletes:      noto-serif-tangut-fonts < %{version}
Provides:       noto-serif-tangut-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-tangut-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tangut Serif font, hinted.

%package -n google-noto-serif-telugu-fonts
Summary:        Noto Telugu Serif Font
Obsoletes:      noto-serif-telugu < %{version}
Provides:       noto-serif-telugu = %{version}
Obsoletes:      noto-serif-telugu-fonts < %{version}
Provides:       noto-serif-telugu-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-telugu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Telugu Serif font, hinted.

%package -n google-noto-serif-thai-fonts
Summary:        Noto Thai Serif Font
Obsoletes:      noto-serif-thai < %{version}
Provides:       noto-serif-thai = %{version}
Obsoletes:      noto-serif-thai-fonts < %{version}
Provides:       noto-serif-thai-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-thai-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Thai Serif font, hinted.

%package -n google-noto-serif-tibetan-fonts
Summary:        Noto Tibetan Serif Font
Obsoletes:      noto-serif-tibetan < %{version}
Provides:       noto-serif-tibetan = %{version}
Obsoletes:      noto-serif-tibetan-fonts < %{version}
Provides:       noto-serif-tibetan-fonts = %{version}
Obsoletes:      noto-sans-tibetan < %{version}
Provides:       noto-sans-tibetan = %{version}
Obsoletes:      noto-sans-tibetan-fonts < %{version}
Provides:       noto-sans-tibetan-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-tibetan-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Tibetan Serif font, hinted.

%package -n google-noto-serif-toto-fonts
Summary:        Noto Toto Serif Font
Obsoletes:      noto-serif-toto < %{version}
Provides:       noto-serif-toto = %{version}
Obsoletes:      noto-serif-toto-fonts < %{version}
Provides:       noto-serif-toto-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-toto-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Toto Serif font, hinted.

%package -n google-noto-serif-vithkuqi-fonts
Summary:        Noto Vithkuqi Serif Font
Obsoletes:      noto-serif-vithkuqi < %{version}
Provides:       noto-serif-vithkuqi = %{version}
Obsoletes:      noto-serif-vithkuqi-fonts < %{version}
Provides:       noto-serif-vithkuqi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-vithkuqi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Vithkuqi Serif font, hinted.

%package -n google-noto-serif-yezidi-fonts
Summary:        Noto Yezidi Serif Font
Obsoletes:      noto-serif-yezidi < %{version}
Provides:       noto-serif-yezidi = %{version}
Obsoletes:      noto-serif-yezidi-fonts < %{version}
Provides:       noto-serif-yezidi-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-serif-yezidi-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Yezidi Serif font, hinted.

%package -n google-noto-traditionalnushu-fonts
Summary:        Noto Traditional Nushu Font
Obsoletes:      noto-traditionalnushu < %{version}
Provides:       noto-traditionalnushu = %{version}
Obsoletes:      noto-traditionalnushu-fonts < %{version}
Provides:       noto-traditionalnushu-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-traditionalnushu-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
TraditionalNushu font, hinted.

%package -n google-noto-znamennymusicalnotation-fonts
Summary:        Noto Znamenny Musical Notation Font
Obsoletes:      noto-znamennymusicalnotation < %{version}
Provides:       noto-znamennymusicalnotation = %{version}
Obsoletes:      noto-znamennymusicalnotation-fonts < %{version}
Provides:       noto-znamennymusicalnotation-fonts = %{version}
%reconfigure_fonts_prereq

%description -n google-noto-znamennymusicalnotation-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
ZnamennyMusicalNotation font, hinted.

%prep
%autosetup -c

cp notofonts.github.io-noto-monthly-release-24.6.1/fonts/LICENSE .

%build

%install

rm -r notofonts.github.io-noto-monthly-release-24.6.1/fonts/Noto*Test

install -Dm 644 -t %{buildroot}%{_ttfontsdir} notofonts.github.io-noto-monthly-release-24.6.1/fonts/*/hinted/ttf/*

%reconfigure_fonts_scriptlets -n google-noto-fangsongkssrotated-fonts

%reconfigure_fonts_scriptlets -n google-noto-fangsongkssvertical-fonts

%reconfigure_fonts_scriptlets -n google-noto-kufiarabic-fonts

%reconfigure_fonts_scriptlets -n google-noto-music-fonts

%reconfigure_fonts_scriptlets -n google-noto-naskharabic-fonts

%reconfigure_fonts_scriptlets -n google-noto-nastaliqurdu-fonts

%reconfigure_fonts_scriptlets -n google-noto-rashihebrew-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-adlam-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-adlamunjoined-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-anatolianhieroglyphs-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-arabic-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-armenian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-avestan-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-balinese-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-bamum-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-bassavah-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-batak-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-bengali-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-bhaiksuki-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-brahmi-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-buginese-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-buhid-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-canadianaboriginal-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-carian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-caucasianalbanian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-chakma-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-cham-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-cherokee-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-chorasmian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-coptic-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-cuneiform-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-cypriot-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-cyprominoan-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-deseret-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-devanagari-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-duployan-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-egyptianhieroglyphs-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-elbasan-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-elymaic-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-ethiopic-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-georgian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-glagolitic-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-gothic-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-grantha-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-gujarati-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-gunjalagondi-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-gurmukhi-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-hanifirohingya-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-hanunoo-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-hatran-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-hebrew-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-imperialaramaic-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-indicsiyaqnumbers-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-inscriptionalpahlavi-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-inscriptionalparthian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-javanese-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kaithi-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kannada-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kawi-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kayahli-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kharoshthi-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-khmer-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-khojki-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-khudawadi-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-lao-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-laolooped-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-lepcha-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-limbu-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-lineara-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-linearb-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-lisu-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-lycian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-lydian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-mahajani-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-malayalam-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-mandaic-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-manichaean-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-marchen-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-masaramgondi-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-math-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-mayannumerals-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-medefaidrin-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-meeteimayek-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-mendekikakui-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-meroitic-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-miao-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-modi-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-mongolian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-mono-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-mro-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-multani-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-myanmar-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-nabataean-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-nagmundari-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-nandinagari-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-newa-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-newtailue-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-nko-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-nkounjoined-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-nushu-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-ogham-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-olchiki-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-oldhungarian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-olditalic-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-oldnortharabian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-oldpermic-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-oldpersian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-oldsogdian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-oldsoutharabian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-oldturkic-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-oriya-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-osage-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-osmanya-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-pahawhhmong-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-palmyrene-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-paucinhau-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-phagspa-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-phoenician-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-psalterpahlavi-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-rejang-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-runic-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-samaritan-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-saurashtra-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-sharada-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-shavian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-siddham-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-signwriting-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-sinhala-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-sogdian-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-sorasompeng-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-soyombo-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-sundanese-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-sylotinagri-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-symbols-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-symbols2-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-syriac-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-syriaceastern-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-syriacwestern-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tagalog-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tagbanwa-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-taile-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-taitham-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-taiviet-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-takri-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tamil-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tamilsupplement-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tangsa-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-telugu-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-thaana-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-thai-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-thailooped-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tifinagh-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tirhuta-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-ugaritic-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-vai-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-vithkuqi-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-wancho-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-warangciti-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-yi-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-zanabazarsquare-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-ahom-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-armenian-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-balinese-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-bengali-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-devanagari-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-display-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-divesakuru-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-dogra-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-ethiopic-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-georgian-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-grantha-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-gujarati-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-gurmukhi-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-hebrew-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-kannada-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-khitansmallscript-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-khmer-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-khojki-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-lao-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-makasar-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-malayalam-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-myanmar-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-nphmong-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-olduyghur-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-oriya-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-ottomansiyaq-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-sinhala-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-tamil-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-tangut-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-telugu-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-thai-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-tibetan-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-toto-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-vithkuqi-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-yezidi-fonts

%reconfigure_fonts_scriptlets -n google-noto-traditionalnushu-fonts

%reconfigure_fonts_scriptlets -n google-noto-znamennymusicalnotation-fonts

%files

%files -n google-noto-fangsongkssrotated-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoFangsongKSSRotated-*.?tf

%files -n google-noto-fangsongkssvertical-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoFangsongKSSVertical-*.?tf

%files -n google-noto-kufiarabic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoKufiArabic-*.?tf

%files -n google-noto-music-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoMusic-*.?tf

%files -n google-noto-naskharabic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoNaskhArabic-*.?tf
%{_ttfontsdir}/NotoNaskhArabicUI-*.?tf

%files -n google-noto-nastaliqurdu-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoNastaliqUrdu-*.?tf

%files -n google-noto-rashihebrew-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoRashiHebrew-*.?tf

%files -n google-noto-sans-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSans-*.?tf

%files -n google-noto-sans-adlam-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansAdlam-*.?tf

%files -n google-noto-sans-adlamunjoined-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansAdlamUnjoined-*.?tf

%files -n google-noto-sans-anatolianhieroglyphs-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansAnatolianHieroglyphs-*.?tf

%files -n google-noto-sans-arabic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansArabic-*.?tf

%files -n google-noto-sans-armenian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansArmenian-*.?tf

%files -n google-noto-sans-avestan-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansAvestan-*.?tf

%files -n google-noto-sans-balinese-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBalinese-*.?tf

%files -n google-noto-sans-bamum-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBamum-*.?tf

%files -n google-noto-sans-bassavah-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBassaVah-*.?tf

%files -n google-noto-sans-batak-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBatak-*.?tf

%files -n google-noto-sans-bengali-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBengali-*.?tf
%{_ttfontsdir}/NotoSansBengaliUI-*.?tf

%files -n google-noto-sans-bhaiksuki-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBhaiksuki-*.?tf

%files -n google-noto-sans-brahmi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBrahmi-*.?tf

%files -n google-noto-sans-buginese-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBuginese-*.?tf

%files -n google-noto-sans-buhid-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansBuhid-*.?tf

%files -n google-noto-sans-canadianaboriginal-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCanadianAboriginal-*.?tf

%files -n google-noto-sans-carian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCarian-*.?tf

%files -n google-noto-sans-caucasianalbanian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCaucasianAlbanian-*.?tf

%files -n google-noto-sans-chakma-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansChakma-*.?tf

%files -n google-noto-sans-cham-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCham-*.?tf

%files -n google-noto-sans-cherokee-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCherokee-*.?tf

%files -n google-noto-sans-chorasmian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansChorasmian-*.?tf

%files -n google-noto-sans-coptic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCoptic-*.?tf

%files -n google-noto-sans-cuneiform-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCuneiform-*.?tf

%files -n google-noto-sans-cypriot-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCypriot-*.?tf

%files -n google-noto-sans-cyprominoan-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCyproMinoan-*.?tf

%files -n google-noto-sans-deseret-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansDeseret-*.?tf

%files -n google-noto-sans-devanagari-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansDevanagari-*.?tf
%{_ttfontsdir}/NotoSansDevanagariUI-*.?tf

%files -n google-noto-sans-duployan-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansDuployan-*.?tf

%files -n google-noto-sans-egyptianhieroglyphs-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansEgyptianHieroglyphs-*.?tf

%files -n google-noto-sans-elbasan-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansElbasan-*.?tf

%files -n google-noto-sans-elymaic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansElymaic-*.?tf

%files -n google-noto-sans-ethiopic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansEthiopic-*.?tf

%files -n google-noto-sans-georgian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGeorgian-*.?tf

%files -n google-noto-sans-glagolitic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGlagolitic-*.?tf

%files -n google-noto-sans-gothic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGothic-*.?tf

%files -n google-noto-sans-grantha-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGrantha-*.?tf

%files -n google-noto-sans-gujarati-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGujarati-*.?tf
%{_ttfontsdir}/NotoSansGujaratiUI-*.?tf

%files -n google-noto-sans-gunjalagondi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGunjalaGondi-*.?tf

%files -n google-noto-sans-gurmukhi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansGurmukhi-*.?tf
%{_ttfontsdir}/NotoSansGurmukhiUI-*.?tf

%files -n google-noto-sans-hanifirohingya-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHanifiRohingya-*.?tf

%files -n google-noto-sans-hanunoo-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHanunoo-*.?tf

%files -n google-noto-sans-hatran-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHatran-*.?tf

%files -n google-noto-sans-hebrew-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHebrew-*.?tf

%files -n google-noto-sans-imperialaramaic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansImperialAramaic-*.?tf

%files -n google-noto-sans-indicsiyaqnumbers-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansIndicSiyaqNumbers-*.?tf

%files -n google-noto-sans-inscriptionalpahlavi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansInscriptionalPahlavi-*.?tf

%files -n google-noto-sans-inscriptionalparthian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansInscriptionalParthian-*.?tf

%files -n google-noto-sans-javanese-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansJavanese-*.?tf

%files -n google-noto-sans-kaithi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKaithi-*.?tf

%files -n google-noto-sans-kannada-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKannada-*.?tf
%{_ttfontsdir}/NotoSansKannadaUI-*.?tf

%files -n google-noto-sans-kawi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKawi-*.?tf

%files -n google-noto-sans-kayahli-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKayahLi-*.?tf

%files -n google-noto-sans-kharoshthi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKharoshthi-*.?tf

%files -n google-noto-sans-khmer-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKhmer-*.?tf

%files -n google-noto-sans-khojki-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKhojki-*.?tf

%files -n google-noto-sans-khudawadi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKhudawadi-*.?tf

%files -n google-noto-sans-lao-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLao-*.?tf

%files -n google-noto-sans-laolooped-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLaoLooped-*.?tf

%files -n google-noto-sans-lepcha-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLepcha-*.?tf

%files -n google-noto-sans-limbu-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLimbu-*.?tf

%files -n google-noto-sans-lineara-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLinearA-*.?tf

%files -n google-noto-sans-linearb-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLinearB-*.?tf

%files -n google-noto-sans-lisu-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLisu-*.?tf

%files -n google-noto-sans-lycian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLycian-*.?tf

%files -n google-noto-sans-lydian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansLydian-*.?tf

%files -n google-noto-sans-mahajani-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMahajani-*.?tf

%files -n google-noto-sans-malayalam-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMalayalam-*.?tf
%{_ttfontsdir}/NotoSansMalayalamUI-*.?tf

%files -n google-noto-sans-mandaic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMandaic-*.?tf

%files -n google-noto-sans-manichaean-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansManichaean-*.?tf

%files -n google-noto-sans-marchen-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMarchen-*.?tf

%files -n google-noto-sans-masaramgondi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMasaramGondi-*.?tf

%files -n google-noto-sans-math-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMath-*.?tf

%files -n google-noto-sans-mayannumerals-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMayanNumerals-*.?tf

%files -n google-noto-sans-medefaidrin-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMedefaidrin-*.?tf

%files -n google-noto-sans-meeteimayek-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMeeteiMayek-*.?tf

%files -n google-noto-sans-mendekikakui-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMendeKikakui-*.?tf

%files -n google-noto-sans-meroitic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMeroitic-*.?tf

%files -n google-noto-sans-miao-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMiao-*.?tf

%files -n google-noto-sans-modi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansModi-*.?tf

%files -n google-noto-sans-mongolian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMongolian-*.?tf

%files -n google-noto-sans-mono-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMono-*.?tf

%files -n google-noto-sans-mro-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMro-*.?tf

%files -n google-noto-sans-multani-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMultani-*.?tf

%files -n google-noto-sans-myanmar-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMyanmar-*.?tf

%files -n google-noto-sans-nabataean-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNabataean-*.?tf

%files -n google-noto-sans-nagmundari-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNagMundari-*.?tf

%files -n google-noto-sans-nandinagari-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNandinagari-*.?tf

%files -n google-noto-sans-newa-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNewa-*.?tf

%files -n google-noto-sans-newtailue-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNewTaiLue-*.?tf

%files -n google-noto-sans-nko-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNKo-*.?tf

%files -n google-noto-sans-nkounjoined-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNKoUnjoined-*.?tf

%files -n google-noto-sans-nushu-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansNushu-*.?tf

%files -n google-noto-sans-ogham-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOgham-*.?tf

%files -n google-noto-sans-olchiki-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOlChiki-*.?tf

%files -n google-noto-sans-oldhungarian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldHungarian-*.?tf

%files -n google-noto-sans-olditalic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldItalic-*.?tf

%files -n google-noto-sans-oldnortharabian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldNorthArabian-*.?tf

%files -n google-noto-sans-oldpermic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldPermic-*.?tf

%files -n google-noto-sans-oldpersian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldPersian-*.?tf

%files -n google-noto-sans-oldsogdian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldSogdian-*.?tf

%files -n google-noto-sans-oldsoutharabian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldSouthArabian-*.?tf

%files -n google-noto-sans-oldturkic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOldTurkic-*.?tf

%files -n google-noto-sans-oriya-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOriya-*.?tf

%files -n google-noto-sans-osage-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOsage-*.?tf

%files -n google-noto-sans-osmanya-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansOsmanya-*.?tf

%files -n google-noto-sans-pahawhhmong-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPahawhHmong-*.?tf

%files -n google-noto-sans-palmyrene-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPalmyrene-*.?tf

%files -n google-noto-sans-paucinhau-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPauCinHau-*.?tf

%files -n google-noto-sans-phagspa-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPhagsPa-*.?tf

%files -n google-noto-sans-phoenician-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPhoenician-*.?tf

%files -n google-noto-sans-psalterpahlavi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansPsalterPahlavi-*.?tf

%files -n google-noto-sans-rejang-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansRejang-*.?tf

%files -n google-noto-sans-runic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansRunic-*.?tf

%files -n google-noto-sans-samaritan-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSamaritan-*.?tf

%files -n google-noto-sans-saurashtra-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSaurashtra-*.?tf

%files -n google-noto-sans-sharada-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSharada-*.?tf

%files -n google-noto-sans-shavian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansShavian-*.?tf

%files -n google-noto-sans-siddham-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSiddham-*.?tf

%files -n google-noto-sans-signwriting-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSignWriting-*.?tf

%files -n google-noto-sans-sinhala-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSinhala-*.?tf
%{_ttfontsdir}/NotoSansSinhalaUI-*.?tf

%files -n google-noto-sans-sogdian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSogdian-*.?tf

%files -n google-noto-sans-sorasompeng-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSoraSompeng-*.?tf

%files -n google-noto-sans-soyombo-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSoyombo-*.?tf

%files -n google-noto-sans-sundanese-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSundanese-*.?tf

%files -n google-noto-sans-sylotinagri-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSylotiNagri-*.?tf

%files -n google-noto-sans-symbols-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSymbols-*.?tf

%files -n google-noto-sans-symbols2-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSymbols2-*.?tf

%files -n google-noto-sans-syriac-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSyriac-*.?tf

%files -n google-noto-sans-syriaceastern-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSyriacEastern-*.?tf

%files -n google-noto-sans-syriacwestern-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSyriacWestern-*.?tf

%files -n google-noto-sans-tagalog-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTagalog-*.?tf

%files -n google-noto-sans-tagbanwa-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTagbanwa-*.?tf

%files -n google-noto-sans-taile-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTaiLe-*.?tf

%files -n google-noto-sans-taitham-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTaiTham-*.?tf

%files -n google-noto-sans-taiviet-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTaiViet-*.?tf

%files -n google-noto-sans-takri-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTakri-*.?tf

%files -n google-noto-sans-tamil-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTamil-*.?tf
%{_ttfontsdir}/NotoSansTamilUI-*.?tf

%files -n google-noto-sans-tamilsupplement-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTamilSupplement-*.?tf

%files -n google-noto-sans-tangsa-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTangsa-*.?tf

%files -n google-noto-sans-telugu-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTelugu-*.?tf
%{_ttfontsdir}/NotoSansTeluguUI-*.?tf

%files -n google-noto-sans-thaana-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansThaana-*.?tf

%files -n google-noto-sans-thai-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansThai-*.?tf

%files -n google-noto-sans-thailooped-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansThaiLooped-*.?tf

%files -n google-noto-sans-tifinagh-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTifinagh*.?tf

%files -n google-noto-sans-tirhuta-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTirhuta-*.?tf

%files -n google-noto-sans-ugaritic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansUgaritic-*.?tf

%files -n google-noto-sans-vai-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansVai-*.?tf

%files -n google-noto-sans-vithkuqi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansVithkuqi-*.?tf

%files -n google-noto-sans-wancho-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansWancho-*.?tf

%files -n google-noto-sans-warangciti-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansWarangCiti-*.?tf

%files -n google-noto-sans-yi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansYi-*.?tf

%files -n google-noto-sans-zanabazarsquare-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansZanabazarSquare-*.?tf

%files -n google-noto-serif-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerif-*.?tf

%files -n google-noto-serif-ahom-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifAhom-*.?tf

%files -n google-noto-serif-armenian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifArmenian-*.?tf

%files -n google-noto-serif-balinese-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifBalinese-*.?tf

%files -n google-noto-serif-bengali-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifBengali-*.?tf

%files -n google-noto-serif-devanagari-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifDevanagari-*.?tf

%files -n google-noto-serif-display-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifDisplay-*.?tf

%files -n google-noto-serif-divesakuru-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifDivesAkuru-*.?tf

%files -n google-noto-serif-dogra-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifDogra-*.?tf

%files -n google-noto-serif-ethiopic-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifEthiopic-*.?tf

%files -n google-noto-serif-georgian-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifGeorgian-*.?tf

%files -n google-noto-serif-grantha-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifGrantha-*.?tf

%files -n google-noto-serif-gujarati-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifGujarati-*.?tf

%files -n google-noto-serif-gurmukhi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifGurmukhi-*.?tf

%files -n google-noto-serif-hebrew-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifHebrew-*.?tf

%files -n google-noto-serif-kannada-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifKannada-*.?tf

%files -n google-noto-serif-khitansmallscript-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifKhitanSmallScript-*.?tf

%files -n google-noto-serif-khmer-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifKhmer-*.?tf

%files -n google-noto-serif-khojki-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifKhojki-*.?tf

%files -n google-noto-serif-lao-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifLao-*.?tf

%files -n google-noto-serif-makasar-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifMakasar-*.?tf

%files -n google-noto-serif-malayalam-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifMalayalam-*.?tf

%files -n google-noto-serif-myanmar-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifMyanmar-*.?tf

%files -n google-noto-serif-nphmong-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifNPHmong-*.?tf

%files -n google-noto-serif-olduyghur-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifOldUyghur-*.?tf

%files -n google-noto-serif-oriya-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifOriya-*.?tf

%files -n google-noto-serif-ottomansiyaq-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifOttomanSiyaq-*.?tf

%files -n google-noto-serif-sinhala-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifSinhala-*.?tf

%files -n google-noto-serif-tamil-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifTamil-*.?tf

%files -n google-noto-serif-tangut-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifTangut-*.?tf

%files -n google-noto-serif-telugu-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifTelugu-*.?tf

%files -n google-noto-serif-thai-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifThai-*.?tf

%files -n google-noto-serif-tibetan-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifTibetan-*.?tf

%files -n google-noto-serif-toto-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifToto-*.?tf

%files -n google-noto-serif-vithkuqi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifVithkuqi-*.?tf

%files -n google-noto-serif-yezidi-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifYezidi-*.?tf

%files -n google-noto-traditionalnushu-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoTraditionalNushu-*.?tf

%files -n google-noto-znamennymusicalnotation-fonts
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoZnamennyMusicalNotation-*.?tf

%changelog
