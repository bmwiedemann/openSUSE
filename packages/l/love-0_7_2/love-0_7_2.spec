#
# spec file for package love-0_7_2
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


Name:           love-0_7_2
Version:        0.7.2
Release:        0
Summary:        2D gaming engine written in Lua
License:        Zlib
Group:          Development/Languages/Other
URL:            http://love2d.org/
Source:         https://github.com/love2d/love/releases/download/%version/love-%version-linux-src.tar.gz
Patch1:         love-modplug.patch
Patch2:         system-packages.diff
Patch3:         0001-Clean-up-warnings-in-luasocket-and-box2d.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libmng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  physfs-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(IL)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(lua5.1)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(vorbisfile)

%description
LÖVE is a framework for making 2D games in Lua.

%prep
%autosetup -n love-HEAD -p1

%build
sed -i 's/\r$//' *.txt
mv configure.{in,ac}
autoreconf -fi
export CPPFLAGS="-DGL_GLEXT_PROTOTYPES"
%configure
%make_build

%install
%make_install
mv "%buildroot/%_bindir/love" "%buildroot/%_bindir/love-0.7.2"

%files
%license license.txt
%doc readme.txt
%_bindir/love-0.7.2

%changelog
