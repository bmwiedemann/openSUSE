#
# spec file for package arphic-fonts
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


Name:           arphic-fonts
Version:        20001125
Release:        0
Summary:        Chinese TrueType Fonts (Contains Only the License Text)
License:        Arphic-1999
Group:          System/X11/Fonts
URL:            https://www.arphic.com.tw/
# ttf files have been downloaded from debian.
Source0:        ttf-arphic.tar.bz2
Source1:        fonts.scale.bkai00mp
Source2:        fonts.scale.bsmi00lp
Source3:        fonts.scale.gkai00mp
Source4:        fonts.scale.gbsn00lp
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       ttf-arphic = %{version}
Obsoletes:      ttf-arphic <= 20001125
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Chinese TrueType fonts by Arphic Technology. This package contains only
the license texts. The fonts themselves are in the sub-packages
arphic-bkai00mp-fonts, arphic-bsmi00lp-fonts, arphic-gkai00mp-fonts, and
arphic-gbsn00lp-fonts.

%package -n arphic-bkai00mp-fonts
Summary:        AR PL KaitiM Big5 Chinese TrueType font by Arphic Technology
Group:          System/X11/Fonts
Requires:       arphic-fonts
Provides:       ttf-arphic-bkai00mp = %{version}
Obsoletes:      ttf-arphic-bkai00mp <= 20001125

%description -n arphic-bkai00mp-fonts
AR PL KaitiM Big5 is a high quality Chinese TrueType font
(bkai00mp.ttf) generously provided by Arphic Technology to the Free
Software community under the Arphic Public License.

%package -n arphic-bsmi00lp-fonts
Summary:        AR PL Mingti2L Big5 Chinese TrueType font by Arphic Technology
Group:          System/X11/Fonts
Requires:       arphic-fonts
Provides:       ttf-arphic-bsmi00lp = %{version}
Obsoletes:      ttf-arphic-bsmi00lp <= 20001125

%description -n arphic-bsmi00lp-fonts
AR PL Mingti2L Big5 is a high quality Chinese TrueType font
(bsmi00lp.ttf) generously provided by Arphic Technology to the Free
Software community under the Arphic Public License.

%package -n arphic-gkai00mp-fonts
Summary:        AR PL KaitiM GB Chinese TrueType font by Arphic Technology
Group:          System/X11/Fonts
Requires:       arphic-fonts
Provides:       ttf-arphic-gkai00mp = %{version}
Obsoletes:      ttf-arphic-gkai00mp <= 20001125

%description -n arphic-gkai00mp-fonts
AR PL KaitiM GB is a high quality Chinese TrueType font (gkai00mp.ttf)
generously provided by Arphic Technology to the Free Software community
under the Arphic Public License.

%package -n arphic-gbsn00lp-fonts
Summary:        AR PL SungtiL GB Chinese TrueType font by Arphic Technology
Group:          System/X11/Fonts
Requires:       arphic-fonts
Provides:       ttf-arphic-gbsn00lp = %{version}
Obsoletes:      ttf-arphic-gbsn00lp <= 20001125

%description -n arphic-gbsn00lp-fonts
AR PL SungtiL GB is a high quality Chinese TrueType font (gbsn00lp.ttf)
generously provided by Arphic Technology to the Free Software community
under the Arphic Public License.

%prep
%setup -n ttf-arphic
cp $RPM_SOURCE_DIR/fonts.scale* .

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}/
install -c -m 644 fonts.scale.* %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets -c -n arphic-bkai00mp-fonts

%reconfigure_fonts_scriptlets -c -n arphic-bsmi00lp-fonts

%reconfigure_fonts_scriptlets -c -n arphic-gkai00mp-fonts

%reconfigure_fonts_scriptlets -c -n arphic-gbsn00lp-fonts

%files
%defattr(-, root,root)
%doc ./license

%files -n arphic-bkai00mp-fonts
%defattr(-, root,root)
%dir %{_ttfontsdir}/
%{_ttfontsdir}/bkai00mp.ttf
%config %{_ttfontsdir}/fonts.scale.bkai00mp

%files -n arphic-bsmi00lp-fonts
%defattr(-, root,root)
%dir %{_ttfontsdir}/
%{_ttfontsdir}/bsmi00lp.ttf
%config %{_ttfontsdir}/fonts.scale.bsmi00lp

%files -n arphic-gkai00mp-fonts
%defattr(-, root,root)
%dir %{_ttfontsdir}/
%{_ttfontsdir}/gkai00mp.ttf
%config %{_ttfontsdir}/fonts.scale.gkai00mp

%files -n arphic-gbsn00lp-fonts
%defattr(-, root,root)
%dir %{_ttfontsdir}/
%{_ttfontsdir}/gbsn00lp.ttf
%config %{_ttfontsdir}/fonts.scale.gbsn00lp

%changelog
