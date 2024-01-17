#
# spec file for package fred
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           fred
Version:        0.2.0
Release:        0
Summary:        Forensic Registry EDitor, an editor for Microsoft Registry hives
License:        GPL-2.0+
Group:          Productivity/File utilities
URL:            https://www.pinguin.lu/fred
Source:         https://files.pinguin.lu/fred-%{version}.tar.gz
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(hivex)
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  update-desktop-files

%description
Forensic Registry EDitor (fred) is a editor for Microsoft Registry
hives with special features useful during forensic analysis, such as
a hex viewer with data interpreter and a reporting function that can
be extended with custom ECMAScript report templates.

%prep
%setup -q

%build
qmake-qt5 DEFINES+="SYSTEM_REPORT_TEMPLATE_DIR=\'\\\"%{_datadir}/fred/report_templates\\\"\'" QMAKE_CFLAGS+="%optflags" QMAKE_CXXFLAGS+="%optflags" QMAKE_STRIP="/bin/true"
%make_build

%install
install -Dm 755 fred %{buildroot}%{_bindir}/fred
%suse_update_desktop_file -i -G "fred" -r fred Qt Office Database
install -Dm 644 report_templates/*.qs --target-directory %{buildroot}%{_datadir}/fred/report_templates/
install -Dm 644 resources/fred.png %{buildroot}%{_datadir}/pixmaps/fred.png

%files
%doc README
%{_bindir}/fred
%{_datadir}/applications/fred.desktop
%{_datadir}/pixmaps/fred.png
%{_datadir}/fred/

%license debian/copyright

%changelog
