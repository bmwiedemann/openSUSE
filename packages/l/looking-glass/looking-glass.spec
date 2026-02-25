#
# spec file for package looking-glass
#
# Copyright (c) 2026 SUSE LLC
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

Name:           looking-glass
Version:        B7
Release:        0
Summary:        An extremely low latency KVMFR (KVM FrameRelay)
License:        GPL-2.0
URL:            https://looking-glass.io/
Source0:        %{name}-%{version}.tar.xz
Patch1:         fix-bfd-ctf-zstd.patch
BuildRequires:  binutils-devel
BuildRequires:  cmake
BuildRequires:  c++_compiler
BuildRequires:  libdecor-devel
BuildRequires:  libglvnd-devel
BuildRequires:  libnettle-devel
BuildRequires:  libvulkan1
BuildRequires:  libwayland-egl1
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXss-devel
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  mingw64-cross-gcc-c++
BuildRequires:  mingw64-cross-cmake
BuildRequires:  mingw64-cross-pkgconf
BuildRequires:  obs-studio-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpresent)
BuildRequires:  sdl2-compat-devel
BuildRequires:  simde-devel
BuildRequires:  spice-protocol-devel
BuildRequires:  vulkan-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
Epoch:          2
ExclusiveArch:  x86_64

%description
An extremely low latency KVMFR (KVM FrameRelay) implementation for guests with VGA PCI Passthrough.

%prep
%autosetup -n %{name}-%{version} -p1

sed -i 's|@CMAKE_INSTALL_PREFIX@|%{_prefix}|g' resources/looking-glass-client.desktop.in

%build
export CFLAGS="%{optflags} -fPIC -I%{_includedir}/simde"
export CXXFLAGS="%{optflags} -fPIC -I%{_includedir}/simde"
export LDFLAGS="%{?__global_ldflags} -pie"

build_subproject() {
    local subdir=$1
    shift
    echo "--- Building subproject: $subdir ---"
    pushd "$subdir"
    %cmake "$@"
    %cmake_build
    popd
}

build_subproject client -DENABLE_BACKTRACE=no -DCMAKE_POSITION_INDEPENDENT_CODE=ON
build_subproject host -DCMAKE_C_FLAGS="$CFLAGS -Wno-maybe-uninitialized" -DENABLE_BACKTRACE=no
build_subproject obs -DCMAKE_DISABLE_FIND_PACKAGE_BFD=ON -DCMAKE_SHARED_LINKER_FLAGS="-shared"

mkdir -p host/build_win
pushd host/build_win
mingw64-cmake .. -DENABLE_BACKTRACE=no -DCMAKE_EXE_LINKER_FLAGS="-static"
cd build
%make_build
popd

%install
install_dir() {
  local dir=$1
  pushd "$dir/build"
  %make_install
  popd
}

install_dir client
install_dir host

install -Dm644 obs/build/liblooking-glass-obs.so %{buildroot}%{_libdir}/obs-plugins/liblooking-glass-obs.so
install -Dm644 resources/looking-glass-client.desktop.in %{buildroot}%{_datadir}/applications/looking-glass-client.desktop
install -Dm644 resources/lg-logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/looking-glass.svg
install -Dm644 host/build_win/build/looking-glass-host.exe %{buildroot}%{_datadir}/looking-glass/looking-glass-host.exe


find %{buildroot} -type f -executable -exec %{__strip} --strip-unneeded {} \; || true
%{__strip} %{buildroot}/usr/lib64/obs-plugins/liblooking-glass-obs.so

%check

%package client
Summary:        A client application for accessing the LookingGlass
Group:          System/Emulators/PC
Recommends:     (looking-glass-obs-plugin if obs-studio)
Requires:       Mesa-libGL1
Requires:        looking-glass-kvmfr-kmp-default

%description client
A client application for accessing the LookingGlass IVSHMEM device of a VM.

%files client
%license LICENSE
%doc README.md
%{_bindir}/looking-glass-client
%_datadir/applications/looking-glass-client.desktop
%_datadir/icons/hicolor/scalable/apps/looking-glass.svg

%package host
Summary:        Application for pushing frame data to the LookingGlass IVSHMEM device
Group:          System/Emulators/PC

%description host
Linux host application for pushing frame data to the LookingGlass IVSHMEM device.

%files host
%{_bindir}/looking-glass-host

%package obs-plugin
Summary:        Plugin for OBS Studio to stream directly from Looking Glass
Group:          System/Emulators/PC
Requires:       obs-studio

%description obs-plugin
Plugin for OBS Studio to stream directly from Looking Glass without having to record the Looking Glass client.

%files obs-plugin
%dir %{_libdir}/obs-plugins
%{_libdir}/obs-plugins/liblooking-glass-obs.so

%package windows-host
Summary:        Looking Glass Host executable for Windows guests
BuildArch:      noarch
AutoReqProv:    no

%description windows-host
This package contains the looking-glass-host.exe compiled for Windows.
Copy this file to your Windows Guest to run the host service.

%files windows-host
%dir %{_datadir}/looking-glass
%{_datadir}/looking-glass/looking-glass-host.exe

%changelog
