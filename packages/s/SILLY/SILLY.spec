#
# spec file for package SILLY
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


%define SILLYso 1

Name:           SILLY
Version:        0.1.0
Release:        0
Summary:        Simple Image Loading LibrarY
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://cegui.org.uk/wiki/SILLY
Source0:        http://prdownloads.sourceforge.net/crayzedsgui/%{name}-%{version}.tar.gz
Source1:        http://prdownloads.sourceforge.net/crayzedsgui/%{name}-DOCS-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Debian patch 01_SILLYPNGImageLoader.patch
Patch1:         01_SILLYPNGImageLoader.patch
# PATCH-FIX-UPSTREAM SILLY-gcc47.patch
Patch2:         SILLY-gcc47.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SILLY means Simple Image Loading LibrarY. The aim of this library is to provide
a simple library for loading image in the context of CEGUI. The library supports
only the most common image format. The project was initially launch in order
to provide an MIT based replacement of DevIL with less image format supported
and focused on loading image only.

%package -n lib%{name}%{SILLYso}
Summary:        Simple Image Loading LibrarY
Group:          System/Libraries

%description -n lib%{name}%{SILLYso}
SILLY means Simple Image Loading LibrarY. The aim of this library is to provide
a simple library for loading image in the context of CEGUI. The library supports
only the most common image format. The project was initially launch in order
to provide an MIT based replacement of DevIL with less image format supported
and focused on loading image only.

%package -n lib%{name}-devel
Summary:        Simple Image Loading LibrarY development package
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{SILLYso} = %{version}

%description -n lib%{name}-devel
Development files for libSILLY
SILLY means Simple Image Loading LibrarY. The aim of this library is to provide
a simple library for loading image in the context of CEGUI. The library supports
only the most common image format. The project was initially launch in order
to provide an MIT based replacement of DevIL with less image format supported
and focused on loading image only.

%prep
%setup -b 1 -D -q
%patch1 -p1
%patch2 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/libSILLY.la
mkdir -p %{buildroot}%{_defaultdocdir}/libSILLY-devel
cp -R doc/html/* %{buildroot}%{_defaultdocdir}/libSILLY-devel
%fdupes %{buildroot}%{_defaultdocdir}/lib%{name}-devel

%post -n lib%{name}%{SILLYso} -p /sbin/ldconfig
%postun -n lib%{name}%{SILLYso} -p /sbin/ldconfig

%files -n lib%{name}%{SILLYso}
%defattr(-,root,root)
%doc AUTHORS
%license COPYING
%doc ChangeLog
%{_libdir}/libSILLY.so.%{SILLYso}*

%files -n lib%{name}-devel
%defattr(-,root,root)
%docdir %{_defaultdocdir}/lib%{name}-devel
%{_defaultdocdir}/lib%{name}-devel/
%{_includedir}/SILLY
%{_libdir}/libSILLY.so
%{_libdir}/pkgconfig/SILLY.pc

%changelog
