#
# spec file for package python-espressopp
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


%define modname espressopp
Name:           python-%{modname}
# Build with OpenMPI
%if 0%{?suse_version} >= 1330
  # OpenMPI >= 2 is not available on ppc64be
  %ifarch ppc64
    %define mpiver openmpi
  %else
    %define mpiver openmpi2
  %endif
%else
  # Keep OpenMPI1 for older releases where OpenMPI2 is not available
  %define mpiver openmpi
%endif
Version:        2.0
Release:        0
Summary:        Parallel simulation software for soft matter research
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Chemistry
Url:            http://www.espresso-pp.de/
Source0:        https://github.com/%{modname}/%{modname}/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM 229.patch: fix build with boost-1.67
Patch0:         https://github.com/espressopp/espressopp/pull/229.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel  >= 1.58.0
BuildRequires:  libboost_mpi-devel  >= 1.58.0
BuildRequires:  libboost_python-devel  >= 1.58.0
BuildRequires:  libboost_serialization-devel  >= 1.58.0
BuildRequires:  libboost_system-devel  >= 1.58.0
%else
BuildRequires:  boost-devel >= 1.58.0
%endif
BuildRequires:  %{mpiver}
BuildRequires:  %{mpiver}-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
Requires:       %{mpiver}
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  python-mpi4py-devel
Requires:       python-mpi4py
BuildRequires:  pkgconfig(fftw3)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel >= 1.58.0
BuildRequires:  libboost_mpi-devel >= 1.58.0
BuildRequires:  libboost_python-devel >= 1.58.0
BuildRequires:  libboost_serialization-devel >= 1.58.0
BuildRequires:  libboost_system-devel >= 1.58.0
%else
BuildRequires:  boost-devel >= 1.58.0
%endif
Requires:       python-h5py
BuildRequires:  python-h5py

%description
ESPResSo++ is an extensible, flexible, parallel simulation software
for soft matter research. It is a software package for the
scientific simulation and analysis of coarse-grained atomistic or bead-spring
models as they are used in soft matter research. ESPResSo and ESPResSo++ have
common roots and share parts of the developer/user community. However, their
development is independent and they are different software packages.

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1

# Remove bundled libs
rm -rf contrib/boost contrib/mpi4py

# Avoid unnecessary rebuilds of the package
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
sed -i -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" src/Version.cpp

%build
source %{_libdir}/mpi/gcc/%{mpiver}/bin/mpivars.sh

%cmake -DWITH_RC_FILES=OFF -DEXTERNAL_BOOST=ON -DEXTERNAL_MPI4PY=ON
#no parallel build to save memory
make

%install
make -C build install DESTDIR=%{buildroot}

#check
# not enough memory
#LD_LIBRARY_PATH='%{buildroot}/%{_libdir}::%{_libdir}/mpi/gcc/%{mpiver}/%{_lib}' make -C build test CTEST_OUTPUT_ON_FAILURE=1

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{python_sitearch}/%{modname}
%{python_sitearch}/_%{modname}.so

%changelog
