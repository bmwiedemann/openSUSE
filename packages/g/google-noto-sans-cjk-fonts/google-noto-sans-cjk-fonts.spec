#
# spec file for package google-noto-sans-cjk-fonts
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


Name:           google-noto-sans-cjk-fonts
Version:        2.004
Release:        0
Summary:        Noto Sans CJK Font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/googlefonts/noto-cjk
Source0:        https://github.com/googlefonts/noto-cjk/releases/download/Sans%{version}/01_NotoSansCJK-OTF-VF.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
Requires:       google-noto-sans-jp-fonts = %{version}
Requires:       google-noto-sans-kr-fonts = %{version}
Requires:       google-noto-sans-sc-fonts = %{version}
Requires:       google-noto-sans-tc-fonts = %{version}
Provides:       noto-sans-cjk-fonts = %{version}
Obsoletes:      noto-sans-cjk-fonts <= %{version}
Provides:       noto-sans-cjk = %{version}
Obsoletes:      noto-sans-cjk <= %{version}

%description
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package Noto Sans fonts for the
four CJK languages.

%package -n google-noto-sans-sc-mono-fonts
Summary:        Noto Sans Simplified Chinese Font - Monospace
Group:          System/X11/Fonts
Provides:       noto-sans-sc-mono-fonts = %{version}
Obsoletes:      noto-sans-sc-mono-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-sc-mono-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Monospace fonts
for Simplified Chinese, hinted.

%package -n google-noto-sans-sc-fonts
Summary:        Noto Sans Simplified Chinese Font
Group:          System/X11/Fonts
Provides:       noto-sans-cjksc = %{version}
Obsoletes:      noto-sans-cjksc <= %{version}
Provides:       noto-sans-cjksc-fonts = %{version}
Obsoletes:      noto-sans-cjksc-fonts <= %{version}
Provides:       noto-sans-sc-fonts = %{version}
Obsoletes:      noto-sans-sc-fonts <= %{version}
Provides:       google-noto-sans-sc-thin-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-sc-thin-fonts < %{version}-%{release}
Provides:       google-noto-sans-sc-regular-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-sc-regular-fonts < %{version}-%{release}
Provides:       google-noto-sans-sc-light-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-sc-light-fonts < %{version}-%{release}
Provides:       google-noto-sans-sc-demilight-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-sc-demilight-fonts < %{version}-%{release}
Provides:       google-noto-sans-sc-medium-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-sc-medium-fonts < %{version}-%{release}
Provides:       google-noto-sans-sc-bold-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-sc-bold-fonts < %{version}-%{release}
Provides:       google-noto-sans-sc-black-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-sc-black-fonts < %{version}-%{release}
Provides:       google-noto-sans-sc-fonts-full = %{version}-%{release}
Obsoletes:      google-noto-sans-sc-fonts-full < %{version}-%{release}
Provides:       scalable-font-zh-CN
Provides:       scalable-font-zh-SG
Provides:       locale(zh_CN;zh_SG)
%reconfigure_fonts_prereq

%description -n google-noto-sans-sc-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Sans font for
Simplified Chinese, hinted and variable.

%package -n google-noto-sans-tc-mono-fonts
Summary:        Noto Sans Traditional Chinese Font - Monospace
Group:          System/X11/Fonts
Provides:       noto-sans-tc-mono-fonts = %{version}
Obsoletes:      noto-sans-tc-mono-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tc-mono-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Monospace fonts
for Traditional Chinese, hinted.

