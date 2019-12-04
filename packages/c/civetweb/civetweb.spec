#
# spec file for package civetweb
#
# Copyright (c) 2019 SUSE LLC
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


%define         soname  1_11_0
%define         _libname libcivetweb

Name:           civetweb
Summary:        A C/C++ web server
License:        MIT
Group:          Productivity/Networking/Web/Servers
Version:        1.11
Release:        0
Url:            https://github.com/civetweb/civetweb
Source0:        https://github.com/civetweb/civetweb/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        civetweb.conf
Patch1:         fix-libpath.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel

%description
civetweb is a C/C++ embeddable web server with optional CGI, SSL and Lua support. 

%package -n %{_libname}%{soname}
Summary:        Shared Object for applications that use %{name} embedded
Group:          Productivity/Networking/Web/Servers

%description -n %{_libname}%{soname}
This package contains the shared library required by applications that
are using %{name}'s embeddable API to provide web services. 

%package devel
Summary:        Header files and development libraries for %{name}
Group:          Productivity/Networking/Web/Servers
Requires:       %{_libname}%{soname} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs embedding %{name} on them,
you will need to install %{name}-devel and check %{name}'s API at its
comprisable header file.

%prep
%setup -q
%patch1 -p1

install -pm0644  %{SOURCE1} .

%build
rm -rf build
%cmake -DWITH_ALL=1 \
       -DCIVETWEB_BUILD_TESTING=OFF

%cmake_build %{?_smp_mflags}

%install
%cmake_install

%post -n %{_libname}%{soname} -p /sbin/ldconfig
%postun -n %{_libname}%{soname} -p /sbin/ldconfig

%files
%doc %{name}.conf
%license LICENSE.md
%{_bindir}/%{name}

%files -n %{_libname}%{soname}
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
