#
# spec file for package meshlab
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


%if 0%{?suse_version} >= 1550
%bcond_without gmp
%else
%bcond_with    gmp
%endif

Name:           meshlab
Version:        2022.02
Release:        0
Summary:        System for the processing and editing of unstructured 3D triangular meshes
License:        GPL-2.0-or-later AND BSD-3-Clause
Group:          Productivity/Graphics/3D Editors
URL:            https://www.meshlab.net/
Source0:        https://github.com/cnr-isti-vclab/meshlab/archive/refs/tags/MeshLab-%{version}.tar.gz#/meshlab-%{version}.tar.gz
# Probably belongs in its own package, but nothing else depends on it
Source1:        https://github.com/cnr-isti-vclab/vcglib/archive/refs/tags/%{version}.tar.gz#/vcglib-%{version}.tar.gz
# PATCH-FIX-OPENSUSE -- adjust plugin and shader search path
Patch1:         0001-Use-same-paths-for-shader-plugin-lookup-as-used-for-.patch
# PATCH-FIX-OPENSUSE -- https://github.com/cnr-isti-vclab/vcglib/issues/210
Patch2:         0001-Remove-unused-return-value-in-unused-function.patch
# PATCH-FIX-OPENSUSE
Patch3:         0001-Set-correct-RPATH-for-libraries-and-executable.patch
# PATCH-FIX-OPENSUSE
Patch4:         0001-Allow-usage-of-system-provided-levmar.patch
Patch5:         gcc13-fix.patch

BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  levmar-devel
BuildRequires:  libbz2-devel
BuildRequires:  muparser-devel
BuildRequires:  qhull-devel
BuildRequires:  cmake(CGAL)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xerces-c)
%if %{with gmp}
BuildRequires:  pkgconfig(gmp)
%endif
BuildRequires:  pkgconfig(lib3ds)
# Optional, missing:
#BuildRequires:  pkgconfig(OpenCTM)
# Incompatibility between GLEW and Qt GLES builds
ExcludeArch:    %{arm} aarch64

# Do not add plugins to provides
%global __provides_exclude_from ^%{_libdir}/meshlab/plugins/.*\\.so

%description
MeshLab is an open source, portable, and extensible system for the processing
and editing of unstructured large 3D triangular meshes. The source is
released under the GPL license. The system is aimed to help the processing
of the typical not-so-small unstructured models arising in 3D scanning,
providing a set of tools for editing, cleaning, healing, inspecting,
rendering and converting this kind of meshes.

%prep
%setup -a1 -n %{name}-MeshLab-%{version}

# rename vcglib folder
rmdir src/vcglib
mv vcglib-%{version} src/vcglib

%autopatch -p1

# Remove bundled library sources, since we use the packaged libraries
rm -r src/external/{glew*,levmar*,lib3ds*,muparser*,qhull*,xerces*}/*

# set plugin and shader search path
sed -i 's|PLUGIN_DIR|QString("%{_libdir}/meshlab/plugins")|g'  src/common/globals.cpp
sed -i 's|SHADER_DIR|QString("%{_datadir}/meshlab/shaders")|g' src/common/globals.cpp

%build
pushd src
%cmake
%cmake_build
popd


%install
pushd src
%cmake_install
popd

for i in 16 48 64 128 512 ; do
  install -D -m 644 src/meshlab/images/eye${i}.png \
                    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/meshlab.png
done

# Make sure Xorg or XWayland is used, native Wayland is not working
sed -i -e 's/Exec=.*/Exec=env QT_QPA_PLATFORM=xcb meshlab/' %{buildroot}%{_datadir}/applications/meshlab.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/meshlab.desktop

# Remove leftover libIFX*.so -- https://github.com/cnr-isti-vclab/meshlab/issues/1353
rm %{buildroot}%{_libdir}/meshlab/libIFX*.so

install -D -m 0644 -t %{buildroot}%{_mandir}/man1/ docs/man/*.1

%fdupes %{buildroot}%{_datadir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/meshlab
%{_libdir}/meshlab/
%{_datadir}/meshlab/
%{_mandir}/man1/*.1%{?ext_man}
%doc README.md
%doc docs/privacy.txt
%license LICENSE.txt
%license distrib/shaders/3Dlabs-license.txt
%license distrib/shaders/LightworkDesign-license.txt
%{_datadir}/icons/hicolor/*/apps/meshlab.*
%{_datadir}/applications/meshlab.desktop

%changelog
