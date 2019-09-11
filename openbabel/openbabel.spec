#
# spec file for package openbabel
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           openbabel
Version:        2.4.1
Release:        1.5
Summary:        A chemistry toolbox
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://openbabel.sourceforge.net/
Source0:        https://sourceforge.net/projects/openbabel/files/openbabel/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.changes
Source2:        baselibs.conf
Patch0:         fix_narrowing.patch
Patch1:         fix_yasara.patch
BuildRequires:  cairo-devel
BuildRequires:  cmake >= 2.4.8
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  swig
BuildRequires:  zlib-devel
BuildRequires:  wxWidgets-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Open Babel is a chemical toolbox understanding many formats of
chemical data. It allows to search, convert, analyze, or store data
from molecular modeling, chemistry, solid-state materials,
biochemistry, or related areas.

%package -n libopenbabel5
Summary:        Component library of Open Babel, a chemistry toolbox
Group:          System/Libraries

%description -n libopenbabel5
Open Babel is a chemical toolbox understanding many formats of
chemical data. It allows to search, convert, analyze, or store data
from molecular modeling, chemistry, solid-state materials,
biochemistry, or related areas.

%package -n libinchi0
Summary:        Component library of Open Babel, a chemistry toolbox
Group:          System/Libraries

%description -n libinchi0
Open Babel is a chemical toolbox understanding many formats of
chemical data. It allows to search, convert, analyze, or store data
from molecular modeling, chemistry, solid-state materials,
biochemistry, or related areas.

%package -n python-openbabel
Summary:        Python bindings for Open Babel, a chemistry toolbox
Group:          Productivity/Scientific/Chemistry
%py_requires

%description -n python-openbabel
Open Babel is a chemical toolbox understanding many formats of
chemical data. It allows to search, convert, analyze, or store data
from molecular modeling, chemistry, solid-state materials,
biochemistry, or related areas.

%package devel
Summary:        Development files for Open Babel
Group:          Development/Libraries/C and C++
Requires:       libopenbabel5 = %{version}
Requires:       zlib-devel
Provides:       libopenbabel-devel = %{version}
Obsoletes:      libopenbabel-devel < %{version}

%description devel
Open Babel is a chemical toolbox understanding many formats of
chemical data. It allows to search, convert, analyze, or store data
from molecular modeling, chemistry, solid-state materials,
biochemistry, or related areas.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# fix builddate info
# Remove build time references so build-compare can do its work
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{SOURCE1} '+%%H:%%M')
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{SOURCE1} '+%%b %%e %%Y')
sed -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" -i tools/babel.cpp tools/obabel.cpp
sed -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -i tools/babel.cpp tools/obabel.cpp

%build
%cmake \
%if 0%{?suse_version} > 1320
%ifarch ppc64 ppc64le
      -DCMAKE_CXX_FLAGS="%{optflags} -std=gnu++98" \
%endif
%endif
      -DCMAKE_BUILD_TYPE="Release" \
      -DRUN_SWIG=ON \
      -DPYTHON_BINDINGS=ON \
      -DPYTHON_EXECUTABLE=%{_bindir}/python2 \
      -DBUILD_GUI=FALSE \
      -ULIB_INSTALL_DIR
make %{?_smp_mflags}

%install
pushd build
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%post -n libinchi0 -p /sbin/ldconfig
%postun -n libinchi0 -p /sbin/ldconfig

%post -n libopenbabel5 -p /sbin/ldconfig
%postun -n libopenbabel5 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/roundtrip
%{_bindir}/ob*
%{_bindir}/babel
%{_mandir}/man1/*
%{_libdir}/openbabel
%{_datadir}/openbabel

%files -n libinchi0
%defattr(-,root,root,-)
%{_libdir}/libinchi.so.0
%{_libdir}/libinchi.so.0.4.1

%files -n libopenbabel5
%defattr(-,root,root,-)
%{_libdir}/libopenbabel.so.5
%{_libdir}/libopenbabel.so.5.0.0

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/inchi
%dir %{_includedir}/openbabel-2.0
%dir %{_libdir}/cmake/openbabel2
%{_includedir}/inchi/inchi_api.h
%{_includedir}/openbabel-2.0/openbabel/
%{_libdir}/cmake/openbabel2/OpenBabel2Config.cmake
%{_libdir}/cmake/openbabel2/OpenBabel2ConfigVersion.cmake
%{_libdir}/cmake/openbabel2/OpenBabel2_EXPORTS*.cmake
%{_libdir}/libinchi.so
%{_libdir}/libopenbabel.so
%{_libdir}/pkgconfig/openbabel-2.0.pc

%files -n python-openbabel
%defattr(-,root,root,-)
%{python_sitearch}*

%changelog
