#
# spec file for package lcov
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


Name:           lcov
Version:        1.15+git.20200812.d100e6c
Release:        0
Summary:        A Graphical GCOV Front-end
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/linux-test-project/lcov
Source0:        %{name}-%{version}.tar.xz
Requires:       gcc
Requires:       perl-GD
Requires:       perl-PerlIO-gzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
LCOV is a graphical front-end for GCC's coverage testing tool gcov. It collects
gcov data for multiple source files and creates HTML pages containing the
source code annotated with coverage information. It also adds overview pages
for easy navigation within the file structure.

%prep
%setup -q
sed -i "s/1.0/%{version}/" bin/get_version.sh

%build

%install
make install PREFIX=%{buildroot}/usr CFG_DIR=%{buildroot}/etc

%files
%defattr(644,root,root)
%config %{_sysconfdir}/lcovrc
%{_mandir}/man1/lcov.1.gz
%{_mandir}/man1/genhtml.1.gz
%{_mandir}/man1/geninfo.1.gz
%{_mandir}/man1/genpng.1.gz
%{_mandir}/man1/gendesc.1.gz
%{_mandir}/man5/lcovrc.5.gz
%defattr(-,root,root)
%{_bindir}/lcov
%{_bindir}/genhtml
%{_bindir}/geninfo
%{_bindir}/genpng
%{_bindir}/gendesc

%changelog
