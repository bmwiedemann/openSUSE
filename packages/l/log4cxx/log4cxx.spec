#
# spec file for package log4cxx
#
# Copyright (c) 2020 SUSE LLC
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


Name:           log4cxx
Version:        0.11.0
Release:        0
%define soname 11
Summary:        Log4j like C++ Logging Library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://logging.apache.org/log4cxx/latest_stable/
Source:         https://downloads.apache.org/logging/log4cxx/%{version}/apache-log4cxx-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libapr-util1-devel
BuildRequires:  libapr1-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  unixODBC-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?sles_version} > 10
BuildRequires:  libesmtp-devel
%else
BuildRequires:  openldap2-devel
%endif

%description
Log4cxx is a port to C++ of the log4j logging library.

The goal is have the same functionalities and interfaces of log4j.

It is built with the following features enabled:
 - unicode
 - thread: pthread
 - XML:    libxml2
 - ODBC:   unixODBC

And for the documentation it is built with:
 - doxygen
 - dot
 - html-docs
 - latex-docs

It's a flexible and highly configurable logging framework
Main features :
- Configurable logging destinations (appenders)
- Configurable logging format (layouts)
- Categorized logging statements through a hierarchy (loggers)
- Advanced filtering (filters)
- Thread safe library
- UTF-16 Unicode support

* Appenders:
AsyncAppender, ConsoleAppender, DailyRollingFileAppender,
FileAppender, NTEventLogAppender, ODBCAppender, RollingFileAppender,
SMTPAppender, SocketAppender,
SocketHubAappender, SyslogAppender, TelnetAppender, XMLSocketAppender

* Layouts:
HTMLLayout, PatternLayout, SimpleLayout, TTCCLayout, XMLLayout

* Filters:
DenyAllFilter, LevelMatchFilter, LevelRangeFilter, StringMatchFilter

* Configurators:
BasicConfigurator, DOMConfigurator, PropertyConfigurator

* Java like objects with dynamic cast and instanciation. Custom objects can
be configured through the DOMConfigurator and PropertyConfigurator classes

%package -n liblog4cxx%{soname}
Summary:        Log4j like C++ Logging Library
Group:          System/Libraries

%description -n liblog4cxx%{soname}
Log4cxx is a port to C++ of the log4j logging library.

%package -n liblog4cxx-devel
Summary:        Log4j like C++ Logging Library
Group:          Development/Libraries/C and C++
Requires:       liblog4cxx%{soname} = %{version}

%description -n liblog4cxx-devel
Log4cxx is a port to C++ of the log4j logging library.

%prep
%setup -qn apache-log4cxx-%{version}

%build
./autogen.sh
# --enable-latex-docs apparently doesn't do anything
%configure --disable-static \
	--with-ODBC=unixODBC \
	--with-charset=utf-8 \
	--with-logchar=utf-8 \
	--enable-wchar_t \
	--enable-html-docs \
	--enable-dot \
%if 0%{?sles_version} > 10
	--with-SMTP=libesmtp \
%endif
	--enable-doxygen

make %{?_smp_mflags}

%install
%makeinstall
rm -f "%buildroot/%_libdir"/*.la
mkdir -p %{buildroot}%{_docdir}/liblog4cxx
mv %{buildroot}%{_datadir}/doc/log4cxx %{buildroot}%{_docdir}/liblog4cxx

%post   -n liblog4cxx%{soname} -p /sbin/ldconfig
%postun -n liblog4cxx%{soname} -p /sbin/ldconfig

%files -n liblog4cxx%{soname}
%{_libdir}/liblog4cxx.so.*

%files -n liblog4cxx-devel
%{_libdir}/liblog4cxx.so
%{_libdir}/pkgconfig/liblog4cxx.pc
%{_includedir}/log4cxx
%{_docdir}/liblog4cxx

%changelog
