#
# spec file for package guake
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


Name:           guake
Version:        3.6.3
Release:        0
Summary:        Drop-down terminal for GNOME
License:        GPL-2.0-only
Group:          System/X11/Terminals
Url:            http://guake-project.org/
Source:         https://github.com/Guake/guake/archive/%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  glib2-tools
BuildRequires:  gobject-introspection
BuildRequires:  pandoc
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libwnck-3.0)
Requires:       python3-cairo
Requires:       python3-dbus-python
Requires:       python3-gobject-Gdk
Requires:       python3-pbr
Recommends:     libutempter0
Suggests:       gtk3-metatheme-numix
BuildArch:      noarch
# Other requirements documented upstream but apparently not needed:
#     dconf-editor
#     glade
#     gnome-tweak-tool
#     gsettings-desktop-schemas

%description
Guake is a dropdown terminal made for the GNOME desktop environment.

%prep
%setup -q

%build
make

%install
PBR_VERSION=%{version} make install DESTDIR=%{buildroot} prefix=%{_prefix}
rm -r %{buildroot}%{python3_sitelib}/guake/tests/
# conflicts with libgio-2_0-0
rm %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled
%fdupes %{buildroot}
%suse_update_desktop_file -G "Guake Preferences" %{name}-prefs Settings DesktopSettings
%suse_update_desktop_file -G "Guake Terminal" %{name} System TerminalEmulator
%find_lang %{name}

%files -f %{name}.lang
%doc README.rst NEWS.rst
%license COPYING
%{python3_sitelib}/*
%{_bindir}/guake
%{_bindir}/guake-toggle
%{_datadir}/applications/guake-prefs.desktop
%{_datadir}/applications/guake.desktop
%{_datadir}/glib-2.0/schemas/org.guake.gschema.xml
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/guake.appdata.xml
%{_datadir}/pixmaps/
%{_datadir}/guake/

%changelog
