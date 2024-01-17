#
# spec file for package usbauth-notifier
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2017-2018 Stefan Koch <stefan.koch10@gmail.com>
# Copyright (c) 2015 SUSE LLC. All Rights Reserved.
# Author: Stefan Koch <skoch@suse.de>
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


%define _name   usbauth-all
Name:           usbauth-notifier
Version:        1.0.4
Release:        0
Summary:        Notifier for USB Firewall to use with desktop environments
License:        GPL-2.0-only
Group:          System/X11/Utilities
URL:            https://github.com/kochstefan/usbauth-all/
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Requires(pre):  permissions
Requires:       usbauth
BuildRequires:  gettext-runtime
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  libusbauth-configparser-devel
BuildRequires:  permissions
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libudev)

%description
A notifier for the usbauth firewall against BadUSB attacks. The user could manually allow or deny USB devices.

%lang_package

%prep
%setup -q -n %{_name}-%{version}

%build
cd %{name}
autoreconf -f -i
%configure
%make_build

%pre
if ! getent group usbauth>/dev/null; then groupadd -r usbauth; fi
if ! getent group usbauth-notifier>/dev/null; then groupadd -r usbauth-notifier; fi

%install
%make_install -C %{name}
%find_lang %{name}

%files
%doc %{name}/README %{name}/CHANGELOG.md
%license %{name}/COPYING
%dir /etc/xdg/autostart
/etc/xdg/autostart/usbauth-notifier.desktop
%verify(not mode) %attr(04750,root,usbauth) %{_libexecdir}/usbauth-npriv
%dir %verify(not mode) %attr(00750,root,usbauth-notifier) %{_libexecdir}/usbauth-notifier
%verify(not mode) %attr(02755,root,usbauth) %{_libexecdir}/usbauth-notifier/usbauth-notifier
%_mandir/man1/usbauth-notifier.1*
%_mandir/man1/usbauth-npriv.1*

%files lang -f %{name}.lang

%post
%set_permissions %{_libexecdir}/usbauth-npriv %{_libexecdir}/usbauth-notifier %{_libexecdir}/usbauth-notifier/usbauth-notifier

%verifyscript
%verify_permissions -e %{_libexecdir}/usbauth-npriv %{_libexecdir}/usbauth-notifier %{_libexecdir}/usbauth-notifier/usbauth-notifier

%changelog
