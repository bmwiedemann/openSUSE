#
# spec file for package fatrace
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2013 Philipp Thomas <pth@suse.de>
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


%bcond_with tests
Name:           fatrace
Version:        0.17.0
Release:        0
Summary:        System wide file access event reporting utility
License:        GPL-3.0-or-later
Group:          System/Monitoring
URL:            https://github.com/martinpitt/fatrace
Source:         https://github.com/martinpitt/fatrace/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  glibc-devel

%description
The fatrace trace uses fanotify, a couple of /proc lookups and some
glue to trace file access events system-wide, in an effort to
identify processes which keep waking up the disk even when the
computer is idle.

By default, it monitors the whole system, i.e. all mounts except
virtual ones like /proc, tmpfs, etc. It can be told to monitor just
the mount of the current directory. The log can be written to a file
and runtime be capped. Optional time stamps and PID filters are also
provided.

%prep
%setup -q

%build
%make_build CFLAGS="%{optflags}" PREFIX="%{_prefix}"

%install
%make_install CFLAGS="%{optflags}" PREFIX="%{_prefix}"

%if %{with tests}
%check
sh ./tests/run
%endif

%files
%license COPYING
%doc NEWS
%{_sbindir}/%{name}
%{_sbindir}/power-usage-report
%{_mandir}/man8/%{name}.8%{?ext_man}

%changelog
