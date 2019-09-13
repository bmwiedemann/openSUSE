#
# spec file for package bmon
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bmon
Version:        4.0
Release:        0
Summary:        Bandwidth Monitor and Rate Estimator
License:        MIT or BSD-2-Clause
Group:          System/Monitoring
Url:            https://github.com/tgraf/bmon
Source:         https://github.com/tgraf/bmon/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        bmon.desktop
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libconfuse)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
bmon is a portable bandwidth monitor and rate estimator. It supports various
input methods for different architectures. Various output modes exist,
including an interactive curses interface, lightweight HTML output, and simple
ASCII output. Statistics may be distributed over a network using multicast or
unicast and collected at some point to generate a summary of statistics for a
set of nodes.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
install -d -m0755 %{buildroot}%{_sysconfdir}
mv %{buildroot}%{_datadir}/doc/bmon/examples/bmon.conf %{buildroot}%{_sysconfdir}/bmon.conf
install -D -m0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"
%suse_update_desktop_file -r "%{name}" System Monitor

%files
%defattr(-,root,root)
%doc LICENSE.BSD LICENSE.MIT NEWS README.md
%{_bindir}/bmon
%config %{_sysconfdir}/bmon.conf
%{_mandir}/man8/bmon.8%{ext_man}
%{_datadir}/applications/%{name}.desktop

%changelog
