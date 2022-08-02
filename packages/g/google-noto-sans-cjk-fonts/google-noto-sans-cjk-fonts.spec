#
# spec file for package google-noto-sans-cjk-fonts
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


Name:           google-noto-sans-cjk-fonts
Version:        2.004
Release:        0
Summary:        Noto Sans CJK Font - Regular and Bold
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/googlefonts/noto-cjk
Source0:        https://github.com/googlefonts/noto-cjk/releases/download/Sans%{version}/04_NotoSansCJK-OTF.zip
Source1:        https://github.com/googlefonts/noto-cjk/releases/download/Sans%{version}/11_NotoSansMonoCJKjp.zip
Source2:        https://github.com/googlefonts/noto-cjk/releases/download/Sans%{version}/12_NotoSansMonoCJKkr.zip
Source3:        https://github.com/googlefonts/noto-cjk/releases/download/Sans%{version}/13_NotoSansMonoCJKsc.zip
Source4:        https://github.com/googlefonts/noto-cjk/releases/download/Sans%{version}/14_NotoSansMonoCJKtc.zip
Source5:        https://github.com/googlefonts/noto-cjk/releases/download/Sans%{version}/15_NotoSansMonoCJKhk.zip
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
and stroke thicknesses) across languages. This package contains Regular and Bold
weights for Noto Sans fonts for the four CJK languages.

%package -n google-noto-sans-sc-regular-fonts
Summary:        Noto Sans Simplified Chinese Font - Regular
Group:          System/X11/Fonts
Provides:       noto-sans-sc-regular-fonts = %{version}
Obsoletes:      noto-sans-sc-regular-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-sc-regular-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular weight
of Sans font for Simplified Chinese, hinted.

%package -n google-noto-sans-sc-thin-fonts
Summary:        Noto Sans Simplified Chinese Font - Thin
Group:          System/X11/Fonts
Provides:       noto-sans-sc-thin-fonts = %{version}
Obsoletes:      noto-sans-sc-thin-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-sc-thin-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Thin weight of
Sans font for Simplified Chinese, hinted.

%package -n google-noto-sans-sc-light-fonts
Summary:        Noto Sans Simplified Chinese Font - Light
Group:          System/X11/Fonts
Provides:       noto-sans-sc-light-fonts = %{version}
Obsoletes:      noto-sans-sc-light-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-sc-light-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Light weight of
Sans font for Simplified Chinese, hinted.

%package -n google-noto-sans-sc-demilight-fonts
Summary:        Noto Sans Simplified Chinese Font - DemiLight
Group:          System/X11/Fonts
Provides:       noto-sans-sc-demilight-fonts = %{version}
Obsoletes:      noto-sans-sc-demilight-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-sc-demilight-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Demilight weight
of Sans font for Simplified Chinese, hinted.

%package -n google-noto-sans-sc-bold-fonts
Summary:        Noto Sans Simplified Chinese Font - Bold
Group:          System/X11/Fonts
Provides:       noto-sans-sc-bold-fonts = %{version}
Obsoletes:      noto-sans-sc-bold-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-sc-bold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Bold weight of
Sans font for Simplified Chinese, hinted.

%package -n google-noto-sans-sc-black-fonts
Summary:        Noto Sans Simplified Chinese Font - Black
Group:          System/X11/Fonts
Provides:       noto-sans-sc-black-fonts = %{version}
Obsoletes:      noto-sans-sc-black-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-sc-black-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Black weight of
Sans font for Simplified Chinese, hinted.

