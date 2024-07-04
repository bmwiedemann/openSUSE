#
# spec file for package f3d
#
# Copyright (c) 2024 SUSE LLC
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


%define c_lib   libf3d2
Name:           f3d
Version:        2.5.0
Release:        0
Summary:        Fast and minimalist 3D viewer
License:        BSD-3-Clause
Group:          Productivity/Graphics/Viewers
URL:            https://f3d.app
Source0:        https://github.com/%{name}-app/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         help.patch
BuildRequires:  cmake
BuildRequires:  fast_float-devel
BuildRequires:  fmt-devel
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  cmake(Alembic)
BuildRequires:  cmake(Imath)
BuildRequires:  cmake(OpenCASCADE)
BuildRequires:  cmake(vtk) >= 9.3
BuildRequires:  pkgconfig(assimp)
BuildRequires:  pkgconfig(draco)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
%if 0%{?sle_version} >= 150400
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif

%description
F3D is a VTK-based 3D viewer following the KISS principle, so it is
minimalist, efficient, has no GUI, has simple interaction mechanisms and is
fully controllable using arguments in the command line.

%package        bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description    bash-completion
Bash command line completion support for %{name}.

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description    fish-completion
Fish command line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description    zsh-completion
ZSH command line completion support for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{c_lib} = %{version}

%description devel
Development files and headers for %{name}

%package -n %{c_lib}
Summary:        F3d library
Group:          System/Libraries

%description -n %{c_lib}
Library for f3d.

%prep
%autosetup -p1

%build
%cmake \
%if 0%{?suse_version} < 1600
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
%endif
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
    -DBUILD_TESTING=OFF \
    -DF3D_BINDINGS_JAVA=OFF \
    -DF3D_BINDINGS_PYTHON=OFF \
    -DF3D_LINUX_APPLICATION_LINK_FILESYSTEM=ON \
    -DF3D_LINUX_GENERATE_MAN=ON \
    -DF3D_LINUX_INSTALL_DEFAULT_CONFIGURATION_FILE_IN_PREFIX=ON \
    -DF3D_MODULE_EXTERNAL_RENDERING=OFF \
    -DF3D_MODULE_RAYTRACING=OFF \
    -DF3D_PLUGINS_STATIC_BUILD=OFF \
%if 0%{?sle_version} >= 150400
    -DCMAKE_CXX_COMPILER=%{_bindir}/g++-11 \
%endif
    -DF3D_PLUGIN_BUILD_ALEMBIC=ON \
    -DF3D_PLUGIN_BUILD_ASSIMP=ON \
    -DF3D_PLUGIN_BUILD_DRACO=OFF \
    -DF3D_PLUGIN_BUILD_EXODUS=ON \
    -DF3D_PLUGIN_BUILD_OCCT=ON
%cmake_build

%install
%cmake_install
rm -rfv %{buildroot}%{_docdir}/f3d

# this is needed so f3d autoloads the plugins for those filetypes specified in the configs
mkdir -p %{buildroot}%{_sysconfdir}/f3d/config.d
install -Dm644 plugins/assimp/configs/config.d/10_assimp.json %{buildroot}%{_sysconfdir}/f3d/config.d/10_assimp.json
install -Dm644 plugins/alembic/configs/config.d/10_alembic.json %{buildroot}%{_sysconfdir}/f3d/config.d/10_alembic.json
install -Dm644 plugins/exodus/configs/config.d/10_exodus.json %{buildroot}%{_sysconfdir}/f3d/config.d/10_exodus.json
install -Dm644 plugins/native/configs/config.d/10_native.json %{buildroot}%{_sysconfdir}/f3d/config.d/10_native.json
install -Dm644 plugins/occt/configs/config.d/10_occt.json %{buildroot}%{_sysconfdir}/f3d/config.d/10_occt.json

%post -n %{c_lib} -p /sbin/ldconfig
%postun -n %{c_lib} -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE.md doc/THIRD_PARTY_LICENSES.md
%{_bindir}/%{name}
%{_libdir}/lib%{name}-plugin-*.so
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-plugin-*.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/*.json
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{_datadir}/metainfo/app.%{name}.F3D.metainfo.xml
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/%{name}*.thumbnailer
%{_mandir}/man?/%{name}.?%{?ext_man}
%dir %{_sysconfdir}/f3d
%dir %{_sysconfdir}/f3d/config.d
%config %{_sysconfdir}/f3d/config.d/*.json

%dir %{_includedir}/f3d
%{_includedir}/f3d/vtkF3DFaceVaryingPointDispatcher.h
%{_includedir}/f3d/vtkextModule.h
%dir %{_libdir}/cmake/f3d_vtkext
%{_libdir}/cmake/f3d_vtkext/f3d_vtkext-targets-relwithdebinfo.cmake
%{_libdir}/cmake/f3d_vtkext/f3d_vtkext-targets.cmake
%{_libdir}/cmake/f3d_vtkext/f3d_vtkext-vtk-module-properties.cmake
%{_libdir}/libvtkext.so
%dir %{_libdir}/vtk/
%dir %{_libdir}/vtk/hierarchy
%dir %{_libdir}/vtk/hierarchy/f3d_vtkext
%{_libdir}/vtk/hierarchy/f3d_vtkext/vtkext-hierarchy.txt

%files devel
%doc README.md
%license LICENSE.md doc/THIRD_PARTY_LICENSES.md
%{_libdir}/lib%{name}.so

%files -n %{c_lib}
%{_libdir}/lib%{name}.so.*

%files bash-completion
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
