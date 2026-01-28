#
# spec file for package gedit-plugins
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2009 Dominique Leuenberger, Almere, The Netherlands.
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


Name:           gedit-plugins
Version:        49.0
Release:        0
Summary:        A collection of plugins for gedit
License:        GPL-2.0-or-later
Group:          Productivity/Text/Editors
URL:            https://wiki.gnome.org/Apps/Gedit/PluginsLists
Source0:        %{name}-%{version}.tar.zst
Source1:        gedit-plugins.SUSE

BuildRequires:  fdupes
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
# configure tests for python gi-bindings of gucharmap
BuildRequires:  typelib-1_0-Gucharmap-2_90
BuildRequires:  vala >= 0.28.0
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(dbus-python) >= 0.82
BuildRequires:  pkgconfig(gedit) >= 49
BuildRequires:  pkgconfig(gio-2.0) >= 2.32.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.0
BuildRequires:  pkgconfig(libgit2-glib-1.0) >= 0.0.6
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.7.0
BuildRequires:  pkgconfig(libpeas-gtk-1.0) >= 1.7.0
BuildRequires:  pkgconfig(vte-2.91)
Requires:       gedit >= 48.1
Recommends:     %{name}-data
Suggests:       gedit-plugin-bookmarks
Suggests:       gedit-plugin-drawspaces
Suggests:       gedit-plugin-smartspaces
Suggests:       gedit-plugin-wordcompletion
Enhances:       gedit
Obsoletes:      gedit-plugin-dashboard <= %{version}
# Zeitgeist plugin was removed with version 3.35.90
Obsoletes:      gedit-plugin-zeitgeist < 3.35.90
# gedit-plugin-colorschemer was removed with version 45.alpha
Obsoletes:      gedit-plugin-colorschemer < 45.alpha
# Synctex plugin was removed with version 45.0
Obsoletes:      gedit-plugin-synctex < 45.0

%description
This package contains a number of plugins for gedit, such as:

 * Smart Spaces: Allows to unindent like if you were using tabs while
   you're using spaces

%package -n gedit-plugin-bookmarks
Summary:        Gedit bookmarks plugin
Group:          Productivity/Text/Editors
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/bookmarks.plugin

%description -n gedit-plugin-bookmarks
The gedit bookmarks plugin.

%package -n gedit-plugin-drawspaces
Summary:        Gedit drawspaces plugin
Group:          Productivity/Text/Editors
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/drawspaces.plugin

%description -n gedit-plugin-drawspaces
The gedit drawspaces plugin.

%package -n gedit-plugin-smartspaces
Summary:        Gedit smartspaces plugin
Group:          Productivity/Text/Editors
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/smartspaces.plugin

%description -n gedit-plugin-smartspaces
The gedit smartspaces plugin

%package -n gedit-plugin-wordcompletion
Summary:        Gedit wordcompletion plugin
Group:          Productivity/Text/Editors
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/wordcompletion.plugin

%description -n gedit-plugin-wordcompletion
The gedit wordcompletion plugin

%lang_package

%prep
%autosetup -p1
install -m644 %{SOURCE1} .

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}
%find_lang gedit %{name}.lang %{?no_lang_C}
%fdupes %{buildroot}%{_prefix}

%files
%doc gedit-plugins.SUSE
%doc %{_datadir}/help/C/gedit

%files -n gedit-plugin-bookmarks
## Explicitly list all plugins so we know when we miss one
# bookmarks
%{_datadir}/metainfo/gedit-bookmarks.metainfo.xml
%{_libdir}/gedit/plugins/bookmarks.plugin
%{_libdir}/gedit/plugins/libbookmarks.so

%files -n gedit-plugin-drawspaces
# drawspaces
%{_datadir}/metainfo/gedit-drawspaces.metainfo.xml
%{_libdir}/gedit/plugins/drawspaces.plugin
%{_libdir}/gedit/plugins/libdrawspaces.so
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.drawspaces.gschema.xml

%files -n gedit-plugin-smartspaces
# smartspaces
%{_datadir}/metainfo/gedit-smartspaces.metainfo.xml
%{_libdir}/gedit/plugins/smartspaces.plugin
%{_libdir}/gedit/plugins/libsmartspaces.so

%files -n gedit-plugin-wordcompletion
# wordcompletion
%{_datadir}/metainfo/gedit-wordcompletion.metainfo.xml
%{_libdir}/gedit/plugins/wordcompletion.plugin
%{_libdir}/gedit/plugins/libwordcompletion.so
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.wordcompletion.gschema.xml

%files lang -f %{name}.lang

%changelog
