#
# spec file for package ipa-bolditalic-fonts
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2012 Yasuhiko Kamata
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


Name:           ipa-bolditalic-fonts
Version:        003.02
Release:        0
Summary:        IPAGothic/IPAPGothic Italic (Oblique) / Bold Variants
License:        IPA
Group:          System/X11/Fonts
URL:            http://ossipedia.ipa.go.jp/ipafont/
Source0:        IPAFont00302_bolditalic.tar.bz2
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Italic (oblique) / Bold variants (processed with fontforge) fonts.

Original Japanese TrueType font is made by IPA
(Information-technology Promotion Agency).

%package -n ipa-gothic-italic-fonts
Summary:        Italic Variant of "Gothic" Japanese TrueType Font Made by IPA
Group:          System/X11/Fonts
Provides:       IPAGothic_Italic = %{version}
Obsoletes:      IPAGothic_Italic <= 003.02
%reconfigure_fonts_prereq

%description -n ipa-gothic-italic-fonts
Italic variant of "Gothic" Japanese TrueType font made by IPA
(Information-technology Promotion Agency).

%package -n ipa-gothic-bold-fonts
Summary:        Bold Variant of "Gothic" Japanese TrueType Font Made by IPA
Group:          System/X11/Fonts
Provides:       IPAGothic_Bold = %{version}
Obsoletes:      IPAGothic_Bold <= 003.02
%reconfigure_fonts_prereq

%description -n ipa-gothic-bold-fonts
Bold variant of "Gothic" Japanese TrueType font made by IPA
(Information-technology Promotion Agency).

%package -n ipa-gothic-bolditalic-fonts
Summary:        Bold+Italic Variant of "Gothic" Japanese TrueType Font Made by IPA
Group:          System/X11/Fonts
Provides:       IPAGothic_BoldItalic = %{version}
Obsoletes:      IPAGothic_BoldItalic <= 003.02
%reconfigure_fonts_prereq

%description -n ipa-gothic-bolditalic-fonts
Bold+Italic variant of "Gothic" Japanese TrueType font made by IPA
(Information-technology Promotion Agency).

%package -n ipa-pgothic-italic-fonts
Summary:        Italic Variant of "Proportional Gothic" Japanese TrueType Font Made by IPA
Group:          System/X11/Fonts
Provides:       IPAPGothic_Italic = %{version}
Obsoletes:      IPAPGothic_Italic <= 003.02

%description -n ipa-pgothic-italic-fonts
Italic variant of "Proportional Gothic" Japanese TrueType font made by IPA
(Information-technology Promotion Agency).

%package -n ipa-pgothic-bold-fonts
Summary:        Bold Variant of "Proportional Gothic" Japanese TrueType Font Made by IPA
Group:          System/X11/Fonts
Provides:       IPAPGothic_Bold = %{version}
Obsoletes:      IPAPGothic_Bold <= 003.02
%reconfigure_fonts_prereq

%description -n ipa-pgothic-bold-fonts
Bold variant of "Proportional Gothic" Japanese TrueType font made by IPA
(Information-technology Promotion Agency).

%package -n ipa-pgothic-bolditalic-fonts
Summary:        Bold+Italic Variant of "Proportional Gothic" Japanese TrueType Font Made by IPA
Group:          System/X11/Fonts
Provides:       IPAPGothic_BoldItalic = %{version}
Obsoletes:      IPAPGothic_BoldItalic <= 003.02
%reconfigure_fonts_prereq

%description -n ipa-pgothic-bolditalic-fonts
Bold+Italic variant of "Proportional Gothic" Japanese TrueType font made by IPA
(Information-technology Promotion Agency).

%prep
%setup -n IPAFont00302_bolditalic

%build
##### DISABLED due to too long time to complete. #####
# cp /usr/share/fonts/truetype/ipag{,p}.ttf .

# fontforge -lang=ff -c "Open(\$1); SelectAll(); ClearInstrs(); Skew(20); SetFontNames('IPAGothic_Italic', 'IPAGothic Italic', 'IPAGothic Italic'); SetTTFName(0x409, 1, 'IPAGothic Italic'); SetTTFName(0x409, 2, 'Italic'); SetTTFName(0x409, 3, 'IPAGothic Italic'); SetTTFName(0x409, 4, 'IPAGothic Italic'); SetTTFName(0x411, 1, 'IPAゴシック Italic'); SetTTFName(0x411, 2, 'Italic'); SetTTFName(0x411, 3, 'IPAGothic Italic'); SetTTFName(0x411, 4, 'IPAゴシック Italic'); Generate(\$2);" ipag.ttf ipag_i.ttf
# fontforge -lang=ff -c "Open(\$1); SelectAll(); ClearInstrs(); ExpandStroke(100, 0, 0, 0, 1); SetFontNames('IPAGothic_Bold', 'IPAGothic Bold', 'IPAGothic Bold'); SetTTFName(0x409, 1, 'IPAGothic Bold'); SetTTFName(0x409, 2, 'Bold'); SetTTFName(0x409, 3, 'IPAGothic Bold'); SetTTFName(0x409, 4, 'IPAGothic Bold'); SetTTFName(0x411, 1, 'IPAゴシック Bold'); SetTTFName(0x411, 2, 'Bold'); SetTTFName(0x411, 3, 'IPAGothic Bold'); SetTTFName(0x411, 4, 'IPAゴシック Bold'); Generate(\$2);" ipag.ttf ipag_b.ttf
# fontforge -lang=ff -c "Open(\$1); SelectAll(); ClearInstrs(); Skew(20); ExpandStroke(100, 0, 0, 0, 1); SetFontNames('IPAGothic_BoldItalic', 'IPAGothic BoldItalic', 'IPAGothic BoldItalic'); SetTTFName(0x409, 1, 'IPAGothic BoldItalic'); SetTTFName(0x409, 2, 'Bold Italic'); SetTTFName(0x409, 3, 'IPAGothic BoldItalic'); SetTTFName(0x409, 4, 'IPAGothic BoldItalic'); SetTTFName(0x411, 1, 'IPAゴシック BoldItalic'); SetTTFName(0x411, 2, 'Bold Italic'); SetTTFName(0x411, 3, 'IPAGothic BoldItalic'); SetTTFName(0x411, 4, 'IPAゴシック BoldItalic'); Generate(\$2);" ipag.ttf ipag_bi.ttf

