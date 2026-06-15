#
# spec file for package pascube
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


Name:           pascube
Version:        1.7.0
Release:        0
Summary:        Simple Vulkan spinning cube written in Pascal
License:        GPL-2.0-or-later
URL:            https://github.com/benjamimgois/pascube
Source0:        https://github.com/benjamimgois/pascube/archive/refs/tags/%{version}.tar.gz#/pascube-%{version}.tar.gz
BuildRequires:  SDL2-devel
BuildRequires:  clang
BuildRequires:  fpc
BuildRequires:  fpc-src
BuildRequires:  gcc-c++
BuildRequires:  lazarus
BuildRequires:  libQt6Pas-devel
Requires:       Mesa-libGL1

%description
A simple Vulkan spinning cube written in Pascal using Lazarus,
Qt6 and PasVulkan.

%prep
%autosetup -n pascube-%{version}

mkdir -p build
%ifarch aarch64
sed -i '/TargetCPU/d' pascube.lpi
sed -i 's/-dPasVulkanPasMP//g' pascube.lpi
%endif

%build
clang -c \
    -target x86_64-linux \
    -g -gdwarf-2 \
    -masm=intel \
    -O3 \
    -Dlinux \
    -fverbose-asm \
    -fno-builtin \
    pasvulkan/src/lzma_c/LzmaDec.c \
    -o pasvulkan/src/lzma_c/lzmadec_linux_x86_64.o

lazbuild \
    --lazarusdir=/usr/lib64/lazarus \
    --widgetset=qt6 \
    --primary-config-path=build \
    pascube.lpi

%install
install -Dm755 pascube %{buildroot}%{_bindir}/pascube

mkdir -p %{buildroot}%{_datadir}/pascube
cp -a assets %{buildroot}%{_datadir}/pascube/

install -Dm644 data/skybox.png \
    %{buildroot}%{_datadir}/pascube/skybox.png

install -Dm644 data/pascube.desktop \
    %{buildroot}%{_datadir}/applications/pascube.desktop

for sz in 128x128 256x256 512x512; do
if [ -f data/icons/${sz}/pascube.png ]; then
install -Dm644 data/icons/${sz}/pascube.png \
    %{buildroot}%{_datadir}/icons/hicolor/${sz}/apps/pascube.png
fi
done

%files
%{_bindir}/pascube
%{_datadir}/pascube
%{_datadir}/applications/pascube.desktop
%{_datadir}/icons/hicolor/*/apps/pascube.png

%license LICENSE

%changelog
