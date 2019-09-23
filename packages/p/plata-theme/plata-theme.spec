#
# spec file for package plata-theme
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


%define         _name               plata
%define         asc_link_uid        707967e2abe63d5f3366d79a428a8be3
%define         _theme              Plata
%define         gtk3_min_version    3.20.0
%define         gtk2_min_version    2.24.30
Name:           plata-theme
Version:        0.8.9
Release:        0
Summary:        A Gtk+ theme based on Material Design Refresh
License:        GPL-2.0-only AND CC-BY-SA-4.0
Group:          System/GUI/Other
URL:            https://gitlab.com/tista500/plata-theme
Source0:        https://gitlab.com/tista500/plata-theme/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://gitlab.com/tista500/plata-theme/uploads/%{asc_link_uid}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gnome-shell >= 3.20.0
BuildRequires:  gnu_parallel
BuildRequires:  inkscape >= 0.91
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  sassc >= 3.3
BuildRequires:  zip
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.32.2
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0) >= 2.32.2
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.48.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(libmarco-private)
%endif
BuildRequires:  pkgconfig(libxml-2.0)
BuildArch:      noarch

%description
Plata is a GTK+ theme based on Material Design Refresh.

%package -n metatheme-%{_name}-common
Summary:        Plata common theme files
Group:          System/GUI/Other
Requires:       google-roboto-fonts
Requires:       noto-sans-fonts
Suggests:       gtk2-metatheme-%{_name} = %{version}
Suggests:       gtk3-metatheme-%{_name} = %{version}
Provides:       plata-theme

%description -n metatheme-%{_name}-common
Plata is a GTK+ theme based on Material Design Refresh.

This package contains common files for all Plata themes.

%package -n gtk2-metatheme-%{_name}
Summary:        Plata GTK+2 themes
Group:          System/GUI/Other
Requires:       gtk2 >= %{gtk2_min_version}
Requires:       gtk2-engine-murrine >= 0.98.1
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and gtk2)

%description -n gtk2-metatheme-%{_name}
Plata is a GTK+ theme based on Material Design Refresh.

This package contains the GTK2+ themes.

%package -n gtk3-metatheme-%{_name}
Summary:        Plata GTK+3 themes
Group:          System/GUI/Other
Requires:       gtk3 >= %{gtk3_min_version}
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and gtk3)

%description -n gtk3-metatheme-%{_name}
Plata is a GTK+ theme based on Material Design Refresh.

This package contains the GTK3+ themes.

%if 0%{?suse_version} > 1500
%package -n gtk4-metatheme-%{_name}
Summary:        Plata GTK+4 themes
Group:          System/GUI/Other
Requires:       gtk4
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and gtk4)

%description -n gtk4-metatheme-%{_name}
Plata is a GTK+ theme based on Material Design Refresh.

This package contains the GTK+4 themes.
%endif

%package -n metacity-theme-%{_name}
Summary:        Plata Metacity themes
Group:          System/GUI/Other
Requires:       metacity
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and metacity)

%description -n metacity-theme-%{_name}
Plata is a GTK+ theme based on Material Design Refresh.

This package contains the metacity themes.

%package -n cinnamon-theme-%{_name}
Summary:        Plata Cinnamon themes
Group:          System/GUI/Other
Requires:       cinnamon >= 3.2.0
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and cinnamon)

%description -n cinnamon-theme-%{_name}
Plata is a GTK+ theme based on Material Design Refresh.

This package contains the cinnamon themes.

%package -n gnome-shell-theme-plata
Summary:        Plata GNOME Shell themes
Group:          System/GUI/Other
Requires:       gnome-shell >= 3.20.0
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and gnome-shell)

%description -n gnome-shell-theme-plata
Plata is a GTK+ theme based on Material Design Refresh.

This package contains the GNOME Shell themes.

%package -n xfwm4-theme-%{_name}
Summary:        Plata Xfwm4 themes
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common = %{version}
Requires:       xfwm4
Supplements:    (metatheme-%{_name}-common and xfwm4)

%description -n xfwm4-theme-%{_name}
Plata is a GTK+ theme based on Material Design Refresh.

This package contains the Xfwm4 themes.

