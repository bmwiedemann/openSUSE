#
# spec file for package notes-up
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           notes-up
Version:        2.0.2
Release:        0
Summary:        Markdown notes editor & manager
License:        GPL-3.0-only
Group:          Productivity/Office/Word Processor
URL:            https://github.com/Philip-Scott/Notes-up
Source:         https://github.com/Philip-Scott/Notes-up/archive/%{version}.tar.gz#/Notes-up-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.39.0
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(libmarkdown)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
Recommends:     %{name}-lang

%description
Notes Up is a notes manager written for Elementary OS. Notes in
Markdown format can be created.

%lang_package

%prep
%setup -q -n Notes-up-%{version}

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
%find_lang %{name}

%files
%license LICENSE
%doc changelog.md README.md
%{_bindir}/com.github.philip-scott.notes-up
%{_datadir}/applications/com.github.philip-scott.notes-up.desktop
%{_datadir}/glib-2.0/schemas/org.notes.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.philip-scott.notes-up.??g
%{_datadir}/metainfo/com.github.philip-scott.notes-up.appdata.xml
%{_datadir}/notes-up/

%files lang -f %{name}.lang

%changelog
