#
# spec file for package dianara
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


%define _name   Dianara
Name:           dianara
Version:        1.4.4
Release:        0
Summary:        Pump.io social network desktop client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            http://dianara.nongnu.org/
Source:         https://download-mirror.savannah.gnu.org/releases/%{name}/%{name}-v%{version}.tar.gz
%if 0%{?suse_version} <= 1320
Source1:        %{name}.changes
%endif
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qoauth-qt5-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
Dianara is a client for pump.io (and GNU MediaGoblin), a desktop
application for GNU/Linux that allows users to manage their pump.io
social networking accounts without the need to use a web browser.
You can read your timelines, post messages and pictures, and manage
your contacts.

%prep
%setup -q -n %{name}-v%{version}

%build
%if 0%{?suse_version} <= 1320
SOURCE_DATE="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
export SOURCE_DATE_EPOCH="$(date -d "$SOURCE_DATE" "+%%s")"

%endif
%qmake5
make %{?_smp_mflags} V=1

%install
%qmake5_install

%suse_update_desktop_file -r org.nongnu.%{name} Network InstantMessaging

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license LICENSE
%doc CHANGELOG README TRANSLATING
%{_bindir}/%{name}
%{_datadir}/applications/org.nongnu.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/org.nongnu.%{name}.appdata.xml
%{_mandir}/man1/dianara.1%{?ext_man}

%changelog
