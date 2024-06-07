#
# spec file for package piglit
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


%ifarch %{arm} aarch64
# Enable openGL ES only
%bcond_with opengl
%bcond_without opengles
%else
# Enable openGL and openGL ES
%bcond_without opengl
%bcond_without opengles
%endif
Name:           piglit
Version:        1~20240530
Release:        0
Summary:        OpenGL driver testing framework
License:        MIT
Group:          System/Benchmark
URL:            https://cgit.freedesktop.org/piglit
Source0:        %{name}-%{version}.tar.gz
Source1:        piglit-rpmlintrc
Source2:        suse_qa.py
Source3:        suse_qa-skip-tests.txt
Source4:        opensuse_qa.py
Source5:        opensuse_qa-skip-tests.txt
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  glslang-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-Mako
BuildRequires:  python3-numpy
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(waffle-1) >= 1.6.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       python3
Requires:       python3-Mako
Requires:       python3-numpy
Requires:       python3-xml
Recommends:     waffle >= 1.6.0
ExcludeArch:    %{ix86} ppc
%if %{with opengl}
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(glu)
%endif
%if %{with opengles}
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  pkgconfig(glesv1_cm)
BuildRequires:  pkgconfig(glesv2)
%endif
%ifarch x86_64
BuildRequires:  pkgconfig(libdrm_intel)
%endif

%description
Piglit is a collection of automated tests for OpenGL and OpenCL
implementations.

The goal of Piglit is to help improve the quality of open source
OpenGL drivers by providing developers with means to perform
regression tests.

It contains the Glean tests, some tests adapted from Mesa, as well as
some specific regression tests for certain bugs. HTML summaries can
be generated, including the ability to compare different test runs.

%prep
%autosetup

%build
# Note: Overwriting CMAKE_SHARED_LINKER_FLAGS with those from the cmake macro,
# but leaving out -Wl,--no-undefined
# Note: Overwriting CMAKE_SKIP_RPATH to be off,  but enabling
# CMAKE_BUILD_WITH_INSTALL_RPATH so the individual test binaries in
# /usr/lib64/piglit/bin/* can find the libraries in /usr/lib64/piglit/lib
%cmake \
%if %{without opengl}
  -DPIGLIT_BUILD_GL_TESTS=OFF \
%endif
%if %{without opengles}
  -DPIGLIT_BUILD_GL_ES1_TESTS=OFF \
  -DPIGLIT_BUILD_GL_ES2_TESTS=OFF \
  -DPIGLIT_BUILD_GL_ES3_TESTS=OFF \
%endif
  -DCMAKE_C_FLAGS="%{optflags} -fcommon -DNDEBUG" \
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now" \
  -DCMAKE_SKIP_RPATH:BOOL=OFF \
  -DCMAKE_BUILD_WITH_INSTALL_RPATH:BOOL=ON \
  -Wno-dev
%cmake_build

%install
%cmake_install

install -Dpm 644 %{SOURCE2} \
  %{buildroot}%{_libdir}/piglit/tests
install -Dpm 644 %{SOURCE3} \
  %{buildroot}%{_libdir}/piglit/tests
install -Dpm 644 %{SOURCE4} \
  %{buildroot}%{_libdir}/piglit/tests
install -Dpm 644 %{SOURCE5} \
  {buildroot}%{_libdir}/piglit/tests
%fdupes %{buildroot}/%{_libdir}/piglit

%ldconfig_scriptlets

%files
%{_libdir}/piglit
%{_bindir}/piglit
%doc %{_datadir}/doc/piglit

%changelog