%package -n google-noto-sans-tc-fonts
Summary:        Noto Sans Traditional Chinese Font
Group:          System/X11/Fonts
Provides:       noto-sans-cjktc = %{version}
Obsoletes:      noto-sans-cjktc <= %{version}
Provides:       noto-sans-cjktc-fonts = %{version}
Obsoletes:      noto-sans-cjktc-fonts <= %{version}
Provides:       noto-sans-tc-fonts = %{version}
Obsoletes:      noto-sans-tc-fonts <= %{version}
Provides:       google-noto-sans-tc-thin-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-tc-thin-fonts < %{version}-%{release}
Provides:       google-noto-sans-tc-regular-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-tc-regular-fonts < %{version}-%{release}
Provides:       google-noto-sans-tc-light-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-tc-light-fonts < %{version}-%{release}
Provides:       google-noto-sans-tc-demilight-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-tc-demilight-fonts < %{version}-%{release}
Provides:       google-noto-sans-tc-medium-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-tc-medium-fonts < %{version}-%{release}
Provides:       google-noto-sans-tc-bold-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-tc-bold-fonts < %{version}-%{release}
Provides:       google-noto-sans-tc-black-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-tc-black-fonts < %{version}-%{release}
Provides:       google-noto-sans-tc-fonts-full = %{version}-%{release}
Obsoletes:      google-noto-sans-tc-fonts-full < %{version}-%{release}
Provides:       scalable-font-zh-TW
Provides:       locale(;zh_TW)
%reconfigure_fonts_prereq

%description -n google-noto-sans-tc-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Sans font for
Traditional Chinese, hinted and variable.

%package -n google-noto-sans-hk-mono-fonts
Summary:        Noto Sans Traditional Chinese (Hong Kong) Font - Monospace
Group:          System/X11/Fonts
Provides:       noto-sans-hk-mono-fonts = %{version}
Obsoletes:      noto-sans-hk-mono-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-hk-mono-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Monospace fonts
for Traditional Chinese (Hong Kong), hinted.

%package -n google-noto-sans-hk-fonts
Summary:        Noto Sans Traditional Chinese (Hong Kong) Font
Group:          System/X11/Fonts
Provides:       noto-sans-cjkhk = %{version}
Obsoletes:      noto-sans-cjkhk <= %{version}
Provides:       noto-sans-cjkhk-fonts = %{version}
Obsoletes:      noto-sans-cjkhk-fonts <= %{version}
Provides:       noto-sans-hk-fonts = %{version}
Obsoletes:      noto-sans-hk-fonts <= %{version}
Provides:       google-noto-sans-hk-thin-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-hk-thin-fonts < %{version}-%{release}
Provides:       google-noto-sans-hk-regular-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-hk-regular-fonts < %{version}-%{release}
Provides:       google-noto-sans-hk-light-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-hk-light-fonts < %{version}-%{release}
Provides:       google-noto-sans-hk-demilight-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-hk-demilight-fonts < %{version}-%{release}
Provides:       google-noto-sans-hk-medium-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-hk-medium-fonts < %{version}-%{release}
Provides:       google-noto-sans-hk-bold-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-hk-bold-fonts < %{version}-%{release}
Provides:       google-noto-sans-hk-black-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-hk-black-fonts < %{version}-%{release}
Provides:       google-noto-sans-hk-fonts-full = %{version}-%{release}
Obsoletes:      google-noto-sans-hk-fonts-full < %{version}-%{release}
Provides:       scalable-font-zh-HK
Provides:       scalable-font-zh-MO
Provides:       locale(zh_HK;zh_MO)
%reconfigure_fonts_prereq

%description -n google-noto-sans-hk-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Sans font for
Traditional Chinese (Hong Kong), hinted and variable.

%package -n google-noto-sans-jp-mono-fonts
Summary:        Noto Sans Japanese Font - Monospace
Group:          System/X11/Fonts
Provides:       noto-sans-jp-mono-fonts = %{version}
Obsoletes:      noto-sans-jp-mono-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-jp-mono-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Monospace fonts
for Japanese, hinted.

