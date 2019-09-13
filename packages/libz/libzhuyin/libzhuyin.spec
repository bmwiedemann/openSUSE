#
# spec file for package libzhuyin
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


%define sover	7
Name:           libzhuyin
Version:        1.1.1
Release:        0
Summary:        Library to deal with zhuyin
License:        GPL-2.0
Group:          System/I18n/Chinese
Url:            https://github.com/libzhuyin/libzhuyin
Source:         %{name}-%{version}.tar.gz
Source1:        http://downloads.sourceforge.net/libzhuyin/models/model9.text.tar.gz
# PATCH-FIX-UPSTREAM marguerite@opensuse.org - no download when build
Patch:          libzhuyin-no-download.patch
# PATCH-FIX-UPSTREAM marguerite@opensuse.org 
# it will use current date eg. /usr/include/libzhuyin-0.9.99.20140716
# Don't do this
Patch1:         libzhuyin-no-random-version-number-includedir.patch
BuildRequires:  db-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gnome-common
BuildRequires:  libtool
Obsoletes:      libzhuyin-tools < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#
# libzhuyin has been source-merged with libpinyin and recent versions
# come from there.

%description
The libzhuyin project provides the algorithms core 
for intelligent sentence-based Chinese zhuyin input methods.

%package -n libzhuyin%{sover}
Summary:        Runtime libraries for libzhuyin 1.1
Group:          System/Libraries
Requires:       libzhuyin-1_1-data

%description -n libzhuyin%{sover}
The libzhuyin project provide the algorithms core
for intelligent sentence-based Chinese zhuyin input methods.

This package provides the runtime libraries for libzhuyin.

%package -n libzhuyin-1_1-data
Summary:        Data files for libzhuyin 1.1
Group:          System/I18n/Chinese

%description -n libzhuyin-1_1-data
The libzhuyin project aims to provide the algorithms core
for intelligent sentence-based Chinese zhuyin input methods.

This package provides the data files used by libzhuyin%{sover} to be functional.

%package -n libzhuyin-1_1-devel
Summary:        Development headers for libzhuyin
Group:          Development/Libraries/C and C++
Requires:       libzhuyin%{sover} = %{version}
Conflicts:      libzhuyin-devel

%description -n libzhuyin-1_1-devel
The libzhuyin project aims to provide the algorithms core
for intelligent sentence-based Chinese zhuyin input methods.

This package provides the development headers for libzhuyin project.

%prep
%setup -q
%patch -p1
%patch1 -p1
cp -r %{SOURCE1} data
pushd data &> /dev/null
tar -xf model9.text.tar.gz
popd &> /dev/null
NOCONFIGURE=1 ./autogen.sh
# Add version number to directory for (arch-dependent!) data
perl -i -lpe 's{^pkgdatadir=.*}{pkgdatadir=\@libdir\@/\@PACKAGE_NAME\@-1.1}' *.pc.in

%build
%configure --disable-static
make %{?_smp_mflags} libzhuyin_dbdir='${libdir}/${PACKAGE_NAME}-1.1/data'

%install
%make_install %{?_smp_mflags} libzhuyin_dbdir='${libdir}/${PACKAGE_NAME}-1.1/data'
rm -rf %{buildroot}/%{_libdir}/%{name}.la
%fdupes %{buildroot}/%{_prefix}

%post -n libzhuyin%{sover} -p /sbin/ldconfig

%postun -n libzhuyin%{sover} -p /sbin/ldconfig

%files -n libzhuyin%{sover}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/%{name}.so.*

%files -n libzhuyin-1_1-data
%defattr(-,root,root)
%{_libdir}/%{name}-1.1/

%files -n libzhuyin-1_1-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_includedir}/%{name}-%{version}
%{_libdir}/%{name}.so
%{_libdir}/libzhuyin.so
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/%{name}.1.gz

%changelog
