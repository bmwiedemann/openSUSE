#
# spec file for package xorg-x11
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xorg-x11
Url:            http://xorg.freedesktop.org/
Version:        7.6_1
Release:        0
## Recommends of packages that we split away from xorg-x11
Recommends:     appres
Recommends:     bdftopcf
Recommends:     beforelight
Recommends:     bitmap
Recommends:     editres
Recommends:     fonttosfnt
Recommends:     fslsfonts
Recommends:     fstobdf
Recommends:     ico
Recommends:     lbxproxy
Recommends:     listres
Recommends:     luit
Recommends:     mkcomposecache
Recommends:     oclock
Recommends:     proxymngr
Recommends:     rendercheck
Recommends:     rstart
Recommends:     showfont
Recommends:     smproxy
Recommends:     twm
Recommends:     viewres
Recommends:     x11perf
Recommends:     xbacklight
Recommends:     xbiff
Recommends:     xcalc
Recommends:     xclipboard
Recommends:     xclock
Recommends:     xcmsdb
Recommends:     xcompmgr
Recommends:     xcursor-themes
Recommends:     xcursorgen
Recommends:     xdbedizzy
Recommends:     xditview
Recommends:     xdpyinfo
Recommends:     xedit
Recommends:     xev
Recommends:     xeyes
Recommends:     xf86dga
Recommends:     xfd
Recommends:     xfindproxy
Recommends:     xfontsel
Recommends:     xfs
Recommends:     xfsinfo
Recommends:     xfwp
Recommends:     xgamma
Recommends:     xgc
Recommends:     xhost
Recommends:     xinput
Recommends:     xkbevd
Recommends:     xkbprint
Recommends:     xkbutils
Recommends:     xkill
Recommends:     xload
Recommends:     xlogo
Recommends:     xlsatoms
Recommends:     xlsclients
Recommends:     xlsfonts
Recommends:     xmag
Recommends:     xman
Recommends:     xmore
Recommends:     xorg-scripts
Recommends:     xplsprinters
Recommends:     xpr
Recommends:     xprehashprinterlist
Recommends:     xrandr
Recommends:     xrefresh
Recommends:     xrestop
Recommends:     xrx
Recommends:     xscope
Recommends:     xsetmode
Recommends:     xsetpointer
Recommends:     xsm
Recommends:     xstdcmap
Recommends:     xtrap
Recommends:     xvidtune
Recommends:     xvinfo
Recommends:     xwd
Recommends:     xwininfo
Recommends:     xwud
## End Recommends of packages that we split away from xorg-x11
Requires:       xorg-x11-essentials
Provides:       XFree86
Summary:        Compatibility metapackage for X.Org sample applications
License:        MIT
Group:          System/X11/Utilities
Source0:        README.meta
Source200:      misc.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package is a compatibility metapackage. It used to contain the
X.Org sample applications.

%package essentials
Summary:        Compatibility metapackage for X.Org core applications
Group:          System/X11/Utilities
## Requires of packages that we split away from xorg-x11
Requires:       iceauth
Requires:       mkfontdir
Requires:       mkfontscale
Requires:       rgb
Requires:       sessreg
Requires:       setxkbmap
Requires:       xauth
Requires:       xconsole
Requires:       xdm
Requires:       xinit
Requires:       xkbcomp
Requires:       xmessage
Requires:       xmodmap
Requires:       xprop
Requires:       xrdb
Requires:       xset
Requires:       xsetroot
## End Requires of packages that we split away from xorg-x11

%description essentials
This package is a compatibility metapackage. It requires the
X.Org core applications packages.

%prep
%setup -q -T -c '%{name}'
cp %{SOURCE0} .

%build

%install
pushd $RPM_BUILD_ROOT
%{__tar} xjf '%{S:200}'
popd
# Compatibility symlink (Bug #223524)
mkdir -p "${RPM_BUILD_ROOT}%{_bindir}"
%{__ln_s}nf . "${RPM_BUILD_ROOT}%{_bindir}/X11"

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README.meta

%files essentials
%defattr(-,root,root)
%dir %{_datadir}/X11
%{_datadir}/X11/nls/
%{_bindir}/X11

%changelog
