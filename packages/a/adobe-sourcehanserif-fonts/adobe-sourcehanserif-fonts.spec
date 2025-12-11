#
# spec file for package adobe-sourcehanserif-fonts
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define shared_description Source Han Serif is a pan-CJK typeface. It is the serif counterpart to Source Han Sans and comes in seven weights.

Name:           adobe-sourcehanserif-fonts
Version:        2.003
Release:        0
Summary:        Multi-weight serif-style Pan-CJK typeface family
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/adobe-fonts/source-han-serif
Source0:        https://github.com/adobe-fonts/source-han-serif/releases/download/%{version}R/02_SourceHanSerif-VF.zip
Source1:        https://github.com/adobe-fonts/source-han-serif/releases/download/%{version}R/05_SourceHanSerifSubsetOTF.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch

%description
%{shared_description}

%prep
%{uncompress:%{S:0}}
%if 0%{?suse_version} < 1600
# Next archive will unpack the same file again; and SL15.x rpm's %%uncompress
# forgets passing a force-overwrite flag for ZIPs, causing a build failure.
rm -v LICENSE.txt
%endif
%{uncompress:%{S:1}}

%build

%install
install -d %{buildroot}%{_ttfontsdir}
install -m 644 Variable/OTF/Subset/*.otf %{buildroot}%{_ttfontsdir}
install -m 644 SubsetOTF/*/*.otf %{buildroot}%{_ttfontsdir}

# Simplified Chinese package
%package -n adobe-sourcehanserif-cn-fonts
Summary:        Source Han Serif variation for Simplified Chinese
Group:          System/X11/Fonts
Provides:       scalable-font-zh_CN
Provides:       locale(zh_CN)

%description -n adobe-sourcehanserif-cn-fonts
%{shared_description}

%reconfigure_fonts_scriptlets -c -n adobe-sourcehanserif-cn-fonts

%files -n adobe-sourcehanserif-cn-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifCN-*.otf

# Traditional Chinese Hong Kong package
%package -n adobe-sourcehanserif-hk-fonts
Summary:        Source Han Serif variation for Traditional Chinese in Hong Kong
Group:          System/X11/Fonts
Provides:       scalable-font-zh_HK
Provides:       locale(zh_HK)

%description -n adobe-sourcehanserif-hk-fonts
%{shared_description}

%reconfigure_fonts_scriptlets -c -n adobe-sourcehanserif-hk-fonts

%files -n adobe-sourcehanserif-hk-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifHK-*.otf

# Japanese package
%package -n adobe-sourcehanserif-jp-fonts
Summary:        Source Han Serif variation for Japanese
Group:          System/X11/Fonts
Provides:       scalable-font-jp
Provides:       locale(jp)

%description -n adobe-sourcehanserif-jp-fonts
%{shared_description}

%reconfigure_fonts_scriptlets -c -n adobe-sourcehanserif-jp-fonts

%files -n adobe-sourcehanserif-jp-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifJP-*.otf

# Korean package
%package -n adobe-sourcehanserif-kr-fonts
Summary:        Source Han Serif variation for Korean
Group:          System/X11/Fonts
Provides:       scalable-font-kr
Provides:       locale(kr)

%description -n adobe-sourcehanserif-kr-fonts
%{shared_description}

%reconfigure_fonts_scriptlets -c -n adobe-sourcehanserif-kr-fonts

%files -n adobe-sourcehanserif-kr-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifKR-*.otf

# Traditional Chinese Taiwan package
%package -n adobe-sourcehanserif-tw-fonts
Summary:        Source Han Serif variation for Traditional Chinese in Taiwan
Group:          System/X11/Fonts
Provides:       adobe-sourcehanserif-fonts = %version
Provides:       scalable-font-zh_TW
Provides:       locale(zh_TW)
Obsoletes:      adobe-sourcehanserif-fonts < %version

%description -n adobe-sourcehanserif-tw-fonts
%{shared_description}

%reconfigure_fonts_scriptlets -c -n adobe-sourcehanserif-tw-fonts

%files -n adobe-sourcehanserif-tw-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifTW-*.otf

%changelog
