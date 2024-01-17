#
# spec file for package dejagnu
#
# Copyright (c) 2021 SUSE LLC
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


Name:           dejagnu
Version:        1.6.3
Release:        0
Summary:        Framework for Running Test Suites on Software Tools
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://www.gnu.org/software/dejagnu/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/release-gpgkeys.php?group=dejagnu&download=1#/%{name}.keyring
Source3:        site.exp
Patch0:         testsuite-legacy.patch
BuildRequires:  expect
BuildRequires:  fdupes
BuildRequires:  gcc-c++
Requires:       expect
Requires:       info
Requires:       tcl
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
DejaGnu is a framework for testing other programs.  Its purpose is to
provide a single front-end for all tests.  Beyond this, DejaGnu offers
several advantages for testing:

1. The flexibility and consistency of the DejaGnu framework make it
   easy to write tests for any program.

1. DejaGnu provides a layer of abstraction that allows you to write
   tests that are portable to any host or target where a program
   must be tested.  For instance, a test for GDB can run (from any
   Unix-based host) on any target architecture that DejaGnu
   supports.

1. All tests have the same output format.  This makes it easy to
   integrate testing into other software development processes.
   DejaGnu's output is designed to be parsed by other filtering
   scripts and it is also human-readable.

DejaGnu is written in expect, which in turn uses "Tcl"--Tool command
language.

Running tests requires two things: the testing framework and the test
suites themselves.

%prep
%setup -q
%patch0 -p1

%build
# 49078@debbugs.gnu.org: bug in Expect 5.45.4 triggers a testsuite failure
# when building in source directory
mkdir build
cd build
%define _configure ../configure
%configure
make %{?_smp_mflags}

%check
make -C build check

%install
make -C build %{?_smp_mflags} DESTDIR=%{buildroot} install
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/dejagnu/site.exp
ln -s -f %{_sysconfdir}/dejagnu/site.exp %{buildroot}%{_datadir}/dejagnu/site.exp
%fdupes -s %{buildroot}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/dejagnu.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/dejagnu.info%{ext_info}

%files
%defattr(-, root, root)
%license COPYING
%doc ChangeLog NEWS README AUTHORS TODO
%dir %{_datadir}/dejagnu
%dir %{_sysconfdir}/dejagnu
%{_bindir}/dejagnu
%{_bindir}/runtest
%{_mandir}/man1/dejagnu.1%{ext_man}
%{_mandir}/man1/dejagnu-help.1%{ext_man}
%{_mandir}/man1/dejagnu-report-card.1%{ext_man}
%{_mandir}/man1/runtest.1%{ext_man}
%{_infodir}/dejagnu.info%{ext_info}
%{_includedir}/*
%config(noreplace) %{_sysconfdir}/dejagnu/site.exp
%{_datadir}/dejagnu/*

%changelog
