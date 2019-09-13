#
# spec file for package gmsh
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%define libver 4_4
%bcond_with static_lib
%bcond_with python_bindings
%bcond_with pdf_doc

Name:           gmsh
Summary:        A three-dimensional finite element mesh generator
License:        GPL-2.0
Group:          Productivity/Scientific/Math
Version:        4.4.1
Release:        0
Url:            http://gmsh.info/
Source0:        http://gmsh.info/src/gmsh-%{version}-source.tgz

Patch0:         link_dynamic_gl2ps.patch
Patch1:         gmsh-2.10.1-implicit.patch
#this isn't needed to correctly compile documentation on versions after Leap_42.3
%if 0%{?suse_version} <= 120300
Patch5:         gmsh-3.0.5-doc-building.patch
%endif
Patch6:         gmsh-3.0.5-add-shebang-to-onelib.patch
Patch7:         0001-Fix-ODR-violations-move-private-classes-into-anonymo.patch
Patch8:         0002-Fix-two-definition-mismatches-in-contrib-mmg3d.patch

BuildRequires:  bison
BuildRequires:  cmake >= 2.8
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  Mesa-devel
BuildRequires:  glu-devel
BuildRequires:  blas-devel
BuildRequires:  cgns-devel >= 3.4.0
BuildRequires:  fltk-devel >= 1.1.7
BuildRequires:  gl2ps-devel
BuildRequires:  gmp-devel
BuildRequires:  hdf5-devel
BuildRequires:  lapack-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  makeinfo
BuildRequires:  metis-devel
BuildRequires:  oce-devel
BuildRequires:  zlib-devel
%if %{with pdf_doc}
BuildRequires:  texinfo-texlive
%endif
%if %{with python_bindings}
BuildRequires:  swig
BuildRequires:  python-devel
%endif

%description
Gmsh is a 3D finite element grid generator with a build-in CAD engine
and post-processor.


%package -n libgmsh%{libver}
Summary:        A three-dimensional finite element mesh generator
Group:          System/Libraries

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

%description    doc
Gmsh is a 3D finite element grid generator with a build-in CAD engine
and post-processor.

This package contains the documentation for gmsh.

%package        demos
Summary:        A three-dimensional finite element mesh generator
Group:          Development/Libraries/C and C++
Recommends:     %{name}

%description    demos
Gmsh is a 3D finite element grid generator with a build-in CAD engine
and post-processor.

This package contains demos and tutorials.

%prep
%setup  -q -n %{name}-%{version}-source
%patch0 -p1
%patch1 -p1
%if 0%{?suse_version} <= 120300
%patch5 -p1
%endif
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
%global _lto_cflags %{nil}
%cmake \
  -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name}/ \
  -DENABLE_BUILD_SHARED:BOOL=ON \
  -DENABLE_BUILD_DYNAMIC:BOOL=ON \
  -DENABLE_SYSTEM_CONTRIB:BOOL=ON \
  -DENABLE_BUILD_LIB:BOOL=%{?with static_lib:ON}%{!?with static_lib:OFF} \

# build libs/binaries
make %{?_smp_mflags} all

# build documentation
make %{?_smp_mflags} info html
%if %{with pdf_doc}
make %{?_smp_mflags} pdf
%endif

%install
%cmake_install
# Cleanup installation
rm -Rf %{buildroot}/`pwd`

# The info file is not installed by make install
mkdir -p %{buildroot}%{_infodir}
mv doc/texinfo/gmsh.info %{buildroot}%{_infodir}

chmod 755 %{buildroot}/%{_bindir}/*

%post -n libgmsh%{libver} -p /sbin/ldconfig

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun -n libgmsh%{libver} -p /sbin/ldconfig

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%doc %{_mandir}/*/*
%doc %{_infodir}/%{name}.*
%{_bindir}/*

%files -n libgmsh%{libver}
%{_libdir}/libgmsh.so.*
%{_libdir}/gmsh.jl
%{_libdir}/gmsh.py

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
%doc %{_docdir}/%{name}/gmsh.html

%files demos
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/demos
%{_docdir}/%{name}/tutorial

%changelog