%package -n google-noto-sans-sc-medium-fonts
Summary:        Noto Sans Simplified Chinese Font - Medium
Group:          System/X11/Fonts
Provides:       noto-sans-sc-medium-fonts = %{version}
Obsoletes:      noto-sans-sc-medium-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-sc-medium-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Medium weight of
Sans font for Simplified Chinese, hinted.

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
Summary:        Noto Sans Simplified Chinese Font - Regular and Bold
Group:          System/X11/Fonts
Provides:       noto-sans-cjksc = %{version}
Obsoletes:      noto-sans-cjksc <= %{version}
Provides:       noto-sans-cjksc-fonts = %{version}
Obsoletes:      noto-sans-cjksc-fonts <= %{version}
Provides:       noto-sans-sc-fonts = %{version}
Obsoletes:      noto-sans-sc-fonts <= %{version}
Provides:       scalable-font-zh-CN
Provides:       scalable-font-zh-SG
Provides:       locale(zh_CN;zh_SG)
Requires:       google-noto-sans-sc-bold-fonts = %{version}
Requires:       google-noto-sans-sc-regular-fonts = %{version}

%description -n google-noto-sans-sc-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular and Bold
weights of Sans font for Simplified Chinese, hinted.

%package -n google-noto-sans-sc-fonts-full
Summary:        Noto Sans Simplified Chinese Font - All Weights
Group:          System/X11/Fonts
Provides:       noto-sans-sc-fonts-full = %{version}
Obsoletes:      noto-sans-sc-fonts-full <= %{version}
Requires:       google-noto-sans-sc-black-fonts = %{version}
Requires:       google-noto-sans-sc-demilight-fonts = %{version}
Requires:       google-noto-sans-sc-fonts = %{version}
Requires:       google-noto-sans-sc-light-fonts = %{version}
Requires:       google-noto-sans-sc-medium-fonts = %{version}
Requires:       google-noto-sans-sc-thin-fonts = %{version}

%description -n google-noto-sans-sc-fonts-full
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains All weights for
Sans fonts for Simplified Chinese, hinted.

%package -n google-noto-sans-tc-regular-fonts
Summary:        Noto Sans Traditional Chinese Font - Regular
Group:          System/X11/Fonts
Provides:       noto-sans-tc-regular-fonts = %{version}
Obsoletes:      noto-sans-tc-regular-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tc-regular-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular weight
of Sans font for Traditional Chinese, hinted.

%package -n google-noto-sans-tc-thin-fonts
Summary:        Noto Sans Traditional Chinese Font - Thin
Group:          System/X11/Fonts
Provides:       noto-sans-tc-thin-fonts = %{version}
Obsoletes:      noto-sans-tc-thin-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tc-thin-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Thin weight of
Sans font for Traditional Chinese, hinted.

%package -n google-noto-sans-tc-light-fonts
Summary:        Noto Sans Traditional Chinese Font - Light
Group:          System/X11/Fonts
Provides:       noto-sans-tc-light-fonts = %{version}
Obsoletes:      noto-sans-tc-light-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tc-light-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Light weight of
Sans font for Traditional Chinese, hinted.

%package -n google-noto-sans-tc-demilight-fonts
Summary:        Noto Sans Traditional Chinese Font - DemiLight
Group:          System/X11/Fonts
Provides:       noto-sans-tc-demilight-fonts = %{version}
Obsoletes:      noto-sans-tc-demilight-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tc-demilight-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Demilight weight
of Sans font for Traditional Chinese, hinted.

%package -n google-noto-sans-tc-bold-fonts
Summary:        Noto Sans Traditional Chinese Font - Bold
Group:          System/X11/Fonts
Provides:       noto-sans-tc-bold-fonts = %{version}
Obsoletes:      noto-sans-tc-bold-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tc-bold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Bold weight of
Sans font for Traditional Chinese, hinted.

%package -n google-noto-sans-tc-black-fonts
Summary:        Noto Sans Traditional Chinese Font - Black
Group:          System/X11/Fonts
Provides:       noto-sans-tc-black-fonts = %{version}
Obsoletes:      noto-sans-tc-black-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tc-black-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Black weight of
Sans font for Traditional Chinese, hinted.

