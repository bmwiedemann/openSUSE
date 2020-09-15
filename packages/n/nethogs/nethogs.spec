#
# spec file for package nethogs
#
# Copyright (c) 2020 SUSE LLC
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
Version:        0.8.6
Release:        0
Summary:        Network Bandwidth Usage Monitor
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://raboof.github.io/nethogs/
Source:         https://github.com/raboof/nethogs/archive/v%{version}/nethogs-v%{version}.tar.gz
Source3:        https://keybase.io/raboof/key.asc#/%{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  ncurses-devel

%description
NetHogs is a small 'net top' tool. Instead of breaking the traffic down per
protocol or per subnet, like most tools do, it groups bandwidth by process.
NetHogs does not rely on a special kernel module to be loaded. If there's
suddenly a lot of network traffic, you can fire up NetHogs and immediately see
which PID is causing this. This makes it easy to indentify programs that have
gone wild and are suddenly taking up your bandwidth.

%prep
%setup -q

%build
%make_build \
    sbin="%{_sbindir}" \
    bin="%{_sbindir}" \
    man8="%{_mandir}/man8" \
    CFLAGS="%{optflags}" \
    CXXFLAGS="%{optflags}" \
    CXX="g++" \
    nethogs

%install
make  %{?_smp_mflags} \
    sbin="%{buildroot}%{_sbindir}" \
    bin="%{buildroot}%{_sbindir}" \
    man8="%{buildroot}%{_mandir}/man8" \
    CFLAGS="%{optflags}" \
    CXXFLAGS="%{optflags}" \
    CXX="g++" \
    install

%check
%make_build test

%files
%license COPYING
%doc README.md DESIGN
%{_sbindir}/nethogs
%{_mandir}/man8/nethogs.8%{?ext_man}

%changelog
