#
# spec file for package icewm
#
# Copyright (c) 2022 SUSE LLC
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


%global lites icewm icewmhint icewmbg icesh icewm-session
Name:           icewm
Version:        3.2.2
Release:        0
Summary:        Window Manager with a Taskbar
License:        LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://ice-wm.org/
Source0:        https://github.com/ice-wm/%{name}/releases/download/%{version}/%{name}-%{version}.tar.lz
# PATCH-FEATURE-SUSE icewm-susemenu.patch tyang@suse.com -- Add xdg-menu for SLED icewm
Patch1:         icewm-susemenu.patch
# PATCH-FIX-OPENSUSE icewm-desktop-nodisplay.patch qkzhu@suse.com -- Set NoDisplay for icewm.desktop
Patch2:         icewm-desktop-nodisplay.patch
Patch99:        icewm-preferences.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  lzip
BuildRequires:  pkgconfig
BuildRequires:  update-alternatives
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
Requires:       alsa-utils
Requires:       desktop-data
Requires:       icewm-bin
Requires:       imlib2-loaders
Requires:       xdg-menu
Requires(post): update-alternatives
Requires(postun):update-alternatives
# If you have the choice, prefer the big one.
Recommends:     icewm-default
Recommends:     icewm-lang = %{version}
Recommends:     xclock
# For locking you need xscreensaver
Recommends:     xscreensaver
Provides:       icewm-gnome = %{version}
Obsoletes:      icewm-gnome < %{version}
Provides:       windowmanager
# Needed for documentation.
%if 0%{?suse_version} <= 1320
BuildRequires:  asciidoc
%else
BuildRequires:  rubygem(asciidoctor)
%endif
%if !0%{?sle_version}
Requires:       icewm-configuration-files
%else
Requires:       icewm-theme-branding
%endif
%if 0%{?sle_version}
Recommends:     polkit-gnome
%endif
%if 0%{?suse_version} > 1315
Requires:       xterm-bin
%else
Requires:       xterm
%endif

%description
A window manager for the X Window System that can emulate the look
of Windows '95, OS/2 Warp 3, OS/2 Warp 4, and Motif and tries to
take the best features from those systems. IceWM features multiple
workspaces, opaque move and resize, a taskbar, a window list,
mailbox status, and a digital clock. It is fast and small.

%package config-upstream
Summary:        Window Manager with a Taskbar -- Default configuration
Group:          System/GUI/Other
Conflicts:      icewm-theme-branding
Provides:       icewm-configuration-files = %{version}
BuildArch:      noarch

%description config-upstream
A window manager for the X Window System that can emulate the look
of Windows '95, OS/2 Warp 3, OS/2 Warp 4, and Motif and tries to
take the best features from those systems. IceWM features multiple
workspaces, opaque move and resize, a taskbar, a window list,
mailbox status, and a digital clock. It is fast and small.

Configuration files from upstream provider without suse branding

%package default
Summary:        Window Manager with a Taskbar -- Default Version
Group:          System/GUI/Other
Requires:       adwaita-icon-theme
Requires:       icewm
Requires:       update-alternatives
Recommends:     icewm-lang
Provides:       icewm-bin

%description default
A window manager for the X Window System that can emulate the look
of Windows '95, OS/2 Warp 3, OS/2 Warp 4, and Motif and tries to
take the best features from those systems. IceWM features multiple
workspaces, opaque move and resize, a taskbar, a window list,
mailbox status, and a digital clock. It is fast and small.

%package lite
Summary:        Window Manager with a Taskbar -- Lite Version
Group:          System/GUI/Other
Requires:       icewm
Requires:       update-alternatives
Recommends:     icewm-lang
Provides:       icewm-bin

%description lite
A window manager for the X Window System that can emulate the look
of Windows '95, OS/2 Warp 3, OS/2 Warp 4, and Motif and tries to
take the best features from those systems. IceWM features multiple
workspaces, opaque move and resize, a taskbar, a window list,
mailbox status, and a digital clock. It is fast and small.

%lang_package

%prep
%setup -q
%patch1 -p1
%patch2 -p1

# Do not require needlessly new gettext.
sed -i 's/0.19.6/0.18.3/g' configure.ac

%build
autoreconf -fi
# Build the Lite version
%configure \
  --disable-silent-rules             \
  --with-cfgdir=%{_sysconfdir}/icewm \
  --enable-i18n                      \
  --disable-nls                      \
  --disable-guievents                \
  --disable-winmenu                  \
  --without-icesound                 \
  --enable-lite                      \
  --enable-taskbar                   \
  --disable-menus-fdo                \
  --disable-menus-mate               \
  --disable-fribidi
%make_build
# Grab the lite content.
mkdir lite
for file in %{lites}; do
    mv -f src/$file lite/$file-lite
done
%make_build clean
# Configure for full deployment.
%configure \
  --docdir=%{_docdir}/%{name}        \
  --disable-silent-rules             \
  --with-cfgdir=%{_sysconfdir}/icewm \
  --with-icesound=alsa               \
  --enable-i18n                      \
  --enable-nls                       \
  --enable-corefonts                 \
  --enable-guievents                 \
  --enable-antialiasing              \
  --enable-gradients                 \
  --enable-shaped-decorations        \
  --enable-menus-fdo                 \
  --enable-i18n
