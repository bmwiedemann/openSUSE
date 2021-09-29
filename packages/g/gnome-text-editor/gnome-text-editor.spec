#
# spec file for package gnome-text-editor
#
# Copyright (c) 2021 SUSE LLC
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


Name:           gnome-text-editor
Version:        41.0
Release:        0
Summary:        GNOME Text Editor
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-text-editor
Source:         https://download.gnome.org/sources/%{name}/41/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(enchant-2) >= 2.2.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.69
BuildRequires:  pkgconfig(gtk4) >= 4.3
BuildRequires:  pkgconfig(gtksourceview-5) >= 5.1.1
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libadwaita-1)

%description
Text Editor is a simple text editor that focus on session
management. It works hard to keep track of changes and state even
if you quit the application. You can come back to your work even if
you've never saved it to a file.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Ddevelopment=false \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc NEWS README.md
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/gnome-text-editor
%{_datadir}/appdata/org.gnome.TextEditor.appdata.xml
%{_datadir}/applications/org.gnome.TextEditor.desktop
%{_datadir}/dbus-1/services/org.gnome.TextEditor.service
%{_datadir}/glib-2.0/schemas/org.gnome.TextEditor.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg

%files lang -f %{name}.lang

%changelog