%package -n xfce4-notifyd-theme-%{_name}
Summary:        Plata Xfce4 notifyd themes
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common = %{version}-%{release}
Requires:       xfce4-notifyd
Supplements:    (metatheme-%{_name}-common and xfce4-notifyd)

%description -n xfce4-notifyd-theme-%{_name}
Plata is a GTK+ theme based on Material Design Refresh.

This package contains the Xfce4 notifyd themes.

%package -n plank-theme-%{_name}
Summary:        Plata Plank themes
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common = %{version}
Requires:       plank
Supplements:    (metatheme-%{_name}-common and plank)

%description -n plank-theme-%{_name}
Plata is a GTK+ theme based on Material Design Refresh.

This package contains the Plank themes.

%package -n openbox-theme-%{_name}
Summary:        Plata openbox themes
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common = %{version}
Requires:       openbox >= 3.6.1
Supplements:    (metatheme-%{_name}-common and openbox)

%description -n openbox-theme-%{_name}
Plata is a GTK+ theme based on Material Design Refresh.

This package contains the openbox themes.

%package -n telegram-theme-%{_name}
Summary:        Plata Telegram themes
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common = %{version}
Requires:       telegram-desktop
Supplements:    (metatheme-%{_name}-common and telegram-desktop)

%description -n telegram-theme-%{_name}
Plata is a GTK+ theme based on Material Design Refresh.

This package contains Telegram themes.

%package -n gedit-theme-%{_name}
Summary:        Plata gedit themes
Group:          System/GUI/Other
Requires:       gedit
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (metatheme-%{_name}-common and gedit)

%description -n gedit-theme-%{_name}
Plata is a GTK+ theme based on Material Design Refresh.

This package contains gedit themes.

%prep
%autosetup

%build
NOCONFIGURE=yes ./autogen.sh --prefix=%{_prefix}
%configure \
    --disable-chrome-legacy \
%if 0%{?suse_version} > 1500
    --enable-gtk_next \
%else
    --disable-gtk_next \
    --disable-mate \
%endif
    --enable-parallel \
    --enable-plank \
    --enable-telegram \
    --disable-tweetdeck
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_datadir}/themes/%{_theme}/index.theme
rm %{buildroot}%{_datadir}/themes/%{_theme}-Lumine/index.theme
rm %{buildroot}%{_datadir}/themes/%{_theme}-Noir/index.theme
rm %{buildroot}%{_datadir}/themes/%{_theme}-Compact/index.theme
rm %{buildroot}%{_datadir}/themes/%{_theme}-Lumine-Compact/index.theme
rm %{buildroot}%{_datadir}/themes/%{_theme}-Noir-Compact/index.theme

# Remove files that will be pack in doc directory.
rm %{buildroot}%{_datadir}/themes/%{_theme}/COPYING
rm %{buildroot}%{_datadir}/themes/%{_theme}/LICENSE_CC_BY_SA4

# Remove duplicated files.
%fdupes %{buildroot}%{_datadir}/themes/

%files -n metatheme-%{_name}-common
%license COPYING LICENSE_CC_BY_SA4
%doc README.md
%dir %{_datadir}/themes/%{_theme}/
%dir %{_datadir}/themes/%{_theme}-Lumine/
%dir %{_datadir}/themes/%{_theme}-Noir/
%dir %{_datadir}/themes/%{_theme}-Compact/
%dir %{_datadir}/themes/%{_theme}-Lumine-Compact/
%dir %{_datadir}/themes/%{_theme}-Noir-Compact/

%files -n gtk2-metatheme-%{_name}
%{_datadir}/themes/%{_theme}/gtk-2.0/
%{_datadir}/themes/%{_theme}-Lumine/gtk-2.0/
%{_datadir}/themes/%{_theme}-Noir/gtk-2.0/
%{_datadir}/themes/%{_theme}-Compact/gtk-2.0/
%{_datadir}/themes/%{_theme}-Lumine-Compact/gtk-2.0/
%{_datadir}/themes/%{_theme}-Noir-Compact/gtk-2.0/

