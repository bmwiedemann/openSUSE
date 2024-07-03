#
# spec file for package calcurse
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


Name:           calcurse
Version:        4.8.1
Release:        0
Summary:        Text-based Organizer
License:        BSD-2-Clause
Group:          Productivity/Office/Organizers
URL:            https://calcurse.org
Source:         https://calcurse.org/files/%{name}-%{version}.tar.gz
Source1:        https://calcurse.org/files/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        %{name}.desktop
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  update-desktop-files

%description
Calcurse is a text-based personal organizer which helps keep track of events
and everyday tasks. It has a calendar and a "todo" list, and puts your
appointments in order. The user interface is configurable, and you can choose
between different color schemes and layouts. All of the commands are
documented within an online help system.

%lang_package

%prep
%setup -q
sed -i "s/#!\/usr\/bin\/env python3/#!\/usr\/bin\/python3/" contrib/caldav/calcurse-caldav.py
sed -i "s/#!\/usr\/bin\/env python3/#!\/usr\/bin\/python3/" contrib/vdir/calcurse-vdir

%build
%configure
%make_build

%install
%make_install

rm -rf "%{buildroot}%{_datadir}/doc"

install -D -m 0644 %{SOURCE3} "%{buildroot}%{_datadir}/applications/%{name}.desktop"
%if 0%{?suse_version}
%suse_update_desktop_file -r "%{name}" Office Calendar
%endif

mv "%{buildroot}%{_datadir}/locale/en" \
   "%{buildroot}%{_datadir}/locale/en_US"

%find_lang %{name}

%files
%license COPYING
%doc AUTHORS
%doc doc/manual.html
%{_bindir}/%{name}
%{_bindir}/%{name}-caldav
%{_bindir}/%{name}-upgrade
%{_bindir}/%{name}-vdir
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/%{name}.desktop

%files lang -f %{name}.lang

%changelog
