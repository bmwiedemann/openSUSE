#
# spec file for package libfunambol
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


%define libname %{name}-9_0_1
Name:           libfunambol
Version:        9.0.1
Release:        0
Summary:        C++ SyncML Client Engine
License:        AGPL-3.0
Group:          Development/Libraries/C and C++
Url:            http://funambol.com
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libfunambol allows to integrate a SyncML stack in a C++ application on a
variety of platforms. Currently, Windows, Windows Mobile and Linux, Mac OS X,
iPhone and Symbian are actively supported, but you can easily build it on other
Unixes or other mobile/embedded platforms.

%package -n %{libname}
Summary:        C++ SyncML Client Engine
# O/P erroneous earlier name - remove when going to 9.0.2 or above.
Group:          System/Libraries
Obsoletes:      libfunambol9
Provides:       libfunambol9

%description -n %{libname}
Libfunambol allows to integrate a SyncML stack in a C++ application on a
variety of platforms. Currently, Windows, Windows Mobile and Linux, Mac OS X,
iPhone and Symbian are actively supported, but you can easily build it on other
Unixes or other mobile/embedded platforms.

%package devel
Summary:        C++ SyncML Client Engine
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       libcurl-devel

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libfunambol.

%prep
%setup -q

%build
cd build/autotools
autoreconf -fvi
%configure \
    --disable-static \
    --disable-unit-tests \
    --disable-integration-tests
make %{?_smp_mflags}

%install
cd build/autotools
make %{?_smp_mflags} DESTDIR=%{buildroot} install
cd ../..
# remove unneeded files
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_includedir}/funambol/test
# install additional documentation
install -d %{buildroot}%{_docdir}/%{libname}
install -m 0644 {LICENSE,TODO,changeslog}.txt README %{buildroot}%{_docdir}/%{libname}
install -m 0644 docs/funambol-cppsdk-tutorial.pdf %{buildroot}%{_docdir}/%{libname}
install -d %{buildroot}%{_docdir}/%{libname}/html
install -m 0644 docs/html/* %{buildroot}%{_docdir}/%{libname}/html

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr (-,root,root)
%doc LICENSE.txt
%{_libdir}/%{name}-9.0.1.so
%{_docdir}/%{libname}

%files devel
%defattr (-,root,root)
%{_includedir}/funambol
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/libfunambol.pc
%doc TODO.txt changeslog.txt README docs/funambol-cppsdk-tutorial.pdf docs/html

%changelog
