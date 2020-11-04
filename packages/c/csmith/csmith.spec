#
# spec file for package csmith
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


Name:           csmith
Version:        2.3.0
Release:        0
Summary:        Random C code generator
License:        BSD-3-Clause
Group:          Development/Tools/Other
Url:            https://github.com/csmith-project/csmith
Source:         https://github.com/csmith-project/%{name}/archive/csmith-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  m4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Csmith is a tool that can generate random C programs that statically and
dynamically conform to the C99 standard. It is useful for stress-testing
compilers, static analyzers, and other tools that process C code.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%configure --disable-static --docdir="%{_docdir}/%{name}"
make %{?_smp_mflags}

%install
install -d %{buildroot}/%{_bindir}
install -m 755 src/csmith %{buildroot}/%{_bindir}/csmith
install -d %{buildroot}/%{_includedir}
install -m 644 runtime/*.h %{buildroot}/%{_includedir}

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/csmith
%{_includedir}/*.h

%changelog
