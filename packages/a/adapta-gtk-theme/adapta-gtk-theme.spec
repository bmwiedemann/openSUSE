#
# spec file for package adapta-gtk-theme
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


%define         _name               adapta
%define         _theme              Adapta
%define         gtk3_min_version    3.20.0
%define         gtk2_min_version    2.24.30
Name:           adapta-gtk-theme
Version:        3.95.0.11
Release:        0
Summary:        An adaptive Gtk+ theme based on Material Design Guidelines
License:        GPL-2.0-only AND CC-BY-SA-4.0
Group:          System/GUI/Other
URL:            https://github.com/adapta-project/adapta-gtk-theme
Source:         https://github.com/adapta-project/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gnome-shell >= 3.20.0
BuildRequires:  gnu_parallel
BuildRequires:  inkscape >= 0.91
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  sassc >= 3.3
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
BuildRequires:  pkgconfig(libxml-2.0)

%description
Adapta is a GTK+ theme based on Material Design Guidelines that was
created based on the Flat-Plat theme.

%package -n metatheme-%{_name}-common
Summary:        Adapta common theme files
Group:          System/GUI/Other
Requires:       google-roboto-fonts
Requires:       noto-sans-fonts
Suggests:       gtk2-metatheme-%{_name} = %{version}
Suggests:       gtk3-metatheme-%{_name} = %{version}
Provides:       adapta-gtk-theme
BuildArch:      noarch

%description -n metatheme-%{_name}-common
Adapta is a GTK+ theme based on Material Design Guidelines that was
created based on the Flat-Plat theme.

This package contains common files for all Adapta themes.

%package -n gtk2-metatheme-%{_name}
Summary:        Adapta GTK+2 themes
Group:          System/GUI/Other
Requires:       gtk2 >= %{gtk2_min_version}
Requires:       gtk2-engine-murrine >= 0.98.1
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gtk2)
BuildArch:      noarch

%description -n gtk2-metatheme-%{_name}
Adapta is a GTK+ theme based on Material Design Guidelines that was
created based on the Flat-Plat theme.

This package contains the GTK2+ themes.

%package -n gtk3-metatheme-%{_name}
Summary:        Adapta GTK+3 themes
Group:          System/GUI/Other
Requires:       gtk3 >= %{gtk3_min_version}
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gtk3)
BuildArch:      noarch

%description -n gtk3-metatheme-%{_name}
Adapta is a GTK+ theme based on Material Design Guidelines that was
created based on the Flat-Plat theme.

This package contains the GTK3+ themes.

%if 0%{?suse_version} > 1500
%package -n gtk4-metatheme-%{_name}
Summary:        Adapta GTK+4 themes
Group:          System/GUI/Other
Requires:       gtk4
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gtk4)
BuildArch:      noarch

%description -n gtk4-metatheme-%{_name}
Adapta is a GTK+ theme based on Material Design Guidelines that was
created based on the Flat-Plat theme.

This package contains the GTK+4 themes.
%endif

%package -n metacity-theme-%{_name}
Summary:        Adapta Metacity themes
Group:          System/GUI/Other
Requires:       metacity
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:metacity)
BuildArch:      noarch

%description -n metacity-theme-%{_name}
Adapta is a GTK+ theme based on Material Design Guidelines that was
created based on the Flat-Plat theme.

This package contains the metacity themes.

%package -n cinnamon-theme-%{_name}
Summary:        Adapta Cinnamon themes
Group:          System/GUI/Other
Requires:       cinnamon >= 3.2.0
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:cinnamon)
BuildArch:      noarch

%description -n cinnamon-theme-%{_name}
Adapta is a GTK+ theme based on Material Design Guidelines that was
created based on the Flat-Plat theme.

This package contains the cinnamon themes.

%package -n gnome-shell-theme-adapta
Summary:        Adapta GNOME Shell themes
Group:          System/GUI/Other
Requires:       gnome-shell >= 3.20.0
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gnome-shell)
BuildArch:      noarch

%description -n gnome-shell-theme-adapta
Adapta is a GTK+ theme based on Material Design Guidelines that was
created based on the Flat-Plat theme.

This package contains the GNOME Shell themes.

%package -n xfwm4-theme-%{_name}
Summary:        Adapta Xfwm4 themes
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common = %{version}
Requires:       xfwm4
Supplements:    packageand(metatheme-%{_name}-common:xfwm4)
BuildArch:      noarch

%description -n xfwm4-theme-%{_name}
Adapta is a GTK+ theme based on Material Design Guidelines that was
created based on the Flat-Plat theme.

This package contains the Xfwm4 themes.

%package -n xfce4-notifyd-theme-%{_name}
Summary:        Adapta Xfce4 notifyd themes
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common = %{version}-%{release}
Requires:       xfce4-notifyd
Supplements:    packageand(metatheme-%{_name}-common:xfce4-notifyd)
BuildArch:      noarch

%description -n xfce4-notifyd-theme-%{_name}
Adapta is a GTK+ theme based on Material Design Guidelines that was
created based on the Flat-Plat theme.

This package contains the Xfce4 notifyd themes.

%package -n plank-theme-%{_name}
Summary:        Adapta Plank themes
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common = %{version}
Requires:       plank
Supplements:    packageand(metatheme-%{_name}-common:plank)
BuildArch:      noarch

%description -n plank-theme-%{_name}
Adapta is a GTK+ theme based on Material Design Guidelines that was
created based on the Flat-Plat theme.

This package contains the Plank themes.

%package -n openbox-theme-%{_name}
Summary:        Adapta openbox themes
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common = %{version}
Requires:       openbox >= 3.6.1
Supplements:    packageand(metatheme-%{_name}-common:openbox)
BuildArch:      noarch

