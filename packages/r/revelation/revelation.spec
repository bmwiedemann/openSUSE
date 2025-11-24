#
# spec file for package revelation
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           revelation
Version:        0.5.6
Release:        0
Summary:        Password manager for GNOME
License:        GPL-2.0-only
Group:          Productivity/Security
URL:            http://revelation.olasagasti.info
Source:         https://github.com/mikelolasagasti/revelation/releases/download/revelation-%{version}/revelation-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  intltool >= 0.35.0
BuildRequires:  meson
BuildRequires:  perl-XML-Parser
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-pwquality
BuildRequires:  python3-pycryptodomex
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14
BuildRequires:  pkgconfig(pygobject-3.0)
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-pwquality
Requires:       python3-pycryptodomex
BuildArch:      noarch

%description
Revelation is a password manager. It organizes accounts in
a tree structure, and stores them as AES-encrypted XML files.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}
%fdupes %{buildroot}%{_prefix}

%files
%defattr(-, root, root)
%license COPYING
%doc AUTHORS ChangeLog README.md TODO NEWS
%{_bindir}/revelation
%{_datadir}/applications/info.olasagasti.revelation.desktop
%{_datadir}/metainfo/info.olasagasti.revelation.metainfo.xml
%{_datadir}/revelation/
%{_datadir}/icons/hicolor/*/apps/info.olasagasti.revelation*
%{_datadir}/mime/packages/revelation.xml
%{python3_sitelib}/revelation/
%{_datadir}/glib-2.0/schemas/info.olasagasti.revelation.gschema.xml
%{_datadir}/icons/hicolor/48x48/mimetypes/gnome-mime-application-x-revelation.png

%files lang -f %{name}.lang

%changelog
