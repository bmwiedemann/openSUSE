#
# spec file for package lcov
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


Name:           lcov
Version:        2.6
Release:        0
Summary:        A Graphical GCOV Front-end
License:        GPL-2.0-or-later
URL:            https://github.com/linux-test-project/lcov
Source0:        %{name}-%{version}.tar.xz
Source1:        lcov.rpmlintrc
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  make
# plain tool dependency: --perl mode would explode this into hundreds of
# perl(...) lines on this non-Perl package, so it stays a package name
BuildRequires:  perl
BuildRequires:  perl-Capture-Tiny
BuildRequires:  perl-DateTime
BuildRequires:  perl-Devel-StackTrace
BuildRequires:  perl-TimeDate
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinx_rtd_theme
Requires:       findutils
Requires:       gcc
Requires:       perl-Capture-Tiny
Requires:       perl-DateTime
Requires:       perl-Devel-StackTrace
Requires:       perl-GD
Requires:       perl-PerlIO-gzip
Requires:       perl-TimeDate
# The XS (C++) backend ships a compiled .so, so this is no longer noarch

%description
LCOV is a graphical front-end for GCC's coverage testing tool gcov. It collects
gcov data for multiple source files and creates HTML pages containing the
source code annotated with coverage information. It also adds overview pages
for easy navigation within the file structure.

%package example
Summary:        Example for %{name}
Requires:       %{name}
BuildArch:      noarch

%description example
Example sources for %{name}

%prep
%autosetup
# get_version.sh falls back to a stale version without git metadata - stamp ours
sed -i 's/VERSION="2\.5\.0"/VERSION="%{version}"/' bin/get_version.sh

# fix  E: env-script-interpreter
sed -i 's,#!%{_bindir}/env ,#!/usr/bin/,' bin/gen* bin/xml2lcovutil.py bin/*lcov scripts/*
sed -i 's,#!/usr/bin/env bash,#!/bin/bash,' example/java_avail.sh

%build

%install
%make_install PREFIX=%{_prefix} CFG_DIR=%{_sysconfdir} LIB_DIR=%{_datadir}/%{name}/lib/
rm -rf %{buildroot}%{_datadir}/%{name}/tests/
rm -f %{buildroot}%{_datadir}/%{name}/html/.buildinfo
%fdupes %{buildroot}%{_datadir}/%{name}/html
find %{buildroot}%{_datadir}/%{name}/support-scripts/ -name "*.pm" -exec chmod -x {} \;

%files
%config %{_sysconfdir}/lcovrc
%{_mandir}/man1/lcov.1%{?ext_man}
%{_mandir}/man1/genhtml.1%{?ext_man}
%{_mandir}/man1/geninfo.1%{?ext_man}
%{_mandir}/man1/genpng.1%{?ext_man}
%{_mandir}/man1/gendesc.1%{?ext_man}
%{_mandir}/man1/html2lcov.1%{?ext_man}
%{_mandir}/man1/jacoco2lcov.1%{?ext_man}
%{_mandir}/man1/llvm2lcov.1%{?ext_man}
%{_mandir}/man1/perl2lcov.1%{?ext_man}
%{_mandir}/man1/py2lcov.1%{?ext_man}
%{_mandir}/man1/spreadsheet.py.1%{?ext_man}
%{_mandir}/man1/xml2lcov.1%{?ext_man}
%{_mandir}/man5/lcovrc.5%{?ext_man}
%{_bindir}/lcov
%{_bindir}/genhtml
%{_bindir}/geninfo
%{_bindir}/genpng
%{_bindir}/gendesc
%{_bindir}/html2lcov
%{_bindir}/jacoco2lcov
%{_bindir}/perl2lcov
%{_bindir}/py2lcov
%{_bindir}/llvm2lcov
%{_bindir}/xml2lcov
%{_bindir}/xml2lcovutil.py
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/html/
%{_datadir}/%{name}/lib/
%{_datadir}/%{name}/support-scripts

%files example
%{_datadir}/%{name}/example/

%changelog
