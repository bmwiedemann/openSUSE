#
# spec file for package gmsh
#
# Copyright (c) 2022 SUSE LLC
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


%define libver 4_11
%bcond_with static_lib
%bcond_with pdf_doc
# julia dropped from oS:Factory [2022-06-10 13:57:27]
%bcond_with julia
Name:           gmsh
Version:        4.11.1
Release:        0
Summary:        A three-dimensional finite element mesh generator
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gmsh.info/
Source0:        https://gmsh.info/src/gmsh-%{version}-source.tgz
Patch0:         link_dynamic_gl2ps.patch
Patch1:         gmsh-2.10.1-implicit.patch
Patch2:         gmsh-3.0.5-add-shebang-to-onelab.patch
BuildRequires:  Mesa-devel
BuildRequires:  cgns-devel >= 3.4.0
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  fltk-devel >= 1.1.7
BuildRequires:  gcc-c++
BuildRequires:  gl2ps-devel >= 1.4.1
BuildRequires:  glu-devel
BuildRequires:  gmp-devel
BuildRequires:  hdf5-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  makeinfo
BuildRequires:  metis-devel
BuildRequires:  occt-devel
BuildRequires:  python-rpm-macros
BuildRequires:  zlib-devel
%if %{with pdf_doc}
BuildRequires:  texinfo-texlive
%endif

%description
Gmsh is a 3D finite element grid generator with a build-in CAD engine
and post-processor.

%package -n libgmsh%{libver}
Summary:        A three-dimensional finite element mesh generator
# Added API in 1.4.1
Group:          System/Libraries
Requires:       libgl2ps1 >= 1.4.1

%description -n libgmsh%{libver}
Gmsh is a 3D finite element grid generator with a build-in CAD engine
and post-processor.

This package contains the shared libraries.

%package        devel
Summary:        A three-dimensional finite element mesh generator
Group:          Development/Libraries/C and C++
Requires:       libgmsh%{libver} = %{version}
# Old name used by gmsh 3.2
Conflicts:      libGmsh-devel

%description    devel
Gmsh is a 3D finite element grid generator with a build-in CAD engine
and post-processor.

This package contains the header files needed for development.

%package        devel-static
Summary:        A three-dimensional finite element mesh generator
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel

%description    devel-static
Gmsh is a 3D finite element grid generator with a build-in CAD engine
and post-processor.

This package contains the static version of the libraries for
development.

%package        doc
Summary:        A three-dimensional finite element mesh generator
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
Gmsh is a 3D finite element grid generator with a build-in CAD engine
and post-processor.

This package contains the documentation for gmsh.

%package        demos
Summary:        A three-dimensional finite element mesh generator
Group:          Development/Libraries/C and C++
Recommends:     %{name}
BuildArch:      noarch

%description    demos
Gmsh is a 3D finite element grid generator with a build-in CAD engine
and post-processor.

This package contains demos and tutorials.

%package -n gmsh-julia
Summary:        Julia API for the gmsh mesh generator
Group:          Development/Libraries
Requires:       julia
Requires:       libgmsh%{libver}
Suggests:       %{name}-demos
Supplements:    packageand(julia:gmsh)
BuildArch:      noarch

%description  -n gmsh-julia
Gmsh is a 3D finite element grid generator with a build-in CAD engine
and post-processor.

This package contains the public gmsh API for Julia.

%package -n python3-gmsh
Summary:        Python API for the gmsh mesh generator
Group:          Development/Libraries
Requires:       libgmsh%{libver}
Suggests:       %{name}-demos
Supplements:    packageand(python3-base:gmsh)
BuildArch:      noarch

%description  -n python3-gmsh
Gmsh is a 3D finite element grid generator with a build-in CAD engine
and post-processor.

This package contains the public gmsh API for Python.

%prep
%autosetup -p1 -n %{name}-%{version}-source

%build
%cmake \
  -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name}/ \
  -DENABLE_BUILD_SHARED:BOOL=ON \
  -DENABLE_BUILD_DYNAMIC:BOOL=ON \
  -DENABLE_OPENMP:BOOL=ON \
  -DENABLE_SYSTEM_CONTRIB:BOOL=ON \
  -DENABLE_BUILD_LIB:BOOL=%{?with static_lib:ON}%{!?with static_lib:OFF} \
  -DPACKAGER=OBS \
  -DGMSH_HOST=OBS \

# build libs/binaries
%cmake_build all

# build documentation
%cmake_build info html
%if %{with pdf_doc}
%cmake_build pdf
%endif

%install
%cmake_install
# Cleanup installation
rm -Rf %{buildroot}/`pwd`

# The info file is not installed by make install
mkdir -p %{buildroot}%{_infodir}
mv doc/texinfo/gmsh.info %{buildroot}%{_infodir}

chmod 755 %{buildroot}/%{_bindir}/*

# mv python API into python's search path, dito for julia
mkdir -p %{buildroot}%{python3_sitelib}
mv %{buildroot}%{_libdir}/gmsh.py %{buildroot}%{python3_sitelib}/gmsh.py
mv %{buildroot}%{_libdir}/gmsh-*.dist-info %{buildroot}%{python3_sitelib}/

%if %{with julia}
mkdir -p %{buildroot}%{_datadir}/julia
mv %{buildroot}%{_libdir}/gmsh.jl %{buildroot}%{_datadir}/julia/gmsh.jl
%else
rm %{buildroot}%{_libdir}/gmsh.jl
rm %{buildroot}%{_docdir}/%{name}/examples/api/*.jl
rm -Rf %{buildroot}%{_docdir}/%{name}/tutorials/julia
%endif

%fdupes %{buildroot}/%{_docdir}/%{name}/{examples,tutorials}

%post -n libgmsh%{libver} -p /sbin/ldconfig

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun -n libgmsh%{libver} -p /sbin/ldconfig

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%{_mandir}/*/*
%{_infodir}/%{name}.*
%{_bindir}/*

%files -n libgmsh%{libver}
%{_libdir}/libgmsh.so.*

%if %{with julia}
%files -n gmsh-julia
%dir %{_datadir}/julia
%{_datadir}/julia/gmsh.jl
%endif

%files -n python3-gmsh
%{python3_sitelib}/gmsh.py
%{python3_sitelib}/gmsh-*.dist-info

%files devel
%{_includedir}/gmsh*
%{_libdir}/libgmsh.so

%if %{with static_lib}
%files devel-static
%{_libdir}/libgmsh.a
%endif

%files doc
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*.txt
%doc %{_docdir}/%{name}/images
%doc %{_docdir}/%{name}/gmsh.html

%files demos
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/examples
%{_docdir}/%{name}/tutorials

%changelog
