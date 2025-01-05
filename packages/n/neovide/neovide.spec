#
# spec file for package neovide
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


%define skia_version m131-0.79.1
%define wuffs_commit e3f919ccfe3ef542cfc983a82146070258fb57f8

Name:           neovide
Version:        0.14.0
Release:        0
Summary:        Simple Neovim GUI
License:        MIT
Group:          Productivity/Text/Editors
URL:            https://github.com/neovide/neovide
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        https://github.com/rust-skia/skia/archive/%{skia_version}/skia-%{skia_version}.tar.gz
Source3:        https://github.com/google/wuffs-mirror-release-c/archive/%{wuffs_commit}/wuffs-%{wuffs_commit}.tar.gz
BuildRequires:  cargo >= 1.79
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  gcc-c++
BuildRequires:  gn
BuildRequires:  hicolor-icon-theme
BuildRequires:  ninja
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} && 0%{?suse_version} < 1550
# clang++ needs gcc13 c++ headers to compile skia on Leap 15.6
BuildRequires:  gcc13-c++
%endif
Requires:       neovim >= 0.10.0

ExclusiveArch:  x86_64 aarch64

%description
No Nonsense Neovim Client in Rust

%prep
%setup -q -a 1 -a 2 -a 3
mkdir -p skia-%{skia_version}/third_party/externals/
mv wuffs-mirror-release-c-%{wuffs_commit} skia-%{skia_version}/third_party/externals/wuffs

%build
export SKIA_SOURCE_DIR=%{_builddir}/%{name}-%{version}/skia-%{skia_version}
export SKIA_USE_SYSTEM_LIBRARIES=true
export SKIA_NINJA_COMMAND=ninja
export SKIA_GN_COMMAND=gn
%{cargo_build}

%install
install -Dm755 %{_builddir}/%{name}-%{version}/target/release/neovide %{buildroot}%{_bindir}/neovide
install -Dm644 %{_builddir}/%{name}-%{version}/assets/neovide.desktop %{buildroot}%{_datadir}/applications/neovide.desktop
install -Dm644 %{_builddir}/%{name}-%{version}/assets/neovide.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/neovide.svg

%files
%doc README.md
%license LICENSE
%{_bindir}/neovide
%{_datadir}/applications/neovide.desktop
%{_datadir}/icons/hicolor/scalable/apps/neovide.svg

%changelog
