#
# spec file for package dbus-broker
#
# Copyright (c) 2024 SUSE LLC
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
Version:        36
Release:        0
Summary:        XDG message bus implementation
License:        Apache-2.0
Group:          System/Daemons
URL:            https://github.com/bus1/dbus-broker

Source:         https://github.com/bus1/dbus-broker/releases/download/v%version/dbus-broker-%version.tar.xz
Source2:        https://github.com/bus1/dbus-broker/releases/download/v%version/dbus-broker-%version.tar.xz.asc
Source10:       allow-restart.conf
Source11:       block-restart.conf
BuildRequires:  linux-glibc-devel >= 4.17
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(audit) >= 3.0
# dbus-1 requires dbus-broker, break that dep to avoid a cycle.
#!BuildIgnore: dbus-broker
BuildRequires:  pkgconfig(dbus-1) >= 1.10
BuildRequires:  pkgconfig(expat) >= 2.2.3
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(libcap-ng) >= 0.6
BuildRequires:  pkgconfig(libselinux) >= 3.2
BuildRequires:  pkgconfig(libsystemd) >= 230
BuildRequires:  pkgconfig(systemd) >= 230
Requires(pre):  systemd >= 253.6
Provides:       dbus-service
Provides:       bundled(c-dvar) = 1+
Provides:       bundled(c-ini) = 1+
Provides:       bundled(c-list) = 3+git9
Provides:       bundled(c-rbtree) = 3+git34
Provides:       bundled(c-shquote) = 1+
Provides:       bundled(c-stdaux) = 1+
Provides:       bundled(c-utf8) = 1+
Requires:       dbus-broker-restart-behavior = %version
Suggests:       dbus-broker-block-restart = %version
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

%package allow-restart
Summary:        Restart behavior configuration for dbus-broker - Allow restarting
Provides:       dbus-broker-restart-behavior = %version-%release
Conflicts:      dbus-broker-restart-behavior
BuildArch:      noarch

%description allow-restart
This package configures how the service behave to the systemctl restart command.

By installing this package dbus-broker will be allowed to restart

%package block-restart
Summary:        Restart behavior configuration for dbus-broker - Block restarting
Provides:       dbus-broker-restart-behavior = %version-%release
Conflicts:      dbus-broker-restart-behavior
BuildArch:      noarch

%description block-restart
This package configures how the service behave to the systemctl restart command.

By installing this package dbus-broker will be blocked to restart

%prep
%autosetup -p1

%build
ln -s /bin/true rst2man
%meson -Daudit=true -Dselinux=true
%meson_build

%install
%meson_install
for mode in allow block ; do
	install -Dpm0644 "%_sourcedir/$mode-restart.conf" "%buildroot/%_unitdir/dbus-broker.service.d/$mode-restart.conf"
	install -Dpm0644 "%_sourcedir/$mode-restart.conf" "%buildroot/%_userunitdir/dbus-broker.service.d/$mode-restart.conf"
done

%pre
%service_add_pre dbus-broker.service
%systemd_user_pre dbus-broker.service

%post
%service_add_post dbus-broker.service
%systemd_user_post dbus-broker.service

%preun
%service_del_preun dbus-broker.service

%postun
%service_del_postun_without_restart dbus-broker.service

%files
%_bindir/dbus-broker*
%_unitdir/*.service
%_userunitdir/*.service
%_journalcatalogdir/*
%license LICENSE

%files allow-restart
%license LICENSE
%dir %_unitdir/dbus-broker.service.d/
%dir %_userunitdir/dbus-broker.service.d/
%_unitdir/dbus-broker.service.d/allow-restart.conf
%_userunitdir/dbus-broker.service.d/allow-restart.conf

%files block-restart
%license LICENSE
%dir %_unitdir/dbus-broker.service.d/
%dir %_userunitdir/dbus-broker.service.d/
%_unitdir/dbus-broker.service.d/block-restart.conf
%_userunitdir/dbus-broker.service.d/block-restart.conf

%changelog