%package -n google-noto-sans-tc-medium-fonts
Summary:        Noto Sans Traditional Chinese Font - Medium
Group:          System/X11/Fonts
Provides:       noto-sans-tc-medium-fonts = %{version}
Obsoletes:      noto-sans-tc-medium-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-tc-medium-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Medium weight of
Sans font for Traditional Chinese, hinted.

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
Summary:        Noto Sans Traditional Chinese Font - Regular and Bold
Group:          System/X11/Fonts
Provides:       noto-sans-cjktc = %{version}
Obsoletes:      noto-sans-cjktc <= %{version}
Provides:       noto-sans-cjktc-fonts = %{version}
Obsoletes:      noto-sans-cjktc-fonts <= %{version}
Provides:       noto-sans-tc-fonts = %{version}
Obsoletes:      noto-sans-tc-fonts <= %{version}
Provides:       scalable-font-zh-TW
Provides:       locale(;zh_TW)
Requires:       google-noto-sans-tc-bold-fonts = %{version}
Requires:       google-noto-sans-tc-regular-fonts = %{version}

%description -n google-noto-sans-tc-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular and Bold
weights of Sans font for Traditional Chinese, hinted.

%package -n google-noto-sans-tc-fonts-full
Summary:        Noto Sans Traditional Chinese Font - All Weights
Group:          System/X11/Fonts
Provides:       noto-sans-tc-fonts-full = %{version}
Obsoletes:      noto-sans-tc-fonts-full <= %{version}
Requires:       google-noto-sans-tc-black-fonts = %{version}
Requires:       google-noto-sans-tc-demilight-fonts = %{version}
Requires:       google-noto-sans-tc-fonts = %{version}
Requires:       google-noto-sans-tc-light-fonts = %{version}
Requires:       google-noto-sans-tc-medium-fonts = %{version}
Requires:       google-noto-sans-tc-thin-fonts = %{version}

%description -n google-noto-sans-tc-fonts-full
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains All weights for
Sans fonts for Traditional Chinese, hinted.

%package -n google-noto-sans-hk-regular-fonts
Summary:        Noto Sans Traditional Chinese (Hong Kong) Font - Regular
Group:          System/X11/Fonts
Provides:       noto-sans-hk-regular-fonts = %{version}
Obsoletes:      noto-sans-hk-regular-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-hk-regular-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular weight
of Sans font for Traditional Chinese (Hong Kong), hinted.

%package -n google-noto-sans-hk-thin-fonts
Summary:        Noto Sans Traditional Chinese (Hong Kong) Font - Thin
Group:          System/X11/Fonts
Provides:       noto-sans-hk-thin-fonts = %{version}
Obsoletes:      noto-sans-hk-thin-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-hk-thin-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Thin weight of
Sans font for Traditional Chinese (Hong Kong), hinted.

%package -n google-noto-sans-hk-light-fonts
Summary:        Noto Sans Traditional Chinese (Hong Kong) Font - Light
Group:          System/X11/Fonts
Provides:       noto-sans-hk-light-fonts = %{version}
Obsoletes:      noto-sans-hk-light-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-hk-light-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Light weight of
Sans font for Traditional Chinese (Hong Kong), hinted.

%package -n google-noto-sans-hk-demilight-fonts
Summary:        Noto Sans Traditional Chinese (Hong Kong) Font - DemiLight
Provides:       noto-sans-hk-demilight-fonts = %{version}
Obsoletes:      noto-sans-hk-demilight-fonts <= %{version}
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n google-noto-sans-hk-demilight-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Demilight weight
of Sans font for Traditional Chinese (Hong Kong), hinted.

%package -n google-noto-sans-hk-bold-fonts
Summary:        Noto Sans Traditional Chinese (Hong Kong) Font - Bold
Group:          System/X11/Fonts
Provides:       noto-sans-hk-bold-fonts = %{version}
Obsoletes:      noto-sans-hk-bold-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-hk-bold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Bold weight of
Sans font for Traditional Chinese (Hong Kong), hinted.

%package -n google-noto-sans-hk-black-fonts
Summary:        Noto Sans Traditional Chinese (Hong Kong) Font - Black
Group:          System/X11/Fonts
Provides:       noto-sans-hk-black-fonts = %{version}
Obsoletes:      noto-sans-hk-black-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-hk-black-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Black weight of
Sans font for Traditional Chinese (Hong Kong), hinted.

