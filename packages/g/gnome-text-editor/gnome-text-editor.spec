#
# spec file for package gnome-text-editor
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        49.1
Release:        0
Summary:        GNOME Text Editor
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-text-editor
Source:         %{name}-%{version}.tar.zst

BuildSystem:    meson
BuildOption:    -Ddevelopment=false

BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson >= 0.59.1

# Optional test dependencies
BuildRequires:  desktop-file-utils

%description
Text Editor is a simple text editor that focus on session
management. It works hard to keep track of changes and state even
if you quit the application. You can come back to your work even if
you've never saved it to a file.

%lang_package

%generate_buildrequires
%meson_buildrequires

%install -a
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc NEWS README.md
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.TextEditor.desktop
%{_datadir}/dbus-1/services/org.gnome.TextEditor.service
%{_datadir}/glib-2.0/schemas/org.gnome.TextEditor.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/org.gnome.TextEditor.metainfo.xml

%files lang -f %{name}.lang

%changelog
