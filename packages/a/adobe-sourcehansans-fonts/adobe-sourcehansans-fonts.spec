#
# spec file for package adobe-sourcehansans-fonts
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


%define shared_description Source Han Sans is a pan-CJK typeface in OpenType/CFF and CID forms.

Name:           adobe-sourcehansans-fonts
Version:        2.005
Release:        0
Summary:        Sans serif-style Pan-CJK typeface family
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/adobe-fonts/source-han-sans
Source0:        https://github.com/adobe-fonts/source-han-sans/releases/download/%{version}R/02_SourceHanSans-VF.zip
Source1:        https://github.com/adobe-fonts/source-han-sans/releases/download/%{version}R/05_SourceHanSansSubsetOTF.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch

%description
Source Han Sans is a sans-serif gothic typeface family. (It is also
released under the Noto fonts project as Noto Sans CJK.) The Source
Han Sans family includes seven weights, and supports Traditional
Chinese, Simplified Chinese, Japanese and Korean. It also includes
Latin, Greek and Cyrillic characters from the Source Sans family.

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
%package -n adobe-sourcehansans-cn-fonts
Summary:        Source Han Sans variation for Simplified Chinese
Group:          System/X11/Fonts
Provides:       scalable-font-zh_CN
Provides:       locale(zh_CN)

%description -n adobe-sourcehansans-cn-fonts
%{shared_description}

%reconfigure_fonts_scriptlets -c -n adobe-sourcehansans-cn-fonts

%files -n adobe-sourcehansans-cn-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSansCN-*.otf

# Traditional Chinese Hong Kong package
%package -n adobe-sourcehansans-hk-fonts
Summary:        Source Han Sans variation for Traditional Chinese in Hong Kong
Group:          System/X11/Fonts
Provides:       scalable-font-zh_HK
Provides:       locale(zh_HK)

%description -n adobe-sourcehansans-hk-fonts
%{shared_description}

%reconfigure_fonts_scriptlets -c -n adobe-sourcehansans-hk-fonts

%files -n adobe-sourcehansans-hk-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSansHK-*.otf

# Japanese package
%package -n adobe-sourcehansans-jp-fonts
Summary:        Source Han Sans variation for Japanese
Group:          System/X11/Fonts
Provides:       scalable-font-jp
Provides:       locale(jp)

%description -n adobe-sourcehansans-jp-fonts
%{shared_description}

%reconfigure_fonts_scriptlets -c -n adobe-sourcehansans-jp-fonts

%files -n adobe-sourcehansans-jp-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSansJP-*.otf

# Korean package
%package -n adobe-sourcehansans-kr-fonts
Summary:        Source Han Sans variation for Korean
Group:          System/X11/Fonts
Provides:       scalable-font-kr
Provides:       locale(kr)

%description -n adobe-sourcehansans-kr-fonts
%{shared_description}

%reconfigure_fonts_scriptlets -c -n adobe-sourcehansans-kr-fonts

%files -n adobe-sourcehansans-kr-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSansKR-*.otf

# Traditional Chinese Taiwan package
%package -n adobe-sourcehansans-tw-fonts
Summary:        Source Han Sans variation for Traditional Chinese in Taiwan
Group:          System/X11/Fonts
Provides:       adobe-sourcehansans-fonts = %version-%release
Provides:       scalable-font-zh_TW
Provides:       locale(zh_TW)
Obsoletes:      adobe-sourcehansans-fonts < %version-%release

%description -n adobe-sourcehansans-tw-fonts
%{shared_description}

%reconfigure_fonts_scriptlets -c -n adobe-sourcehansans-tw-fonts

%files -n adobe-sourcehansans-tw-fonts
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSansTW-*.otf

%changelog
