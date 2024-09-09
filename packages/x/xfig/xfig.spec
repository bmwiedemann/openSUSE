#
# spec file for package xfig
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


Name:           xfig
Version:        3.2.9
Release:        0
Summary:        Facility for Interactive Generation of Figures under the X Window System
License:        MIT
Group:          Productivity/Graphics/Vector Editors
URL:            https://sourceforge.net/projects/mcj/
#
# Remove forbidden files: aircraft.fig
# <uncompess> xfig-3.2.8a.tar
# tar -f xfig-3.2.8a.tar --delete xfig-3.2.8a/Libraries/Examples/aircraft.fig
# <compress> xfig-3.2.8a.tar
#
#Source:        https://sourceforge.net/projects/mcj/files/xfig-%{version}.tar.xz/download#/xfig-%{version}.tar.xz
Source:         xfig-%{version}.tar.xz
Source1:        font-test.fig
Source4:        xfig.desktop
Patch0:         xfig-3.2.6.dif
Patch1:         xfig-3.2.9-dingbats.dif
Patch3:         xfig.3.2.3d-international-std-fonts.dif
# PATCH-FIX-UPSTREAM xfig.3.2.5b-mediaboxrealnb.dif [debian#530898]
Patch5:         xfig.3.2.5b-null.dif
Patch6:         xfig.3.2.5b-locale.dif
Patch7:         xfig.3.2.5b-fixes.dif
# PATCH-FIX-UPSTREAM
Patch8:         Sanitize-a-call-to-realloc-ticket-165.patch
# PATCH-FIX-UPSTREAM
Patch9:         Fix-exporting-only-active-layers-ticket-163.patch
# PATCH-FIX-UPSTREAM
Patch10:        xfig-3.2.9-gcc14.patch
# PATCH-FIX-UPSTREAM for boo#1230298 / upstream bug report #179
Patch11:        042708.patch
Patch12:        7e0157.patch
Patch13:        a038d6.patch
Patch14:        f3466c.patch
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  freetype2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  netpbm
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(ijs)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw3d)
BuildRequires:  pkgconfig(xaw6)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
Requires:       efont-unicode
Requires:       fontconfig
%if 0%{?suse_version} >= 1699
Requires:       (ghostscript-fonts-std or urw-base35-fonts)
%else
Requires:       ghostscript-fonts-std
%endif
Requires:       ifnteuro
Requires:       netpbm
Requires:       transfig >= %{version}
Requires:       xorg-x11-fonts
Requires:       xorg-x11-fonts-core
Provides:       xfig.3.2.3d
%if ! %{defined make_build}
%define make_build make %{?_smp_mflags}
%endif
%if ! %{defined make_install}
%define make_install make install DESTDIR=%{?buildroot} INSTALL="install -p"
%endif

%description
Xfig is a menu-driven tool that allows the user to draw and manipulate
objects interactively in an X Window System window.  The resulting
pictures can be saved, printed on PostScript printers, or converted to
a variety of other formats (to allow inclusion in LaTeX documents, for
example).

%prep
%setup -q -n xfig-%{version}
set +x
find -type f | xargs -r chmod a-x,go-w
find -type f | while read file; do
    if grep -qr $'\r' $file ; then
	dos2unix --keepdate --quiet $file
    fi
done
set -x
%patch -P0
%patch -P1 -b .dingbats
%patch -P3 -b .international-std-fonts
%patch -P5 -b .null
%patch -P6 -b .locale
%patch -P7 -b .fixes
%patch -P8 -p1
%patch -P9 -p1
%patch -P10
%patch -P11
%patch -P12
%patch -P13
%patch -P14
cp %{SOURCE1} .
test ! -e Libraries/Examples/aircraft.fig || { echo forbidden file found 1>&2; exit 1; }

%build
CC=gcc
CFLAGS="%{optflags} -w -D_GNU_SOURCE -std=gnu99 -DUSE_XPM -DUSE_SPLASH"
CFLAGS="$CFLAGS $(getconf LFS_CFLAGS) -DMAXNUMPTS=50000"
export CC CFLAGS
chmod +x configure
%configure \
    --docdir=%{_defaultdocdir}/%{name} \
    --enable-tablet \
    --enable-splash \
    --with-x \
    --with-xaw3d1_5e \
    --with-xaw3d
touch src/splash.xbm
touch src/splash.xpm
%make_build CCOPTIONS="$CFLAGS"

%install
find -name '*.bak' -exec rm -vf '{}' \+
%make_install
mv %{buildroot}%{_mandir}/man1/xfig.1 %{buildroot}%{_mandir}/man1/xfig.1x
gzip -9 %{buildroot}%{_mandir}/man1/xfig.1x
%fdupes %{buildroot}
%suse_update_desktop_file xfig VectorGraphics

%files
%defattr(-,root,root,755)
%doc %{_docdir}/%{name}
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/Fig
%{_bindir}/xfig*
%{_datadir}/applications/xfig.desktop
%{_datadir}/pixmaps/xfig.png
%{_datadir}/xfig
%{_mandir}/man1/xfig.1*.gz

%changelog
