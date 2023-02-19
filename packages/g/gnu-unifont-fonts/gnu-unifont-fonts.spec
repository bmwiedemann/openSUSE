#
# spec file for package gnu-unifont-fonts
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

Name:           gnu-unifont-fonts
Version:        15.0.01
Release:        0
Summary:        GNU Unifont fonts
License:        GPL-2.0-or-later OR OFL-1.1
Group:          System/X11/Fonts
URL:            https://unifoundry.com/unifont.html
Source8:        https://ftp.gnu.org/gnu/unifont/unifont-%{version}/unifont-%{version}.otf
Source9:        https://ftp.gnu.org/gnu/unifont/unifont-%{version}/unifont-%{version}.otf.sig
Source10:       https://ftp.gnu.org/gnu/unifont/unifont-%{version}/unifont_csur-%{version}.otf
Source11:       https://ftp.gnu.org/gnu/unifont/unifont-%{version}/unifont_csur-%{version}.otf.sig
Source12:       https://ftp.gnu.org/gnu/unifont/unifont-%{version}/unifont_jp-%{version}.otf
Source13:       https://ftp.gnu.org/gnu/unifont/unifont-%{version}/unifont_jp-%{version}.otf.sig
Source14:       https://ftp.gnu.org/gnu/unifont/unifont-%{version}/unifont_upper-%{version}.otf
Source15:       https://ftp.gnu.org/gnu/unifont/unifont-%{version}/unifont_upper-%{version}.otf.sig
Source98:       http://unifoundry.com/LICENSE.txt
Source99:       %{name}.keyring
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
The GNU Unifont by Roman Czyborra.
The Standard Unifont OTF.
Glyphs above the Unicode Basic Multilingual Plane.
Unicode ConScript Unicode Registry (CSUR) PUA Glyphs.

%package -n gnu-unifont-otf-fonts
Summary:        GNU Unifont (OpenType Format)
Group:          System/X11/Fonts

%description -n gnu-unifont-otf-fonts
The GNU Unifont by Roman Czyborra.
Glyphs above the Unicode Basic Multilingual Plane.
Unicode ConScript Unicode Registry (CSUR) PUA Glyphs.

This package contains fonts in OpenType format.

%package -n gnu-unifont-jp-otf-fonts
Summary:        GNU Unifont Japanese (OpenType Format)
Group:          System/X11/Fonts

%description -n gnu-unifont-jp-otf-fonts
The GNU Unifont by Roman Czyborra.
Unifont Japanese OpenType Version.

%prep
cp %{SOURCE98} COPYING

%build

%install
install -Dm 0644 %{SOURCE8}  %{buildroot}%{_ttfontsdir}/Unifont.otf
install -Dm 0644 %{SOURCE10} %{buildroot}%{_ttfontsdir}/Unifont_CSUR.otf
install -Dm 0644 %{SOURCE12} %{buildroot}%{_ttfontsdir}/Unifont_JP.otf
install -Dm 0644 %{SOURCE14} %{buildroot}%{_ttfontsdir}/Unifont_Upper.otf

%reconfigure_fonts_scriptlets -n gnu-unifont-otf-fonts
%reconfigure_fonts_scriptlets -n gnu-unifont-jp-otf-fonts

%files -n gnu-unifont-otf-fonts
%license COPYING
%dir %{_ttfontsdir}
%{_ttfontsdir}/Unifont.otf
%{_ttfontsdir}/Unifont_CSUR.otf
%{_ttfontsdir}/Unifont_Upper.otf

%files -n gnu-unifont-jp-otf-fonts
%license COPYING
%dir %{_ttfontsdir}
%{_ttfontsdir}/Unifont_JP.otf

%changelog
