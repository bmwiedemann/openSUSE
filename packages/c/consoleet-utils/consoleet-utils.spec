#
# spec file for package consoleet-utils
#
# Copyright (c) 2022 SUSE LLC
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


Name:           consoleet-utils
Version:        1.1
Release:        0
Summary:        Utilities for manipulating terminal fonts and colors
License:        GPL-3.0-or-later and MIT
Group:          Productivity/Other
URL:            https://inai.de/projects/consoleet/
#Git-Clone:     https://codeberg.org/consoleet/consoleet-utils
Source:         https://inai.de/files/consoleet/%name-%version.tar.zst
Source2:        https://inai.de/files/consoleet/%name-%version.tar.asc
Source3:        %name.keyring
Patch1:         libhx.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  zstd
BuildRequires:  pkgconfig >= 0.21
BuildRequires:  pkgconfig(libHX) >= 3.22
Conflicts:      hxtools < 20200310
Obsoletes:      vfontas < 20221121
Provides:       vfontas = 20221121

%description
This is a set of utilities for manipulating terminal fonts and
colors.

A key component is vfontas, which can read/write bitmap fonts from/to
a number of formats and transform the glyphs in various ways. vfontas
is able to generate outline fonts from bitmapped fonts, including a
high-quality mode that upscales based on outline rather than pixel
blocks, setting it apart from scalers like xBRZ or potrace.

%prep
%if 0%{?suse_version} < 1550
%setup -Tcq
pushd .. && tar --use=zstd -xf %{S:0} && popd
%patch -P 1 -p1
%else
%autosetup -p1
%endif

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%license LICENSE*
%_bindir/*
%_mandir/man1/*.1*

%changelog
