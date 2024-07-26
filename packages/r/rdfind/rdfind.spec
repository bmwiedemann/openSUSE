#
# spec file for package rdfind
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2014 Johannes Kastl
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


Name:           rdfind
Version:        1.6.0
Release:        0
Summary:        Find duplicate files and replace them with symlinks or hardlinks
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://rdfind.pauldreik.se/
Source0:        https://rdfind.pauldreik.se/%{name}-%{version}.tar.gz
Source1:        https://rdfind.pauldreik.se/%{name}-%{version}.tar.gz.asc
BuildRequires:  gcc-c++
BuildRequires:  libnettle-devel
BuildRequires:  make

%description
Rdfind is a program that finds duplicate files. It is useful for compressing
backup directories or just finding duplicate files. It compares files based on
their content, NOT on their file names.

%prep
%autosetup -p1

%build
%configure
%{make_build}

%install
%{makeinstall}

%check
%{make_build} check

%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/rdfind.1%{?ext_man}

%changelog
