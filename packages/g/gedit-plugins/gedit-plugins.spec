#
# spec file for package gedit-plugins
#
# Copyright (c) 2024 SUSE LLC
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
Version:        48.1
Release:        0
Summary:        A collection of plugins for gedit
License:        GPL-2.0-or-later
Group:          Productivity/Text/Editors
URL:            https://wiki.gnome.org/Apps/Gedit/PluginsLists
Source0:        %{name}-%{version}.tar.zst
Source1:        gedit-plugins.SUSE
# PATCH-FIX-UPSTREAM bracketcompletion-use-key-release-event-to-work-wi.patch boo#1027448 bgo#778737 hillwood@opensuse.org -- Switch to use key release event for ibus pinyin input method
Patch0:         bracketcompletion-use-key-release-event-to-work-wi.patch

BuildRequires:  fdupes
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  python3-base
# configure tests for python gi-bindings of gucharmap
BuildRequires:  typelib-1_0-Gucharmap-2_90
BuildRequires:  vala >= 0.28.0
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(dbus-python) >= 0.82
BuildRequires:  pkgconfig(gedit) >= 48.1
BuildRequires:  pkgconfig(gio-2.0) >= 2.32.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.0
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(libgit2-glib-1.0) >= 0.0.6
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.7.0
BuildRequires:  pkgconfig(libpeas-gtk-1.0) >= 1.7.0
BuildRequires:  pkgconfig(vte-2.91)
Requires:       gedit >= 48.1
Recommends:     %{name}-data
Suggests:       gedit-plugin-bookmarks
Suggests:       gedit-plugin-bracketcompletion
Suggests:       gedit-plugin-charmap
Suggests:       gedit-plugin-codecomment
Suggests:       gedit-plugin-colorpicker
Suggests:       gedit-plugin-drawspaces
Suggests:       gedit-plugin-joinlines
Suggests:       gedit-plugin-multiedit
Suggests:       gedit-plugin-smartspaces
Suggests:       gedit-plugin-session-saver
Suggests:       gedit-plugin-terminal
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

 * Bracket Completion: Automatically adds a closing bracket when you
   insert an opening one
 * Charmap: Select characters from a charactermap
 * Code Comment: Comment or uncomment blocks of code
 * Color picker: Select and insert a color from a dialog (for html,
   css, php)
 * Join lines/Split lines: Join or split multiple lines through Ctrl+J
   and Ctrl+Shift+J
 * Session Saver: Allows to bookmark working sessions in order to get
   them back for further use
 * Smart Spaces: Allows to unindent like if you were using tabs while
   you're using spaces
 * Show tabbar: A plugin to show or hide the gedit tabbar
 * Terminal: A terminal widget accessible from the bottom panel

%package -n %{name}-data
Summary:        Common data required by gedit plugins
Group:          Productivity/Text/Editors
Requires:       gedit

%description -n %{name}-data
Common files required by all gedit plugins

%package -n gedit-plugin-bookmarks
Summary:        Gedit bookmarks plugin
Group:          Productivity/Text/Editors
Requires:       %{name}-data = %{version}
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/bookmarks.plugin

%description -n gedit-plugin-bookmarks
The gedit bookmarks plugin.

%package -n gedit-plugin-bracketcompletion
Summary:        Gedit bracketcompletion plugin
Group:          Productivity/Text/Editors
Requires:       %{name}-data = %{version}
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/bracketcompletion.plugin

%description -n gedit-plugin-bracketcompletion
The gedit bracketcompletion plugin.

%package -n gedit-plugin-charmap
Summary:        Gedit charmap plugin
Group:          Productivity/Text/Editors
Requires:       %{name}-data = %{version}
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/charmap.plugin

%description -n gedit-plugin-charmap
The gedit charmap plugin.

%package -n gedit-plugin-codecomment
Summary:        Gedit codecomment plugin
Group:          Productivity/Text/Editors
Requires:       %{name}-data = %{version}
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/codecomment.plugin

%description -n gedit-plugin-codecomment
The gedit codecomment plugin.

%package -n gedit-plugin-colorpicker
Summary:        Gedit colorpicker plugin
Group:          Productivity/Text/Editors
Requires:       %{name}-data = %{version}
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/colorpicker.plugin

%description -n gedit-plugin-colorpicker
The gedit colorpicker plugin.

%package -n gedit-plugin-drawspaces
Summary:        Gedit drawspaces plugin
Group:          Productivity/Text/Editors
Requires:       %{name}-data = %{version}
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/drawspaces.plugin

%description -n gedit-plugin-drawspaces
The gedit drawspaces plugin.

%package -n gedit-plugin-joinlines
Summary:        Gedit joinlines plugin
Group:          Productivity/Text/Editors
Requires:       %{name}-data = %{version}
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/joinlines.plugin

%description -n gedit-plugin-joinlines
The gedit joinlines plugin

