#
# spec file for package libnova
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define so_ver 0_15-0

Name:           libnova
Version:        0.15.0
Release:        0
Summary:        Celestial Mechanics, Astrometry and Astrodynamics Library
License:        LGPL-2.0+
Group:          System/Libraries
Url:            http://libnova.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM automake-1.13.patch asterios.dramis@gmail.com -- Fix build with automake 1.13
Patch0:         automake-1.13.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libnova is a general purpose, double precision, Celestial Mechanics,
Astrometry and Astrodynamics library. The intended audience of libnova
is C & C++ programmers, astronomers and anyone else interested in
calculating positions of astronomical objects or celestial mechanics.

%package devel
Summary:        Development files for libnova
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libnova-%{so_ver} = %{version}

%description devel
This package contains development files for libnova.

%package -n libnova-%{so_ver}
Summary:        Celestial Mechanics, Astrometry and Astrodynamics Library
Group:          System/Libraries

%description -n libnova-%{so_ver}
libnova is a general purpose, double precision, Celestial Mechanics,
Astrometry and Astrodynamics library. The intended audience of libnova
is C & C++ programmers, astronomers and anyone else interested in
calculating positions of astronomical objects or celestial mechanics.

%prep
%setup -q
%patch0

%build
# Regenerate build system because of errors about libtool during compilation
autoreconf -vif
echo 'HTML_TIMESTAMP=NO' >> doc/doxyfile.in
%configure --disable-static --with-pic
make CFLAGS+="%{optflags}" %{?_smp_mflags}
cd doc
make doc %{?_smp_mflags}
cd ..

%install
make DESTDIR=%{buildroot} install

# Manually install doc files in order to fix rpmlint warning "files-duplicate"
mkdir -p %{buildroot}%{_docdir}/%{name}-devel
cp -a doc/html/ %{buildroot}%{_docdir}/%{name}-devel/
cp -a AUTHORS COPYING ChangeLog NEWS %{buildroot}%{_docdir}/%{name}-devel/

# Remove libtool config files
rm -f %{buildroot}%{_libdir}/*.la

%fdupes -s %{buildroot}

%post -n libnova-%{so_ver} -p /sbin/ldconfig

%postun -n libnova-%{so_ver} -p /sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-devel/
%{_includedir}/libnova/
%{_libdir}/libnova.so
%{_bindir}/libnovaconfig

%files -n libnova-%{so_ver}
%defattr(-,root,root,-)
%{_libdir}/libnova-0.15.so.0*

%changelog
