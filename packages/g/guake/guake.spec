#
# spec file for package guake
#
# Copyright (c) 2022 SUSE LLC
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
Version:        3.9.0
Release:        0
Summary:        Drop-down terminal for GNOME
License:        GPL-2.0-only
Group:          System/X11/Terminals
URL:            http://guake-project.org/
# Use PyPI source, not GitHub tag-ref tarballs, see https://guake.readthedocs.io/en/latest/user/installing.html#install-from-source
Source0:        https://files.pythonhosted.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz
# PyPI tarball missed this file
Source1:        https://raw.githubusercontent.com/Guake/guake/%{version}/guake/paths.py.in
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  glib2-tools
BuildRequires:  gobject-introspection
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools >= 57.5.0
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libwnck-3.0)
Requires:       python3-cairo
Requires:       python3-dbus-python
Requires:       python3-gobject-Gdk
Recommends:     libutempter0
Suggests:       gtk3-metatheme-numix
BuildArch:      noarch
# Other requirements documented upstream but apparently not needed:
#     dconf-editor
#     glade
#     gnome-tweak-tool
#     gsettings-desktop-schemas

%lang_package

%description
Guake is a dropdown terminal made for the GNOME desktop environment.

%prep
%autosetup -p1
cp %{SOURCE1} ./guake/
# Remove a useless placeholder dir from docs
rm -fr ./docs/source/_static

sed -i 's/\r$//' ./docs/make.bat

%build
%make_build
# docs cannot be built as they require a local git repository

%install
%make_install PREFIX=%{_prefix}

rm -fr %{buildroot}%{_datadir}/%{name}/po

# conflicts with libgio-2_0-0
rm %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled
%fdupes %{buildroot}
%suse_update_desktop_file -G "Guake Preferences" %{name}-prefs Settings DesktopSettings
%suse_update_desktop_file -G "Guake Terminal" %{name} System TerminalEmulator
%find_lang %{name} %{?no_lang_C}

%files
%doc README.rst NEWS.rst docs/
%license COPYING
%{python3_sitelib}/guake/
%{python3_sitelib}/guake-%{version}-py%{python3_version}.egg-info/
%{_bindir}/guake
%{_bindir}/guake-toggle
%{_datadir}/applications/guake-prefs.desktop
%{_datadir}/applications/guake.desktop
%{_datadir}/glib-2.0/schemas/org.guake.gschema.xml
%{_datadir}/metainfo/guake.desktop.metainfo.xml
%{_datadir}/pixmaps/guake.png
%{_datadir}/guake/

%files lang -f %{name}.lang

%changelog
