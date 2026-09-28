#
# spec file for package xemu
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%define git_commit %({ \
	cat %{_sourcedir}/_service | grep revision | awk -F '[<>]' '{print $3}'
})
Name:           xemu
Version:        0.8.136
Release:        0
Summary:        Xbox emulator
License:        GPL-2.0-only AND LGPL-2.1-only AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-or-later AND MIT
URL:            https://xemu.app/
Source0:        %{name}-%{version}.tar.zst
Source1000:     README.SUSE
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  flex
BuildRequires:  make
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python3-PyYAML
BuildRequires:  zstd
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sdl2)
# use the system libslirp instead of the bundled subproject, otherwise the
# binary gets a RUNPATH into the build tree (binary-or-shlib-defines-rpath)
BuildRequires:  pkgconfig(slirp)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(xscrnsaver)
ExclusiveArch:  x86_64 aarch64

%description
Original Xbox emulator.

Based on qemu and xqemu.

%prep
%autosetup

%build
export CXX=gcc
export XBOX=1

printf %{git_commit} > XEMU_COMMIT
printf %{version} > XEMU_VERSION

# this is not autotools, but rather a bespoke script originated in the qemu project
./configure \
	--extra-cflags="-DXBOX=1 %{optflags} -lstdc++ -lm -ldl" \
	--disable-docs --disable-tools \
	--enable-kvm --disable-xen --disable-werror \
	--enable-trace-backends="nop" \
	--target-list=i386-softmmu \
	--enable-sdl \
	--enable-opengl \
	--disable-spice \
	--disable-virglrenderer \
	--disable-vnc --disable-vnc-sasl
%make_build

%install
install -Dm755 build/qemu-system-i386 %{buildroot}%{_bindir}/%{name}

install -Dm644 ui/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
for _size in 16 24 32 48 64 128 256 512; do
	install -Dm644 ui/icons/%{name}_${_size}x${_size}.png %{buildroot}%{_datadir}/icons/hicolor/${_size}x${_size}/apps/%{name}.png
done
install -Dm644 ui/icons/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -Dm644 xemu.metainfo.xml %{buildroot}%{_datadir}/metainfo/xemu.metainfo.xml

%files
%license COPYING COPYING.LIB LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/xemu.metainfo.xml

%changelog
