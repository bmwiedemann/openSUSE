#
# spec file for package usbauth-notifier
#
# Copyright (c) 2024 SUSE LLC
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
Summary:        Notifier for USB Firewall to use with desktop environments
URL:            https://github.com/kochstefan/usbauth-all/
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz

Release:        0
License:        GPL-2.0-only
Group:          System/X11/Utilities

Requires(pre):  permissions
Requires:       usbauth
BuildRequires:  gcc
BuildRequires:  gettext-runtime
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  permissions
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusbauth-configparser)
Provides:       group(usbauth)
Provides:       group(usbauth-notifier)

%description
A notifier for the usbauth firewall against BadUSB attacks. The user could manually allow or deny USB devices.

%lang_package

%prep
%autosetup -n %{_name}-%{version}

%build
pushd %{name}/
autoreconf -f -i
%configure
%make_build
popd

%pre
if ! getent group usbauth>/dev/null; then groupadd -r usbauth; fi
if ! getent group usbauth-notifier>/dev/null; then groupadd -r usbauth-notifier; fi

%install
pushd %{name}/
%make_install
popd
%find_lang %{name} --with-man

%files
%license %{name}/COPYING
%doc %{name}/README
%doc %_mandir/*/*
%dir %_sysconfdir/xdg/autostart
%_sysconfdir/xdg/autostart/usbauth-notifier.desktop
%verify(not mode) %attr(04750,root,usbauth) %_libexecdir/usbauth-npriv
%dir %verify(not mode) %attr(00750,root,usbauth-notifier) %_libexecdir/usbauth-notifier
%verify(not mode) %attr(02755,root,usbauth) %_libexecdir/usbauth-notifier/usbauth-notifier

%files lang -f %{name}.lang

%post
%set_permissions %_libexecdir/usbauth-npriv %_libexecdir/usbauth-notifier %_libexecdir/usbauth-notifier/usbauth-notifier

%verifyscript
%verify_permissions -e %_libexecdir/usbauth-npriv %_libexecdir/usbauth-notifier %_libexecdir/usbauth-notifier/usbauth-notifier

%changelog
