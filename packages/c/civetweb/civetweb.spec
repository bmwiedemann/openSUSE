#
# spec file for package civetweb
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


%define         soname  1_15_0
%define         _libname libcivetweb

Name:           civetweb
Summary:        A C/C++ web server
License:        MIT
Group:          Productivity/Networking/Web/Servers
Version:        1.15
Release:        0
URL:            https://github.com/civetweb/civetweb
Source0:        https://github.com/civetweb/civetweb/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        civetweb.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel

%description
civetweb is a C/C++ embeddable web server with optional CGI, SSL and Lua support.

%package -n %{_libname}%{soname}
Summary:        Shared Object for applications that use %{name} embedded
Group:          Productivity/Networking/Web/Servers

%description -n %{_libname}%{soname}
This package contains the shared library required by applications that
are using %{name}'s embeddable API to provide web services.

%package -n %{_libname}-cpp%{soname}
Summary:        Shared Object for applications that use %{name} embedded
Group:          Productivity/Networking/Web/Servers

%description -n %{_libname}-cpp%{soname}
This package contains the shared library required by applications that
are using %{name}'s embeddable API to provide web services. 

%package devel
Summary:        Header files and development libraries for %{name}
Group:          Productivity/Networking/Web/Servers
Requires:       %{_libname}%{soname} = %{version}-%{release}
Requires:       %{_libname}-cpp%{soname} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs embedding %{name} on them,
you will need to install %{name}-devel and check %{name}'s API at its
comprisable header file.

%prep
%setup -q

install -pm0644  %{SOURCE1} .

#we dont need github files
rm -rf .github
rm .git* .clan*

%build
rm -rf build
%cmake -DWITH_ALL=1 \
       -DCIVETWEB_BUILD_TESTING=OFF \
       -DCIVETWEB_ENABLE_CXX=ON \
       -DCIVETWEB_ENABLE_SSL_DYNAMIC_LOADING=OFF

%cmake_build %{?_smp_mflags}

%install
%cmake_install

%post -n %{_libname}%{soname} -p /sbin/ldconfig
%postun -n %{_libname}%{soname} -p /sbin/ldconfig

%post -n %{_libname}-cpp%{soname} -p /sbin/ldconfig
%postun -n %{_libname}-cpp%{soname} -p /sbin/ldconfig

%files
%doc %{name}.conf
%license LICENSE.md
%{_bindir}/%{name}

%files -n %{_libname}%{soname}
%{_libdir}/lib%{name}.so.*

%files -n %{_libname}-cpp%{soname}
%{_libdir}/lib%{name}-cpp.so.*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/CivetServer.h
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-cpp.so

%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*cmake

%changelog
