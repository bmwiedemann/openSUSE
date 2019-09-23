#
# spec file for package xplanet
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 B1 Systems GmbH, Vohburg, Germany.
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


Name:           xplanet
Version:        1.3.1
Release:        0
Summary:        Planets as Background Pictures or Interactive Animations
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Astronomy
URL:            http://xplanet.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# new giflib-5 api
Patch0:         xplanet-giflib5.patch
# PATCH-FIX-UPSTREAM gcc6.patch boo#985129 asterios.dramis@gmail.com -- Fix compilation with GCC 6
Patch1:         gcc6.patch
Patch2:         glib2.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  glib2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  pango-devel
%if 0%{?suse_version}
BuildRequires:  libnetpbm-devel
%else
BuildRequires:  netpbm-devel
%endif
%if 0%{?suse_version} == 1110
BuildRequires:  xorg-x11-devel
BuildRequires:  xorg-x11-libICE-devel
#BuildRequires:  XScrnSaver-devel
%else
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xscrnsaver)
%endif

%description
Xplanet can display the earth or other planets in the background of
your display, similar to xearth or xglobe. Additionally, it can run in
interactive mode allowing you to rotate or zoom the planet. Also, with
an included script, it is very easy to combine map files with current
satellite cloud images.

%prep
%setup -q
%if 0%{?suse_version} > 1320
%patch0 -p1
%endif
%patch1
%patch2 -p1

%build
autoreconf -fi
# configure does not check if netpbm headers are installed in /usr/include/netpbm
export CPPFLAGS=-I%{_includedir}/netpbm
# Set our preferred architecture-specific flags for the compiler and linker:
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/%{name}/

%changelog
