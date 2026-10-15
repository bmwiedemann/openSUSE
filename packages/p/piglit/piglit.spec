#
# spec file for package piglit
#
# Copyright (c) 2025 SUSE LLC
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
Version:        1~20260521
Release:        0
Summary:        OpenGL driver testing framework
License:        MIT
URL:            https://cgit.freedesktop.org/piglit
Source0:        %{name}-%{version}.tar.gz
Source1:        piglit-rpmlintrc
Source2:        suse_qa.py
Source3:        suse_qa-skip-tests.txt
Source4:        opensuse_qa.py
Source5:        opensuse_qa-skip-tests.txt
Patch0:         vulkan-xml-generated-tests.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glslang-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-Mako
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-timeout
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 17.1
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(waffle-1) >= 1.6.0
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       python3
Requires:       python3-Mako
# For the replay subcommand (framework/replay)
Recommends:     python3-Pillow
Recommends:     python3-PyYAML
Recommends:     python3-packaging
Recommends:     python3-requests
Recommends:     waffle >= 1.6.0
ExcludeArch:    %{ix86} ppc
%if %{with opengl}
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glproto)
%endif
%if %{with opengles}
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  pkgconfig(glesv1_cm)
BuildRequires:  pkgconfig(glesv2)
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
%autosetup -p1

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

%check
# Unit tests for the code generators that produce much of the shipped
# test data (upstream's "generator" tox environment). The two deselected
# tests need the pytest-raises plugin, which is not packaged in openSUSE.
python3 -m pytest unittests/generators -q \
  --deselect unittests/generators/test_glsl.py::test_glsl_glsles_exception \
  --deselect unittests/generators/test_glsl.py::test_glsles_glsl_exception
# Smoke-run real test programs against Mesa's software renderer on the
# surfaceless EGL platform (no X server or GPU needed); each must pass.
for test in arb_blend_func_extended-blend-api_gles2 egl_ext_device_enumeration; do
  LD_LIBRARY_PATH=$PWD/build/lib \
  PIGLIT_PLATFORM=surfaceless_egl \
  LIBGL_ALWAYS_SOFTWARE=1 \
  GALLIUM_DRIVER=llvmpipe \
    ./build/bin/$test | grep -q '"result": "pass"'
done

%install
%cmake_install

install -Dpm 644 %{SOURCE2} \
  %{buildroot}%{_libdir}/piglit/tests
install -Dpm 644 %{SOURCE3} \
  %{buildroot}%{_libdir}/piglit/tests
install -Dpm 644 %{SOURCE4} \
  %{buildroot}%{_libdir}/piglit/tests
install -Dpm 644 %{SOURCE5} \
  %{buildroot}%{_libdir}/piglit/tests
# Ship the python scripts with a fixed interpreter, and make the ones
# carrying a shebang executable
sed -i '1s|^#!%{_bindir}/env python.*|#!%{_bindir}/python3|' \
  %{buildroot}%{_bindir}/piglit \
  %{buildroot}%{_libdir}/piglit/bin/replayer.py \
  %{buildroot}%{_libdir}/piglit/framework/replay/backends/renderdoc/renderdoc_dump_images.py \
  %{buildroot}%{_libdir}/piglit/tests/glslparsertest/glsl2/gen_builtin_test.py \
  %{buildroot}%{_libdir}/piglit/tests/oglconform.py \
  %{buildroot}%{_libdir}/piglit/tests/vulkan.py
chmod a+x \
  %{buildroot}%{_libdir}/piglit/framework/replay/backends/renderdoc/renderdoc_dump_images.py \
  %{buildroot}%{_libdir}/piglit/tests/glslparsertest/glsl2/gen_builtin_test.py \
  %{buildroot}%{_libdir}/piglit/tests/oglconform.py \
  %{buildroot}%{_libdir}/piglit/tests/vulkan.py
%fdupes %{buildroot}/%{_libdir}/piglit

%ldconfig_scriptlets

%files
%{_libdir}/piglit
%{_bindir}/piglit
%doc %{_datadir}/doc/piglit

%changelog