%package -n gedit-plugin-multiedit
Summary:        Gedit multiedit plugin
Group:          Productivity/Text/Editors
Requires:       %{name}-data = %{version}
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/multiedit.plugin

%description -n gedit-plugin-multiedit
The gedit multiedit plugin

%package -n gedit-plugin-smartspaces
Summary:        Gedit smartspaces plugin
Group:          Productivity/Text/Editors
Requires:       %{name}-data = %{version}
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/smartspaces.plugin

%description -n gedit-plugin-smartspaces
The gedit smartspaces plugin

%package -n gedit-plugin-session-saver
Summary:        Gedit session-saver plugin
Group:          Productivity/Text/Editors
Requires:       %{name}-data = %{version}
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/session-saver.plugin

%description -n gedit-plugin-session-saver
The gedit session-saver plugin

%package -n gedit-plugin-terminal
Summary:        Gedit terminal plugin
Group:          Productivity/Text/Editors
Requires:       %{name}-data = %{version}
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/terminal.plugin

%description -n gedit-plugin-terminal
The gedit terminal plugin

%package -n gedit-plugin-wordcompletion
Summary:        Gedit wordcompletion plugin
Group:          Productivity/Text/Editors
Requires:       %{name}-data = %{version}
Provides:       gedit-plugins:%{_libdir}/gedit/plugins/wordcompletion.plugin

%description -n gedit-plugin-wordcompletion
The gedit wordcompletion plugin

%lang_package

%prep
%autosetup -p1
install -m644 %{SOURCE1} .

%build
%meson
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

%files -n %{name}-data
# Common files
%{_libdir}/gedit/plugins/gpdefs.py*

%files -n gedit-plugin-bookmarks
## Explicitly list all plugins so we know when we miss one
# bookmarks
%{_datadir}/metainfo/gedit-bookmarks.metainfo.xml
%{_libdir}/gedit/plugins/bookmarks.plugin
%{_libdir}/gedit/plugins/libbookmarks.so

%files -n gedit-plugin-bracketcompletion
# bracketcompletion
%{_datadir}/metainfo/gedit-bracketcompletion.metainfo.xml
%{_libdir}/gedit/plugins/bracketcompletion.plugin
%{_libdir}/gedit/plugins/bracketcompletion.py*

%files -n gedit-plugin-charmap
# charmap
%{_datadir}/metainfo/gedit-charmap.metainfo.xml
%{_libdir}/gedit/plugins/charmap.plugin
%{_libdir}/gedit/plugins/charmap/

%files -n gedit-plugin-codecomment
# codecomment
%{_datadir}/metainfo/gedit-codecomment.metainfo.xml
%{_libdir}/gedit/plugins/codecomment.plugin
%{_libdir}/gedit/plugins/codecomment.py*

%files -n gedit-plugin-colorpicker
# colorpicker
%{_datadir}/metainfo/gedit-colorpicker.metainfo.xml
%{_libdir}/gedit/plugins/colorpicker.plugin
%{_libdir}/gedit/plugins/colorpicker.py*

%files -n gedit-plugin-drawspaces
# drawspaces
%{_datadir}/metainfo/gedit-drawspaces.metainfo.xml
%{_libdir}/gedit/plugins/drawspaces.plugin
%{_libdir}/gedit/plugins/libdrawspaces.so
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.drawspaces.gschema.xml

%files -n gedit-plugin-joinlines
# joinlines
%{_datadir}/metainfo/gedit-joinlines.metainfo.xml
%{_libdir}/gedit/plugins/joinlines.plugin
%{_libdir}/gedit/plugins/joinlines.py*

%files -n gedit-plugin-multiedit
# multiedit
%{_datadir}/metainfo/gedit-multiedit.metainfo.xml
%{_libdir}/gedit/plugins/multiedit.plugin
%{_libdir}/gedit/plugins/multiedit/

%files -n gedit-plugin-smartspaces
# smartspaces
%{_datadir}/metainfo/gedit-smartspaces.metainfo.xml
%{_libdir}/gedit/plugins/smartspaces.plugin
%{_libdir}/gedit/plugins/libsmartspaces.so

%files -n gedit-plugin-session-saver
# session-saver
%{_datadir}/gedit/plugins/sessionsaver/
%{_libdir}/gedit/plugins/sessionsaver.plugin
%{_libdir}/gedit/plugins/sessionsaver/

%files -n gedit-plugin-terminal
# terminal
%{_datadir}/metainfo/gedit-terminal.metainfo.xml
%{_libdir}/gedit/plugins/terminal.plugin
%{_libdir}/gedit/plugins/terminal.py*
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.terminal.gschema.xml

%files -n gedit-plugin-wordcompletion
# wordcompletion
%{_datadir}/metainfo/gedit-wordcompletion.metainfo.xml
%{_libdir}/gedit/plugins/wordcompletion.plugin
%{_libdir}/gedit/plugins/libwordcompletion.so
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.wordcompletion.gschema.xml

%files lang -f %{name}.lang

%changelog