%package -n google-noto-sans-jp-fonts
Summary:        Noto Sans Japanese Font
Group:          System/X11/Fonts
Provides:       noto-sans-cjkjp = %{version}
Obsoletes:      noto-sans-cjkjp <= %{version}
Provides:       noto-sans-cjkjp-fonts = %{version}
Obsoletes:      noto-sans-cjkjp-fonts <= %{version}
Provides:       noto-sans-jp-fonts = %{version}
Obsoletes:      noto-sans-jp-fonts <= %{version}
Provides:       google-noto-sans-jp-thin-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-jp-thin-fonts < %{version}-%{release}
Provides:       google-noto-sans-jp-regular-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-jp-regular-fonts < %{version}-%{release}
Provides:       google-noto-sans-jp-light-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-jp-light-fonts < %{version}-%{release}
Provides:       google-noto-sans-jp-demilight-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-jp-demilight-fonts < %{version}-%{release}
Provides:       google-noto-sans-jp-medium-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-jp-medium-fonts < %{version}-%{release}
Provides:       google-noto-sans-jp-bold-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-jp-bold-fonts < %{version}-%{release}
Provides:       google-noto-sans-jp-black-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-jp-black-fonts < %{version}-%{release}
Provides:       google-noto-sans-jp-fonts-full = %{version}-%{release}
Obsoletes:      google-noto-sans-jp-fonts-full < %{version}-%{release}
Provides:       scalable-font-ja
Provides:       locale(ja)
%reconfigure_fonts_prereq

%description -n google-noto-sans-jp-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Sans font for
Japanese, hinted and variable.

%package -n google-noto-sans-kr-mono-fonts
Summary:        Noto Sans Korean Font - Monospace
Group:          System/X11/Fonts
Provides:       noto-sans-kr-mono-fonts = %{version}
Obsoletes:      noto-sans-kr-mono-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-kr-mono-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Monospace fonts
for Korean, hinted.

%package -n google-noto-sans-kr-fonts
Summary:        Noto Sans Korean Font
Group:          System/X11/Fonts
Provides:       noto-sans-cjkkr = %{version}
Obsoletes:      noto-sans-cjkkr <= %{version}
Provides:       noto-sans-cjkkr-fonts = %{version}
Obsoletes:      noto-sans-cjkkr-fonts <= %{version}
Provides:       noto-sans-kr-fonts = %{version}
Obsoletes:      noto-sans-kr-fonts <= %{version}
Provides:       google-noto-sans-kr-thin-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-kr-thin-fonts < %{version}-%{release}
Provides:       google-noto-sans-kr-regular-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-kr-regular-fonts < %{version}-%{release}
Provides:       google-noto-sans-kr-light-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-kr-light-fonts < %{version}-%{release}
Provides:       google-noto-sans-kr-demilight-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-kr-demilight-fonts < %{version}-%{release}
Provides:       google-noto-sans-kr-medium-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-kr-medium-fonts < %{version}-%{release}
Provides:       google-noto-sans-kr-bold-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-kr-bold-fonts < %{version}-%{release}
Provides:       google-noto-sans-kr-black-fonts = %{version}-%{release}
Obsoletes:      google-noto-sans-kr-black-fonts < %{version}-%{release}
Provides:       google-noto-sans-kr-fonts-full = %{version}-%{release}
Obsoletes:      google-noto-sans-kr-fonts-full < %{version}-%{release}
Provides:       scalable-font-ko
Provides:       locale(ko)
%reconfigure_fonts_prereq

%description -n google-noto-sans-kr-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Sans font for
Korean, hinted and variable.

%prep
unzip -qqn %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
cp Variable/OTF/*-VF.otf %{buildroot}%{_ttfontsdir}/
cp Variable/OTF/Mono/*-VF.otf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets -n google-noto-sans-sc-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-sc-mono-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tc-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tc-mono-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-hk-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-hk-mono-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-jp-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-jp-mono-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kr-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kr-mono-fonts

%files
%defattr(0644,root,root,755)
%license LICENSE

%files -n google-noto-sans-sc-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKsc-VF.?tf

%files -n google-noto-sans-sc-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKsc-VF.?tf

%files -n google-noto-sans-tc-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKtc-VF.?tf

%files -n google-noto-sans-tc-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKtc-VF.?tf

%files -n google-noto-sans-hk-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKhk-VF.?tf

%files -n google-noto-sans-hk-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKhk-VF.?tf

%files -n google-noto-sans-jp-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKjp-VF.?tf

%files -n google-noto-sans-jp-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKjp-VF.?tf

%files -n google-noto-sans-kr-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKkr-VF.?tf

%files -n google-noto-sans-kr-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKkr-VF.?tf

%changelog
