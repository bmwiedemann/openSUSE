#
# spec file for package google-noto-sans-cjk-fonts
#
# Copyright (c) 2020 SUSE LLC
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


%define _version 2.001

Name:           google-noto-sans-cjk-fonts
Version:        20190410
Release:        0
Summary:        Noto Sans CJK Font Families
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/googlefonts/noto-cjk
Source0:        https://github.com/googlefonts/noto-cjk/archive/NotoSansV%{_version}.tar.gz
BuildRequires:  fontpackages-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages.

%package -n noto-sans-sc-regular-fonts
Summary:        Noto Sans Simplified Chinese Font - Regular
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-sc-regular-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular weight
of Sans font for Simplified Chinese, hinted.

%package -n noto-sans-sc-thin-fonts
Summary:        Noto Sans Simplified Chinese Font - Thin
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-sc-thin-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Thin weight of
Sans font for Simplified Chinese, hinted.

%package -n noto-sans-sc-light-fonts
Summary:        Noto Sans Simplified Chinese Font - Light
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-sc-light-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Light weight of
Sans font for Simplified Chinese, hinted.

%package -n noto-sans-sc-demilight-fonts
Summary:        Noto Sans Simplified Chinese Font - DemiLight
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-sc-demilight-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Demilight weight
of Sans font for Simplified Chinese, hinted.

%package -n noto-sans-sc-bold-fonts
Summary:        Noto Sans Simplified Chinese Font - Bold
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-sc-bold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Bold weight of
Sans font for Simplified Chinese, hinted.

%package -n noto-sans-sc-black-fonts
Summary:        Noto Sans Simplified Chinese Font - Black
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-sc-black-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Black weight of
Sans font for Simplified Chinese, hinted.

%package -n noto-sans-sc-medium-fonts
Summary:        Noto Sans Simplified Chinese Font - Medium
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-sc-medium-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Medium weight of
Sans font for Simplified Chinese, hinted.

%package -n noto-sans-sc-mono-fonts
Summary:        Noto Sans Simplified Chinese Font - Monospace
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-sc-mono-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Monospace fonts
for Simplified Chinese, hinted.

%package -n noto-sans-sc-fonts
Summary:        Noto Sans Simplified Chinese Font - Regular and Bold
Group:          System/X11/Fonts
Provides:       noto-sans-cjksc = %{version}
Obsoletes:      noto-sans-cjksc < %{version}
Provides:       noto-sans-cjksc-fonts = %{version}
Obsoletes:      noto-sans-cjksc-fonts < %{version}
Provides:       scalable-font-zh-CN
Provides:       scalable-font-zh-SG
Provides:       locale(zh_CN;zh_SG)
Requires:       noto-sans-sc-bold-fonts = %{version}
Requires:       noto-sans-sc-regular-fonts = %{version}

%description -n noto-sans-sc-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular and Bold
weights of Sans font for Simplified Chinese, hinted.

%package -n noto-sans-sc-fonts-full
Summary:        Noto Sans Simplified Chinese Font - All Weights
Group:          System/X11/Fonts
Requires:       noto-sans-sc-black-fonts = %{version}
Requires:       noto-sans-sc-demilight-fonts = %{version}
Requires:       noto-sans-sc-fonts = %{version}
Requires:       noto-sans-sc-light-fonts = %{version}
Requires:       noto-sans-sc-medium-fonts = %{version}
Requires:       noto-sans-sc-thin-fonts = %{version}

%description -n noto-sans-sc-fonts-full
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains All weights for
Sans and Monospace fonts for Simplified Chinese, hinted.

%package -n noto-sans-tc-regular-fonts
Summary:        Noto Sans Traditional Chinese Font - Regular
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-tc-regular-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular weight
of Sans font for Traditional Chinese, hinted.

%package -n noto-sans-tc-thin-fonts
Summary:        Noto Sans Traditional Chinese Font - Thin
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-tc-thin-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Thin weight of
Sans font for Traditional Chinese, hinted.

%package -n noto-sans-tc-light-fonts
Summary:        Noto Sans Traditional Chinese Font - Light
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-tc-light-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Light weight of
Sans font for Traditional Chinese, hinted.

