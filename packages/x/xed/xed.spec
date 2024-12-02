#
# spec file for package xed
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


Name:           xed
Version:        3.6.8
Release:        0
Summary:        A text editor with highlighting
License:        GPL-2.0-or-later
URL:            https://github.com/linuxmint/xed
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xapp)

%description
xed is a text editor designed for the Cinnamon desktop. It has most
standard text editor functions and supports international text in
Unicode. Advanced features include syntax highlighting and automatic
indentation of source code, printing and editing of multiple
documents in one window.

xed is extensible through a plugin system, which currently
includes support for spell checking, comparing files, viewing VCS
ChangeLogs, and adjusting indentation levels.

%package devel
Summary:        Development files for Xed, a text editor
Requires:       %{name} = %{version}
Requires:       pkgconfig(gtksourceview-3.0)

%description devel
xed is a text editor designed for the Cinnamon desktop. It has most
standard text editor functions and supports international text in
Unicode. Advanced features include syntax highlighting and automatic
indentation of source code, printing and editing of multiple
documents in one window.

xed is extensible through a plugin system, which currently
includes support for spell checking, comparing files, viewing VCS
ChangeLogs, and adjusting indentation levels.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/gir-1.0/
%{_libdir}/%{name}
%{_datadir}/glib-2.0/schemas/org.x.editor.*.xml
%{_datadir}/metainfo/xed.appdata.xml
%{_datadir}/dbus-1/services/org.x.editor.service
%{_datadir}/applications/org.x.editor.desktop
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_datadir}/help/C/%{name}
%{_datadir}/gtksourceview-4/styles/%{name}.xml

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/gir-1.0

%files lang -f %{name}.lang

%changelog
