#
# spec file for package jasper
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


Name:           jasper
Version:        2.0.22
Release:        0
Summary:        An Implementation of the JPEG-2000 Standard, Part 1
License:        SUSE-Public-Domain
Group:          Productivity/Graphics/Convertors
URL:            https://jasper-software.github.io/jasper
Source:         https://github.com/jasper-software/jasper/archive/version-%{version}.tar.gz
Source2:        baselibs.conf
BuildRequires:  Mesa-libGL-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  glu-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libdrm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig

%description
This package contains an implementation of the image compression
standard, JPEG-2000, Part 1. It consists of tools for conversion to and
from the JP2 and JPC formats.

%package -n libjasper4
Summary:        JPEG-2000 library
# bug437293
# used in <= 11.3
Group:          Productivity/Graphics/Convertors
Obsoletes:      libjasper < %{version}-%{release}
Provides:       libjasper = %{version}-%{release}
%ifarch ppc64
Obsoletes:      libjasper-64bit
%endif
#

%description -n libjasper4
This package contains libjasper, a library implementing the JPEG-2000
image compression standard Part 1.

%package -n libjasper-devel
Summary:        Development files for libjasper, a JPEG-2000 library
# bug437293
#
Group:          Development/Libraries/C and C++
Requires:       libjasper4 = %{version}
Requires:       libjpeg-devel
%ifarch ppc64
Obsoletes:      libjasper-devel-64bit
%endif

%description -n libjasper-devel
This package contains libjasper, a library implementing the JPEG-2000
image compression standard Part 1.

%prep
%setup -q -n %{name}-version-%{version}

%build
export CFLAGS="%{optflags} -Wall -std=c99 -D_BSD_SOURCE"
%cmake -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%cmake_install
mv doc/README doc/README.doc
%fdupes -s %{buildroot}/%{_docdir}/%{name}

%post -n libjasper4 -p /sbin/ldconfig
%postun -n libjasper4 -p /sbin/ldconfig

%files
%license LICENSE
%doc COPYRIGHT README doc/*
%doc %{_docdir}/jasper
%{_bindir}/imgcmp
%{_bindir}/imginfo
%{_bindir}/jasper
%{_bindir}/jiv
%{_mandir}/man*/*

%files -n libjasper4
%{_libdir}/libjasper*.so.*

%files -n libjasper-devel
%{_includedir}/jasper
%{_libdir}/libjasper.so
%{_libdir}/pkgconfig/jasper.pc

%changelog
