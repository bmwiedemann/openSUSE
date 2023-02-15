#
# spec file for package ngspice
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_with    oldapps

%global flavor @BUILD_FLAVOR@%{nil}

%if "%flavor" == "shlibs"
%define build_shared 1
%endif
%define pname   ngspice

Name:           %pname%{?build_shared:-shared}
%define so_ver 0
Version:        39
Release:        0
Summary:        Mixed-level, Mixed-signal Circuit Simulator Based on spice3f5
License:        BSD-2-Clause
Group:          Productivity/Scientific/Electronics
URL:            https://ngspice.sourceforge.io
Source0:        https://downloads.sourceforge.net/%{pname}/%{pname}-%{version}.tar.gz
Source1:        https://ngspice.sourceforge.io/docs/ngspice-%{version}-manual.pdf
BuildRequires:  bison
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(tinfo)
%if ! 0%{?build_shared}
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXmu-devel
%endif
Requires:       %{pname}-scripts = %{version}
Requires:       %{pname}-xspice-cm = %{version}
Recommends:     %{pname}-doc = %{version}

%description
Ngspice is a mixed-level/mixed-signal circuit simulator. Its code
is based on three open source software packages: Spice3f5, Cider1b1
and Xspice.

%package oldapps
Summary:        Some deprecated applications included in ngspice
Group:          Productivity/Scientific/Electronics
Requires:       %{pname} = %{version}
Provides:       %{pname}:%{_bindir}/ngmakeidx

%description oldapps
Some deprecated applications formerly distributed in the main
ngspice package:
- ngmakeidx
- ngmultidec
- ngnutmeg
- ngproc2mod
- ngsconvert

%package doc
Summary:        Documentation for ngspice
Group:          Documentation/Other
Recommends:     %{pname} = %{version}
BuildArch:      noarch

%description doc
Ngspice is a mixed-level/mixed-signal circuit simulator. Its code
is based on three open source software packages: Spice3f5, Cider1b1
and Xspice.

%package xspice-cm
Summary:        Xspice code model Plugins
Group:          Productivity/Scientific/Electronics

%description xspice-cm
Ngspice is a mixed-level/mixed-signal circuit simulator. Its code
is based on three open source software packages: Spice3f5, Cider1b1
and Xspice. This package contains the Xspice code model plugins.

%package scripts
Summary:        Ngspice init scripts
Group:          Productivity/Scientific/Electronics
# https://sourceforge.net/p/ngspice/bugs/615/
# BuildArch:      noarch

%description scripts
Ngspice is a mixed-level/mixed-signal circuit simulator. Its code
is based on three open source software packages: Spice3f5, Cider1b1
and Xspice. This package contains the ngspice init scripts shared
between ngspice and libngspice.

%package -n lib%{pname}%{so_ver}
Summary:        Shared libraries for ngspice
Group:          System/Libraries
Requires:       %{pname}-scripts
Requires:       %{pname}-xspice-cm

%description -n lib%{pname}%{so_ver}
Ngspice is a mixed-level/mixed-signal circuit simulator. Its code
is based on three open source software packages: Spice3f5, Cider1b1
and Xspice. This package contains the shared libraries.

%package -n lib%{pname}-devel
Summary:        Development files for ngspice
Group:          Development/Libraries/Other
Requires:       lib%{pname}%{so_ver} = %{version}

%description -n lib%{pname}-devel
Ngspice is a mixed-level/mixed-signal circuit simulator. Its code
is based on three open source software packages: Spice3f5, Cider1b1
and Xspice. This package contains the development files.

%prep
%setup -q -n ngspice-%{version}
cp %{S:1} .
%autopatch -p1

%build
export CFLAGS="%{optflags} -fPIE"
export LDFLAGS="-pie"
%configure \
    --disable-debug \
%if 0%{?build_shared}
    --with-ngshared \
%else
    --with-x \
    %{?with_oldapps:--enable-oldapps} \
%endif
    --with-readline=yes \
    --enable-xspice \
    --enable-cider \
    --enable-openmp

%make_build

%install
%make_install
chmod -x ANALYSES AUTHORS BUGS DEVICES FAQ NEWS README

%if ! 0%{?build_shared}
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_mandir}/man1/cmpp.1*
%else
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_includedir}/config.h
# Remove files distributed in the main package
rm -rf %{buildroot}/%{_mandir} \
       %{buildroot}%{_libdir}/%{pname} \
       %{buildroot}%{_datadir}/%{pname}/scripts
%endif

%post -n lib%{pname}%{so_ver} -p /sbin/ldconfig
%postun -n lib%{pname}%{so_ver} -p /sbin/ldconfig

%if ! 0%{?build_shared}
%files
%license COPYING
%doc ANALYSES AUTHORS BUGS DEVICES FAQ NEWS README
%{_bindir}/ngspice
%{_mandir}/man1/ngspice.1%{?ext_man}
%dir %{_datadir}/ngspice

%if 0%{?with_oldapps}
%files oldapps
%{_bindir}/ngmakeidx
%{_bindir}/ngmultidec
%{_bindir}/ngnutmeg
%{_bindir}/ngproc2mod
%{_bindir}/ngsconvert
%{_mandir}/man1/ngmakeidx.1%{?ext_man}
%{_mandir}/man1/ngmultidec.1%{?ext_man}
%{_mandir}/man1/ngnutmeg.1%{?ext_man}
%{_mandir}/man1/ngproc2mod.1%{?ext_man}
%{_mandir}/man1/ngsconvert.1%{?ext_man}
%endif

%files scripts
%{_datadir}/ngspice/scripts

%files doc
%doc ngspice-%{version}-manual.pdf

%files xspice-cm
%{_libdir}/%{pname}

%else

%files -n lib%{pname}%{so_ver}
%{_libdir}/lib%{pname}.so.*

%files -n lib%{pname}-devel
%dir %{_includedir}/%{pname}
%{_includedir}/%{pname}/sharedspice.h
%{_libdir}/lib%{pname}.so
%{_libdir}/pkgconfig/%{pname}.pc
%endif

%changelog
