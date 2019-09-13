#
# spec file for package ispell-slovak
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


Name:           ispell-slovak
Version:        0.3.2
Release:        0
Summary:        Slovak Ispell Dictionary
License:        GPL-2.0+ or LGPL-2.1+ or MPL-1.1
Group:          Productivity/Text/Spell
Url:            http://sk-spell.sk.cx/?id=4
Source:         http://sk-spell.sk.cx/files/ispell-sk-%{version}.tar.gz
Source1:        slovak.el
Patch0:         ispell-sk-%{version}-installdir.patch
Patch1:         ispell-sk-%{version}-encoding_readme.patch.bz2
BuildRequires:  ispell
Provides:       ispell_dictionary
Provides:       locale(ispell:sk)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This packages includes a ready Slovak dictionary for ispell. A short
usage description for ispell is given in
%{_docdir}/ispell/README of the packages ispell. The
sources for this dictionary are included in the package dicts.

%prep
%setup -q -n ispell-sk-%{version}
%patch0
%patch1

%build
make %{?_smp_mflags}

%install
%make_install

install -Dm644 %{SOURCE1} %{buildroot}%{_prefix}/lib/ispell/emacs/slovak.el

%files
%defattr(-,root,root)
%doc AUTHORS CHANGELOG Copyright GPL LGPL MPL README* TODO
%{_prefix}/lib/ispell/slovak.*
%{_prefix}/lib/ispell/emacs/slovak.el

%changelog
