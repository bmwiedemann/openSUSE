#
# spec file for package xorg-x11-libs
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


Name:           xorg-x11-libs
Version:        7.6.1
Release:        0
Summary:        Compatibility metapackage for X.Org libraries
License:        GPL-2.0-or-later AND MIT
Group:          System/Libraries
Url:            http://xorg.freedesktop.org/
Source0:        README.meta
# bug437293
%ifarch ppc64
Obsoletes:      xorg-x11-libs-64bit
%endif
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package is a compatibility metapackage. It used to contain the
X.Org libraries.

%package -n xorg-x11-devel
Summary:        Compatibility metapackage for X.Org development libraries
Group:          Development/Libraries/X11
Provides:       XFree86-devel
Provides:       xorg-x11-compat70-devel
Provides:       xorg-x11-man
Provides:       xorg-x11-util-devel = 7.6.1
Obsoletes:      xorg-x11-compat70-devel
Obsoletes:      xorg-x11-man
Obsoletes:      xorg-x11-util-devel < 7.6.1
# bug437293
%ifarch ppc64
Obsoletes:      xorg-x11-devel-64bit
%endif
Requires:       Mesa-libEGL-devel
Requires:       Mesa-libGL-devel
Requires:       fontconfig-devel
Requires:       freetype2-devel
Requires:       libFS-devel
Requires:       libICE-devel
Requires:       libSM-devel
Requires:       libX11-devel
Requires:       libXScrnSaver-devel
%if 0%{?suse_version} < 1550
Requires:       libXTrap-devel
%endif
Requires:       libXau-devel
Requires:       libXaw-devel
Requires:       libXcomposite-devel
Requires:       libXcursor-devel
Requires:       libXdamage-devel
Requires:       libXdmcp-devel
Requires:       libXevie-devel
Requires:       libXext-devel
Requires:       libXfixes-devel
Requires:       libXfont-devel
Requires:       libXfontcache-devel
Requires:       libXft-devel
Requires:       libXi-devel
Requires:       libXi6-devel
Requires:       libXinerama-devel
Requires:       libXmu-devel
Requires:       libXp-devel
Requires:       libXpm-devel
Requires:       libXprintAppUtil-devel
Requires:       libXprintUtil-devel
Requires:       libXrandr-devel
Requires:       libXrender-devel
Requires:       libXres-devel
Requires:       libXt-devel
Requires:       libXtst-devel
Requires:       libXv-devel
Requires:       libXvMC-devel
Requires:       libXxf86dga-devel
%if 0%{?suse_version} < 1550
Requires:       libXxf86misc-devel
%endif
Requires:       libXxf86vm-devel
Requires:       libdmx-devel
Requires:       libfontenc-devel
Requires:       liblbxutil-devel
Requires:       liboldX-devel
Requires:       libpciaccess-devel
Requires:       libpixman-1-0-devel
Requires:       libxcb-devel
Requires:       libxkbfile-devel
Requires:       libxkbui-devel
Requires:       pkgconfig
Requires:       xbitmaps-devel
%if %suse_version > 1210
Requires:       xcb-util-devel
%else
Requires:       xcb-util-0_3_6-devel
%endif
Requires:       xorg-x11-fonts-devel
Requires:       xorg-x11-libxcb-devel
Requires:       xorg-x11-libxkbfile-devel
Requires:       xorg-x11-xtrans-devel
# Directly require packages, which were required by xorg-x11-util-devel
# meta package (bsc#1077489)
Requires:       gccmakedep
Requires:       imake
Requires:       lndir
Requires:       makedepend
Requires:       xorg-cf-files
Requires:       xorg-sgml-doctools

%description -n xorg-x11-devel
This package is a compatibility metapackage. It used to contain the
X.Org development libraries.

%prep
%setup -T -c
cp %{SOURCE0} .

%build

%install

%files
%defattr(-,root,root)
%doc README.meta

%files -n xorg-x11-devel
%defattr(-,root,root)
%doc README.meta

%changelog
