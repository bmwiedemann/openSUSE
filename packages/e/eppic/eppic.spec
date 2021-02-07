#
# spec file for package eppic
#
# Copyright (c) 2021 SUSE LLC
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


Name:           eppic
Version:        3.99.git.1612358888.e8844d3
Release:        0
Summary:        Embeddable Pre-Processor and Interpreter for C
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Source:         lib%{name}-%{version}.tar.bz2
Patch1:         %{name}-fix-install.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  ncurses-devel
URL:            https://github.com/lucchouina/eppic
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
EPPIC is a C interpreter that permits easy access to the symbol and type
information stored in a executable image like a coredump or live memory
interfaces (e.g. /dev/kmem, /dev/mem). Although it has a strong association
with live or postmortem kernel analysis, it is not constraint to it and can be
embedded in any tools that is C friendly.

%package -n libeppic-devel
Summary:        EPPIC include files and libraries
Group:          Development/Languages/C and C++

%description -n libeppic-devel
EPPIC is a C interpreter that permits easy access to the symbol and type
information stored in a executable image like a coredump or live memory
interfaces (e.g. /dev/kmem, /dev/mem). Although it has a strong association
with live or postmortem kernel analysis, it is not constraint to it and can be
embedded in any tools that is C friendly.

This package provides the include files and libraries needed for development.

%prep
%setup -n lib%{name}-%{version}
%patch1 -p2

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
make CFLAGS="%{optflags} -fPIC" %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
make ROOT="%{buildroot}" LIBDIR=%{_libdir} install

%files -n libeppic-devel
%defattr(-,root,root)
%doc README
%{_includedir}/eppic.h
%{_includedir}/eppic_api.h
%attr(644,root,root) %{_libdir}/libeppic.a

%changelog
