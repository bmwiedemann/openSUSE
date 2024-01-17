#
# spec file for package lib3ds
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


%define libname %{name}-1-3
Name:           lib3ds
Version:        1.3.0
Release:        0
Summary:        Import and Export of Autodesk 3DS Files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://lib3ds.sourceforge.net
Source0:        %{name}-%{version}.tar.bz2
Patch0:         lib3ds-pkgconfig.patch
Patch1:         lib3ds-mesh.c.patch
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
Lib3ds is a free alternative to Autodesk's 3DS File Toolkit for
handling 3DS files. Its main goal is to simplify the creation of 3DS
import and export filters.

%package -n %{libname}
Summary:        Import and Export of Autodesk 3DS Files
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}

%description -n %{libname}
Lib3ds is a free alternative to Autodesk's 3DS File Toolkit for
handling 3DS files. Its main goal is to simplify the creation of 3DS
import and export filters.

%package devel
Summary:        Import and Export of Autodesk 3DS Files
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       glibc-devel

%description devel
Lib3ds is a free alternative to Autodesk's 3DS File Toolkit for
handling 3DS files. Its main goal is to simplify the creation of 3DS
import and export filters.

%prep
%autosetup -p1

%build
autoreconf -fvi
export CFLAGS="%{optflags}"
%configure \
    --enable-shared \
    --disable-static
%make_build

%install
rm -rf examples/.deps
%make_install
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
install -m644 lib3ds.pc %{buildroot}%{_libdir}/pkgconfig/
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%files -n %{libname}
%{_libdir}/lib3ds-1.so.3*

%files devel
%doc AUTHORS README COPYING ChangeLog examples
%dir %{_includedir}/lib3ds
%{_bindir}/3dsdump
%{_includedir}/lib3ds/*.h
%{_bindir}/lib3ds-config
%{_mandir}/man1/*gz
%{_libdir}/lib3ds.so
%{_datadir}/aclocal/lib3ds.m4
%{_libdir}/pkgconfig/lib3ds.pc

%post -n %{libname}  -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%changelog
