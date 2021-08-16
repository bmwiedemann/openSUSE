#
# spec file for package dotconf
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


Name:           dotconf
Version:        1.3
Release:        0
Summary:        Configuration file parser library
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
URL:            https://github.com/williamh/dotconf/
Source:         https://github.com/williamh/dotconf/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
dotconf is a configuration-file parser
library written in C. The configuration files created for dotconf look
similar to those used by the Apache web server. Even
container directives known from httpd.conf can be used in the
same manner as for Apache modules. It supports various types of
arguments, dynamically loadable modules that create their own
configuration options on-the-fly, a here-documents feature to pass
long ARG_STR data to programs, and on-the-fly inclusion of additional
config files.

%package -n libdotconf0
Summary:        Configuration file parser library
Group:          System/Languages
# Package was formerly libdotconf-1_0-0
Provides:       libdotconf-1_0-0 = %{version}
Obsoletes:      libdotconf-1_0-0 < %{version}

%description  -n libdotconf0
dotconf is a configuration-file parser
library written in C. The configuration files created for dotconf look
similar to those used by the Apache web server. Even
container directives known from httpd.conf can be used in the
same manner as for Apache modules. It supports various types of
arguments, dynamically loadable modules that create their own
configuration options on-the-fly, a here-documents feature to pass
long ARG_STR data to programs, and on-the-fly inclusion of additional
config files.

%package devel
Summary:        Configuration file parser library
Group:          Development/Languages/C and C++
Requires:       libdotconf0 = %{version}
# Package dotconf contained only documentation, which was moved here
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}

%description devel
dotconf is a configuration-file parser
library written in C. The configuration files created for dotconf look
similar to those used by the Apache web server. Even
container directives known from httpd.conf can be used in the
same manner as for Apache modules. It supports various types of
arguments, dynamically loadable modules that create their own
configuration options on-the-fly, a here-documents feature to pass
long ARG_STR data to programs, and on-the-fly inclusion of additional
config files.

%prep
%autosetup

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm doc/Makefile*

%post -n libdotconf0 -p /sbin/ldconfig

%postun -n libdotconf0 -p /sbin/ldconfig

%files -n libdotconf0
%{_libdir}/libdotconf*.so.*

%files devel
%doc %{_datadir}/doc/dotconf/*
%dir %{_datadir}/doc/dotconf
%{_libdir}/libdotconf*.so
%{_libdir}/pkgconfig/dotconf.pc
%{_includedir}/dotconf.h

%changelog
