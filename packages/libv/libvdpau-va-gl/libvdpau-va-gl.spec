#
# spec file for package libvdpau-va-gl
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


%define soname  libvdpau_va_gl
%define sover   1
Name:           libvdpau-va-gl
Version:        0.4.2
Release:        0
Summary:        VDPAU driver with OpenGL/VAAPI backend
License:        LGPL-3.0+
Group:          System/Libraries
Url:            https://github.com/i-rinat/libvdpau-va-gl
Source:         https://github.com/i-rinat/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libva-glx)
BuildRequires:  pkgconfig(vdpau)
%if 0%{?suse_version} > 1320
BuildRequires:  gcc-c++
%else
# C++11 unified initialisation is of need.
BuildRequires:  gcc5-c++
%endif

%description
Many applications can use VDPAU to accelerate portions of the video
decoding process and video post-processing to the GPU video hardware.
Unfortunately, there is no such library for many graphic chipsets.
Some applications also support VA-API but many of them, including
Adobe Flash Player, don't.

This library proposes a generic VDPAU library. It uses OpenGL under
the hood to accelerate drawing and scaling and VA-API (if
available) to accelerate video decoding.

%package -n %{soname}%{sover}
Summary:        VDPAU driver with OpenGL/VAAPI backend
Group:          System/Libraries
Supplements:    xf86-video-intel
Provides:       %{soname} = %{version}

%description -n %{soname}%{sover}
Many applications can use VDPAU to accelerate portions of the video
decoding process and video post-processing to the GPU video hardware.
Unfortunately, there is no such library for many graphic chipsets.
Some applications also support VA-API but many of them, including
Adobe Flash Player, don't.

This library proposes a generic VDPAU library. It uses OpenGL under
the hood to accelerate drawing and scaling and VA-API (if
available) to accelerate video decoding.

%prep
%setup -q
cat > %{name}.sh << EOF
# Avoid usage of this library when NVIDIA's proprietary driver is running.
if [ ! -c /dev/nvidiactl ]; then
    export VDPAU_DRIVER='va_gl'
fi
EOF
cat > %{name}.csh << EOF
# Avoid usage of this library when NVIDIA's proprietary driver is running.
if ( ! -c /dev/nvidiactl ) then
    setenv VDPAU_DRIVER 'va_gl'
endif
EOF

%build
%if 0%{?suse_version} <= 1320
export CC="gcc-5"
export CXX="g++-5"
# Default ABI up to G++4.9.
export CXXFLAGS="%{optflags} -fabi-version=2 -fabi-compat-version=2"
%endif
%cmake \
  -DLIB_INSTALL_DIR=%{_libdir}/vdpau
make %{?_smp_mflags} V=1

%install
%cmake_install

install -Dpm 0644 %{name}.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -Dpm 0644 %{name}.csh %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh

%files -n %{soname}%{sover}
%defattr(-,root,root)
%doc ChangeLog LICENSE README.md
%config %{_sysconfdir}/profile.d/%{name}.*sh
%{_libdir}/vdpau/

%changelog
