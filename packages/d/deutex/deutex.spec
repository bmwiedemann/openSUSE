#
# spec file for package deutex
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           deutex
Version:        5.2.2
Release:        0
Summary:        WAD composer for Doom and related games
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
#Historic-URL:  http://www.teaser.fr/~amajorel/deutex/
URL:            https://github.com/Doom-Utils/deutex
Source:         https://github.com/Doom-Utils/deutex/releases/download/v%version/%name-%version.tar.zst
Source2:        https://github.com/Doom-Utils/deutex/releases/download/v%version/%name-%version.tar.zst.sig
BuildRequires:  asciidoc
BuildRequires:  automake
BuildRequires:  pkg-config
BuildRequires:  zstd

%description
DeuTex is a .wad file composer for Doom, Heretic, Hexen and Strife.
It can be used to extract the lumps of a WAD and save them as
individual files. Conversely, it can also build a WAD from separate
files. When extracting a lump to a file, it does not just copy the
raw data, it converts it to an appropriate format (such as PNG for
graphics, WAVE for audio samples, etc.). Conversely, when it reads
files for inclusion in PWADs, it does the necessary conversions (for
example, from PPM to Doom picture format). In addition, DeuTex has
functions such as merging WADs.

%prep
%if 0%{?suse_version} < 1550
# Leap <= 15.3 does not support tar with zstd
%setup -T -c
tar -I zstd --strip-components=1 -xf %{SOURCE0}
%else
%autosetup -p1
%endif

%build
autoreconf -fiv
%configure --enable-man
%make_build

%install
%make_install

%files
%license COPYING COPYING.LIB
%_bindir/*
%_mandir/man6/%name.6%ext_man

%changelog