%files -n gtk3-metatheme-%{_name}
%{_datadir}/themes/%{_theme}/gtk-3.*/
%{_datadir}/themes/%{_theme}-Lumine/gtk-3.*
%{_datadir}/themes/%{_theme}-Noir/gtk-3.*
%{_datadir}/themes/%{_theme}-Compact/gtk-3.*
%{_datadir}/themes/%{_theme}-Lumine-Compact/gtk-3.*
%{_datadir}/themes/%{_theme}-Noir-Compact/gtk-3.*

%if 0%{?suse_version} > 1500
%files -n gtk4-metatheme-%{_name}
%{_datadir}/themes/%{_theme}/gtk-4.*/
%{_datadir}/themes/%{_theme}-Lumine/gtk-4.*
%{_datadir}/themes/%{_theme}-Noir/gtk-4.*
%{_datadir}/themes/%{_theme}-Compact/gtk-4.*
%{_datadir}/themes/%{_theme}-Lumine-Compact/gtk-4.*
%{_datadir}/themes/%{_theme}-Noir-Compact/gtk-4.*
%endif

%files -n gnome-shell-theme-%{_name}
%{_datadir}/themes/%{_theme}/gnome-shell/
%{_datadir}/themes/%{_theme}-Lumine/gnome-shell/
%{_datadir}/themes/%{_theme}-Noir/gnome-shell/
%{_datadir}/themes/%{_theme}-Compact/gnome-shell/
%{_datadir}/themes/%{_theme}-Lumine-Compact/gnome-shell/
%{_datadir}/themes/%{_theme}-Noir-Compact/gnome-shell/

%files -n metacity-theme-%{_name}
%{_datadir}/themes/%{_theme}/metacity-1/
%{_datadir}/themes/%{_theme}-Lumine/metacity-1/
%{_datadir}/themes/%{_theme}-Noir/metacity-1/
%{_datadir}/themes/%{_theme}-Compact/metacity-1/
%{_datadir}/themes/%{_theme}-Lumine-Compact/metacity-1/
%{_datadir}/themes/%{_theme}-Noir-Compact/metacity-1/

%files -n cinnamon-theme-%{_name}
%{_datadir}/themes/%{_theme}/cinnamon/
%{_datadir}/themes/%{_theme}-Lumine/cinnamon/
%{_datadir}/themes/%{_theme}-Noir/cinnamon/

%files -n xfwm4-theme-%{_name}
%{_datadir}/themes/%{_theme}/xfwm4/
%{_datadir}/themes/%{_theme}-Lumine/xfwm4/
%{_datadir}/themes/%{_theme}-Noir/xfwm4/
%{_datadir}/themes/%{_theme}-Compact/xfwm4/
%{_datadir}/themes/%{_theme}-Lumine-Compact/xfwm4/
%{_datadir}/themes/%{_theme}-Noir-Compact/xfwm4/

%files -n xfce4-notifyd-theme-%{_name}
%{_datadir}/themes/%{_theme}/xfce-notify-4.0/
%{_datadir}/themes/%{_theme}-Lumine/xfce-notify-4.0/
%{_datadir}/themes/%{_theme}-Noir/xfce-notify-4.0/

%files -n plank-theme-%{_name}
%{_datadir}/themes/%{_theme}/plank/
%{_datadir}/themes/%{_theme}-Lumine/plank/
%{_datadir}/themes/%{_theme}-Noir/plank/
%{_datadir}/themes/%{_theme}-Compact/plank/
%{_datadir}/themes/%{_theme}-Lumine-Compact/plank/
%{_datadir}/themes/%{_theme}-Noir-Compact/plank/

%files -n openbox-theme-%{_name}
%{_datadir}/themes/%{_theme}/openbox-3/
%{_datadir}/themes/%{_theme}-Lumine/openbox-3/
%{_datadir}/themes/%{_theme}-Noir/openbox-3/

%files -n telegram-theme-%{_name}
%{_datadir}/themes/%{_theme}/telegram/
%{_datadir}/themes/%{_theme}-Lumine/telegram/
%{_datadir}/themes/%{_theme}-Noir/telegram/

%files -n gedit-theme-%{_name}
%{_datadir}/themes/%{_theme}/gtksourceview/
%{_datadir}/themes/%{_theme}-Lumine/gtksourceview/
%{_datadir}/themes/%{_theme}-Noir/gtksourceview/

%changelog
