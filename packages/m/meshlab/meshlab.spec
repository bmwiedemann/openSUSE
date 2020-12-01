#
# spec file for package meshlab
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


%if 0%{?suse_version} >= 1550
%bcond_without gmp
%else
%bcond_with    gmp
%endif

Name:           meshlab
Version:        2020.09
Release:        0
Summary:        System for the processing and editing of unstructured 3D triangular meshes
License:        GPL-2.0-or-later AND BSD-3-Clause
Group:          Productivity/Graphics/3D Editors
URL:            https://www.meshlab.net/
Source0:        https://github.com/cnr-isti-vclab/meshlab/archive/Meshlab-%{version}.tar.gz#/meshlab-%{version}.tar.gz
# Probably belongs in its own package, but nothing else depends on it
Source1:        https://github.com/cnr-isti-vclab/vcglib/archive/%{version}.tar.gz#/vcglib-%{version}.tar.gz

# PATCH-FIX-OPENSUSE -- put plugins and shaders in appropriate directories
Patch1:         meshlab-2016.12-plugin-path.patch
Patch2:         meshlab-2016.12-shader-path.patch
# consecutive double slashes cause a problem for debugedit,
# used by rpmbuild to extract debuginfo
Patch3:        meshlab-2016.12-remove-double-slash.patch
# PATCH-FIX-UPSTREAM -- fix build with vcglib release
Patch4:        Added-easyexif-minimal-lib-for-exif-loading.patch
Patch5:        Substituted-the-notorious-jhead-with-a-smaller-minimal-lib.patch
Patch6:        libjhead-removed.patch
Patch7:        fixed-cmake-removed-any-other-reference-to-jhead.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libbz2-devel
BuildRequires:  levmar-devel
BuildRequires:  muparser-devel
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  qhull-devel
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
%if %{with gmp}
BuildRequires:  pkgconfig(gmp)
%endif
BuildRequires:  pkgconfig(lib3ds)
# Optional, missing:
#BuildRequires:  pkgconfig(OpenCTM)
# Incompatibility between GLEW and Qt GLES builds
ExcludeArch:    %{arm} aarch64

# Do not add plugins to provides
%global __provides_exclude_from %{_libdir}/meshlab/plugins


%description
MeshLab is an open source, portable, and extensible system for the processing
and editing of unstructured large 3D triangular meshes. The source is
released under the GPL license. The system is aimed to help the processing
of the typical not-so-small unstructured models arising in 3D scanning,
providing a set of tools for editing, cleaning, healing, inspecting,
rendering and converting this kind of meshes.

%prep
%setup -q -a1 -n %{name}-Meshlab-%{version}
%patch1 -p1 -b .plugin-path
%patch2 -p1 -b .shader-path
%patch3 -p1 -b .remove-double-slash
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# rename vcglib folder
rmdir vcglib
mv vcglib-%{version} vcglib

# Remove bundled library sources, since we use the packaged libraries
#rm -rf vcglib/wrap/system/multithreading vcglib/wrap/system/*getopt* vcglib/wrap/system/time
rm -r src/external/{glew*,levmar*,lib3ds*,muparser*,qhull*}

# set plugin path
sed -i 's|PLUGIN_DIR|QString("%{_libdir}/meshlab")|g'  src/common/pluginmanager.cpp

%build
pushd src
%cmake
%cmake_build
popd


%install
pushd src
%cmake_install
popd

rm %{buildroot}%{_datadir}/pixmaps/meshlab.png
rmdir %{buildroot}%{_datadir}/pixmaps
for i in 16 48 64 128 512 ; do
  install -D -m 644 src/meshlab/images/eye${i}.png \
                    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/meshlab.png
done

sed -i -e 's/Icon=.*/Icon=meshlab/' %{buildroot}%{_datadir}/applications/meshlab.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/meshlab.desktop

install -D -m 0644 -t %{buildroot}%{_mandir}/man1/ docs/man/*.1


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/meshlab
%{_bindir}/meshlabserver
%{_libdir}/meshlab/
%{_datadir}/meshlab/
%{_mandir}/man1/*.1%{?ext_man}
%doc README.md
%doc docs/privacy.txt
%license LICENSE.txt
%license distrib/shaders/3Dlabs-license.txt
%license distrib/shaders/LightworkDesign-license.txt
%license src/plugins_unsupported/filter_poisson/license.txt
%license src/plugins_experimental/filter_segmentation/license.txt
%{_datadir}/icons/hicolor/*/apps/meshlab.*
%{_datadir}/applications/meshlab.desktop

%changelog