# fontforge -lang=ff -c "Open(\$1); SelectAll(); ClearInstrs(); Skew(20); SetFontNames('IPAPGothic_Italic', 'IPAPGothic Italic', 'IPAPGothic Italic'); SetTTFName(0x409, 1, 'IPAPGothic Italic'); SetTTFName(0x409, 2, 'Italic'); SetTTFName(0x409, 3, 'IPAPGothic Italic'); SetTTFName(0x409, 4, 'IPAPGothic Italic'); SetTTFName(0x411, 1, 'IPA Pゴシック Italic'); SetTTFName(0x411, 2, 'Italic'); SetTTFName(0x411, 3, 'IPAPGothic Italic'); SetTTFName(0x411, 4, 'IPA Pゴシック Italic'); Generate(\$2);" ipagp.ttf ipagp_i.ttf
# fontforge -lang=ff -c "Open(\$1); SelectAll(); ClearInstrs(); ExpandStroke(100, 0, 0, 0, 1); SetFontNames('IPAPGothic_Bold', 'IPAPGothic Bold', 'IPAPGothic Bold'); SetTTFName(0x409, 1, 'IPAPGothic Bold'); SetTTFName(0x409, 2, 'Bold'); SetTTFName(0x409, 3, 'IPAPGothic Bold'); SetTTFName(0x409, 4, 'IPAPGothic Bold'); SetTTFName(0x411, 1, 'IPA Pゴシック Bold'); SetTTFName(0x411, 2, 'Bold'); SetTTFName(0x411, 3, 'IPAPGothic Bold'); SetTTFName(0x411, 4, 'IPA Pゴシック Bold'); Generate(\$2);" ipagp.ttf ipagp_b.ttf
# fontforge -lang=ff -c "Open(\$1); SelectAll(); ClearInstrs(); Skew(20); ExpandStroke(100, 0, 0, 0, 1); SetFontNames('IPAPGothic_BoldItalic', 'IPAPGothic BoldItalic', 'IPAPGothic BoldItalic'); SetTTFName(0x409, 1, 'IPAPGothic BoldItalic'); SetTTFName(0x409, 2, 'Bold Italic'); SetTTFName(0x409, 3, 'IPAPGothic BoldItalic'); SetTTFName(0x409, 4, 'IPAPGothic BoldItalic'); SetTTFName(0x411, 1, 'IPA Pゴシック BoldItalic'); SetTTFName(0x411, 2, 'Bold Italic'); SetTTFName(0x411, 3, 'IPAPGothic BoldItalic'); SetTTFName(0x411, 4, 'IPA Pゴシック BoldItalic'); Generate(\$2);" ipagp.ttf ipagp_bi.ttf

%install
mkdir -p %{buildroot}%{_ttfontsdir}
for i in *.ttf
do
    install -m 644 $i %{buildroot}%{_ttfontsdir}
done

rm -f ipag_{i,b,bi}.ttf ipagp_{i,b,bi}.ttf

%reconfigure_fonts_scriptlets -c -n ipa-gothic-italic-fonts

%reconfigure_fonts_scriptlets -c -n ipa-gothic-bold-fonts

%reconfigure_fonts_scriptlets -c -n ipa-gothic-bolditalic-fonts

%reconfigure_fonts_scriptlets -c -n ipa-pgothic-italic-fonts

%reconfigure_fonts_scriptlets -c -n ipa-pgothic-bold-fonts

%reconfigure_fonts_scriptlets -c -n ipa-pgothic-bolditalic-fonts

%files -n ipa-gothic-italic-fonts
%defattr(-,root,root)
%doc *.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/ipag_i.*

%files -n ipa-gothic-bold-fonts
%defattr(-,root,root)
%doc *.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/ipag_b.*

%files -n ipa-gothic-bolditalic-fonts
%defattr(-,root,root)
%doc *.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/ipag_bi.*

%files -n ipa-pgothic-italic-fonts
%defattr(-,root,root)
%doc *.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/ipagp_i.*

%files -n ipa-pgothic-bold-fonts
%defattr(-,root,root)
%doc *.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/ipagp_b.*

%files -n ipa-pgothic-bolditalic-fonts
%defattr(-,root,root)
%doc *.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/ipagp_bi.*

%changelog
