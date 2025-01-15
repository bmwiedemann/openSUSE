#
# spec file for package xfig
#
# Copyright (c) 2025 SUSE LLC
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
Version:        3.2.9a
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
Patch0:         xfig-3.2.6.dif
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
Requires:       urw-base35-fonts
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
%patch -P5 -b .null
%patch -P6 -b .locale
%patch -P7 -b .fixes
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
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/org.%name.%name.desktop VectorGraphics

%files
%defattr(-,root,root,755)
%doc %{_docdir}/%{name}
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/Fig
%{_bindir}/xfig*
%{_datadir}/applications/*xfig.desktop
%{_datadir}/metainfo/*xfig.metainfo.xml
%{_datadir}/pixmaps/xfig.png
%{_datadir}/xfig
%{_mandir}/man1/xfig.1*%{?ext_man}

%changelog
