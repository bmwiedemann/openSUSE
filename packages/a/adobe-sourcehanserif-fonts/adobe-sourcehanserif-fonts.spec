#
# spec file for package adobe-sourcehanserif-fonts
#
# Copyright (c) 2023 SUSE LLC
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


%define shared_description Source Han Serif is a Pan-CJK typeface. It is the serif counterpart to Source Han Sans and comes in seven weights.

Name:           adobe-sourcehanserif-fonts
Version:        2.002
Release:        0
Summary:        Multi-weight pan-CJK fonts
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/adobe-fonts/source-han-serif
Source0:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/SubsetOTF/SourceHanSerifCN.zip
Source1:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/SubsetOTF/SourceHanSerifHK.zip
Source2:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/SubsetOTF/SourceHanSerifJP.zip
Source3:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/SubsetOTF/SourceHanSerifKR.zip
Source4:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/SubsetOTF/SourceHanSerifTW.zip
Source5:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/Variable/OTF/Subset/SourceHanSerifCN-VF.otf
Source6:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/Variable/OTF/Subset/SourceHanSerifHK-VF.otf
Source7:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/Variable/OTF/Subset/SourceHanSerifJP-VF.otf
Source8:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/Variable/OTF/Subset/SourceHanSerifKR-VF.otf
Source9:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/Variable/OTF/Subset/SourceHanSerifTW-VF.otf
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch

%description
%{shared_description}

%prep
%setup -Tcq
for i in %_sourcedir/*.zip; do
	unzip -o "$i"
done

%build

%install
chmod go-w *.otf *.txt
mkdir -p %{buildroot}%{_ttfontsdir}
mv *.otf %{buildroot}%{_ttfontsdir}
cp -a %_sourcedir/*.otf %buildroot/%_ttfontsdir/

%package -n adobe-sourcehanserif-cn-fonts
Summary:        Multi-weight pan-CJK font with Simplified Chinese localization
Group:          System/X11/Fonts
Provides:       scalable-font-zh_CN
Provides:       locale(zh_CN)

%description -n adobe-sourcehanserif-cn-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehanserif-cn-fonts

%files -n adobe-sourcehanserif-cn-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifCN-*.otf

%package -n adobe-sourcehanserif-hk-fonts
Summary:        Multi-weight pan-CJK font with Hong Kong glyph forms
Group:          System/X11/Fonts
Provides:       scalable-font-zh_HK
Provides:       locale(zh_HK)

%description -n adobe-sourcehanserif-hk-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehanserif-hk-fonts

%files -n adobe-sourcehanserif-hk-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifHK-*.otf

%package -n adobe-sourcehanserif-jp-fonts
Summary:        Multi-weight pan-CJK font with Japanese glyph forms
Group:          System/X11/Fonts
Provides:       scalable-font-jp
Provides:       locale(jp)

%description -n adobe-sourcehanserif-jp-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehanserif-jp-fonts

%files -n adobe-sourcehanserif-jp-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifJP-*.otf

%package -n adobe-sourcehanserif-kr-fonts
Summary:        Multi-weight pan-CJK font with Korean glyph forms
Group:          System/X11/Fonts
Provides:       scalable-font-kr
Provides:       locale(kr)

%description -n adobe-sourcehanserif-kr-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehanserif-kr-fonts

%files -n adobe-sourcehanserif-kr-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifKR-*.otf

%package -n adobe-sourcehanserif-tw-fonts
Summary:        Multi-weight pan-CJK font with Traditional Chinese glyph forms
# Replace the old single package that only provided Taiwan fonts
Group:          System/X11/Fonts
Provides:       adobe-sourcehanserif-fonts = %version
Provides:       scalable-font-zh_TW
Provides:       locale(zh_TW)
Obsoletes:      adobe-sourcehanserif-fonts < %version

%description -n adobe-sourcehanserif-tw-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehanserif-tw-fonts

%files -n adobe-sourcehanserif-tw-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifTW-*.otf

%changelog
