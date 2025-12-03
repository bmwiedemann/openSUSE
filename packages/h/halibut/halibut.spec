#
# spec file for package halibut
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           halibut
Version:        1.3
Release:        0
Summary:        Document preparation system similar to TeX
License:        MIT AND APAFML
URL:            https://www.chiark.greenend.org.uk/~sgtatham/halibut/
Source:         https://www.chiark.greenend.org.uk/~sgtatham/halibut/halibut-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake

%description
Halibut is a documentation production system, with elements similar to TeX,
debiandoc-sgml, TeXinfo, and others. It is primarily targeted at people
producing software manuals.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENCE
%{_bindir}/halibut
%{_docdir}/%{name}
%{_mandir}/man1/halibut.1%{?ext_man}
%{_infodir}/halibut.info*%{?ext_info}

%changelog
