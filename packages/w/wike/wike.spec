#
# spec file for package wike
#
# Copyright (c) 2023 SUSE LLC
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


Name:           wike
Version:        1.8.3
Release:        0
Summary:        A Wikipedia reader for the GNOME Desktop
License:        GPL-3.0-or-later
URL:            https://github.com/hugolabe/Wike
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# appstream-glib disabled due to upstream expecting internet connectivity during test.
#BuildRequires:  appstream-glib
BuildRequires:  dbus-1
BuildRequires:  desktop-file-utils
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
Requires:       python3-gobject-Gdk
BuildArch:      noarch

%description
Wike is a Wikipedia reader for the GNOME Desktop. Provides access to all the
content of this online encyclopedia in a native application, with a simpler and
distraction-free view of articles.

%package -n gnome-shell-search-provider-wike
Summary:        Wikipedia reader for GNOME -- Search Provider for GNOME Shell
Requires:       %{name} = %{version}
Requires:       gnome-shell
Supplements:    (%{name} and gnome-shell)

%description -n gnome-shell-search-provider-wike
This package contains a search provider to enable GNOME Shell to return search
results from wike.

%lang_package

%prep
%autosetup -n Wike-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/wike
%{_datadir}/wike/
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg

%files -n gnome-shell-search-provider-wike
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/*.ini
%{_datadir}/dbus-1/services/*.service

%files lang -f %{name}.lang

%changelog