%package -n google-noto-sans-hk-medium-fonts
Summary:        Noto Sans Traditional Chinese (Hong Kong) Font - Medium
Group:          System/X11/Fonts
Provides:       noto-sans-hk-medium-fonts = %{version}
Obsoletes:      noto-sans-hk-medium-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-hk-medium-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Medium weight of
Sans font for Traditional Chinese (Hong Kong), hinted.

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
Summary:        Noto Sans Traditional Chinese (Hong Kong) Font - Regular and Bold
Group:          System/X11/Fonts
Provides:       noto-sans-cjkhk = %{version}
Obsoletes:      noto-sans-cjkhk <= %{version}
Provides:       noto-sans-cjkhk-fonts = %{version}
Obsoletes:      noto-sans-cjkhk-fonts <= %{version}
Provides:       noto-sans-hk-fonts = %{version}
Obsoletes:      noto-sans-hk-fonts <= %{version}
Provides:       scalable-font-zh-HK
Provides:       scalable-font-zh-MO
Provides:       locale(zh_HK;zh_MO)
Requires:       google-noto-sans-hk-bold-fonts = %{version}
Requires:       google-noto-sans-hk-regular-fonts = %{version}

%description -n google-noto-sans-hk-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular and Bold
weights of Sans font for Traditional Chinese (Hong Kong), hinted.

%package -n google-noto-sans-hk-fonts-full
Summary:        Noto Sans Traditional Chinese (Hong Kong) Font - All Weights
Group:          System/X11/Fonts
Provides:       noto-sans-hk-fonts-full = %{version}
Obsoletes:      noto-sans-hk-fonts-full <= %{version}
Requires:       google-noto-sans-hk-black-fonts = %{version}
Requires:       google-noto-sans-hk-demilight-fonts = %{version}
Requires:       google-noto-sans-hk-fonts = %{version}
Requires:       google-noto-sans-hk-light-fonts = %{version}
Requires:       google-noto-sans-hk-medium-fonts = %{version}
Requires:       google-noto-sans-hk-thin-fonts = %{version}

%description -n google-noto-sans-hk-fonts-full
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains All weights for
Sans fonts for Traditional Chinese (Hong Kong), hinted.

%package -n google-noto-sans-jp-regular-fonts
Summary:        Noto Sans Japanese Font - Regular
Group:          System/X11/Fonts
Provides:       noto-sans-jp-regular-fonts = %{version}
Obsoletes:      noto-sans-jp-regular-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-jp-regular-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular weight
of Sans font for Japanese, hinted.

%package -n google-noto-sans-jp-thin-fonts
Summary:        Noto Sans Japanese Font - Thin
Group:          System/X11/Fonts
Provides:       noto-sans-jp-thin-fonts = %{version}
Obsoletes:      noto-sans-jp-thin-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-jp-thin-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Thin weight of
Sans font for Japanese, hinted.

%package -n google-noto-sans-jp-light-fonts
Summary:        Noto Sans Japanese Font - Light
Group:          System/X11/Fonts
Provides:       noto-sans-jp-light-fonts = %{version}
Obsoletes:      noto-sans-jp-light-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-jp-light-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Light weight of
Sans font for Japanese, hinted.

%package -n google-noto-sans-jp-demilight-fonts
Summary:        Noto Sans Japanese Font - DemiLight
Group:          System/X11/Fonts
Provides:       noto-sans-jp-demilight-fonts = %{version}
Obsoletes:      noto-sans-jp-demilight-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-jp-demilight-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Demilight weight
of Sans font for Japanese, hinted.

%package -n google-noto-sans-jp-bold-fonts
Summary:        Noto Sans Japanese Font - Bold
Group:          System/X11/Fonts
Provides:       noto-sans-jp-bold-fonts = %{version}
Obsoletes:      noto-sans-jp-bold-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-jp-bold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Bold weight of
Sans font for Japanese, hinted.

