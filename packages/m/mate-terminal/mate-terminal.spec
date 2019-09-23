#
# spec file for package mate-terminal
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


%define _version 1.23
Name:           mate-terminal
Version:        1.23.0
Release:        0
Summary:        MATE Desktop terminal emulator
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(vte-2.91) >= 0.44
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
%autosetup -p1

%build
NOCONFIGURE=1 mate-autogen
%configure
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name}

# Axe out scrollkeeper stuff.
rm -rf %{buildroot}%{_localstatedir}/

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%glib2_gsettings_schema_postun
%endif

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
