#
# spec file for package abi-dumper
#
# Copyright (c) 2025 SUSE LLC
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


Name:           abi-dumper
Version:        1.4
Release:        0
Summary:        Tool to dump ABI of an ELF object containing DWARF debug info
License:        LGPL-2.1-or-later
URL:            https://github.com/lvc/abi-dumper
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  help2man
Requires:       binutils
Requires:       elfutils
Requires:       gcc-c++
Requires:       vtable-dumper
Requires:       perl(Storable)
BuildArch:      noarch

%description
The tool is intended to be used with ABI Compliance Checker tool for tracking
ABI changes of a C/C++ library or kernel module.

%prep
%autosetup

%build
chmod 0755 %{name}.pl
ln -s %{name}.pl %{name}
help2man -N -o %{name}.1 ./%{name}

%install
mkdir -vp %{buildroot}%{_prefix}
env \
	"DESTDIR=%{buildroot}"  \
	perl Makefile.pl -install \
	--prefix=%{_prefix}
# Generate man page with help2man
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man*/*

%changelog
