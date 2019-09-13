#
# spec file for package dotconf
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dotconf
Version:        1.3
Release:        0
Summary:        Configuration file parser library
License:        LGPL-2.1+
Group:          Development/Languages/C and C++
Url:            https://github.com/williamh/dotconf/
Source:         https://github.com/williamh/dotconf/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
dotconf is a simple-to-use and powerful configuration-file parser
library written in C. The configuration files created for dotconf look
very similar to those used by the Apache Webserver. Even
Container-Directives known from httpd.conf can easily be used in the
exact same manner as for Apache-Modules. It supports various types of
arguments, dynamically loadable modules that create their own
configuration options on-the-fly, a here-documents feature to pass very
long ARG_STR data to your app, and on-the-fly inclusion of additional
config files.

%package -n libdotconf0
Summary:        Configuration file parser library
Group:          Development/Languages/C and C++
# Package was formerly libdotconf-1_0-0
Provides:       libdotconf-1_0-0 = %{version}
Obsoletes:      libdotconf-1_0-0 < %{version}

%description  -n libdotconf0
dotconf is a simple-to-use and powerful configuration-file parser
library written in C. The configuration files created for dotconf look
very similar to those used by the Apache Webserver. Even
Container-Directives known from httpd.conf can easily be used in the
exact same manner as for Apache-Modules. It supports various types of
arguments, dynamically loadable modules that create their own
configuration options on-the-fly, a here-documents feature to pass very
long ARG_STR data to your app, and on-the-fly inclusion of additional
config files.

%package devel
Summary:        Configuration file parser library
Group:          Development/Languages/C and C++
Requires:       libdotconf0 = %{version}
# Package dotconf contained only documentation, which was moved here
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}

%description devel
dotconf is a simple-to-use and powerful configuration-file parser
library written in C. The configuration files created for dotconf look
very similar to those used by the Apache Webserver. Even
Container-Directives known from httpd.conf can easily be used in the
exact same manner as for Apache-Modules. It supports various types of
arguments, dynamically loadable modules that create their own
configuration options on-the-fly, a here-documents feature to pass very
long ARG_STR data to your app, and on-the-fly inclusion of additional
config files.

%prep
%setup -q

%build
autoreconf -fiv
%configure \
  --disable-static \
  --with-pic
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
rm doc/Makefile*

%post -n libdotconf0 -p /sbin/ldconfig

%postun -n libdotconf0 -p /sbin/ldconfig

%files -n libdotconf0
%defattr (-,root,root,755)
%{_libdir}/libdotconf*.so.*

%files devel
%defattr (-,root,root,755)
%doc %{_datadir}/doc/dotconf/*
%dir %{_datadir}/doc/dotconf
%{_libdir}/libdotconf*.so
%{_libdir}/pkgconfig/dotconf.pc
%{_includedir}/dotconf.h

%changelog
