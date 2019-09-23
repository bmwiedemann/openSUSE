#
# spec file for package votca-ctp
#
# Copyright (c) 2016-2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018-2019 Christoph Junghans
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


Name:           votca-ctp
Version:        1.5
%define         uversion %{version}
%define         sover 5
Release:        0
Summary:        VOTCA charge transport module
License:        Apache-2.0
Group:          Productivity/Scientific/Chemistry
Url:            http://www.votca.org
Source0:        https://github.com/votca/ctp/archive/v%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz
Source1:        https://github.com/votca/ctp/releases/download/v%{uversion}/votca-ctp-manual-%{uversion}.pdf

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gsl)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_program_options-devel >= 1.48.0
BuildRequires:  libboost_serialization-devel >= 1.48.0
BuildRequires:  libboost_filesystem-devel >= 1.48.0
BuildRequires:  libboost_system-devel >= 1.48.0
BuildRequires:  libboost_timer-devel >= 1.48.0
BuildRequires:  libboost_test-devel
%else
BuildRequires:  boost-devel >= 1.39.0
%endif
BuildRequires:  cmake >= 2.8.4
BuildRequires:  fdupes
BuildRequires:  votca-csg-devel = %{version}
BuildRequires:  libxc-devel
BuildRequires:  libceres-devel
BuildRequires:  hdf5-devel
 #for hdf5
BuildRequires:  zlib-devel

#exact same version is needed
Requires:       %{name}-common = %{version}
Requires:       libvotca_ctp%sover = %{version}

%description
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the charge transport module for VOTCA.

%package -n libvotca_ctp%sover
Summary:        VOTCA charge transport module
Group:          System/Libraries

%description -n libvotca_ctp%sover
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the charge transport module for VOTCA.

%package devel
Summary:        Development headers and libraries for VOTCA CTP
Group:          Development/Libraries/C and C++
Requires:       libvotca_ctp%sover = %{version}
Requires:       %{name} = %{version}
Requires:       votca-csg-devel = %{version}

%description devel
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the charge transport module for VOTCA.

%package common
Summary:        Architecture-independent data files for VOTCA CTP
Group:          Productivity/Scientific/Chemistry
BuildArch:      noarch

%description common
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the architecture-independent data files for VOTCA CTP.

%package doc
Summary:        Architecture independent doc files for VOTCA CTP
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Versatile Object-oriented Toolkit for Coarse-graining Applications (VOTCA) is
a package to reduce the amount of routine work when doing systematic
coarse-graining of various systems. The core is written in C++.

This package contains the architecture-independent documentation files for VOTCA CTP.

%prep
%setup -n ctp-%{uversion} -q

FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
sed -i -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" src/libctp/version.cc

# long.bst has non-profit purposes license, but it is not used for build
rm -v manual/long.bst

%build
%{cmake} -DCMAKE_SKIP_RPATH:BOOL=OFF -DLIB=%{_lib} -DBUILD_MANPAGES=ON -DENABLE_TESTING=ON
make #%{?_smp_mflags}

%install
%cmake_install
sed -i -e '1s@env python@python@'  %{buildroot}/%{_bindir}/ctp_*

%define pkgdocdir %{_docdir}/%{name}
mkdir -p %{buildroot}%{pkgdocdir}
cp %{S:1} %{buildroot}%{pkgdocdir}

%fdupes %{buildroot}%{_prefix}

%check
make -C build test CTEST_OUTPUT_ON_FAILURE=1

%post -n libvotca_ctp%sover -p /sbin/ldconfig
%postun -n libvotca_ctp%sover -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/ctp_*
%{_bindir}/kmc_*
%{_bindir}/moo_*
%{_mandir}/man1/ctp_*
%{_mandir}/man1/kmc_*
%{_mandir}/man1/moo_*

%files doc
%defattr(-,root,root,-)
%doc CHANGELOG.md NOTICE README.md
%license LICENSE.md
%{pkgdocdir}

%files common
%license LICENSE.md
%defattr(-,root,root,-)
%{_datadir}/votca

%files -n libvotca_ctp%sover
%defattr(-,root,root,-)
%{_libdir}/libvotca_*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/votca/ctp/
%{_includedir}/votca/moo/
%{_includedir}/votca/kmc/
%{_libdir}/libvotca_*.so
%{_libdir}/pkgconfig/libvotca_*.pc

%changelog
