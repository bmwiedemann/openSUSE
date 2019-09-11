#
# spec file for package nvidia-texture-tools
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           nvidia-texture-tools
Version:        2.0.8
Release:        0
Summary:        NVIDIA Texture Tools
License:        MIT
Group:          Development/Tools/Other
# BuildRequires:  cg-devel
Url:            https://github.com/castano/nvidia-texture-tools
Source0:        https://github.com/castano/nvidia-texture-tools/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         nvidia-texture-tools-gcc47.patch
# patch libpng15 is upstreamed yet (http://code.google.com/p/nvidia-texture-tools/source/detail)
Patch1:         nvidia-texture-tools-libpng15.patch
Patch2:         nvidia-texture-tools-gcc6.patch
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
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%cmake \
  -DNVTT_SHARED=1 \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo
make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install
if [ "%{_lib}" != "lib" ];
then
       mv %{buildroot}%{_prefix}/lib %{buildroot}%{_prefix}/%{_lib}
fi
dos2unix *.txt

%files
%defattr(-, root, root)
%doc NVIDIA_Texture_Tools_LICENSE.txt NVIDIA_Texture_Tools_README.txt ChangeLog
%{_bindir}/nvassemble
%{_bindir}/nvcompress
%{_bindir}/nvddsinfo
%{_bindir}/nvdecompress
%{_bindir}/nvimgdiff
%{_bindir}/nvzoom
%{_includedir}/nvtt
%{_libdir}/libnvcore.so
%{_libdir}/libnvimage.so
%{_libdir}/libnvmath.so
%{_libdir}/libnvtt.so

%changelog
