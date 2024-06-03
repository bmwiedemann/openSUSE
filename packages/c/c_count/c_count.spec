#
# spec file for package c_count
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           c_count
Version:        7.23
Release:        0
Summary:        Source Code Measure Counter for C/C++/Java
License:        MIT
URL:            https://invisible-island.net/c_count/
Source0:        https://invisible-island.net/archives/c_count/%{name}-%{version}.tgz
Source1:        https://invisible-island.net/archives/c_count/%{name}-%{version}.tgz.asc
Source2:        %{name}.keyring

%description
c_count counts lines, statements, and other simple measures of C/C++/Java
source programs. It is not lex/yacc based, and is easily portable to a
variety of systems.

%prep
%autosetup

%build
%configure \
  --enable-warnings
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc CHANGES README
%{_bindir}/c_count
%{_mandir}/man1/c_count.1%{?ext_man}

%changelog
