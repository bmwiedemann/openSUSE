#
# spec file for package dstat
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


Name:           dstat
Version:        0.7.4
Release:        0
Summary:        Versatile vmstat, iostat and ifstat Replacement
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            http://dag.wieers.com/home-made/dstat/
Source:         https://github.com/dagwieers/dstat/archive/v%{version}.tar.gz
Source1:        dstat.desktop
Patch1:         fix_boo_1136279.patch
# PATCH-FIX-OPENSUSE - boo#1138417
Patch2:         0001-Use-python3-compatible-way-of-checking-instance-type.patch
# PATCH-FIX-OPENSUSE - boo#1173004
Patch3:         loop-should-be-integer.patch
BuildRequires:  make
Requires:       python3
BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
Requires:       python3-curses
Requires:       python3-six
%endif

%description
Dstat is a versatile replacement for vmstat, iostat, netstat and ifstat.
Dstat overcomes some of their limitations and adds some extra features,
more counters and flexibility. Dstat is handy for monitoring systems
during performance tuning tests, benchmarks or troubleshooting.

Dstat allows you to view all of your system resources instantly, you
can eg. compare disk usage in combination with interrupts from your
IDE controller, or compare the network bandwidth numbers directly
with the disk throughput (in the same interval).

Dstat gives you detailed selective information in columns and clearly
indicates in what magnitude and unit the output is displayed. Less
confusion, less mistakes.

%prep
%setup -q
# replace env by python
sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' dstat
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build

%install
# Makes examples non-executable
find examples/ -type f -print0 | xargs -0 chmod 0644
# Replace dangling symlink
rm examples/dstat.py
ln -s %{_bindir}/dstat examples/dstat.py

make %{?_smp_mflags} DESTDIR=%{buildroot} install docs-install

install -D -m 0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"

%if 0%{?suse_update_desktop_file:1}
%suse_update_desktop_file -r "%{name}" System Monitor
%endif

rm docs/Makefile

%if 0%{?suse_version}
%fdupes "%{buildroot}%{_datadir}/%{name}"
%endif

%if 0%{?suse_version} < 1330
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog README.adoc TODO
%doc docs/*.html docs/*.adoc examples/ proc/
%{_bindir}/dstat
%dir %{_datadir}/dstat
%{_datadir}/dstat/*
%{_mandir}/man1/dstat.1%{ext_man}
%{_datadir}/applications/dstat.desktop

%changelog