%make_build
%if !0%{?sle_version}
# Patch generated lib/preferences file.
patch -p1 -i %{PATCH99}
# And use proper branding
wallpaper="openSUSEdefault"
sed -i \
    -e "s:BRANDING_PICTURE:%{_datadir}/wallpapers/$wallpaper/contents/images/1920x1080.jpg:" \
    src/preferences
%endif

%install
%make_install

# First just remove GNOME WM setter as we don't have GNOME 2 anyway.
rm -f %{buildroot}%{_bindir}/icewm-set-{gnomewm,matewm}

mkdir -p %{buildroot}%{_sysconfdir}/icewm/
for cfgfile in keys menu preferences toolbar winoptions programs; do
    mv -f %{buildroot}%{_datadir}/icewm/$cfgfile \
      %{buildroot}%{_sysconfdir}/icewm/
done
# move preferences to prefoverride to take preference over themes
mv %{buildroot}/%{_sysconfdir}/icewm/preferences \
   %{buildroot}/%{_sysconfdir}/icewm/prefoverride
%find_lang icewm
ln -sf icewm.html %{buildroot}/%{_docdir}/icewm/index.html

mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
for file in %{lites}; do
    mv -f lite/$file-lite %{buildroot}%{_bindir}
    mv -f %{buildroot}%{_bindir}/$file %{buildroot}%{_bindir}/$file-default

    # Dummy.
    touch %{buildroot}%{_sysconfdir}/alternatives/$file
    ln -s %{_sysconfdir}/alternatives/$file %{buildroot}%{_bindir}/$file
done

%suse_update_desktop_file %{buildroot}%{_datadir}/xsessions/icewm-session.desktop

mv -f %{buildroot}%{_datadir}/xsessions/icewm-session.desktop %{buildroot}%{_datadir}/xsessions/icewm.desktop
ln -s icewm.desktop %{buildroot}%{_datadir}/xsessions/icewm-session.desktop

touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

# Link duplicate theme icons to save some space.
%fdupes %{buildroot}%{_datadir}/icewm/themes/

%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/icewm-session.desktop 15

%postun
[ -f %{_datadir}/xsessions/icewm-session.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/icewm-session.desktop

%post lite
%{_sbindir}/update-alternatives \
  --install %{_bindir}/icewm       icewm         %{_bindir}/icewm-lite 0       \
  --slave %{_bindir}/icewmhint     icewmhint     %{_bindir}/icewmhint-lite     \
  --slave %{_bindir}/icewmbg       icewmbg       %{_bindir}/icewmbg-lite       \
  --slave %{_bindir}/icesh         icesh         %{_bindir}/icesh-lite         \
  --slave %{_bindir}/icewm-session icewm-session %{_bindir}/icewm-session-lite

%postun lite
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove icewm %{_bindir}/icewm-lite
fi

%post default
%{_sbindir}/update-alternatives \
  --install %{_bindir}/icewm       icewm         %{_bindir}/icewm-default 100     \
  --slave %{_bindir}/icewmhint     icewmhint     %{_bindir}/icewmhint-default     \
  --slave %{_bindir}/icewmbg       icewmbg       %{_bindir}/icewmbg-default       \
  --slave %{_bindir}/icesh         icesh         %{_bindir}/icesh-default         \
  --slave %{_bindir}/icewm-session icewm-session %{_bindir}/icewm-session-default

%postun default
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove icewm %{_bindir}/icewm-default
fi

%files
%doc %{_docdir}/icewm
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%{_datadir}/icewm/
%{_datadir}/xsessions/icewm-session.desktop
%{_datadir}/xsessions/icewm.desktop
%{_datadir}/xsessions/default.desktop
%{_mandir}/man1/*
%{_mandir}/man5/*

%files config-upstream
%dir %{_sysconfdir}/icewm/
%config %{_sysconfdir}/icewm/*

%files lang -f icewm.lang

%files default
%ghost %{_sysconfdir}/alternatives/icewm
%ghost %{_sysconfdir}/alternatives/icewmhint
%ghost %{_sysconfdir}/alternatives/icewmbg
%ghost %{_sysconfdir}/alternatives/icesh
%ghost %{_sysconfdir}/alternatives/icewm-session
%{_bindir}/icewm-default
%{_bindir}/icewmhint-default
%{_bindir}/icewmbg-default
%{_bindir}/icehelp
%{_bindir}/icesh-default
%{_bindir}/icewm-session-default
%{_bindir}/icesound
%{_bindir}/icewm
%{_bindir}/icewmhint
%{_bindir}/icewmbg
%{_bindir}/icesh
%{_bindir}/icewm-session
%{_bindir}/icewm-menu-fdo
%{_bindir}/icewm-menu-xrandr

%files lite
%ghost %{_sysconfdir}/alternatives/icewm
%ghost %{_sysconfdir}/alternatives/icewmhint
%ghost %{_sysconfdir}/alternatives/icewmbg
%ghost %{_sysconfdir}/alternatives/icesh
%ghost %{_sysconfdir}/alternatives/icewm-session
%{_bindir}/icewm-lite
%{_bindir}/icewmhint-lite
%{_bindir}/icewmbg-lite
%{_bindir}/icesh-lite
%{_bindir}/icewm-session-lite
%{_bindir}/icewm
%{_bindir}/icewmhint
%{_bindir}/icewmbg
%{_bindir}/icesh
%{_bindir}/icewm-session

%changelog
