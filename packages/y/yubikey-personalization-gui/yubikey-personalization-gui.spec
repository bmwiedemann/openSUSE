#
# spec file for package yubikey-personalization-gui
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yubikey-personalization-gui
Version:        3.1.25
Release:        0
Summary:        GUI for Yubikey personalization
License:        BSD-2-Clause
Group:          Productivity/Networking/Security
Url:            https://developers.yubico.com/
Source0:        https://developers.yubico.com/yubikey-personalization-gui/Releases/%{name}-%{version}.tar.gz
Source1:        https://developers.yubico.com/yubikey-personalization-gui/Releases/%{name}-%{version}.tar.gz.sig
BuildRequires:  desktop-file-utils
BuildRequires:  libykpers-devel => 1.14
BuildRequires:  libyubikey-devel => 1.12
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       ykpers >= 1.14

%description
The YubiKey Personalization Tool is a Qt based Cross-Platform utility
designed to facilitate re-configuration of YubiKeys on Windows, Linux
and MAC platforms. The tool provides a same simple step-by-step
approach to make configuration of YubiKeys easy to follow and
understand, while still being powerful enough to exploit all
functionality both of the YubiKey 1 and YubiKey 2 generation of
keys. The tool provides the same functionality and user interface on
Windows, Linux and MAC platforms.

The Cross-Platform YubiKey Personalization Tool provides the following
main functions:

	* Programming the YubiKey in "Yubico OTP" mode
	* Programming the YubiKey in "OATH-HOTP" mode
	* Programming the YubiKey in "Static Password" mode
	* Programming the YubiKey in "Challenge-Response" mode
	* Programming the NDEF feature of the YubiKey NEO
	* Testing the challenge-response functionality of a YubiKey
	* Deleting the configuration of a YubiKey
	* Checking type and firmware version of the YubiKey

%prep
%setup -q 

%build
qmake-qt5 CONFIG+="nosilent c++11" QMAKE_CXXFLAGS="%optflags -fvisibility=hidden -fvisibility-inlines-hidden"
make %{?_smp_mflags} 

%install
install -D -p -m 0755 build/release/%{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 resources/lin/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
mkdir -p %{buildroot}/%{_datadir}/pixmaps
install -p -m 0644 resources/lin/%{name}.xpm %{buildroot}/%{_datadir}/pixmaps/
%suse_update_desktop_file -i %{name} System Security

%files
%defattr(-,root,root)
%doc NEWS README COPYING ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/%{name}.1*

%changelog
