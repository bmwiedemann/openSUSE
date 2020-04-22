#
# spec file for package google-noto-serif-cjk-fonts
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

Name:           google-noto-serif-cjk-fonts
Version:        20170403
Release:        0
Summary:        Noto Serif CJK Font Families
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/googlefonts/noto-cjk
Source0:        https://github.com/googlefonts/noto-cjk/archive/NotoSansV%{_version}.tar.gz
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Noto's design goal is to achieve visual harmonization (e.g., compatible heights and stroke
thicknesses) across languages.

%package -n noto-serif-sc-regular-fonts
Summary:        Noto Serif Simplified Chinese Font - Regular
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-sc-regular-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Regular weight of Serif font for Simplified Chinese, hinted.

%package -n noto-serif-sc-semibold-fonts
Summary:        Noto Serif Simplified Chinese Font - SemiBold
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-sc-semibold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SemiBold weight of Serif font for Simplified Chinese, hinted.

%package -n noto-serif-sc-light-fonts
Summary:        Noto Serif Simplified Chinese Font - Light
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-sc-light-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Light weight of Serif font for Simplified Chinese, hinted.

%package -n noto-serif-sc-extralight-fonts
Summary:        Noto Serif Simplified Chinese Font - Extralight
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-sc-extralight-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Extralight weight of Serif font for Simplified Chinese, hinted.

%package -n noto-serif-sc-bold-fonts
Summary:        Noto Serif Simplified Chinese Font - Bold
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-sc-bold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bold weight of Serif font for Simplified Chinese, hinted.

%package -n noto-serif-sc-black-fonts
Summary:        Noto Serif Simplified Chinese Font - Black
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-sc-black-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Black weight of Serif font for Simplified Chinese, hinted.

%package -n noto-serif-sc-medium-fonts
Summary:        Noto Serif Simplified Chinese Font - Medium
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-sc-medium-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Medium weight of Serif font for Simplified Chinese, hinted.

%package -n noto-serif-sc-fonts
Summary:        Noto Serif Simplified Chinese Font - Regular and Bold
Group:          System/X11/Fonts
Provides:       scalable-font-zh-CN
Provides:       scalable-font-zh-SG
Provides:       locale(zh_CN;zh_SG)
Requires:       noto-serif-sc-bold-fonts = %{version}
Requires:       noto-serif-sc-regular-fonts = %{version}

%description -n noto-serif-sc-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Regular and Bold weights of Serif font for Simplified Chinese, hinted.

%package -n noto-serif-sc-fonts-full
Summary:        Noto Serif Simplified Chinese Font - All Weights
Group:          System/X11/Fonts
Requires:       noto-serif-sc-black-fonts = %{version}
Requires:       noto-serif-sc-extralight-fonts = %{version}
Requires:       noto-serif-sc-fonts = %{version}
Requires:       noto-serif-sc-light-fonts = %{version}
Requires:       noto-serif-sc-medium-fonts = %{version}
Requires:       noto-serif-sc-semibold-fonts = %{version}

%description -n noto-serif-sc-fonts-full
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
All weights of Serif font for Simplified Chinese, hinted.

%package -n noto-serif-tc-regular-fonts
Summary:        Noto Serif Traditional Chinese Font - Regular
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-tc-regular-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Regular weight of Serif font for Traditional Chinese, hinted.

%package -n noto-serif-tc-semibold-fonts
Summary:        Noto Serif Traditional Chinese Font - SemiBold
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-tc-semibold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SemiBold weight of Serif font for Traditional Chinese, hinted.

%package -n noto-serif-tc-light-fonts
Summary:        Noto Serif Traditional Chinese Font - Light
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-tc-light-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Light weight of Serif font for Traditional Chinese, hinted.

%package -n noto-serif-tc-extralight-fonts
Summary:        Noto Serif Traditional Chinese Font - Extralight
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-tc-extralight-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Extralight weight of Serif font for Traditional Chinese, hinted.