%package -n google-noto-sans-jp-black-fonts
Summary:        Noto Sans Japanese Font - Black
Group:          System/X11/Fonts
Provides:       noto-sans-jp-black-fonts = %{version}
Obsoletes:      noto-sans-jp-black-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-jp-black-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Black weight of
Sans font for Japanese, hinted.

%package -n google-noto-sans-jp-medium-fonts
Summary:        Noto Sans Japanese Font - Medium
Group:          System/X11/Fonts
Provides:       noto-sans-jp-medium-fonts = %{version}
Obsoletes:      noto-sans-jp-medium-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-jp-medium-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Medium weight of
Sans font for Japanese, hinted.

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
Summary:        Noto Sans Japanese Font - Regular and Bold
Group:          System/X11/Fonts
Provides:       noto-sans-cjkjp = %{version}
Obsoletes:      noto-sans-cjkjp <= %{version}
Provides:       noto-sans-cjkjp-fonts = %{version}
Obsoletes:      noto-sans-cjkjp-fonts <= %{version}
Provides:       noto-sans-jp-fonts = %{version}
Obsoletes:      noto-sans-jp-fonts <= %{version}
Provides:       scalable-font-ja
Provides:       locale(ja)
Requires:       google-noto-sans-jp-bold-fonts = %{version}
Requires:       google-noto-sans-jp-regular-fonts = %{version}

%description -n google-noto-sans-jp-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular and Bold
weights of Sans font for Japanese, hinted.

%package -n google-noto-sans-jp-fonts-full
Summary:        Noto Sans Japanese Font - All Weights
Group:          System/X11/Fonts
Provides:       noto-sans-jp-fonts-full = %{version}
Obsoletes:      noto-sans-jp-fonts-full <= %{version}
Requires:       google-noto-sans-jp-black-fonts = %{version}
Requires:       google-noto-sans-jp-demilight-fonts = %{version}
Requires:       google-noto-sans-jp-fonts = %{version}
Requires:       google-noto-sans-jp-light-fonts = %{version}
Requires:       google-noto-sans-jp-medium-fonts = %{version}
Requires:       google-noto-sans-jp-thin-fonts = %{version}

%description -n google-noto-sans-jp-fonts-full
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains All weights for
Sans fonts for Japanese, hinted.

%package -n google-noto-sans-kr-regular-fonts
Summary:        Noto Sans Korean Font - Regular
Group:          System/X11/Fonts
Provides:       noto-sans-kr-regular-fonts = %{version}
Obsoletes:      noto-sans-kr-regular-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-kr-regular-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular weight
of Sans font for Korean, hinted.

%package -n google-noto-sans-kr-thin-fonts
Summary:        Noto Sans Korean Font - Thin
Group:          System/X11/Fonts
Provides:       noto-sans-kr-thin-fonts = %{version}
Obsoletes:      noto-sans-kr-thin-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-kr-thin-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Thin weight of
Sans font for Korean, hinted.

%package -n google-noto-sans-kr-light-fonts
Summary:        Noto Sans Korean Font - Light
Group:          System/X11/Fonts
Provides:       noto-sans-kr-light-fonts = %{version}
Obsoletes:      noto-sans-kr-light-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-kr-light-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Light weight of
Sans font for Korean, hinted.

%package -n google-noto-sans-kr-demilight-fonts
Summary:        Noto Sans Korean Font - DemiLight
Group:          System/X11/Fonts
Provides:       noto-sans-kr-demilight-fonts = %{version}
Obsoletes:      noto-sans-kr-demilight-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-kr-demilight-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Demilight weight
of Sans font for Korean, hinted.

%package -n google-noto-sans-kr-bold-fonts
Summary:        Noto Sans Korean Font - Bold
Group:          System/X11/Fonts
Provides:       noto-sans-kr-bold-fonts = %{version}
Obsoletes:      noto-sans-kr-bold-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-kr-bold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Bold weight of
Sans font for Korean, hinted.

