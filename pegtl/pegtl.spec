#
# spec file for package pegtl
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


Name:           pegtl
Summary:        Parsing Expression Grammar (PEG) Template Library
License:        MIT
Group:          Development/Languages/C and C++
Url:            https://github.com/taocpp/PEGTL
Version:        1.3.1
Release:        0
BuildRequires:  gcc-c++
Source0:        https://github.com/taocpp/PEGTL/archive/%{version}.tar.gz
BuildArch:      noarch

%description
The Parsing Expression Grammar Template Library (PEGTL) is a C++11
library for creating parsers according to a Parsing Expression
Grammar (PEG).

%package devel
Summary:        Parsing Expression Grammar (PEG) Template Library
Group:          Development/Languages/C and C++

%description devel
The Parsing Expression Grammar Template Library (PEGTL) is a C++11
library for creating parsers according to a Parsing Expression
Grammar (PEG). Grammars are embedded as regular C++ code, and
consist of template hierarchies of classes. These hierarchies
naturally correspond to the inductive definition of PEGs. The
library extends on the subject of PEGs with new expression types,
actions that can be attached to grammar rules, and mechanisms to
ensure helpful diagnostics in case of parsing errors.


%prep
%setup -q -n PEGTL-%version

%build
# The package contains just C++ template headers for shipment.

%install
mkdir -p -m 755 %{buildroot}/%{_includedir}
cp -rp pegtl.hh %{buildroot}/%{_includedir}
cp -rp pegtl %{buildroot}/%{_includedir}

%check
make %{?_smp_mflags}

%files devel
%{_includedir}/*

%changelog
