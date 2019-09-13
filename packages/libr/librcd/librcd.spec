#
# spec file for package librcd
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


%define major   0

Name:           librcd
Version:        0.1.14
Release:        0
Summary:        Russian Character Set Detection Library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://rusxmms.sourceforge.net
Source:         http://darksoft.org/files/rusxmms/%name-%version.tar.bz2
Source100:      baselibs.conf
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
librcd is a library for automatic encoding detection of
Russian/Ukrainian language texts.

%package -n %{name}%{major}
Summary:        Russian Charset Detection Library
Group:          System/Libraries

%description -n %{name}%{major}
librcd is a library for automatic encoding detection of
Russian/Ukrainian language texts. It is optimized for very small
words and phrases.

%package devel
Summary:        Development files for librcd, a charset detection library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{major} = %{version}

%description devel
librcd is a library for automatic encoding detection of
Russian/Ukrainian language texts. It is optimized for very small
words and phrases.

This subpackage contains libraries and header files for developing
applications that want to make use of librcd.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{_builddir}/%{name}-%{version}/examples/{.deps,Makefile}

%post -n %{name}%{major} -p /sbin/ldconfig

%postun -n %{name}%{major} -p /sbin/ldconfig

%files -n %{name}%{major}
%defattr(-,root,root,-)
%{_libdir}/librcd.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README examples
%{_includedir}/*
%{_libdir}/librcd.so
%{_libdir}/pkgconfig/*

%changelog
