# vim: set sw=4 ts=4 et nu:
#
# spec file for package latrace
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           latrace
Version:        0.5.11
Release:        0
Summary:        Trace Library Calls using LD_AUDIT
License:        GPL-3.0+
Group:          System/Monitoring
Source:         http://people.redhat.com/jolsa/latrace/dl/latrace-%{version}.tar.bz2
Source99:       latrace-rpmlintrc
Patch0:         reproducible.patch
Patch1:         latrace-0.5.11-fixes.diff
Url:            http://people.redhat.com/jolsa/latrace/index.shtml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  xmlto
ExclusiveArch:  %{ix86} x86_64 %{arm}

%description
latrace is a glibc 2.4+ LD_AUDIT frontend. It allows you to trace library calls
and get their statistics in a manner similar to the strace utility.

%prep
%setup -q
%patch0 -p1
%patch1

%build
autoconf
%configure --libdir=%{_libdir}/latrace
make V=1

%install
%make_install V=1

%files
%defattr(-,root,root)
%doc COPYING ChangeLog README TODO ReleaseNotes
%config %dir %{_sysconfdir}/latrace.d
%config %dir %{_sysconfdir}/latrace.d/headers
%config %{_sysconfdir}/latrace.d/*.conf
%config %{_sysconfdir}/latrace.d/headers/*.h
%ifarch x86_64
%config %dir %{_sysconfdir}/latrace.d/headers/sysdeps
%config %dir %{_sysconfdir}/latrace.d/headers/sysdeps/*
%config %{_sysconfdir}/latrace.d/headers/sysdeps/*/*.h
%endif
%{_bindir}/latrace
%{_bindir}/latrace-ctl
%dir %{_libdir}/latrace
%{_libdir}/latrace/libltaudit.so.%{version}
%doc %{_mandir}/man1/latrace.1%{ext_man}

%changelog
