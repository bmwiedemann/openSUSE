#
# spec file for package tolua
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


%define libname libtolua5
Name:           tolua
Version:        5.2.4
Release:        0
Summary:        Greatly simplifies the integration of C/C++ code with Lua
License:        GPL-2.0-or-later
Group:          Development/Libraries/Other
URL:            http://www.tecgraf.puc-rio.br/~celes/tolua/
Source:         http://www.tecgraf.puc-rio.br/~celes/tolua/tolua-%{version}.tar.gz
Patch0:         %{name}-5.2.0-optflags.patch
Patch1:         %{name}-5.2.0-shared.patch
BuildRequires:  gcc-c++
BuildRequires:  lua-devel
Requires:       %{libname} = %{version}

%description
tolua is a tool that greatly simplifies the integration of
C/C++ code with Lua.

Based on a 'cleaned' header file, tolua automatically generates
the binding code to access C/C++ features from Lua.

Using Lua-5.0 API and tag method facilities, the current version
automatically maps C/C++ constants, external variables, functions,
namespace, classes, and methods to Lua. It also provides
facilities to create Lua modules.

%package -n %{libname}
Summary:        Shared libraries for tolua
Group:          System/Libraries

%description -n %{libname}
This package provides shared libraries for tolua.

%package -n libtolua-devel
Summary:        Development headers for tolua
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Provides:       tolua-devel = %{version}
Obsoletes:      tolua-devel < %{version}

%description -n libtolua-devel
This package contains all necessary include files and libraries
needed to develop applications that require these.

%prep
%autosetup -p1

%build
# no jobserver
make -e \
LUA=%{_prefix} \
LUALIB=%{_libdir} \
LUAINC=%{_includedir}/lua%{lua_version} \
WARN='%{optflags}'

%install
%make_install LIBDIR=%{_libdir}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc README
%{_bindir}/%{name}

%files -n %{libname}
%{_libdir}/lib%{name}.so.5
%{_libdir}/lib%{name}.so.5.2
%{_libdir}/lib%{name}.so.%{version}

%files -n libtolua-devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