%package -n noto-sans-tc-demilight-fonts
Summary:        Noto Sans Traditional Chinese Font - DemiLight
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-tc-demilight-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Demilight weight
of Sans font for Traditional Chinese, hinted.

%package -n noto-sans-tc-bold-fonts
Summary:        Noto Sans Traditional Chinese Font - Bold
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-tc-bold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Bold weight of
Sans font for Traditional Chinese, hinted.

%package -n noto-sans-tc-black-fonts
Summary:        Noto Sans Traditional Chinese Font - Black
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-tc-black-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Black weight of
Sans font for Traditional Chinese, hinted.

%package -n noto-sans-tc-medium-fonts
Summary:        Noto Sans Traditional Chinese Font - Medium
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-tc-medium-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Medium weight of
Sans font for Traditional Chinese, hinted.

%package -n noto-sans-tc-mono-fonts
Summary:        Noto Sans Traditional Chinese Font - Monospace
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-tc-mono-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Monospace fonts
for Traditional Chinese, hinted.

%package -n noto-sans-tc-fonts
Summary:        Noto Sans Traditional Chinese Font - Regular and Bold
Group:          System/X11/Fonts
Provides:       noto-sans-cjktc = %{version}
Obsoletes:      noto-sans-cjktc < %{version}
Provides:       noto-sans-cjktc-fonts = %{version}
Obsoletes:      noto-sans-cjktc-fonts < %{version}
Provides:       scalable-font-zh-MO
Provides:       scalable-font-zh-TW
Provides:       locale(zh_MO;zh_TW)
Requires:       noto-sans-tc-bold-fonts = %{version}
Requires:       noto-sans-tc-regular-fonts = %{version}

%description -n noto-sans-tc-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular and Bold
weights of Sans font for Traditional Chinese, hinted.

%package -n noto-sans-tc-fonts-full
Summary:        Noto Sans Traditional Chinese Font - All Weights
Group:          System/X11/Fonts
Requires:       noto-sans-tc-black-fonts = %{version}
Requires:       noto-sans-tc-demilight-fonts = %{version}
Requires:       noto-sans-tc-fonts = %{version}
Requires:       noto-sans-tc-light-fonts = %{version}
Requires:       noto-sans-tc-medium-fonts = %{version}
Requires:       noto-sans-tc-thin-fonts = %{version}

%description -n noto-sans-tc-fonts-full
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains All weights for
Sans and Monospace fonts for Traditional Chinese, hinted.

%package -n noto-sans-hk-regular-fonts
Summary:        Noto Sans Traditional Chinese Font for HongKong - Regular
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-hk-regular-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular weight
of Sans font for Traditional Chinese, hinted.

%package -n noto-sans-hk-thin-fonts
Summary:        Noto Sans Traditional Chinese Font for HongKong - Thin
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-hk-thin-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Thin weight of
Sans font for Traditional Chinese, hinted.

%package -n noto-sans-hk-light-fonts
Summary:        Noto Sans Traditional Chinese Font for HongKong - Light
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-hk-light-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Light weight of
Sans font for Traditional Chinese, hinted.

%package -n noto-sans-hk-demilight-fonts
Summary:        Noto Sans Traditional Chinese Font for HongKong- DemiLight
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-hk-demilight-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Demilight weight
of Sans font for Traditional Chinese, hinted.

%package -n noto-sans-hk-bold-fonts
Summary:        Noto Sans Traditional Chinese Font for HongKong- Bold
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-hk-bold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Bold weight of
Sans font for Traditional Chinese, hinted.

%package -n noto-sans-hk-black-fonts
Summary:        Noto Sans Traditional Chinese Font for HongKong- Black
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-hk-black-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Black weight of
Sans font for Traditional Chinese, hinted.

%package -n noto-sans-hk-medium-fonts
Summary:        Noto Sans Traditional Chinese Font for HongKong- Medium
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-hk-medium-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Medium weight of
Sans font for Traditional Chinese, hinted.

%package -n noto-sans-hk-mono-fonts
Summary:        Noto Sans Traditional Chinese Font for HongKong- Monospace
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-hk-mono-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Monospace fonts
for Traditional Chinese, hinted.

