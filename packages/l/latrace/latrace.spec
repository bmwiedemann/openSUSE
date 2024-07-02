# vim: set sw=4 ts=4 et nu:
#
# spec file for package latrace
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


Name:           latrace
Version:        0.5.11
Release:        0
Summary:        Trace Library Calls using LD_AUDIT
License:        GPL-3.0-or-later
Group:          System/Monitoring
URL:            http://people.redhat.com/jolsa/latrace/index.shtml
Source:         %{name}-%{version}.tar.xz
# Fresh config.guess and config.sub files
# wget -O config.guess 'http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD'
Source1:        config.guess
# wget -O config.sub 'http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.sub;hb=HEAD'
Source2:        config.sub
Source99:       latrace-rpmlintrc
Patch0:         reproducible.patch
Patch1:         latrace-0.5.11-fixes.diff
Patch2:         0001-make-Fixes-paraller-building-like-make-j16.patch
Patch3:         0002-stats-bugfix-use-timersub-and-timeradd.patch
Patch4:         0003-stats-report-zero-percents-instead-of-NaN.patch
Patch5:         0004-add-aarch64-and-ppc64le-support-to-audit.h.patch
Patch6:         latrace-PRINT-format.patch
Patch7:         ppc-fedora.patch
Patch8:         audit-riscv.patch
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  xmlto

%description
latrace is a glibc 2.4+ LD_AUDIT frontend. It allows you to trace library calls
and get their statistics in a manner similar to the strace utility.

%prep
%autosetup -p1
cp %{SOURCE1} %{SOURCE2} .

%build
autoconf
%configure --libdir=%{_libdir}/latrace
%make_build V=1

%install
%make_install V=1

%files
%license COPYING
%doc ChangeLog README TODO ReleaseNotes
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
%{_mandir}/man1/latrace.1%{?ext_man}

%changelog