%package -n google-noto-sans-kr-black-fonts
Summary:        Noto Sans Korean Font - Black
Group:          System/X11/Fonts
Provides:       noto-sans-kr-black-fonts = %{version}
Obsoletes:      noto-sans-kr-black-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-kr-black-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Black weight of
Sans font for Korean, hinted.

%package -n google-noto-sans-kr-medium-fonts
Summary:        Noto Sans Korean Font - Medium
Group:          System/X11/Fonts
Provides:       noto-sans-kr-medium-fonts = %{version}
Obsoletes:      noto-sans-kr-medium-fonts <= %{version}
%reconfigure_fonts_prereq

%description -n google-noto-sans-kr-medium-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Medium weight of
Sans font for Korean, hinted.

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
Summary:        Noto Sans Korean Font - Regular and Bold
Group:          System/X11/Fonts
Provides:       noto-sans-cjkkr = %{version}
Obsoletes:      noto-sans-cjkkr <= %{version}
Provides:       noto-sans-cjkkr-fonts = %{version}
Obsoletes:      noto-sans-cjkkr-fonts <= %{version}
Provides:       noto-sans-kr-fonts = %{version}
Obsoletes:      noto-sans-kr-fonts <= %{version}
Provides:       scalable-font-ko
Provides:       locale(ko)
Requires:       google-noto-sans-kr-bold-fonts = %{version}
Requires:       google-noto-sans-kr-regular-fonts = %{version}

%description -n google-noto-sans-kr-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains Regular and Bold
weights of Sans font for Korean, hinted.

%package -n google-noto-sans-kr-fonts-full
Summary:        Noto Sans Korean Font - All Weights
Group:          System/X11/Fonts
Provides:       noto-sans-kr-fonts-full = %{version}
Obsoletes:      noto-sans-kr-fonts-full <= %{version}
Requires:       google-noto-sans-kr-black-fonts = %{version}
Requires:       google-noto-sans-kr-demilight-fonts = %{version}
Requires:       google-noto-sans-kr-fonts = %{version}
Requires:       google-noto-sans-kr-light-fonts = %{version}
Requires:       google-noto-sans-kr-medium-fonts = %{version}
Requires:       google-noto-sans-kr-thin-fonts = %{version}

%description -n google-noto-sans-kr-fonts-full
Noto's design goal is to achieve visual harmonization (e.g., compatible heights
and stroke thicknesses) across languages. This package contains All weights for
Sans fonts for Korean, hinted.

