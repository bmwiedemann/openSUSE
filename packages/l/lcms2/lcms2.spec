#
# spec file for package lcms2
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           lcms2
Summary:        Little CMS Engine - A color managment library and tools
License:        MIT
Group:          Productivity/Graphics/Other
Url:            http://www.littlecms.com/
Version:        2.9
Release:        0

%if 0%{?suse_version}
BuildRequires:  autoconf
BuildRequires:  glibc-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
%endif

%if 0%{?fedora_version}
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%endif

%if 0%{?mandriva_version}
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://sourceforge.net/projects/lcms/files/lcms/%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch1:         lcms2-ocloexec.patch
Patch2:         lcms2-visibility.patch
# PATCH-FIX-SECURITY lcms2-cgats-memory-allocation.patch bsc1108813 CVE-2018-16435 sbrabec@suse.cz -- Add check on CGATS memory allocation.
Patch3:         lcms2-cgats-memory-allocation.patch

%description
Littlecms is a small speed optimized color management engine.
Little CMS intends to be a small-footprint color management engine
with a special focus on accuracy and performance. It uses the International
Color Consortium standard (ICC), which is the modern standard when
regarding to color management. The ICC specification is widely used and is
referred to in many International and other de-facto standards.

%package -n liblcms2-2
Summary:        Libraries for the Little CMS Engine
Group:          System/Libraries

%description -n liblcms2-2
Little CMS Engine - A color managment library and tools.

%package -n liblcms2-devel
Summary:        Include Files and Libraries Mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       liblcms2-2 = %{version}

%description -n liblcms2-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package -n liblcms2-doc
Summary:        User and developer documentation for lcms2
Group:          Documentation/Other
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description -n liblcms2-doc
This package contains user and developer documentation for lcms2.


%prep
%setup -q
%patch1
%patch2
%patch3 -p1

chmod a-x doc/* COPYING AUTHORS

%build

autoreconf -fiv
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"

# FIXME --without-threads is a workaround for a linker error
%configure --disable-static --without-threads

make %{?_smp_flags}

%check
# FIXME before submitting to factory
 make %{?_smp_flags} check || true
 make utils

%install
make install DESTDIR=%{buildroot}

rm %{buildroot}/%{_libdir}/liblcms2.la

%post -n liblcms2-2 -p /sbin/ldconfig

%postun -n liblcms2-2 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING AUTHORS
%{_bindir}/*
%{_mandir}/man?/*.*

%files -n liblcms2-2
%defattr(-,root,root)
%{_libdir}/liblcms2.so.2*

%files -n liblcms2-devel
%defattr(-,root,root)

%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n liblcms2-doc
%defattr(-,root,root)
%doc doc/*.pdf

%changelog
