#
# spec file for package usbauth-notifier
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           usbauth-notifier
Version:        1.0
Release:        0
Summary:        Notifier for USB Firewall to use with desktop environments
License:        GPL-2.0
Group:          System/X11/Utilities
Url:            https://github.com/kochstefan/usbauth-all/tree/master/usbauth-notifier

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}.tar.bz2

Requires(pre):  permissions
Requires:       usbauth
BuildRequires:  gettext-runtime
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  libusbauth-configparser-devel
BuildRequires:  permissions
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(dbus-1)

%description
A notifier for the usbauth firewall against BadUSB attacks. The user could manually allow or deny USB devices.

%prep
%setup -n %{name}

%build
autoreconf -f -i
%configure
%make_build

%pre
if ! getent group usbauth>/dev/null; then groupadd -r usbauth; fi
if ! getent group usbauth-notifier>/dev/null; then groupadd -r usbauth-notifier; fi

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING README
%dir /etc/xdg/autostart
/etc/xdg/autostart/usbauth-notifier.desktop
%verify(not mode) %attr(04750,root,usbauth) %_bindir/usbauth-npriv
%dir %verify(not mode) %attr(00750,root,usbauth-notifier) /usr/lib/usbauth-notifier
%verify(not mode) %attr(02755,root,usbauth) /usr/lib/usbauth-notifier/usbauth-notifier
%_mandir/man1/usbauth-notifier.1*
%_mandir/man1/usbauth-npriv.1*
%_datadir/locale/*/LC_MESSAGES/usbauth-notifier.mo

%post
%set_permissions %_bindir/usbauth-npriv /usr/lib/usbauth-notifier /usr/lib/usbauth-notifier/usbauth-notifier

%verifyscript
%verify_permissions -e %_bindir/usbauth-npriv /usr/lib/usbauth-notifier /usr/lib/usbauth-notifier/usbauth-notifier

%changelog
