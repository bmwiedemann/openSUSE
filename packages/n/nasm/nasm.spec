#
# spec file for package nasm
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


Name:           nasm
Version:        2.15.05
Release:        0
Summary:        Netwide Assembler (An x86 Assembler)
License:        BSD-2-Clause
Group:          Development/Languages/Other
URL:            https://www.nasm.us/
Source:         http://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes

%description
NASM is a prototype general-purpose x86 assembler. It can currently output
several binary formats, including ELF, a.out, Win32, and OS/2.

%prep
%autosetup

%build
%configure \
  --enable-lto
%make_build all

%install
%make_install rdf_install
%fdupes %{buildroot}%{_mandir}

%check
%make_build test

%files
%license LICENSE
%doc AUTHORS CHANGES ChangeLog README.md
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%changelog
