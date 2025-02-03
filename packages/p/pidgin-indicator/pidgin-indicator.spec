#
# spec file for package pidgin-indicator
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


%define         _name indicator
Name:           pidgin-indicator
Version:        1.0.2
Release:        0
Summary:        StatusNotifierItem tray icon plugin for Pidgin
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/philipl/pidgin-indicator
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(pidgin)

%description
This plugin provides a StatusNotifierItem tray icon, for use in
KDE Plasma 5, Unity, Elementary and other environments.

It provides all the same functionality as the original tray icon
but not in exactly the same way:
 * The 'smart' click behaviour that either shows the buddy list or
   unread messages is now activated by a middle-click – because
   left click on an libappindicator always opens the menu.
 * As the SNI-icon is a separate process from pidgin itself, there
   are sometimes conflicts with Focus Stealing Prevention when you
   use the indicator to go to unread messages. You may need to
   disable FSP for Pidgin to get around this.
 * Due to how libappindicator work, the middle-click action must
   also be a menu item, so it's the new Show/Hide item at the top
   of the menu.
 * Due to libappindicator limitations, some of the special icons
   can't be shown next to menu items any more.

%package -n pidgin-plugin-%{_name}
Summary:        StatusNotifierItem tray icon plugin for Pidgin
Group:          Productivity/Networking/Instant Messenger
%requires_ge    pidgin
Recommends:     pidgin-plugin-%{_name}-lang
# pidgin-indicator was last used in openSUSE Leap 42.2.
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}
Obsoletes:      %{name}-lang < %{version}-%{release}

%description -n pidgin-plugin-%{_name}
This plugin provides a StatusNotifierItem tray icon, for use in
MATE, KDE Plasma 5, Elementary Pantheon and other environments.

It provides all the same functionality as the original tray icon
but not in exactly the same way:
 * The "smart" click behaviour that either shows the buddy list or
   unread messages is now activated by a middle-click – because
   left click on an libappindicator always opens the menu.
 * As the SNI-icon is a separate process from pidgin itself, there
   are sometimes conflicts with Focus Stealing Prevention when you
   use the indicator to go to unread messages. You may need to
   disable FSP for Pidgin to get around this.
 * Due to how libayatana-appindicator work, the middle-click action
   must also be a menu item, so it's the new Show/Hide item at the
   top of the menu.
 * Due to libayatana-appindicator limitations, some of the special
   icons can't be shown next to menu items any more.

%lang_package -n pidgin-plugin-indicator

%prep
%autosetup

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%files -n pidgin-plugin-%{_name}
%license COPYING
%doc AUTHORS
%{_libdir}/pidgin/%{_name}.so
%{_datadir}/icons/hicolor/*/status/%{name}-nothing.png

%files -n pidgin-plugin-%{_name}-lang -f %{name}.lang

%changelog
