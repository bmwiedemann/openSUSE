#
# spec file for package vtable-dumper
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


Name:           vtable-dumper
Version:        1.2
Release:        0
Summary:        Tool to list content of virtual tables in a C++ shared library
License:        GPL-2.0+ or LGPL-2.0+
Group:          Development/Tools/Other
Url:            https://github.com/lvc/vtable-dumper
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  help2man
BuildRequires:  libelf-devel
BuildRequires:  libstdc++-devel

%description
vtable-dumper is intended for developers of software libraries and
maintainers of Linux distributions who are interested in ensuring
backward binary compatibility.

%prep
%setup -q
sed -i -e 's/-Wall/%optflags/' Makefile

%build
make
help2man -N -o %{name}.1 ./%{name}

%install
make install prefix=%{buildroot}%{_prefix}
# Generate man page with help2man
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1

%files
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/vtable-dumper
%{_mandir}/man*/*

%changelog