%package -n noto-sans-hk-fonts
Summary:        Noto Sans Traditional Chinese Font for HongKong- Regular and Bold
Group:          System/X11/Fonts
Provides:       noto-sans-cjkhk = %{version}
Obsoletes:      noto-sans-cjkhk < %{version}
Provides:       noto-sans-cjkhk-fonts = %{version}
Obsoletes:      noto-sans-cjkhk-fonts < %{version}
Provides:       scalable-font-zh-HK
Provides:       locale(zh_HK)
Requires:       noto-sans-hk-bold-fonts = %{version}
Requires:       noto-sans-hk-regular-fonts = %{version}

%description -n noto-sans-hk-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular and Bold
weights of Sans font for Traditional Chinese, hinted.

%package -n noto-sans-hk-fonts-full
Summary:        Noto Sans Traditional Chinese Font for HongKong- All Weights
Group:          System/X11/Fonts
Requires:       noto-sans-hk-black-fonts = %{version}
Requires:       noto-sans-hk-demilight-fonts = %{version}
Requires:       noto-sans-hk-fonts = %{version}
Requires:       noto-sans-hk-light-fonts = %{version}
Requires:       noto-sans-hk-medium-fonts = %{version}
Requires:       noto-sans-hk-thin-fonts = %{version}

%description -n noto-sans-hk-fonts-full
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains All weights for
Sans and Monospace fonts for Traditional Chinese, hinted.

%package -n noto-sans-jp-regular-fonts
Summary:        Noto Sans Japanese Font - Regular
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-jp-regular-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular weight
of Sans font for Japanese, hinted.

%package -n noto-sans-jp-thin-fonts
Summary:        Noto Sans Japanese Font - Thin
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-jp-thin-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Thin weight of
Sans font for Japanese, hinted.

%package -n noto-sans-jp-light-fonts
Summary:        Noto Sans Japanese Font - Light
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-jp-light-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Light weight of
Sans font for Japanese, hinted.

%package -n noto-sans-jp-demilight-fonts
Summary:        Noto Sans Japanese Font - DemiLight
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-jp-demilight-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Demilight weight
of Sans font for Japanese, hinted.

%package -n noto-sans-jp-bold-fonts
Summary:        Noto Sans Japanese Font - Bold
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-jp-bold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Bold weight of
Sans font for Japanese, hinted.

%package -n noto-sans-jp-black-fonts
Summary:        Noto Sans Japanese Font - Black
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-jp-black-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Black weight of
Sans font for Japanese, hinted.

%package -n noto-sans-jp-medium-fonts
Summary:        Noto Sans Japanese Font - Medium
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-jp-medium-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Medium weight of
Sans font for Japanese, hinted.

%package -n noto-sans-jp-mono-fonts
Summary:        Noto Sans Japanese Font - Monospace
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-jp-mono-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Monospace fonts
for Japanese, hinted.

%package -n noto-sans-jp-fonts
Summary:        Noto Sans Japanese Font - Regular and Bold
Group:          System/X11/Fonts
Provides:       noto-sans-cjkjp = %{version}
Obsoletes:      noto-sans-cjkjp < %{version}
Provides:       noto-sans-cjkjp-fonts = %{version}
Obsoletes:      noto-sans-cjkjp-fonts < %{version}
Provides:       scalable-font-ja
Provides:       locale(ja)
Requires:       noto-sans-jp-bold-fonts = %{version}
Requires:       noto-sans-jp-regular-fonts = %{version}

%description -n noto-sans-jp-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular and Bold
weights of Sans font for Japanese, hinted.

%package -n noto-sans-jp-fonts-full
Summary:        Noto Sans Japanese Font - All Weights
Group:          System/X11/Fonts
Requires:       noto-sans-jp-black-fonts = %{version}
Requires:       noto-sans-jp-demilight-fonts = %{version}
Requires:       noto-sans-jp-fonts = %{version}
Requires:       noto-sans-jp-light-fonts = %{version}
Requires:       noto-sans-jp-medium-fonts = %{version}
Requires:       noto-sans-jp-thin-fonts = %{version}

%description -n noto-sans-jp-fonts-full
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains All weights for
Sans and Monospace fonts for Japanese, hinted.

