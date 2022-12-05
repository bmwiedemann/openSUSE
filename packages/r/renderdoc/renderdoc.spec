#
# spec file for package renderdoc
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


Name:           renderdoc
Version:        1.23
Release:        0
Summary:        A frame-capture based graphics debugger
License:        MIT
Group:          Development/Tools/Debuggers
URL:            https://renderdoc.org/
Source0:        https://github.com/baldurk/renderdoc/archive/v%{version}/renderdoc-%{version}.tar.gz
Source1:        https://github.com/baldurk/swig/archive/renderdoc-modified-7.zip
Patch0:         0001-Fix-install-rpaths.patch
Patch1:         0002-Add-debugger-as-desktop-menu-category.patch
BuildRequires:  Mesa-libGL-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libX11-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  libxcb-devel
BuildRequires:  memory-constraints
BuildRequires:  pcre-devel
BuildRequires:  python3-devel
BuildRequires:  vulkan-devel
BuildRequires:  xcb-util-keysyms-devel

%description
RenderDoc is a frame-capture based graphics debugger, currently
available for Vulkan, D3D11, D3D12, OpenGL, and OpenGL ES development.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
RenderDoc is a frame-capture based graphics debugger, currently
available for Vulkan, D3D11, D3D12, OpenGL, and OpenGL ES development.

%prep
%autosetup -p1 -n renderdoc-%{version}

%build
%limit_build -m 1750
mkdir %{_builddir}/%{name}-%{version}/build && cd %{_builddir}/%{name}-%{version}/build
%{_bindir}/cmake %{_builddir}/%{name}-%{version}/ \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{?_lib}" == "lib64"
        -DLIB_SUFFIX=64 \
%endif
  -DQMAKE_QT5_COMMAND=qmake-qt5 \
  -DRENDERDOC_SWIG_PACKAGE=%{_sourcedir}/renderdoc-modified-7.zip \
  -DENABLE_GL=YES \
  -DENABLE_VULKAN=YES \
  -DENABLE_XCB=YES \
  -DENABLE_XLIB=YES \
  -DVULKAN_LAYER_FOLDER=%{_datadir}/vulkan/implicit_layer.d \
  -DENABLE_RENDERDOCCMD=ON \
  -DENABLE_QRENDERDOC=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_VERSION_STABLE=ON \
  -DCMAKE_INSTALL_RPATH=""
%cmake_build

%install
%cmake_install

%files
%license LICENSE.md
%{_bindir}/qrenderdoc
%{_bindir}/renderdoccmd
%{_datadir}/applications/%{name}.desktop
%{_libdir}/librenderdoc.so
%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_datadir}/icons/hicolor/*/mimetypes/application-x-renderdoc-capture.*
%{_datadir}/mime/packages/renderdoc-capture.xml
%{_datadir}/pixmaps/%{name}-icon-*.xpm
%{_datadir}/vulkan/implicit_layer.d/%{name}_capture.json
%{_datadir}/menu/renderdoc
%doc %{_datadir}/doc/%{name}/
%exclude %{_datadir}/doc/renderdoc/LICENSE.md
%dir %{_datadir}/menu/
%dir %{_datadir}/thumbnailers/
%dir %{_datadir}/vulkan/implicit_layer.d/

%files devel
%{_includedir}/renderdoc_app.h

%changelog
