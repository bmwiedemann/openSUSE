#
# spec file for package xfig
#
# Copyright (c) 2021 SUSE LLC
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
Version:        3.2.8a
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
#Source:        http://sourceforge.net/projects/mcj/files/xfig-%{version}.tar.xz/download#/xfig-%{version}.tar.xz
Source:         xfig-%{version}.tar.xz
Source1:        font-test.fig
Source3:        xfig.sh
Source4:        xfig.desktop
Patch0:         xfig-3.2.6.dif
Patch1:         xfig.3.2.5-urw-fonts.dif
Patch3:         xfig.3.2.3d-international-std-fonts.dif
# PATCH-FIX-UPSTREAM xfig.3.2.5b-mediaboxrealnb.dif [debian#530898]
Patch5:         xfig.3.2.5b-null.dif
Patch6:         xfig.3.2.5b-locale.dif
Patch7:         xfig.3.2.5b-fixes.dif
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  freetype2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  netpbm
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
%if 0%{?suse_version} > 1310
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw3d)
BuildRequires:  pkgconfig(xaw6)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
%else
BuildRequires:  xaw3d-devel
BuildRequires:  xorg-x11-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif
Requires:       efont-unicode
Requires:       ghostscript-fonts-std
Requires:       ifnteuro
Requires:       mkfontdir
Requires:       mkfontscale
Requires:       netpbm
Requires:       transfig
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
%patch0
%patch1   -b .urw-fonts
%patch3   -b .international-std-fonts
%patch5   -b .null
%patch6   -b .locale
%patch7   -b .fixes
cp %{SOURCE1} .
test ! -e Libraries/Examples/aircraft.fig || { echo forbidden file found 1>&2; exit 1; }

%build
%if 0%{?suse_version} <= 1310
cat > xaw3d.pc <<-'EOF'
	prefix=%{_prefix}
	exec_prefix=%{_prefix}
	libdir=%{_prefix}/lib
	includedir=%{_includedir}
Name:           Xaw3d
	Description: X 3D Athena Widgets Library
Version:        1.5E
Requires:       xmu
Requires:       xproto
Requires:       xt
	Requires.private: x11 xext
	Cflags: -I${includedir}  -DXAW_INTERNATIONALIZATION -DXAW_MULTIPLANE_PIXMAPS -DXAW_GRAY_BLKWHT_STIPPLES -DXAW_ARROW_SCROLLBARS
	Libs: -L${libdir} -lXaw3d
EOF
PKG_CONFIG_PATH=%{_datadir}/pkgconfig:%{_prefix}/lib/pkgconfig:${PWD}
export PKG_CONFIG_PATH
%endif
CC=gcc
CFLAGS="%{optflags} -fno-strict-aliasing -w -D_GNU_SOURCE -std=gnu99 -DUSE_XPM -DUSE_SPLASH"
CFLAGS="$CFLAGS -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 -DMAXNUMPTS=50000 -DBSDLPR -DGSBIT"
export CC CFLAGS
chmod +x configure
%configure \
    --docdir=%{_defaultdocdir}/%{name} \
    --enable-cache-size=512 \
    --enable-tablet \
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
