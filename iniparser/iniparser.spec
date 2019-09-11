#
# spec file for package iniparser
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


# if bumping this, also update baselibs.conf
%define sonum 1
Name:           iniparser
Version:        4.1
Release:        0
Summary:        Library to parse ini files
License:        MIT
Group:          System/Libraries
URL:            http://ndevilla.free.fr/iniparser/
Source:         https://github.com/ndevilla/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
Patch00:        iniparser_remove_rpath.patch

%description
Libiniparser offers parsing of ini files from the C level.

%if 0%{?suse_version} == 0 || 0%{?suse_version} > 1100
%define libiniparser_name libiniparser%{sonum}
%else
%define libiniparser_name libiniparser
%endif

%package -n %{libiniparser_name}
Summary:        Library to parse ini files
Group:          System/Libraries

%description -n %{libiniparser_name}
Libiniparser offers parsing of ini files from the C level.

This package includes the libiniparser%{sonum} library.

%package -n libiniparser-devel
Summary:        Libraries and Header Files to Develop Programs with libiniparser Support
Group:          Development/Libraries/C and C++
%if 0%{?suse_version} == 0 || 0%{?suse_version} > 1100
Requires:       %{libiniparser_name} = %{version}
%else
Requires:       libiniparser = %{version}
%endif

%description -n libiniparser-devel
This package contains the static libraries and header files needed to
develop programs which make use of the libiniparser programming
interface.

The libiniparser offers parsing of ini files from the C level.	See a
complete documentation in HTML format, from the
%{_docdir}/libiniparser-devel directory open the file
html/index.html with any HTML-capable browser.

Libraries and Header Files to Develop Programs with iniparser Support.

%prep
%setup -q
%patch00 -p1

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC"

%install
install -d -m 0755 %{buildroot}%{_includedir}
install -d -m 0755 %{buildroot}%{_libdir}
install -m 0755 libiniparser.so.%{sonum} %{buildroot}%{_libdir}
install -m 0644 src/{dictionary,iniparser}.h %{buildroot}%{_includedir}
ln -s -f libiniparser.so.%{sonum} %{buildroot}%{_libdir}/libiniparser.so

%check
ln -s libiniparser.so.%{sonum} libiniparser.so
make %{?_smp_mflags} check

%post -n %{libiniparser_name} -p /sbin/ldconfig
%postun -n %{libiniparser_name} -p /sbin/ldconfig

%files -n %{libiniparser_name}
%{_libdir}/libiniparser.so.*
%doc LICENSE

%files -n libiniparser-devel
%{_includedir}/*.h
%{_libdir}/libiniparser.so
%doc html

%changelog
