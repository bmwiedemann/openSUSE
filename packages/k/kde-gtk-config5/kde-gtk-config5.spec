#
# spec file for package kde-gtk-config5
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


%bcond_without lang
Name:           kde-gtk-config5
Version:        5.17.2
Release:        0
Summary:        KCM Module to Configure GTK2 and GTK3 Applications Appearance Under KDE
License:        LGPL-3.0-or-later AND GPL-3.0-or-later
Group:          System/GUI/KDE
Url:            http://projects.kde.org/kde-gtk-config
Source:         https://download.kde.org/stable/plasma/%{version}/kde-gtk-config-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/kde-gtk-config-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        gtkrc-2.0-kde4.template
Source4:        gtk3-settings.ini-kde4.template
BuildRequires:  extra-cmake-modules >= 0.0.9
BuildRequires:  kf5-filesystem
BuildRequires:  xz
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(Qt5Svg) >= 5.4.0
BuildRequires:  cmake(Qt5Test) >= 5.4.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(x11)
Recommends:     %{name}-lang
Suggests:       gtk2-metatheme-breeze
Suggests:       gtk3-metatheme-breeze
Supplements:    packageand(plasma5-workspace:libgtk-2_0-0)
Supplements:    packageand(plasma5-workspace:libgtk-3-0)
Provides:       kde-gtk-config = %{version}
Obsoletes:      kde-gtk-config < %{version}

%description
kde-gtk-config is a KCM module to configure GTK2 and GTK3 applications
appearance under KDE.

Among its many features, it lets you:
 - Choose which theme is used for GTK2 and GTK3 applications.
 - Tweak some GTK applications behaviour.
 - Select what icon theme to use in GTK applications.
 - Select GTK applications default fonts.
 - Easily browse and install new GTK2 and GTK3 themes.

%package gtk2
Summary:        GTK2 Preview Helper for the GTK Configuration KCM
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:libgtk-2_0-0)

%description gtk2
This package contains a helper application that allows previewing
the GTK2 application style from within the GTK configuration KCM

%package gtk3
Summary:        GTK3 Preview Helper for the GTK Configuration KCM
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:libgtk-3-0)

%description gtk3
This package contains a helper application that allows previewing
the GTK3 application style from within the GTK configuration KCM

%lang_package

%prep
%setup -q -n kde-gtk-config-%{version}
%autopatch -p1

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %make_jobs

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %kf5_find_lang
%endif

install -Dpm 0644 %{SOURCE3} %{buildroot}%{_kf5_sharedir}/%{name}/gtkrc-2.0-kde4.template
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_kf5_sharedir}/%{name}/gtk3-settings.ini-kde4.template

%files
%license COPYING*
%{_kf5_sharedir}/%{name}/
%{_kf5_knsrcfilesdir}/cgctheme.knsrc
%{_kf5_knsrcfilesdir}/cgcgtk3.knsrc
%{_kf5_servicesdir}/
%{_kf5_plugindir}/
%{_kf5_sharedir}/kcm-gtk-module/
%dir %{_kf5_sharedir}/icons/hicolor/8x8
%dir %{_kf5_sharedir}/icons/hicolor/8x8/apps
%{_kf5_sharedir}/icons/hicolor/*/*/*.*

%files gtk2
%license COPYING*
%{_kf5_libdir}/libexec/gtk_preview
%{_kf5_libdir}/libexec/reload_gtk_apps

%files gtk3
%license COPYING*
%{_kf5_libdir}/libexec/gtk3_preview

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
