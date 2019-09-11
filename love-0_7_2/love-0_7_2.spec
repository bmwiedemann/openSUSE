#
# spec file for package love-0_7_2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Url:            http://love2d.org/

Source:         https://bitbucket.org/rude/love/downloads/love-0.7.2-linux-src.tar.gz
Patch1:         love-modplug.patch
Patch2:         system-packages.diff
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
%setup -qn love-HEAD
%patch -P 1 -P 2 -p1

%build
sed -i 's/\r$//' *.txt
mv configure.{in,ac}
autoreconf -fi
export CPPFLAGS="-DGL_GLEXT_PROTOTYPES"
%configure
make %{?_smp_mflags}

%install
b="%buildroot";
make install DESTDIR="$b"
mv "$b/%_bindir"/love{,-0.7.2}

%files
%defattr(-,root,root)
%doc changes.txt license.txt readme.txt
%_bindir/love-0.7.2

%changelog
