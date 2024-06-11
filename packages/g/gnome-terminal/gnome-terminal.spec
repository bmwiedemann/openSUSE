#
# spec file for package gnome-terminal
#
# Copyright (c) 2024 SUSE LLC
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


%bcond_without  nautilus_extension
Name:           gnome-terminal
Version:        3.52.2
Release:        0
Summary:        GNOME Terminal
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          System/X11/Terminals
URL:            https://wiki.gnome.org/Apps/Terminal
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gcc-c++
# Needed for search provider. It should not be needed in my opinion,
# we have to take this up with upstream, or just provide search
# provider interface definition file as source.
BuildRequires:  gnome-shell
BuildRequires:  meson >= 0.62.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(dconf) >= 0.14.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.52.0
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.76.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 0.1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.7
BuildRequires:  pkgconfig(libhandy-1)
%if %{with nautilus_extension}
BuildRequires:  pkgconfig(libnautilus-extension-4)
%endif
BuildRequires:  pkgconfig(libpcre2-8) >= 10.00
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vte-2.91) >= 0.76.0
BuildRequires:  pkgconfig(x11)
Requires(pre):  filesystem

%description
This package provides the GNOME terminal emulator application.

GNOME Terminal uses an architecture with a background process
managing all open terminal windows, which is beneficial to
memory consumption.

%package -n gnome-shell-search-provider-gnome-terminal
Summary:        GNOME Terminal Search Provider for GNOME Shell
Group:          System/X11/Terminals
Requires:       %{name} = %{version}
Supplements:    (gnome-shell and %{name})
BuildArch:      noarch

%description -n gnome-shell-search-provider-gnome-terminal
This package contains a search provider to enable GNOME Shell to get
search results from GNOME Terminal.

%package -n nautilus-extension-terminal
Summary:        Nautilus extension adding "Open Terminal" as folder action
Group:          System/GUI/GNOME
Supplements:    (nautilus and %{name})
# nautilus-open-terminal was merged into gnome-terminal source during 3.9 development.
Provides:       nautilus-open-terminal = %{version}
Obsoletes:      nautilus-open-terminal < %{version}

%description -n nautilus-extension-terminal
This is a nautilus extension that allows you to open a terminal in
arbitrary folders.

%lang_package

%prep
%autosetup -p1

%build
%meson \
%if %{with nautilus_extension}
    -Dnautilus_extension=true
%else
  -Dnautilus_extension=false
%endif
%meson_build

%install
%meson_install
%if ! %{with nautilus_extension}
rm %{buildroot}/usr/share/metainfo/org.gnome.Terminal.Nautilus.metainfo.xml
%endif

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Terminal*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Terminal.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Terminal.Preferences.desktop
desktop-file-validate %{buildroot}%{_datadir}/xdg-terminals/org.gnome.Terminal.desktop
%meson_test

%files
%license COPYING
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/gnome-terminal
%{_datadir}/metainfo/org.gnome.Terminal.metainfo.xml
%{_datadir}/applications/org.gnome.Terminal.desktop
%{_datadir}/applications/org.gnome.Terminal.Preferences.desktop
%dir %{_datadir}/xdg-terminals
%{_datadir}/xdg-terminals/org.gnome.Terminal.desktop
%{_libexecdir}/gnome-terminal-server
%{_datadir}/dbus-1/services/org.gnome.Terminal.service
%{_datadir}/glib-2.0/schemas/org.gnome.Terminal.gschema.xml
%{_userunitdir}/gnome-terminal-server.service
%{_datadir}/icons/hicolor/*/apps/org.gnome.Terminal*.svg
%{_mandir}/man1/gnome-terminal.1%{?ext_man}
%dir %{_libdir}/gnome-terminal
%{_libdir}/gnome-terminal/gschemas.compiled
%{_libexecdir}/gnome-terminal-preferences

%files -n gnome-shell-search-provider-gnome-terminal
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/gnome-terminal-search-provider.ini

%if %{with nautilus_extension}
%files -n nautilus-extension-terminal
%{_libdir}/nautilus/extensions-4/libterminal-nautilus.so
%{_datadir}/metainfo/org.gnome.Terminal.Nautilus.metainfo.xml
%endif

%files lang -f %{name}.lang

%changelog
