#
# spec file for package xfig
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


Name:           xfig
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  freetype2-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
%if 0%{suse_version} > 1310
BuildRequires:  libXaw3d-devel
%else
BuildRequires:  xaw3d-devel
%endif
BuildRequires:  libXmu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  netpbm
BuildRequires:  update-desktop-files
Provides:       xfig.3.2.3d
Requires:       efont-unicode
Requires:       ghostscript-fonts-std
Requires:       ifnteuro
Requires:       mkfontdir
Requires:       mkfontscale
Requires:       netpbm
Requires:       transfig
Requires:       xorg-x11-fonts
Requires:       xorg-x11-fonts-core
Version:        3.2.7b
Release:        0
Summary:        Facility for Interactive Generation of Figures under the X Window System
#  www.xfig.org is dead
License:        MIT
Group:          Productivity/Graphics/Vector Editors
Url:            http://mcj.sourceforge.net/
#
# Remove forbidden files: aircraft.fig
# <uncompess> xfig-3.2.5c.tar
# tar -f xfig-3.2.5c.tar --delete xfig-3.2.5c/Libraries/Examples/aircraft.fig
# <compress> xfig-3.2.5c.tar
#
#Source:        http://sourceforge.net/projects/mcj/files/xfig-%{version}.tar.xz/download#/xfig-%{version}.tar.xz
Source:         xfig-%{version}.tar.xz
Source1:        font-test.fig
Source3:        xfig.sh
Source4:        xfig.desktop
#Patch0:         xfig-%{version}.dif
Patch0:         xfig-3.2.6.dif
Patch1:         xfig.3.2.5-urw-fonts.dif
Patch2:         xfig.3.2.5-xim.dif
Patch3:         xfig.3.2.3d-international-std-fonts.dif
# PATCH-FIX-UPSTREAM xfig.3.2.5b-mediaboxrealnb.dif [debian#530898]
Patch5:         xfig.3.2.5b-null.dif
Patch6:         xfig.3.2.5b-locale.dif
Patch7:         xfig.3.2.5b-fixes.dif
Patch8:         xfig.3.2.5b-pspdftex.dif
Patch10:        xfig.3.2.5b-preview.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{expand: %%global _exec_prefix %(type -p pkg-config &>/dev/null && pkg-config --variable prefix x11 || echo /usr/X11R6)}
%if "%_exec_prefix" == "/usr/X11R6"
%global _mandir     %{_exec_prefix}/man
%define _x11data    %{_exec_prefix}/lib/X11
%define _data       $(LIBDIR)
%define _appdefdir  %{_x11data}/app-defaults
%else
%define _x11data    %{_datadir}/X11
%define _data       $(SHAREDIR)
%define _appdefdir  %{_x11data}/app-defaults
%endif

%description
Xfig is a menu-driven tool that allows the user to draw and manipulate
objects interactively in an X Window System window.  The resulting
pictures can be saved, printed on PostScript printers, or converted to
a variety of other formats (to allow inclusion in LaTeX documents, for
example).

Documentation: /usr/share/doc/packages/xfig & man xfig

Examples: /usr/share/doc/packages/xfig/TheExamples



Authors:
--------
    Anthony Dekker <dekker@ACM.org>
    Brian V. Smith <bvsmith@lbl.gov>
    Jim Daley      <jdaley@cix.compulink.co.uk>
    Ross Martin    <martin@trcsun3.eas.asu.edu>
    Uwe Bonnes     <bon@lte.e-technik.uni-erlangen.de>

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
%patch0  -p0
%patch1  -p0 -b .urw-fonts
%patch2  -p0 -b .xim
%patch3  -p0 -b .international-std-fonts
%patch5  -p0 -b .null
%patch6  -p0 -b .locale
%patch7  -p0 -b .fixes
%patch8  -p0 -b .pspdftex
%patch10 -p0 -b .preview
cp %{S:1} .
test ! -e Libraries/Examples/aircraft.fig || { echo forbidden file found 1>&2; exit 1; }

%build
%if 0%{suse_version} <= 1310
cat > xaw3d.pc <<-'EOF'
	prefix=/usr
	exec_prefix=/usr
	libdir=/usr/lib
	includedir=/usr/include
	Name: Xaw3d
	Description: X 3D Athena Widgets Library
	Version: 1.5E
	Requires: xproto xmu xt
	Requires.private: x11 xext
	Cflags: -I${includedir}  -DXAW_INTERNATIONALIZATION -DXAW_MULTIPLANE_PIXMAPS -DXAW_GRAY_BLKWHT_STIPPLES -DXAW_ARROW_SCROLLBARS
	Libs: -L${libdir} -lXaw3d
EOF
PKG_CONFIG_PATH=/usr/share/pkgconfig:/usr/lib/pkgconfig:${PWD}
export PKG_CONFIG_PATH
%endif
CC=gcc
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -w -D_GNU_SOURCE -std=gnu99 -DUSE_XPM -DUSE_SPLASH"
CFLAGS="$CFLAGS -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
CFLAGS="$CFLAGS -DMAXNUMPTS=50000"
CFLAGS="$CFLAGS -DBSDLPR"
CFLAGS="$CFLAGS -DGSBIT"
export CC CFLAGS
chmod 755 configure
%configure \
    --docdir=%{_defaultdocdir}/%{name} \
    --enable-cache-size=512 \
    --enable-tablet \
    --with-x \
    --with-xaw3d1_5e \
    --with-xaw3d
touch src/splash.xbm
touch src/splash.xpm
make %{?_smp_mflags} CCOPTIONS="$CFLAGS"

%install
find -name '*.bak' -exec rm -vf '{}' \+
make DESTDIR=%{buildroot} install
mv %{buildroot}%{_mandir}/man1/xfig.1 %{buildroot}%{_mandir}/man1/xfig.1x
gzip -9 %{buildroot}%{_mandir}/man1/xfig.1x
%fdupes %{buildroot}
%suse_update_desktop_file xfig VectorGraphics &> /dev/null

%files
%defattr(-,root,root,755)
%doc %{_docdir}/%{name}
%dir %{_appdefdir}
%{_appdefdir}/Fig
%{_bindir}/xfig*
%{_datadir}/applications/xfig.desktop
%{_datadir}/pixmaps/xfig.png
%{_datadir}/xfig
%doc %{_mandir}/man1/xfig.1*.gz

%changelog
