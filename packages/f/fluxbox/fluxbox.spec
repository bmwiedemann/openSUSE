#
# spec file for package fluxbox
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           fluxbox
Version:        1.3.7
Release:        0
Summary:        A window manager for X based on Blackbox 0.61.1
License:        MIT
Group:          System/GUI/Other
Url:            http://www.fluxbox.org/
Source0:        https://downloads.sourceforge.net/project/fluxbox/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        fluxboxmenu
Source2:        SUSE.tar.bz2
Source3:        fluxbox.desktop
# PATCH-FIX-OPENSUSE fluxbox-remove_build_timestamp.patch -- removes __DATE and __TIME from the resulting binary
Patch1:         fluxbox-remove_build_timestamp.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Recommends:     %{name}-styles-upstream
Provides:       windowmanager

BuildRequires:  fribidi-devel
BuildRequires:  gcc-c++
BuildRequires:  imlib2-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
# fdupes not available on SLE10
%if 0%{?suse_version} >= 1100
BuildRequires:  fdupes
%endif

%description
Fluxbox is a stacking windowmanager for the X Window System which
started as a fork of Blackbox 0.61.1 in 2001. Its user interface has
only a taskbar, a pop-up menu accessible by right-clicking on the
desktop, and minimal support for graphical icons. All basic
configurations are controlled by text files, including the
construction of menus and the mapping of key-bindings. Fluxbox
supports the Extended Window Manager Hints specification.

%package styles-upstream
Summary:        Upstream bundle of styles for fluxbox
Group:          System/GUI/Other
BuildArch:      noarch
Requires:       %{name}

%description styles-upstream
Fluxbox is a stacking windowmanager for the X Window System which
started as a fork of Blackbox 0.61.1 in 2001. Its user interface has
only a taskbar, a pop-up menu accessible by right-clicking on the
desktop, and minimal support for graphical icons.

This package provides the upstream bundle of styles.

%prep
%setup -q -a 2
%patch1

%build
export RPM_OPT_FLAGS="%{optflags} -fno-strict-aliasing -Wno-unused"
export CFLAGS="$RPM_OPT_FLAGS -fvisibility=hidden"
export CXXFLAGS="$RPM_OPT_FLAGS -fvisibility=hidden -fvisibility-inlines-hidden"

%configure \
   --enable-remember \
   --enable-regexp \
   --enable-slit \
   --enable-toolbar \
   --enable-ewnh \
   --enable-nls \
   --enable-timedcache \
   --enable-xft \
   --enable-xrender \
   --enable-xpm \
   --enable-imlib2 \
   --enable-xmb \
   --enable-xinerama \
   --enable-shape \
   --enable-randr \
   --enable-fribidi \
   --with-style=%{_datadir}/fluxbox/styles/SUSE
make %{?_smp_mflags} V=1

%install
%make_install
# Install desktop file for xdm/gdm
install -D -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/xsessions/fluxbox.desktop
# menu
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/fluxbox/menu
# theme
mv SUSE %{buildroot}%{_datadir}/fluxbox/styles/
# fdupes not available on SLE10
%if 0%{?suse_version} >= 1100
%fdupes %{buildroot}%{_datadir}/%{name}
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %{_datadir}/fluxbox/
%dir %{_datadir}/fluxbox/styles
%{_bindir}/fluxbox*
%{_bindir}/startfluxbox
%{_bindir}/fbrun
%{_bindir}/fbsetbg
%{_bindir}/fbsetroot
%{_datadir}/fluxbox/apps
%{_datadir}/fluxbox/init
%{_datadir}/fluxbox/keys
%{_datadir}/fluxbox/menu
%{_datadir}/fluxbox/overlay
%{_datadir}/fluxbox/windowmenu
%{_datadir}/fluxbox/nls/
%{_datadir}/fluxbox/styles/SUSE/
%{_datadir}/xsessions/fluxbox.desktop
%{_mandir}/man1/fluxbox.1*
%{_mandir}/man1/startfluxbox.1*
%{_mandir}/man1/fbsetroot.1*
%{_mandir}/man1/fbsetbg.1*
%{_mandir}/man1/fbrun.1*
%{_mandir}/man1/fluxbox-remote.1*
%{_mandir}/man5/fluxbox-keys.5*
%{_mandir}/man5/fluxbox-apps.5*
%{_mandir}/man5/fluxbox-menu.5*
%{_mandir}/man5/fluxbox-style.5*

%files styles-upstream
%defattr(-,root,root,-)
%{_datadir}/fluxbox/styles/Artwiz
%{_datadir}/fluxbox/styles/BlueFlux/
%{_datadir}/fluxbox/styles/BlueNight
%{_datadir}/fluxbox/styles/Emerge/
%{_datadir}/fluxbox/styles/Flux
%{_datadir}/fluxbox/styles/LemonSpace
%{_datadir}/fluxbox/styles/Makro
%{_datadir}/fluxbox/styles/MerleyKay
%{_datadir}/fluxbox/styles/Nyz
%{_datadir}/fluxbox/styles/Operation
%{_datadir}/fluxbox/styles/Outcomes
%{_datadir}/fluxbox/styles/Results
%{_datadir}/fluxbox/styles/Shade
%{_datadir}/fluxbox/styles/Twice
%{_datadir}/fluxbox/styles/arch/
%{_datadir}/fluxbox/styles/bloe/
%{_datadir}/fluxbox/styles/bora_black/
%{_datadir}/fluxbox/styles/bora_blue/
%{_datadir}/fluxbox/styles/bora_green/
%{_datadir}/fluxbox/styles/carp/
%{_datadir}/fluxbox/styles/green_tea/
%{_datadir}/fluxbox/styles/ostrich/
%{_datadir}/fluxbox/styles/qnx-photon
%{_datadir}/fluxbox/styles/zimek_bisque/
%{_datadir}/fluxbox/styles/zimek_darkblue/
%{_datadir}/fluxbox/styles/zimek_green/
%{_datadir}/fluxbox/styles/Meta

%changelog