%package -n noto-sans-kr-regular-fonts
Summary:        Noto Sans Korean Font - Regular
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-kr-regular-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular weight
of Sans font for Korean, hinted.

%package -n noto-sans-kr-thin-fonts
Summary:        Noto Sans Korean Font - Thin
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-kr-thin-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Thin weight of
Sans font for Korean, hinted.

%package -n noto-sans-kr-light-fonts
Summary:        Noto Sans Korean Font - Light
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-kr-light-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Light weight of
Sans font for Korean, hinted.

%package -n noto-sans-kr-demilight-fonts
Summary:        Noto Sans Korean Font - DemiLight
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-kr-demilight-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Demilight weight
of Sans font for Korean, hinted.

%package -n noto-sans-kr-bold-fonts
Summary:        Noto Sans Korean Font - Bold
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-kr-bold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Bold weight of
Sans font for Korean, hinted.

%package -n noto-sans-kr-black-fonts
Summary:        Noto Sans Korean Font - Black
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-kr-black-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Black weight of
Sans font for Korean, hinted.

%package -n noto-sans-kr-medium-fonts
Summary:        Noto Sans Korean Font - Medium
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-kr-medium-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Medium weight of
Sans font for Korean, hinted.

%package -n noto-sans-kr-mono-fonts
Summary:        Noto Sans Korean Font - Monospace
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-sans-kr-mono-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Monospace fonts
for Korean, hinted.

%package -n noto-sans-kr-fonts
Summary:        Noto Sans Korean Font - Regular and Bold
Group:          System/X11/Fonts
Provides:       noto-sans-cjkkr = %{version}
Obsoletes:      noto-sans-cjkkr < %{version}
Provides:       noto-sans-cjkkr-fonts = %{version}
Obsoletes:      noto-sans-cjkkr-fonts < %{version}
Provides:       scalable-font-ko
Provides:       locale(ko)
Requires:       noto-sans-kr-bold-fonts = %{version}
Requires:       noto-sans-kr-regular-fonts = %{version}

%description -n noto-sans-kr-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular and Bold
weights of Sans font for Korean, hinted.

%package -n noto-sans-kr-fonts-full
Summary:        Noto Sans Korean Font - All Weights
Group:          System/X11/Fonts
Requires:       noto-sans-kr-black-fonts = %{version}
Requires:       noto-sans-kr-demilight-fonts = %{version}
Requires:       noto-sans-kr-fonts = %{version}
Requires:       noto-sans-kr-light-fonts = %{version}
Requires:       noto-sans-kr-medium-fonts = %{version}
Requires:       noto-sans-kr-thin-fonts = %{version}

%description -n noto-sans-kr-fonts-full
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains All weights for
Sans and Monospace fonts for Korean, hinted.

%package -n noto-sans-cjk-fonts
Summary:        Noto Sans CJK Font - Regular and Bold
Group:          System/X11/Fonts
Requires:       noto-sans-jp-fonts = %{version}
Requires:       noto-sans-kr-fonts = %{version}
Requires:       noto-sans-sc-fonts = %{version}
Requires:       noto-sans-tc-fonts = %{version}
Provides:       noto-sans-cjk = %{version}
Obsoletes:      noto-sans-cjk < %{version}

%description -n noto-sans-cjk-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular and Bold
weights for Noto Sans fonts for the four CJK languages.

%prep
%setup -q -n noto-cjk-NotoSansV%{_version}

%build

%install
rm -rf NotoSansCJK* NotoSerif*
mkdir -p %{buildroot}%{_ttfontsdir}
cp *.?tf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets -n noto-sans-sc-regular-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sc-thin-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sc-medium-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sc-light-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sc-demilight-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sc-bold-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sc-black-fonts

%reconfigure_fonts_scriptlets -n noto-sans-sc-mono-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tc-regular-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tc-thin-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tc-medium-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tc-light-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tc-demilight-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tc-bold-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tc-black-fonts

%reconfigure_fonts_scriptlets -n noto-sans-tc-mono-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hk-regular-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hk-thin-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hk-medium-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hk-light-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hk-demilight-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hk-bold-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hk-black-fonts