%prep
unzip -qqn %{SOURCE0}
unzip -qqn %{SOURCE1}
unzip -qqn %{SOURCE2}
unzip -qqn %{SOURCE3}
unzip -qqn %{SOURCE4}
unzip -qqn %{SOURCE5}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
cp *.?tf %{buildroot}%{_ttfontsdir}/
cp */*/*.?tf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets -n google-noto-sans-sc-regular-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-sc-thin-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-sc-medium-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-sc-light-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-sc-demilight-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-sc-bold-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-sc-black-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-sc-mono-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tc-regular-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tc-thin-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tc-medium-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tc-light-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tc-demilight-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tc-bold-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tc-black-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-tc-mono-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-hk-regular-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-hk-thin-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-hk-medium-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-hk-light-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-hk-demilight-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-hk-bold-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-hk-black-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-hk-mono-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-jp-regular-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-jp-thin-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-jp-medium-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-jp-light-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-jp-demilight-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-jp-bold-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-jp-black-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-jp-mono-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kr-regular-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kr-thin-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kr-medium-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kr-light-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kr-demilight-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kr-bold-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kr-black-fonts

%reconfigure_fonts_scriptlets -n google-noto-sans-kr-mono-fonts

%files
%defattr(0644,root,root,755)
%license LICENSE

%files -n google-noto-sans-sc-regular-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKsc-Regular.?tf

%files -n google-noto-sans-sc-thin-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKsc-Thin.?tf

%files -n google-noto-sans-sc-medium-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKsc-Medium.?tf

%files -n google-noto-sans-sc-light-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKsc-Light.?tf

%files -n google-noto-sans-sc-demilight-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKsc-DemiLight.?tf

%files -n google-noto-sans-sc-bold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKsc-Bold.?tf

%files -n google-noto-sans-sc-black-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKsc-Black.?tf

%files -n google-noto-sans-sc-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKsc-*.?tf

%files -n google-noto-sans-sc-fonts
%defattr(0644,root,root,755)
%license LICENSE

%files -n google-noto-sans-sc-fonts-full
%defattr(0644,root,root,755)
%license LICENSE

%files -n google-noto-sans-tc-regular-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKtc-Regular.?tf

%files -n google-noto-sans-tc-thin-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKtc-Thin.?tf

%files -n google-noto-sans-tc-medium-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKtc-Medium.?tf

%files -n google-noto-sans-tc-light-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKtc-Light.?tf

%files -n google-noto-sans-tc-demilight-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKtc-DemiLight.?tf

%files -n google-noto-sans-tc-bold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKtc-Bold.?tf

%files -n google-noto-sans-tc-black-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKtc-Black.?tf

%files -n google-noto-sans-tc-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKtc-*.?tf

%files -n google-noto-sans-tc-fonts
%defattr(0644,root,root,755)
%license LICENSE

%files -n google-noto-sans-tc-fonts-full
%defattr(0644,root,root,755)
%license LICENSE

%files -n google-noto-sans-hk-regular-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKhk-Regular.?tf

%files -n google-noto-sans-hk-thin-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKhk-Thin.?tf

%files -n google-noto-sans-hk-medium-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKhk-Medium.?tf

%files -n google-noto-sans-hk-light-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKhk-Light.?tf

%files -n google-noto-sans-hk-demilight-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKhk-DemiLight.?tf

%files -n google-noto-sans-hk-bold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKhk-Bold.?tf

%files -n google-noto-sans-hk-black-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKhk-Black.?tf

%files -n google-noto-sans-hk-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKhk-*.?tf

%files -n google-noto-sans-hk-fonts
%defattr(0644,root,root,755)
%license LICENSE

%files -n google-noto-sans-hk-fonts-full
%defattr(0644,root,root,755)
%license LICENSE

%files -n google-noto-sans-jp-regular-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKjp-Regular.?tf

%files -n google-noto-sans-jp-thin-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKjp-Thin.?tf

%files -n google-noto-sans-jp-medium-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKjp-Medium.?tf

%files -n google-noto-sans-jp-light-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKjp-Light.?tf

%files -n google-noto-sans-jp-demilight-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKjp-DemiLight.?tf

%files -n google-noto-sans-jp-bold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKjp-Bold.?tf

%files -n google-noto-sans-jp-black-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKjp-Black.?tf

%files -n google-noto-sans-jp-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKjp-*.?tf

%files -n google-noto-sans-jp-fonts
%defattr(0644,root,root,755)
%license LICENSE

%files -n google-noto-sans-jp-fonts-full
%defattr(0644,root,root,755)
%license LICENSE

%files -n google-noto-sans-kr-regular-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKkr-Regular.?tf

%files -n google-noto-sans-kr-thin-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKkr-Thin.?tf

%files -n google-noto-sans-kr-medium-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKkr-Medium.?tf

%files -n google-noto-sans-kr-light-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKkr-Light.?tf

%files -n google-noto-sans-kr-demilight-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKkr-DemiLight.?tf

%files -n google-noto-sans-kr-bold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKkr-Bold.?tf

%files -n google-noto-sans-kr-black-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansCJKkr-Black.?tf

%files -n google-noto-sans-kr-mono-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSansMonoCJKkr-*.?tf

%files -n google-noto-sans-kr-fonts
%defattr(0644,root,root,755)
%license LICENSE

%files -n google-noto-sans-kr-fonts-full
%defattr(0644,root,root,755)
%license LICENSE

%changelog
