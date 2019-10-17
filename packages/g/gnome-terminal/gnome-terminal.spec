#
# spec file for package gnome-terminal
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


Name:           gnome-terminal
Version:        3.34.2
Release:        0
Summary:        GNOME Terminal
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          System/X11/Terminals
URL:            https://wiki.gnome.org/Apps/Terminal
Source0:        https://download.gnome.org/sources/gnome-terminal/3.34/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
# Needed for search provider. It should not be needed in my opinion,
# we have to take this up with upstream, or just provide search
# provider interface definition file as source.
BuildRequires:  gnome-shell
BuildRequires:  intltool >= 0.50.1
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(dconf) >= 0.14.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.34.0
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.42.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 0.1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(libnautilus-extension) >= 3.0.0
BuildRequires:  pkgconfig(libpcre2-8) >= 10.00
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vte-2.91) >= 0.58.0
BuildRequires:  pkgconfig(x11)
Requires(pre):  filesystem
Recommends:     %{name}-lang
%if 0%{?sle_version}
BuildRequires:  pkgconfig(gconf-2.0) >= 2.31.3
%endif
%if 0%{?sle_version}
Requires(pre):  gconf2
%endif

%description
This package provides the GNOME terminal emulator application.

%package -n gnome-shell-search-provider-gnome-terminal
Summary:        GNOME Terminal -- Search Provider for GNOME Shell
Group:          System/X11/Terminals
Requires:       %{name} = %{version}
Supplements:    packageand(gnome-shell:%{name})

%description -n gnome-shell-search-provider-gnome-terminal
This package contains a search provider to enable GNOME Shell to get
search results from GNOME Terminal.

%package -n nautilus-extension-terminal
Summary:        Nautilus Extension to Open Terminal in Folders
Group:          System/GUI/GNOME
Supplements:    packageand(nautilus:%{name})
# nautilus-open-terminal was merged into gnome-terminal source during 3.9 development.
Provides:       nautilus-open-terminal = %{version}
Obsoletes:      nautilus-open-terminal < %{version}

%description -n nautilus-extension-terminal
This is a nautilus extension that allows you to open a terminal in
arbitrary folders.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%configure \
	--disable-static \
%if !0%{?sle_version}
	--disable-migration \
%endif
	--with-gtk=3.0 \
	--with-nautilus-extension \
	%{nil}
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/gnome-terminal
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.Terminal.appdata.xml
%{_datadir}/applications/org.gnome.Terminal.desktop
%{_libexecdir}/gnome-terminal-server
%if 0%{?sle_version}
%{_libexecdir}/gnome-terminal-migration
%endif
%{_datadir}/dbus-1/services/org.gnome.Terminal.service
%{_datadir}/glib-2.0/schemas/org.gnome.Terminal.gschema.xml
%{_userunitdir}/gnome-terminal-server.service
%{_datadir}/icons/hicolor/*/apps/org.gnome.Terminal*.svg

%files -n gnome-shell-search-provider-gnome-terminal
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/gnome-terminal-search-provider.ini

%files -n nautilus-extension-terminal
%{_libdir}/nautilus/extensions-3.0/libterminal-nautilus.so
%{_datadir}/metainfo/org.gnome.Terminal.Nautilus.metainfo.xml

%files lang -f %{name}.lang

%changelog
