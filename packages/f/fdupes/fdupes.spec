#
# spec file for package fdupes
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

%{?!_rpmmacrodir:%define _rpmmacrodir /usr/lib/rpm/macros.d}

Name:           fdupes
Version:        2.1.2
Release:        0
Summary:        Tool to identify or delete duplicate files
License:        MIT
Group:          Productivity/Archiving/Compression
Url:            https://github.com/adrianlopezroche/fdupes
Source0:        https://github.com/adrianlopezroche/fdupes/releases/download/v%{version}/fdupes-%{version}.tar.gz
Source1:        macros.fdupes

%description
FDUPES is a program for identifying or deleting duplicate files
residing within specified directories.

%prep
%autosetup -p1

%build
%configure --without-ncurses
%make_build

%install
%make_install
install -D -m644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.%{name}

%check
./%{name} testdir
./%{name} --omitfirst testdir
./%{name} --recurse testdir
./%{name} --size testdir

%files
%doc CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_rpmmacrodir}/macros.%{name}

%changelog
