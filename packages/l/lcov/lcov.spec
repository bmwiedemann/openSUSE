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
Version:        2.4
Release:        0
Summary:        A Graphical GCOV Front-end
License:        GPL-2.0-or-later
URL:            https://github.com/linux-test-project/lcov
Source0:        %{name}-%{version}.tar.xz
Source1:        lcov.rpmlintrc
Requires:       findutils
Requires:       gcc
Requires:       perl-Capture-Tiny
Requires:       perl-DateTime
Requires:       perl-GD
Requires:       perl-PerlIO-gzip
Requires:       perl-TimeDate
BuildArch:      noarch

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
sed -i "s/1.0/%{version}/" bin/get_version.sh

# fix  E: env-script-interpreter
sed -i 's,#!%{_bindir}/env ,#!/usr/bin/,' bin/gen* bin/xml2lcovutil.py bin/*lcov scripts/*

%build

%install
%make_install PREFIX=%{_prefix} CFG_DIR=%{_sysconfdir} LIB_DIR=%{_datadir}/%{name}/lib/
rm -rf %{buildroot}%{_datadir}/%{name}/tests/
find %{buildroot}%{_datadir}/%{name}/support-scripts/ -name "*.pm" -exec chmod -x {} \;

%files
%config %{_sysconfdir}/lcovrc
%{_mandir}/man1/lcov.1%{?ext_man}
%{_mandir}/man1/genhtml.1%{?ext_man}
%{_mandir}/man1/geninfo.1%{?ext_man}
%{_mandir}/man1/genpng.1%{?ext_man}
%{_mandir}/man1/gendesc.1%{?ext_man}
%{_mandir}/man5/lcovrc.5%{?ext_man}
%{_bindir}/lcov
%{_bindir}/genhtml
%{_bindir}/geninfo
%{_bindir}/genpng
%{_bindir}/gendesc
%{_bindir}/perl2lcov
%{_bindir}/py2lcov
%{_bindir}/llvm2lcov
%{_bindir}/xml2lcov
%{_bindir}/xml2lcovutil.py
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/lib/
%{_datadir}/%{name}/support-scripts

%files example
%{_datadir}/%{name}/example/

%changelog
