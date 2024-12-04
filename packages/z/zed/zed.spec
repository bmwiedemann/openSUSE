#
# spec file for package zed
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Marvin Friedrich
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


%if 0%{?suse_version} && 0%{?suse_version} < 1550
%global force_gcc_version 13
%endif

# mold is not on Leap yet
%if 0%{?suse_version} > 1600
%bcond_without mold
%else
%bcond_with    mold
%endif

%if %{with mold}
%global build_rustflags "-C" "linker=clang" "-C" "link-arg='-fuse-ld=/usr/bin/mold -Wl,-z,relro,-z,now'" "-C" "debuginfo=2" "-C" "incremental=false" "-C" "strip=none"
%endif

Name:           zed
Version:        0.163.3
Release:        0
Summary:        A high-performance, multiplayer code editor
License:        AGPL-3.0-or-later AND Apache-2.0 AND GPL-3.0-only
Group:          Development/Tools/IDE
URL:            https://github.com/zed-industries/zed
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.80
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  git
BuildRequires:  hicolor-icon-theme

%if %{with mold}
BuildRequires:  clang
BuildRequires:  mold
%endif

# all pkgconfig BR are based on the the build.rs files in the vendor tree
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2) >= 18.5.12
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(zlib)
# it doesnt try to find this one but then it tries to link to it.
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)

ExclusiveArch:  x86_64 aarch64
# otherwise it downloads a copy of nodejs
Requires:       npm

%description
Code at the speed of thought - Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.

%prep
# Vendored sources
%autosetup -p1 -a1

%build
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif

export ZED_UPDATE_EXPLANATION="Please use the package manager to update zed."
# Build CLI
cd crates/cli/
%{cargo_build}
# Build Editor
cd ../zed/
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -D -d -m 0755 %{buildroot}%{_libexecdir}

# https://github.com/zed-industries/zed/blob/main/script/bundle-linux#L63
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/zed %{buildroot}%{_libexecdir}/zed-editor
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/cli %{buildroot}%{_bindir}/zed

# Desktop file
# https://github.com/zed-industries/zed/blob/main/script/bundle-linux#L85
export DO_STARTUP_NOTIFY="true"
export APP_CLI="zed"
export APP_ICON="zed"
export APP_NAME="Zed"
envsubst < "crates/zed/resources/zed.desktop.in" > "crates/zed/resources/zed.desktop"
install -Dm 0644 crates/zed/resources/zed.desktop %{buildroot}%{_datadir}/applications/zed.desktop
install -Dm 0644 assets/icons/logo_96.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/zed.svg

%files
%license LICENSE-*
%doc README.md
%{_bindir}/zed
%{_libexecdir}/zed-editor
%{_datadir}/applications/zed.desktop
%{_datadir}/icons/hicolor/scalable/apps/zed.svg

%changelog
