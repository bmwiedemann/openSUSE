#
# spec file for package nvidia-texture-tools
#
# Copyright (c) 2021 SUSE LLC
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


Name:           nvidia-texture-tools
Version:        2.1.2
Release:        0
Summary:        NVIDIA Texture Tools
# BuildRequires:  cg-devel
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/castano/nvidia-texture-tools
Source0:        https://github.com/castano/nvidia-texture-tools/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  Mesa-devel
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86} x86_64 ppc

%description
This is the first alpha release of the new NVIDIA Texture Tools. The main highlights of
this release are support for all DX10 texture formats, higher speed and improved
compression quality.

In addition to that it also comes with a hardware accelerated compressor that
uses CUDA to compress blocks in parallel on the GPU and runs around 10 times
faster than the CPU counterpart.

You can obtain CUDA from our developer site at:

http://developer.nvidia.com/object/cuda.html

The source code of the Texture Tools is being released under the terms of
the MIT license.

%prep
%autosetup -p1
%ifarch %{ix86} x86_64
# on i586 compilation will fail without SSE
CPU=corei7
%endif
%ifarch ppc
CPU=power8
%endif
if [ -n "$CPU" ] ; then
  sed -i "s/-march=native/-march=$CPU/" cmake/OptimalOptions.cmake
else
  sed -i "s/-march=native//" cmake/OptimalOptions.cmake
fi

%build
%cmake \
  -DNVTT_SHARED=1 \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install
if [ "%{_lib}" != "lib" ];
then
       mv %{buildroot}%{_prefix}/lib %{buildroot}%{_prefix}/%{_lib}
fi
# remove installed doc-folder, let rpm decide on the correct paths
rm -r %{buildroot}%{_datadir}/doc/nvtt

%files
%defattr(-, root, root)
%license LICENSE
%doc ChangeLog README.md
%{_bindir}/nvassemble
%{_bindir}/nvcompress
%{_bindir}/nvddsinfo
%{_bindir}/nvdecompress
%{_bindir}/nvimgdiff
%{_bindir}/nvzoom
%{_bindir}/nv-gnome-thumbnailer
%{_bindir}/nvhdrtest
%{_bindir}/nvtestsuite
%{_includedir}/nvtt
%{_includedir}/squish.h
%{_libdir}/libnvcore.so
%{_libdir}/libnvimage.so
%{_libdir}/libnvmath.so
%{_libdir}/libnvtt.so
%{_libdir}/libnvthread.so
%{_libdir}/libsquish.so
%{_libdir}/libsquish.so.0.0

%changelog
