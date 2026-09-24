#
# spec file for package fastjet
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           fastjet
Version:        3.5.1
Release:        0
Summary:        Package for jet finding in pp and e+e- collisions
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://fastjet.fr/
Source0:        http://fastjet.fr/repo/%{name}-%{version}.tar.gz
Source1:        %{name}.rpmlintrc
# PATCH-FIX-OPENSUSE fastjet-cmake-soversion.patch badshah400@gmail.com -- Add so versioning to cmake script consistent with autoconf build scripts
Patch0:         fastjet-cmake-soversion.patch
BuildRequires:  %{python_module devel}
BuildRequires:  cgal-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  swig

%define python_subpackage_only 1
%python_subpackages

%description
FastJet is a software package for jet finding in pp and e+e-
collisions. It includes fast native implementations of many sequential
recombination clustering algorithms, plugins for access to a range of
cone jet finders and tools for advanced jet manipulation.

It provides a fast implementation of several
longitudinally invariant sequential recombination jet algorithms, in
particular the longitudinally invariant kt jet algorithm, the
inclusive longitudinally invariant version of the Cambridge/Aachen
jet-algorithm, and the inclusive anti-kt algorithm.

%package -n libfastjet0
Summary:        Shared libraries for fastjet core package
Group:          Development/Libraries/C and C++

%description -n libfastjet0
FastJet is a software package for jet finding in pp and e+e-
collisions. It includes fast native implementations of many sequential
recombination clustering algorithms, plugins for access to a range of
cone jet finders and tools for advanced jet manipulation.

It provides a fast implementation of several
longitudinally invariant sequential recombination jet algorithms, in
particular the longitudinally invariant kt jet algorithm, the
inclusive longitudinally invariant version of the Cambridge/Aachen
jet-algorithm, and the inclusive anti-kt algorithm.

This package provides the shared libraries for fastjet and its
plugins.

%package -n fastjet-devel
Summary:        Shared libraries for fastjet core package
Group:          Development/Libraries/C and C++
Requires:       cgal-devel
Requires:       libfastjet0 = %{version}

%description -n fastjet-devel
FastJet is a software package for jet finding in pp and e+e-
collisions. It includes fast native implementations of many sequential
recombination clustering algorithms, plugins for access to a range of
cone jet finders and tools for advanced jet manipulation.

It provides a fast implementation of several
longitudinally invariant sequential recombination jet algorithms, in
particular the longitudinally invariant kt jet algorithm, the
inclusive longitudinally invariant version of the Cambridge/Aachen
jet-algorithm, and the inclusive anti-kt algorithm.

This package provides the header files for development with fastjet.

%package -n fastjet-plugin-siscone
Summary:        SISCone plugin for fastjet
Group:          Development/Libraries/C and C++

%description -n fastjet-plugin-siscone
FastJet is a software package for jet finding in pp and e+e-
collisions. It includes fast native implementations of many sequential
recombination clustering algorithms, plugins for access to a range of
cone jet finders and tools for advanced jet manipulation.

It provides a fast implementation of several
longitudinally invariant sequential recombination jet algorithms, in
particular the longitudinally invariant kt jet algorithm, the
inclusive longitudinally invariant version of the Cambridge/Aachen
jet-algorithm, and the inclusive anti-kt algorithm.

This package provides shared libraries for SISCone plugin for
fastjet.

%package -n fastjet-plugin-siscone-devel
Summary:        SISCone plugin for fastjet
Group:          Development/Libraries/C and C++
Requires:       fastjet-devel = %{version}
Requires:       fastjet-plugin-siscone = %{version}

%description -n fastjet-plugin-siscone-devel
FastJet is a software package for jet finding in pp and e+e-
collisions. It includes fast native implementations of many sequential
recombination clustering algorithms, plugins for access to a range of
cone jet finders and tools for advanced jet manipulation.

It provides a fast implementation of several
longitudinally invariant sequential recombination jet algorithms, in
particular the longitudinally invariant kt jet algorithm, the
inclusive longitudinally invariant version of the Cambridge/Aachen
jet-algorithm, and the inclusive anti-kt algorithm.

This package provides the develoment files for SISCone plugin for
fastjet.

%package -n python-%{name}
Summary:        Python bindings for fastjet
Group:          Development/Libraries/Python

%description -n python-%{name}
FastJet is a software package for jet finding in pp and e+e-
collisions.

This package provides python3 bindings for fastjet.

%prep
%autosetup -p1
sed -Ei "1{s@/usr/bin/env bash@%{_bindir}/bash@}" fastjet-config.in

%build

%{python_expand # multiple flavours of python
mkdir ../build_$python
cp -pr ./ ../build_$python
pushd ../build_$python
%cmake -DFASTJET_ENABLE_DEBUG:BOOL=OFF \
       -DFASTJET_ENABLE_CGAL:BOOL=ON \
       -DFASTJET_ENABLE_ALLCXXPLUGINS:BOOL=ON \
       -DFASTJET_BUILD_EXAMPLES:BOOL=OFF \
       -DFASTJET_ENABLE_PYTHON:BOOL=ON \
       -DPython_EXECUTABLE:PATH=%{_bindir}/$python \
       -DHAS_SHARED:STRING=yes \
        %{nil}
%cmake_build
popd
}

%install
%{python_expand # multiple flavours of python
pushd ../build_$python
%cmake_install
popd
}

%ldconfig_scriptlets -n libfastjet0
%ldconfig_scriptlets -n fastjet-plugin-siscone

%files -n libfastjet0
%license COPYING
%doc ChangeLog README.md
%{_libdir}/libfastjet.so.*
%{_libdir}/libfastjettools.so.*
%{_libdir}/libfastjetplugins.so.*

%files -n fastjet-devel
%{_bindir}/fastjet-config
%{_includedir}/fastjet/
%{_libdir}/libfastjet.so
%{_libdir}/libfastjettools.so
%{_libdir}/libfastjetplugins.so
%{_libdir}/cmake/%{name}/

%files -n fastjet-plugin-siscone
%{_libdir}/libsiscone*.so.*

%files -n fastjet-plugin-siscone-devel
%{_libdir}/libsiscone*.so
%{_includedir}/siscone/
%{_libdir}/cmake/siscone/

%files %{python_files fastjet}
%{python_sitearch}/%{name}/

%changelog
