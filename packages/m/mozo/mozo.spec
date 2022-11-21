#
# spec file for package mozo
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


%define _version 1.26
Name:           mozo
Version:        1.26.2
Release:        0
Summary:        MATE Desktop menu editor
License:        LGPL-2.1-or-later
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libmate-menu) >= %{_version}
BuildRequires:  pkgconfig(pygobject-3.0)
Requires:       mate-menus >= %{_version}
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Recommends:     %{name}-lang
# mate-menu-editor was last used in openSUSE 13.1.
Provides:       mate-menu-editor = %{version}
Obsoletes:      mate-menu-editor < %{version}
Obsoletes:      mate-menu-editor-lang < %{version}
BuildArch:      noarch

%description
This package provides Mozo, a menu editor for the MATE Desktop,
using the freedesktop.org menu specification.

%lang_package

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure
%make_build

%install
%make_install

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{python_sitelib}/
%suse_update_desktop_file %{name}

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{python3_sitelib}/Mozo/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_mandir}/man?/%{name}.?%{?ext_man}

%files lang -f %{name}.lang

%changelog
