#
# spec file for package ispell-bulgarian
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


Name:           ispell-bulgarian
Version:        4.2
Release:        0
Summary:        Bulgarian Ispell Dictionary
License:        GPL-2.0+ or MPL-1.1 or LGPL-3.0+
Group:          Productivity/Text/Spell
Url:            https://sourceforge.net/projects/bgoffice
Source:         https://downloads.sourceforge.net/bgoffice/ispell-bg-%{version}.tar.gz
Patch0:         destdir.patch
BuildRequires:  ispell
Provides:       ispell_dictionary
Provides:       locale(ispell:bg)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This packages includes a ready Bulgarian dictionary for ispell.
A short usage description for ispell is given in
%{_docdir}/ispell/README of the packages ispell. The
sources for this dictionary are included in the package dicts.

%prep
%setup -q -n ispell-bg-%{version}
%patch0

%build
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc Copyright *.txt ChangeLog
%{_prefix}/lib/ispell/bulgarian.*

%changelog