%package -n noto-serif-tc-bold-fonts
Summary:        Noto Serif Traditional Chinese Font - Bold
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-tc-bold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bold weight of Serif font for Traditional Chinese, hinted.

%package -n noto-serif-tc-black-fonts
Summary:        Noto Serif Traditional Chinese Font - Black
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-tc-black-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Black weight of Serif font for Traditional Chinese, hinted.

%package -n noto-serif-tc-medium-fonts
Summary:        Noto Serif Traditional Chinese Font - Medium
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-tc-medium-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Medium weight of Serif font for Traditional Chinese, hinted.

%package -n noto-serif-tc-fonts
Summary:        Noto Serif Traditional Chinese Font - Regular and Bold
Group:          System/X11/Fonts
Provides:       scalable-font-zh-HK
Provides:       scalable-font-zh-MO
Provides:       scalable-font-zh-TW
Provides:       locale(zh_HK;zh_MO;zh_TW)
Requires:       noto-serif-tc-bold-fonts = %{version}
Requires:       noto-serif-tc-regular-fonts = %{version}

%description -n noto-serif-tc-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Regular and Bold weights of Serif font for Traditional Chinese, hinted.

%package -n noto-serif-tc-fonts-full
Summary:        Noto Serif Traditional Chinese Font - All Weights
Group:          System/X11/Fonts
Requires:       noto-serif-tc-black-fonts = %{version}
Requires:       noto-serif-tc-extralight-fonts = %{version}
Requires:       noto-serif-tc-fonts = %{version}
Requires:       noto-serif-tc-light-fonts = %{version}
Requires:       noto-serif-tc-medium-fonts = %{version}
Requires:       noto-serif-tc-semibold-fonts = %{version}

%description -n noto-serif-tc-fonts-full
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
All weights of Serif font for Traditional Chinese, hinted.

%package -n noto-serif-jp-regular-fonts
Summary:        Noto Serif Japanese Font - Regular
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-jp-regular-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Regular weight of Serif font for Japanese, hinted.

%package -n noto-serif-jp-semibold-fonts
Summary:        Noto Serif Japanese Font - SemiBold
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-jp-semibold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SemiBold weight of Serif font for Japanese, hinted.

%package -n noto-serif-jp-light-fonts
Summary:        Noto Serif Japanese Font - Light
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-jp-light-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Light weight of Serif font for Japanese, hinted.

%package -n noto-serif-jp-extralight-fonts
Summary:        Noto Serif Japanese Font - Extralight
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-jp-extralight-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Extralight weight of Serif font for Japanese, hinted.

%package -n noto-serif-jp-bold-fonts
Summary:        Noto Serif Japanese Font - Bold
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-jp-bold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bold weight of Serif font for Japanese, hinted.

%package -n noto-serif-jp-black-fonts
Summary:        Noto Serif Japanese Font - Black
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-jp-black-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Black weight of Serif font for Japanese, hinted.

%package -n noto-serif-jp-medium-fonts
Summary:        Noto Serif Japanese Font - Medium
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-jp-medium-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Medium weight of Serif font for Japanese, hinted.

%package -n noto-serif-jp-fonts
Summary:        Noto Serif Japanese Font - Regular and Bold
Group:          System/X11/Fonts
Provides:       scalable-font-ja
Provides:       locale(ja)
Requires:       noto-serif-jp-bold-fonts = %{version}
Requires:       noto-serif-jp-regular-fonts = %{version}

%description -n noto-serif-jp-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Regular and Bold weights of Serif font for Japanese, hinted.

%package -n noto-serif-jp-fonts-full
Summary:        Noto Serif Japanese Font - All Weights
Group:          System/X11/Fonts
Requires:       noto-serif-jp-black-fonts = %{version}
Requires:       noto-serif-jp-extralight-fonts = %{version}
Requires:       noto-serif-jp-fonts = %{version}
Requires:       noto-serif-jp-light-fonts = %{version}
Requires:       noto-serif-jp-medium-fonts = %{version}
Requires:       noto-serif-jp-semibold-fonts = %{version}

