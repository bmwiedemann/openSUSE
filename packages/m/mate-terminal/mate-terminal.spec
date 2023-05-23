#
# spec file for package mate-terminal
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


%define _version 1.26
Name:           mate-terminal
Version:        1.26.1
Release:        0
Summary:        MATE Desktop terminal emulator
License:        GPL-3.0-or-later
Group:          System/X11/Terminals
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(vte-2.91)
Requires:       gsettings-backend-dconf
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
MATE Terminal is a terminal emulation application that you can use
to perform the following actions:
 * Access a UNIX shell in the MATE environment.
 * Run any application that is designed to run on VT102, VT220, and
   xterm terminals.

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
%suse_update_desktop_file %{name}

%files
%license COPYING
%doc NEWS README
%{_bindir}/%{name}
%{_bindir}/%{name}.wrapper
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_datadir}/help/C/%{name}

%files lang -f %{name}.lang

%changelog
