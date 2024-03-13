#
# spec file for package google-noto-serif-cjk-fonts
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

Name:           google-noto-serif-cjk-fonts
Version:        2.002
Release:        0
Summary:        Noto Serif CJK Font Families
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/googlefonts/noto-cjk
Source0:        https://github.com/googlefonts/noto-cjk/releases/download/Serif%{version}/02_NotoSerifCJK-OTF-VF.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch

%description
Noto's design goal is to achieve visual harmonization (e.g., compatible heights and stroke
thicknesses) across languages.

%package -n google-noto-serif-sc-fonts
Summary:        Noto Serif Simplified Chinese Font
Group:          System/X11/Fonts
Provides:       noto-serif-sc-fonts = %{version}
Obsoletes:      noto-serif-sc-fonts < %{version}
Provides:       google-noto-serif-sc-regular-fonts = %{version}
Obsoletes:    google-noto-serif-sc-regular-fonts <  %{version}
Provides:       google-noto-serif-sc-semibold-fonts = %{version}
Obsoletes:    google-noto-serif-sc-semibold-fonts < %{version}
Provides:       google-noto-serif-sc-light-fonts = %{version}
Obsoletes:    google-noto-serif-sc-light-fonts < %{version}
Provides:       google-noto-serif-sc-extralight-fonts = %{version}
Obsoletes:    google-noto-serif-sc-extralight-fonts < %{version}
Provides:       google-noto-serif-sc-bold-fonts = %{version}
Obsoletes:    google-noto-serif-sc-bold-fonts < %{version}
Provides:       google-noto-serif-sc-black-fonts = %{version}
Obsoletes:    google-noto-serif-sc-black-fonts < %{version}
Provides:       google-noto-serif-sc-medium-fonts = %{version}
Obsoletes:    google-noto-serif-sc-medium-fonts < %{version}
Provides:       google-noto-serif-sc-fonts-full = %{version}
Obsoletes:    google-noto-serif-sc-fonts-full < %{version}
Provides:       scalable-font-zh-CN
Provides:       scalable-font-zh-SG
Provides:       locale(zh_CN;zh_SG)

%description -n google-noto-serif-sc-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Serif font for Simplified Chinese, hinted and variable.

%package -n google-noto-serif-tc-fonts
Summary:        Noto Serif Traditional Chinese Font
Group:          System/X11/Fonts
Provides:       noto-serif-tc-fonts = %{version}
Obsoletes:      noto-serif-tc-fonts < %{version}
Provides:       google-noto-serif-tc-regular-fonts = %{version}
Obsoletes:    google-noto-serif-tc-regular-fonts <  %{version}
Provides:       google-noto-serif-tc-semibold-fonts = %{version}
Obsoletes:    google-noto-serif-tc-semibold-fonts < %{version}
Provides:       google-noto-serif-tc-light-fonts = %{version}
Obsoletes:    google-noto-serif-tc-light-fonts < %{version}
Provides:       google-noto-serif-tc-extralight-fonts = %{version}
Obsoletes:    google-noto-serif-tc-extralight-fonts < %{version}
Provides:       google-noto-serif-tc-bold-fonts = %{version}
Obsoletes:    google-noto-serif-tc-bold-fonts < %{version}
Provides:       google-noto-serif-tc-black-fonts = %{version}
Obsoletes:    google-noto-serif-tc-black-fonts < %{version}
Provides:       google-noto-serif-tc-medium-fonts = %{version}
Obsoletes:    google-noto-serif-tc-medium-fonts < %{version}
Provides:       google-noto-serif-tc-fonts-full = %{version}
Obsoletes:    google-noto-serif-tc-fonts-full < %{version}
Provides:       scalable-font-zh-TW
Provides:       locale(zh_TW)

%description -n google-noto-serif-tc-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Serif font for Traditional Chinese, hinted and variable.

%package -n google-noto-serif-hk-fonts
Summary:        Noto Serif Traditional Chinese (Hong Kong) Font
Group:          System/X11/Fonts
Provides:       noto-serif-hk-fonts = %{version}
Obsoletes:      noto-serif-hk-fonts < %{version}
Provides:       google-noto-serif-hk-regular-fonts = %{version}
Obsoletes:    google-noto-serif-hk-regular-fonts <  %{version}
Provides:       google-noto-serif-hk-semibold-fonts = %{version}
Obsoletes:    google-noto-serif-hk-semibold-fonts < %{version}
Provides:       google-noto-serif-hk-light-fonts = %{version}
Obsoletes:    google-noto-serif-hk-light-fonts < %{version}
Provides:       google-noto-serif-hk-extralight-fonts = %{version}
Obsoletes:    google-noto-serif-hk-extralight-fonts < %{version}
Provides:       google-noto-serif-hk-bold-fonts = %{version}
Obsoletes:    google-noto-serif-hk-bold-fonts < %{version}
Provides:       google-noto-serif-hk-black-fonts = %{version}
Obsoletes:    google-noto-serif-hk-black-fonts < %{version}
Provides:       google-noto-serif-hk-medium-fonts = %{version}
Obsoletes:    google-noto-serif-hk-medium-fonts < %{version}
Provides:       google-noto-serif-hk-fonts-full = %{version}
Obsoletes:    google-noto-serif-hk-fonts-full < %{version}
Provides:       scalable-font-zh-HK
Provides:       scalable-font-zh-MO
Provides:       locale(zh_HK;zh_MO)