%description -n noto-serif-jp-fonts-full
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
All weights of Serif font for Japanese, hinted.

%package -n noto-serif-kr-regular-fonts
Summary:        Noto Serif Korean Font - Regular
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-kr-regular-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Regular weight of Serif font for Korean, hinted.

%package -n noto-serif-kr-semibold-fonts
Summary:        Noto Serif Korean Font - SemiBold
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-kr-semibold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
SemiBold weight of Serif font for Korean, hinted.

%package -n noto-serif-kr-light-fonts
Summary:        Noto Serif Korean Font - Light
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-kr-light-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Light weight of Serif font for Korean, hinted.

%package -n noto-serif-kr-extralight-fonts
Summary:        Noto Serif Korean Font - Extralight
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-kr-extralight-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Extralight weight of Serif font for Korean, hinted.

%package -n noto-serif-kr-bold-fonts
Summary:        Noto Serif Korean Font - Bold
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-kr-bold-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Bold weight of Serif font for Korean, hinted.

%package -n noto-serif-kr-black-fonts
Summary:        Noto Serif Korean Font - Black
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-kr-black-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Black weight of Serif font for Korean, hinted.

%package -n noto-serif-kr-medium-fonts
Summary:        Noto Serif Korean Font - Medium
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n noto-serif-kr-medium-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Medium weight of Serif font for Korean, hinted.

%package -n noto-serif-kr-fonts
Summary:        Noto Serif Korean Font - Regular and Bold
Group:          System/X11/Fonts
Provides:       scalable-font-ko
Provides:       locale(ko)
Requires:       noto-serif-kr-bold-fonts = %{version}
Requires:       noto-serif-kr-regular-fonts = %{version}

%description -n noto-serif-kr-fonts
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
Regular and Bold weights of Serif font for Korean, hinted.

%package -n noto-serif-kr-fonts-full
Summary:        Noto Serif Korean Font - All Weights
Group:          System/X11/Fonts
Requires:       noto-serif-kr-black-fonts = %{version}
Requires:       noto-serif-kr-extralight-fonts = %{version}
Requires:       noto-serif-kr-fonts = %{version}
Requires:       noto-serif-kr-light-fonts = %{version}
Requires:       noto-serif-kr-medium-fonts = %{version}
Requires:       noto-serif-kr-semibold-fonts = %{version}

%description -n noto-serif-kr-fonts-full
Noto's design goal is to achieve visual harmonization (e.g., compatible
heights and stroke thicknesses) across languages. This package contains
All weights of Serif font for Korean, hinted.

