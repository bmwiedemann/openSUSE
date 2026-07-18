#
# spec file for package nethogs
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2013 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           nethogs
Version:        0.9.0
Release:        0
Summary:        Network Bandwidth Usage Monitor
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://raboof.github.io/nethogs/
Source:         https://github.com/raboof/nethogs/archive/v%{version}/nethogs-v%{version}.tar.gz
Source3:        https://keybase.io/raboof/key.asc#/%{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  meson
BuildRequires:  ncurses-devel

%description
NetHogs is a small 'net top' tool. Instead of breaking the traffic down per
protocol or per subnet, like most tools do, it groups bandwidth by process.
NetHogs does not rely on a special kernel module to be loaded. If there's
suddenly a lot of network traffic, you can fire up NetHogs and immediately see
which PID is causing this. This makes it easy to indentify programs that have
gone wild and are suddenly taking up your bandwidth.

%prep
%autosetup -p1

%build
%meson \
    --bindir=/usr/sbin \
    -Denable-libnethogs=disabled
%meson_build

%install
%meson_install
install -Dpm 0644 doc/nethogs.8 -t %{buildroot}%{_mandir}/man8/

%check
%make_build test

%files
%license COPYING
%doc README.md DESIGN
%{_sbindir}/nethogs
%{_mandir}/man8/nethogs.8%{?ext_man}

%changelog
