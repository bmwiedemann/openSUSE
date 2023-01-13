#
# spec file for package gnome-text-editor
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


Name:           gnome-text-editor
Version:        43.2
Release:        0
Summary:        GNOME Text Editor
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-text-editor
Source:         https://download.gnome.org/sources/gnome-text-editor/43/%{name}-%{version}.tar.xz

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson >= 0.59.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(enchant-2) >= 2.2.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.69
BuildRequires:  pkgconfig(gtk4) >= 4.3
BuildRequires:  pkgconfig(gtksourceview-5) >= 5.5.0
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2.alpha

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
%fdupes %{buildroot}%{_datadir}

%check
%meson_test

%files
%license COPYING
%doc NEWS README.md
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.TextEditor.desktop
%{_datadir}/dbus-1/services/org.gnome.TextEditor.service
%{_datadir}/glib-2.0/schemas/org.gnome.TextEditor.gschema.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/styles
%{_datadir}/%{name}/styles/builder-dark.xml
%{_datadir}/%{name}/styles/builder.xml
%{_datadir}/%{name}/styles/peninsula-dark.xml
%{_datadir}/%{name}/styles/peninsula.xml
%{_datadir}/%{name}/styles/printing.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/org.gnome.TextEditor.appdata.xml

%files lang -f %{name}.lang

%changelog
