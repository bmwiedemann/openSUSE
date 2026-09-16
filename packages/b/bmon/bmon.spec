#
# spec file for package bmon
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           bmon
Version:        5.0
Release:        0
Summary:        Bandwidth Monitor and Rate Estimator
License:        BSD-2-Clause OR MIT
Group:          System/Monitoring
URL:            https://jafaral.github.io/bmon/
Source:         https://github.com/Jafaral/bmon/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:        bmon.desktop
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libnl-3.0)

%description
bmon is a portable bandwidth monitor and rate estimator. It supports various
input methods for different architectures. Various output modes exist,
including an interactive curses interface, lightweight HTML output, and simple
ASCII output. Statistics may be distributed over a network using multicast or
unicast and collected at some point to generate a summary of statistics for a
set of nodes.

%prep
%autosetup

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install
install -d -m0755 %{buildroot}%{_sysconfdir}
mv %{buildroot}%{_datadir}/doc/bmon/examples/bmon.conf %{buildroot}%{_sysconfdir}/bmon.conf
install -D -m0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"
%suse_update_desktop_file -r "%{name}" System Monitor

%files
%license LICENSE.BSD LICENSE.MIT
%doc NEWS README.md
%{_bindir}/bmon
%config %{_sysconfdir}/bmon.conf
%{_mandir}/man8/bmon.8%{?ext_man}
%{_datadir}/applications/%{name}.desktop

%changelog
