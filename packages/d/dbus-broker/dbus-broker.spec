#
# spec file for package dbus-broker
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


Name:           dbus-broker
Version:        24
Release:        0
Summary:        XDG-conforming message bus implementation
License:        Apache-2.0
Group:          System/Daemons
URL:            https://github.com/bus1/dbus-broker

Source:         https://github.com/bus1/dbus-broker/releases/download/v%version/dbus-broker-%version.tar.xz
BuildRequires:  linux-glibc-devel >= 4.13
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(audit) >= 2.7
BuildRequires:  pkgconfig(dbus-1) >= 1.10
BuildRequires:  pkgconfig(expat) >= 2.2.3
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(libcap-ng) >= 0.6
BuildRequires:  pkgconfig(libselinux) >= 2.5
BuildRequires:  pkgconfig(libsystemd) >= 230
BuildRequires:  pkgconfig(systemd) >= 230
Provides:       bundled(c-dvar) = 1+
Provides:       bundled(c-ini) = 1+
Provides:       bundled(c-list) = 3+git9
Provides:       bundled(c-rbtree) = 3+git34
Provides:       bundled(c-shquote) = 1+
Provides:       bundled(c-stdaux) = 1+
Provides:       bundled(c-utf8) = 1+
%{?systemd_ordering}

%description
dbus-broker is an implementation of a message bus as defined by the
D-Bus specification. It has some different characteristics/features
from classic D-Bus:

* No shared medium
* No IPC to implement IPC
* User-based accounting
* Reliable messages
* Just the bus implementation, no external communication
* Local only, no remote transport
* Support for SASL pipelining
* Runtime broker control

%prep
%autosetup -p1

%build
ln -s /bin/true rst2man
%meson -Daudit=true -Dselinux=true
%meson_build

%install
%meson_install
mkdir -p "%buildroot/%_sbindir"
ln -s service "%buildroot/%_sbindir/rcdbus-broker"

%pre
%service_add_pre dbus-broker.service

%post
%service_add_post dbus-broker.service

%preun
%service_del_preun dbus-broker.service

%postun
%service_del_postun dbus-broker.service

%files
%_bindir/dbus-broker*
%_unitdir/*.service
%_prefix/lib/systemd/user/*.service
%_prefix/lib/systemd/catalog/
%_sbindir/rc*
%license LICENSE

%changelog
