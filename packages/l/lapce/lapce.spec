#
# spec file for package lapce
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


%if 0%{?suse_version} && 0%{?suse_version} < 1550
%global force_gcc_version 13
%endif

%if 0%{?suse_version} > 1600
%bcond_without mold
%else
%bcond_with    mold
%endif

%if %{with mold}
%global build_rustflags "-C" "linker=clang" "-C" "link-arg='-fuse-ld=/usr/bin/mold -Wl,-z,relro,-z,now'" "-C" "debuginfo=2" "-C" "incremental=false" "-C" "strip=none"
%endif

Name:           lapce
Version:        0.4.2
Release:        0
Summary:        Lightning-fast and Powerful Code Editor written in Rust
URL:            https://github.com/lapce/lapce
License:        (0BSD OR Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND MIT AND (Artistic-2.0 OR CC0-1.0) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND ISC AND MIT AND (MIT OR Unlicense) AND MPL-2.0 AND MPL-2.0+ AND Zlib AND zlib-acknowledgement AND Apache-2.0
Group:          Productivity/Text/Editors
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
%if 0%{?suse_version} > 1600
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  clang
BuildRequires:  mold
%else
BuildRequires:  gcc13
BuildRequires:  gcc13-c++
BuildRequires:  libstdc++6-devel-gcc13
%endif
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  rust
BuildRequires:  zstd
BuildRequires:  pkgconfig(atk) >= 2.18
BuildRequires:  pkgconfig(cairo) >= 1.14
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdk-3.0) >= 3.22
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.36.8
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(pango) >= 1.38
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
ExclusiveArch:  %{rust_tier1_arches}

%description
Lapce is written in pure Rust, with the UI in Druid
It uses Xi-Editor's Rope Science for text editing, and the
Wgpu Graphics API for rendering.

%prep
%autosetup -a1

%build
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
# We disable default feature as they include auto-update.
# For reference:
# https://github.com/lapce/lapce/blob/0ded46c988d72b563bd78b29cc11107d4e2248bc/lapce-ui/Cargo.toml#L48
%{cargo_build} --no-default-features -p lapce-app

%install
install -Dm 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}-proxy
install -Dm 0644 %{_builddir}/%{name}-%{version}/extra/linux/dev.%{name}.%{name}.metainfo.xml %{buildroot}%{_datadir}/metainfo/dev.%{name}.%{name}.metainfo.xml
install -Dm 0644 %{_builddir}/%{name}-%{version}/extra/linux/dev.%{name}.%{name}.desktop %{buildroot}%{_datadir}/applications/dev.%{name}.%{name}.desktop
install -Dm 0644 %{_builddir}/%{name}-%{version}/extra/images/logo.png %{buildroot}%{_datadir}/pixmaps/dev.%{name}.%{name}.png

%files
%license LICENSE
%doc README.md docs/*.md
%{_bindir}/lapce
%{_bindir}/lapce-proxy
%{_datadir}/metainfo/dev.lapce.lapce.metainfo.xml
%{_datadir}/applications/dev.lapce.lapce.desktop
%{_datadir}/pixmaps/dev.lapce.lapce.png

%changelog
