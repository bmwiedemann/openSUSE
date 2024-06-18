#
# spec file for package tectonic
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


Name:           tectonic
Version:        0.15.0
Release:        0
Summary:        Modernized self-contained TeX and LaTeX engine
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause ) AND ( 0BSD OR MIT OR Apache-2.0 ) AND ( Apache-2.0 OR BSL-1.0 ) AND ( Apache-2.0 OR MIT ) AND ( Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT ) AND ( MIT OR Apache-2.0 AND BSD-2-Clause ) AND ( MIT OR Apache-2.0 OR Zlib ) AND ( MIT OR Zlib OR Apache-2.0 ) AND ( Unlicense OR MIT ) AND ( Zlib OR Apache-2.0 OR MIT ) AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND ISC AND MIT AND WTFPL
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://tectonic-typesetting.github.io
Source0:        https://github.com/tectonic-typesetting/tectonic/archive/refs/tags/%{name}@%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Patch1:         0001-build-set-c-standard-to-c-17.patch
Patch2:         0002-fix-update-symbols-tags_from_lang-hb_ot_tag_from_lan.patch
%if 0%{?suse_version} > 1600
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
%else
BuildRequires:  gcc13
BuildRequires:  gcc13-c++
BuildRequires:  libstdc++6-devel-gcc13
%endif
BuildRequires:  cargo-packaging
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
# https://github.com/tectonic-typesetting/tectonic/issues/1190
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
ExclusiveArch:  %{rust_arches}

%description
Tectonic is a complete self-contained TeX/LaTeX engine powered by
XeTeX and TeXLive.

%prep
%autosetup -p1 -a1 -n %{name}-%{name}-%{version}

%build

%install
%if 0%{?suse_version} <= 1600
export CC=gcc-13
export CXX=g++-13
%endif
%{cargo_install} --features external-harfbuzz

%files
%{_bindir}/tectonic
%license LICENSE
%doc README.md

%changelog