%reconfigure_fonts_scriptlets -n noto-sans-hk-mono-fonts

%reconfigure_fonts_scriptlets -n noto-sans-jp-regular-fonts

%reconfigure_fonts_scriptlets -n noto-sans-jp-thin-fonts

%reconfigure_fonts_scriptlets -n noto-sans-jp-medium-fonts

%reconfigure_fonts_scriptlets -n noto-sans-jp-light-fonts

%reconfigure_fonts_scriptlets -n noto-sans-jp-demilight-fonts

%reconfigure_fonts_scriptlets -n noto-sans-jp-bold-fonts

%reconfigure_fonts_scriptlets -n noto-sans-jp-black-fonts

%reconfigure_fonts_scriptlets -n noto-sans-jp-mono-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kr-regular-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kr-thin-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kr-medium-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kr-light-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kr-demilight-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kr-bold-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kr-black-fonts

%reconfigure_fonts_scriptlets -n noto-sans-kr-mono-fonts

%files -n noto-sans-sc-regular-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSC-Regular.?tf

%files -n noto-sans-sc-thin-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSC-Thin.?tf

%files -n noto-sans-sc-medium-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSC-Medium.?tf

%files -n noto-sans-sc-light-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSC-Light.?tf

%files -n noto-sans-sc-demilight-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSC-DemiLight.?tf

%files -n noto-sans-sc-bold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSC-Bold.?tf

%files -n noto-sans-sc-black-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansSC-Black.?tf

%files -n noto-sans-sc-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKsc-*.?tf

%files -n noto-sans-sc-fonts
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-sans-sc-fonts-full
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-sans-tc-regular-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTC-Regular.?tf

%files -n noto-sans-tc-thin-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTC-Thin.?tf

%files -n noto-sans-tc-medium-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTC-Medium.?tf

%files -n noto-sans-tc-light-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTC-Light.?tf

%files -n noto-sans-tc-demilight-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTC-DemiLight.?tf

%files -n noto-sans-tc-bold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTC-Bold.?tf

%files -n noto-sans-tc-black-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansTC-Black.?tf

%files -n noto-sans-tc-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKtc-*.?tf

%files -n noto-sans-tc-fonts
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-sans-tc-fonts-full
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-sans-hk-regular-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHK-Regular.?tf

%files -n noto-sans-hk-thin-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHK-Thin.?tf

%files -n noto-sans-hk-medium-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHK-Medium.?tf

%files -n noto-sans-hk-light-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHK-Light.?tf

%files -n noto-sans-hk-demilight-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHK-DemiLight.?tf

%files -n noto-sans-hk-bold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHK-Bold.?tf

%files -n noto-sans-hk-black-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansHK-Black.?tf

%files -n noto-sans-hk-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKhk-*.?tf

%files -n noto-sans-hk-fonts
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-sans-hk-fonts-full
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-sans-jp-regular-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansJP-Regular.?tf

%files -n noto-sans-jp-thin-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansJP-Thin.?tf

%files -n noto-sans-jp-medium-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansJP-Medium.?tf

%files -n noto-sans-jp-light-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansJP-Light.?tf

%files -n noto-sans-jp-demilight-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansJP-DemiLight.?tf

%files -n noto-sans-jp-bold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansJP-Bold.?tf

%files -n noto-sans-jp-black-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansJP-Black.?tf

%files -n noto-sans-jp-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKjp-*.?tf

%files -n noto-sans-jp-fonts
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-sans-jp-fonts-full
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-sans-kr-regular-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKR-Regular.?tf

%files -n noto-sans-kr-thin-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKR-Thin.?tf

%files -n noto-sans-kr-medium-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKR-Medium.?tf

%files -n noto-sans-kr-light-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKR-Light.?tf

%files -n noto-sans-kr-demilight-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKR-DemiLight.?tf

%files -n noto-sans-kr-bold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKR-Bold.?tf

%files -n noto-sans-kr-black-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansKR-Black.?tf

%files -n noto-sans-kr-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKkr-*.?tf

%files -n noto-sans-kr-fonts
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-sans-kr-fonts-full
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-sans-cjk-fonts
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%changelog