%prep
%setup -q -n noto-cjk-NotoSansV%{_version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
cp NotoSerifCJK*.?tf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets -n noto-serif-sc-regular-fonts

%reconfigure_fonts_scriptlets -n noto-serif-sc-bold-fonts

%reconfigure_fonts_scriptlets -n noto-serif-sc-semibold-fonts

%reconfigure_fonts_scriptlets -n noto-serif-sc-light-fonts

%reconfigure_fonts_scriptlets -n noto-serif-sc-extralight-fonts

%reconfigure_fonts_scriptlets -n noto-serif-sc-black-fonts

%reconfigure_fonts_scriptlets -n noto-serif-sc-medium-fonts

%reconfigure_fonts_scriptlets -n noto-serif-tc-regular-fonts

%reconfigure_fonts_scriptlets -n noto-serif-tc-bold-fonts

%reconfigure_fonts_scriptlets -n noto-serif-tc-semibold-fonts

%reconfigure_fonts_scriptlets -n noto-serif-tc-light-fonts

%reconfigure_fonts_scriptlets -n noto-serif-tc-extralight-fonts

%reconfigure_fonts_scriptlets -n noto-serif-tc-black-fonts

%reconfigure_fonts_scriptlets -n noto-serif-tc-medium-fonts

%reconfigure_fonts_scriptlets -n noto-serif-jp-regular-fonts

%reconfigure_fonts_scriptlets -n noto-serif-jp-bold-fonts

%reconfigure_fonts_scriptlets -n noto-serif-jp-semibold-fonts

%reconfigure_fonts_scriptlets -n noto-serif-jp-light-fonts

%reconfigure_fonts_scriptlets -n noto-serif-jp-extralight-fonts

%reconfigure_fonts_scriptlets -n noto-serif-jp-black-fonts

%reconfigure_fonts_scriptlets -n noto-serif-jp-medium-fonts

%reconfigure_fonts_scriptlets -n noto-serif-kr-regular-fonts

%reconfigure_fonts_scriptlets -n noto-serif-kr-bold-fonts

%reconfigure_fonts_scriptlets -n noto-serif-kr-semibold-fonts

%reconfigure_fonts_scriptlets -n noto-serif-kr-light-fonts

%reconfigure_fonts_scriptlets -n noto-serif-kr-extralight-fonts

%reconfigure_fonts_scriptlets -n noto-serif-kr-black-fonts

%reconfigure_fonts_scriptlets -n noto-serif-kr-medium-fonts

%files -n noto-serif-sc-regular-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKsc-Regular.?tf

%files -n noto-serif-sc-bold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKsc-Bold.?tf

%files -n noto-serif-sc-semibold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKsc-SemiBold.?tf

%files -n noto-serif-sc-light-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKsc-Light.?tf

%files -n noto-serif-sc-extralight-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKsc-ExtraLight.?tf

%files -n noto-serif-sc-black-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKsc-Black.?tf

%files -n noto-serif-sc-medium-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKsc-Medium.?tf

%files -n noto-serif-sc-fonts
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-serif-sc-fonts-full
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-serif-tc-regular-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKtc-Regular.?tf

%files -n noto-serif-tc-bold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKtc-Bold.?tf

%files -n noto-serif-tc-semibold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKtc-SemiBold.?tf

%files -n noto-serif-tc-light-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKtc-Light.?tf

%files -n noto-serif-tc-extralight-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKtc-ExtraLight.?tf

%files -n noto-serif-tc-black-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKtc-Black.?tf

%files -n noto-serif-tc-medium-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKtc-Medium.?tf

%files -n noto-serif-tc-fonts
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-serif-tc-fonts-full
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-serif-jp-regular-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKjp-Regular.?tf

%files -n noto-serif-jp-bold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKjp-Bold.?tf

%files -n noto-serif-jp-semibold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKjp-SemiBold.?tf

%files -n noto-serif-jp-light-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKjp-Light.?tf

%files -n noto-serif-jp-extralight-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKjp-ExtraLight.?tf

%files -n noto-serif-jp-black-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKjp-Black.?tf

%files -n noto-serif-jp-medium-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKjp-Medium.?tf

%files -n noto-serif-jp-fonts
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-serif-jp-fonts-full
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-serif-kr-regular-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKkr-Regular.?tf

%files -n noto-serif-kr-bold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKkr-Bold.?tf

%files -n noto-serif-kr-semibold-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKkr-SemiBold.?tf

%files -n noto-serif-kr-light-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKkr-Light.?tf

%files -n noto-serif-kr-extralight-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKkr-ExtraLight.?tf

%files -n noto-serif-kr-black-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKkr-Black.?tf

%files -n noto-serif-kr-medium-fonts
%defattr(0644,root,root,755)
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoSerifCJKkr-Medium.?tf

%files -n noto-serif-kr-fonts
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%files -n noto-serif-kr-fonts-full
%defattr(0644,root,root,755)
%doc NEWS HISTORY README.formats README.third_party
%license LICENSE

%changelog
