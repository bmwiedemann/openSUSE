#
# spec file for package surf
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           surf
Version:        1.0.6
Release:        0
Summary:        Algebraic geometry visualizer
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
URL:            http://surf.sf.net/
Source:         https://downloads.sf.net/surf/%name-%version.tar.gz
Patch1:         surf-remove-gtk1.diff
Patch2:         surf-annoy.diff
Patch3:         surf-overlapping.diff
Patch4:         surf-partial.diff
Patch5:         surf-noext.diff
Patch6:         surf-minmax.diff
BuildRequires:  bison
BuildRequires:  cups-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  xorg-x11-devel
BuildRequires:  zlib-devel
Provides:       surf(partial-rendering) = %version-%release

%description
surf is a tool to visualize some real algebraic geometry: plane
algebraic curves, algebraic surfaces and hyperplane sections of
surfaces. surf is script driven and has (optionally) a nifty GUI
using the Gtk widget set.

%prep
%autosetup -p1
mv debug/debug.h debug/sdebug.h

%build
autoreconf -fi
chmod a+x configure
# surf wants gtk1, and that no longer exists.
%configure --disable-gui
%make_build

%install
%make_install
%fdupes %buildroot/%_prefix

%files
%_bindir/surf
%_mandir/man*/surf.1*
%_datadir/surf
%license COPYING

%changelog
