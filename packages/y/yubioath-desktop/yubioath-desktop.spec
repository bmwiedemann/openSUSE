#
# spec file for package yubioath-desktop
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


%define binname yubioath
Name:           yubioath-desktop
Version:        5.1.0
Release:        0
Summary:        Graphical interface for displaying OATH codes with a Yubikey
License:        Apache-2.0 AND GPL-3.0-or-later
Group:          Productivity/Security
URL:            https://developers.yubico.com/yubioath-desktop/
Source0:        https://developers.yubico.com/yubioath-desktop/Releases/%{name}-%{version}.tar.gz
Source1:        https://developers.yubico.com/yubioath-desktop/Releases/%{name}-%{version}.tar.gz.sig
Patch0:         yubioath-desktop-gcc13.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libQt5QuickControls2-devel
BuildRequires:  libqt5-qtbase-devel => 5.12
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(python3)
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols2
Requires:       pyotherside
Requires:       yubikey-manager >= 4.0.7

%description
The Yubico Authenticator is a graphical desktop tool for generating
Open AuTHentication (OATH) event-based HOTP and time-based TOTP
one-time password codes, with the help of a Yubikey NEO that protects
the shared secrets.

%prep
%autosetup -n %{name} -p1
sed -i 's|yubikey-manager==|yubikey-manager>=|' requirements.txt
# workaround for the binary-file installation path
sed -i 's|target.path = $$PREFIX/lib|target.path = $$PREFIX/bin|' QZXing/QZXing-components.pri

%build
%qmake5 QMAKE_CFLAGS+="%{optflags}" QMAKE_CXXFLAGS+="%{optflags} -fPIE" QMAKE_LFLAGS+="-pie" QMAKE_STRIP="/bin/true"
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 0644 resources/icons/com.yubico.yubioath.svg %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/applications
install -p -m 0644 resources/com.yubico.yubioath.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/%{name}.desktop System Security
%fdupes %{buildroot}

%files
%license COPYING QZXing/LICENSE
%doc NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/com.yubico.yubioath.svg
%exclude %{_includedir}/*.h

%changelog