%description -n openbox-theme-%{_name}
Adapta is a GTK+ theme based on Material Design Guidelines that was
created based on the Flat-Plat theme.

This package contains the openbox themes.

%package -n telegram-theme-%{_name}
Summary:        Adapta Telegram themes
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common = %{version}
Requires:       telegram-desktop
Supplements:    packageand(metatheme-%{_name}-common:telegram-desktop)

%description -n telegram-theme-%{_name}
Adapta is a GTK+ theme based on Material Design Guidelines that was
created based on the Flat-Plat theme.

This package contains Telegram themes.

%package -n gedit-theme-%{_name}
Summary:        Adapta gedit themes
Group:          System/GUI/Other
Requires:       gedit
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gedit)
BuildArch:      noarch

%description -n gedit-theme-%{_name}
Adapta is a GTK+ theme based on Material Design Guidelines that was
created based on the Flat-Plat theme.

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
%endif
    --enable-parallel \
    --enable-plank \
%ifnarch i586
    --enable-telegram \
%endif
    --disable-tweetdeck
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_datadir}/themes/%{_theme}/index.theme
rm %{buildroot}%{_datadir}/themes/%{_theme}-Eta/index.theme
rm %{buildroot}%{_datadir}/themes/%{_theme}-Nokto/index.theme
rm %{buildroot}%{_datadir}/themes/%{_theme}-Nokto-Eta/index.theme

# Remove files that will be pack in doc directory.
rm %{buildroot}%{_datadir}/themes/%{_theme}/COPYING
rm %{buildroot}%{_datadir}/themes/%{_theme}/LICENSE_CC_BY_SA4
rm %{buildroot}%{_datadir}/themes/%{_theme}/README.md

# Remove duplicated files.
%fdupes %{buildroot}%{_datadir}/themes/

%files -n metatheme-%{_name}-common
%license COPYING LICENSE_CC_BY_SA4
%doc README.md
%dir %{_datadir}/themes/%{_theme}/
%dir %{_datadir}/themes/%{_theme}-Eta/
%dir %{_datadir}/themes/%{_theme}-Nokto/
%dir %{_datadir}/themes/%{_theme}-Nokto-Eta/

%files -n gtk2-metatheme-%{_name}
%{_datadir}/themes/%{_theme}/gtk-2.0/
%{_datadir}/themes/%{_theme}-Eta/gtk-2.0/
%{_datadir}/themes/%{_theme}-Nokto/gtk-2.0/
%{_datadir}/themes/%{_theme}-Nokto-Eta/gtk-2.0/

%files -n gtk3-metatheme-%{_name}
%{_datadir}/themes/%{_theme}/gtk-3.*/
%{_datadir}/themes/%{_theme}-Eta/gtk-3.*
%{_datadir}/themes/%{_theme}-Nokto/gtk-3.*
%{_datadir}/themes/%{_theme}-Nokto-Eta/gtk-3.*

%if 0%{?suse_version} > 1500
%files -n gtk4-metatheme-%{_name}
%{_datadir}/themes/%{_theme}/gtk-4.*/
%{_datadir}/themes/%{_theme}-Eta/gtk-4.*
%{_datadir}/themes/%{_theme}-Nokto/gtk-4.*
%{_datadir}/themes/%{_theme}-Nokto-Eta/gtk-4.*
%endif

%files -n gnome-shell-theme-%{_name}
%{_datadir}/themes/%{_theme}/gnome-shell/
%{_datadir}/themes/%{_theme}-Nokto/gnome-shell/
%{_datadir}/themes/%{_theme}-Eta/gnome-shell/
%{_datadir}/themes/%{_theme}-Nokto-Eta/gnome-shell/

%files -n metacity-theme-%{_name}
%{_datadir}/themes/%{_theme}/metacity-1/
%{_datadir}/themes/%{_theme}-Eta/metacity-1
%{_datadir}/themes/%{_theme}-Nokto/metacity-1
%{_datadir}/themes/%{_theme}-Nokto-Eta/metacity-1

%files -n cinnamon-theme-%{_name}
%{_datadir}/themes/%{_theme}/cinnamon/
%{_datadir}/themes/%{_theme}-Nokto/cinnamon/

%files -n xfwm4-theme-%{_name}
%{_datadir}/themes/%{_theme}/xfwm4/
%{_datadir}/themes/%{_theme}-Nokto/xfwm4

%files -n xfce4-notifyd-theme-%{_name}
%{_datadir}/themes/%{_theme}/xfce-notify-4.0/

%files -n plank-theme-%{_name}
%{_datadir}/themes/%{_theme}/plank/
%{_datadir}/themes/%{_theme}-Eta/plank
%{_datadir}/themes/%{_theme}-Nokto/plank
%{_datadir}/themes/%{_theme}-Nokto-Eta/plank

%files -n openbox-theme-%{_name}
%{_datadir}/themes/%{_theme}/openbox-3/
%{_datadir}/themes/%{_theme}-Nokto/openbox-3/

%ifnarch i586
%files -n telegram-theme-%{_name}
%{_datadir}/themes/%{_theme}/telegram/
%{_datadir}/themes/%{_theme}-Eta/telegram
%{_datadir}/themes/%{_theme}-Nokto/telegram/
%{_datadir}/themes/%{_theme}-Nokto-Eta/telegram
%endif

%files -n gedit-theme-%{_name}
%{_datadir}/themes/%{_theme}/gedit/
%{_datadir}/themes/%{_theme}-Nokto/gedit

%changelog
