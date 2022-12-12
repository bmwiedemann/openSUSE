#
# spec file for package clingo
#
# Copyright (c) 2022 SUSE LLC
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


%define major 4
Name:           clingo
Version:        5.6.2
Release:        1.1
Summary:        A grounder and solver for logic programs
Group:          Development/Tools/Other

License:        MIT
URL:            https://potassco.org/clingo/
Source0:        https://github.com/potassco/clingo/archive/v%{version}/%{name}-%{version}.tar.gz
# Disable gcc warning no-class-memaccess, which is intended use in this case
Patch0:         clingo.clasp-disable-class-memaccess-warning.patch

BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  re2c

%description
Clingo is part of the Potassco project for Answer Set Programming
(ASP). ASP offers a simple and powerful modeling language to describe
combinatorial problems as logic programs. The clingo system then takes
such a logic program and computes answer sets representing solutions
to the given problem.

%define lib_name lib%{name}

%package        -n %{lib_name}%{major}
Summary:        Libraries file(s) for %{name}
Group:          Development/Libraries/C and C++

%description -n %{lib_name}%{major}
Clingo is part of the Potassco project for Answer Set Programming
(ASP). This package include clingo libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{lib_name}%{major} = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n lua-%{name}
Summary:        Lua bindings for Clingo
Requires:       %{name} = %{version}-%{release}
BuildRequires:  lua-devel

%description -n lua-%{name}
Lua bindings for Clingo, a grounder and solver for logic programs.

Detailed information (including a User's manual), source code, and pre-compiled
binaries are available at: http://potassco.org/

%package -n python3-%{name}
Summary:        Python 3 bindings for Clingo
Requires:       %{name} = %{version}-%{release}
Requires:       python3-cffi
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3-cffi
BuildRequires:  python3-devel

%description -n python3-%{name}
This module provides functions and classes to work with ground terms and to
control the instantiation process. In clingo builts, additional functions to
control and inspect the solving process are available.

Functions defined in a python script block are callable during the
instantiation process using @-syntax. The default grounding/solving process can
be customized if a main function is provided.

Detailed information (including a User's manual), source code, and pre-compiled
binaries are available at: http://potassco.org/

%prep
%autosetup -p1

%build
cmake \
  -H. \
  -Brelease \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DCMAKE_BUILD_TYPE=release \
  -DCLINGO_BUILD_STATIC:BOOL=OFF \
  -DCLINGO_BUILD_EXAMPLES:BOOL=OFF \
  -DCLINGO_BUILD_APPS:BOOL=ON \
  -DCLINGO_BUILD_WITH_PYTHON:BOOT=ON \
  -DCLINGO_BUILD_WITH_LUA:BOOL=ON \
  -DCLINGO_BUILD_LUA_SHARED:BOOL=ON \
  -DPYTHON_EXECUTABLE=%{__python3} \
  -DCLINGO_BUILD_SHARED:BOOL=ON \
  -DCLINGO_MANAGE_RPATH:BOOL=OFF \
  -DLUACLINGO_INSTALL_DIR:PATH=%{lua_archdir}

cmake --build release %{?_smp_mflags}

%install
%make_install -C release DESTDIR=$RPM_BUILD_ROOT

# remove static lib
rm $RPM_BUILD_ROOT/%{_libdir}/libluaclingo.a
# remove empty file
rm $RPM_BUILD_ROOT/%{python3_sitearch}/%{name}/py.typed

%post -n %{lib_name}%{major} -p /sbin/ldconfig
%postun -n %{lib_name}%{major} -p /sbin/ldconfig

%files
%doc README.md INSTALL.md
%license LICENSE.md
%attr(0755,root,root) %{_bindir}/clasp
%attr(0755,root,root) %{_bindir}/clingo
%attr(0755,root,root) %{_bindir}/gringo
%attr(0755,root,root) %{_bindir}/lpconvert
%attr(0755,root,root) %{_bindir}/reify

%files -n %{lib_name}%{major}
%doc README.md INSTALL.md
%license LICENSE.md
%defattr(-,root,root)
%{_libdir}/libclingo.so.4*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/Clingo

%files -n lua-%{name}
%defattr(-,root,root)
%{lua_archdir}/%{name}.so

%files -n python3-%{name}
%defattr(-,root,root)
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-%{version}*

%changelog