%description -n google-noto-serif-hk-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Serif font for Traditional Chinese (Hong Kong), hinted and variable.

%package -n google-noto-serif-jp-fonts
Summary:        Noto Serif Japanese Font
Group:          System/X11/Fonts
Provides:       noto-serif-jp-fonts = %{version}
Obsoletes:      noto-serif-jp-fonts < %{version}
Provides:       google-noto-serif-jp-regular-fonts = %{version}
Obsoletes:    google-noto-serif-jp-regular-fonts <  %{version}
Provides:       google-noto-serif-jp-semibold-fonts = %{version}
Obsoletes:    google-noto-serif-jp-semibold-fonts < %{version}
Provides:       google-noto-serif-jp-light-fonts = %{version}
Obsoletes:    google-noto-serif-jp-light-fonts < %{version}
Provides:       google-noto-serif-jp-extralight-fonts = %{version}
Obsoletes:    google-noto-serif-jp-extralight-fonts < %{version}
Provides:       google-noto-serif-jp-bold-fonts = %{version}
Obsoletes:    google-noto-serif-jp-bold-fonts < %{version}
Provides:       google-noto-serif-jp-black-fonts = %{version}
Obsoletes:    google-noto-serif-jp-black-fonts < %{version}
Provides:       google-noto-serif-jp-medium-fonts = %{version}
Obsoletes:    google-noto-serif-jp-medium-fonts < %{version}
Provides:       google-noto-serif-jp-fonts-full = %{version}
Obsoletes:    google-noto-serif-jp-fonts-full < %{version}
Provides:       scalable-font-ja
Provides:       locale(ja)

%description -n google-noto-serif-jp-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Serif font for Japanese, hinted and variable.

%package -n google-noto-serif-kr-fonts
Summary:        Noto Serif Korean Font
Group:          System/X11/Fonts
Provides:       noto-serif-kr-fonts = %{version}
Obsoletes:      noto-serif-kr-fonts < %{version}
Provides:       google-noto-serif-kr-regular-fonts = %{version}
Obsoletes:    google-noto-serif-kr-regular-fonts <  %{version}
Provides:       google-noto-serif-kr-semibold-fonts = %{version}
Obsoletes:    google-noto-serif-kr-semibold-fonts < %{version}
Provides:       google-noto-serif-kr-light-fonts = %{version}
Obsoletes:    google-noto-serif-kr-light-fonts < %{version}
Provides:       google-noto-serif-kr-extralight-fonts = %{version}
Obsoletes:    google-noto-serif-kr-extralight-fonts < %{version}
Provides:       google-noto-serif-kr-bold-fonts = %{version}
Obsoletes:    google-noto-serif-kr-bold-fonts < %{version}
Provides:       google-noto-serif-kr-black-fonts = %{version}
Obsoletes:    google-noto-serif-kr-black-fonts < %{version}
Provides:       google-noto-serif-kr-medium-fonts = %{version}
Obsoletes:    google-noto-serif-kr-medium-fonts < %{version}
Provides:       google-noto-serif-kr-fonts-full = %{version}
Obsoletes:    google-noto-serif-kr-fonts-full < %{version}
Provides:       scalable-font-ko
Provides:       locale(ko)

%description -n google-noto-serif-kr-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Serif font for Korean, hinted and variable.

%prep
unzip -qqn %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
cp Variable/OTF/NotoSerifCJK*-VF.?tf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets -n google-noto-serif-sc-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-tc-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-hk-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-jp-fonts

%reconfigure_fonts_scriptlets -n google-noto-serif-kr-fonts

%files -n google-noto-serif-sc-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKsc-VF.?tf

%files -n google-noto-serif-tc-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKtc-VF.?tf

%files -n google-noto-serif-hk-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKhk-VF.?tf

%files -n google-noto-serif-jp-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKjp-VF.?tf

%files -n google-noto-serif-kr-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKkr-VF.?tf

%changelog
