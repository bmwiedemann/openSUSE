#
# spec file for package gsmartcontrol
#
# Copyright (c) 2025 SUSE LLC
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


Name:           gsmartcontrol
Version:        2.0.2
Release:        0
Summary:        Hard Disk Health Inspection Tool
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Hardware/Other
URL:            http://gsmartcontrol.sourceforge.net/
#Source0:        http://downloads.sourceforge.net/%%{name}/%%{version}/%%{name}-%%{version}.tar.bz2
Source0:        https://github.com/ashaduri/gsmartcontrol/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  cmake >= 3.14
BuildRequires:  fdupes
%if 0%{?suse_version} < 1600
BuildRequires:  gcc13
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
BuildRequires:  polkit
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.4
Requires:       polkit
Requires:       smartmontools >= 5.43
Recommends:     xdg-utils

%description
GSmartControl is a graphical user interface for smartctl, which is a tool for
querying and controlling SMART (Self-Monitoring, Analysis, and Reporting
Technology) data in hard disk drives. It allows inspecting the drive's
SMART data to determine its health, as well as run various tests on it.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
export CC=gcc-13
export CXX=g++-13
%endif
%cmake .. -DCMAKE_BUILD_TYPE=Release

%install
%cmake_install
%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}%{_prefix}

%files
%doc README.md
%doc %{_defaultdocdir}/%{name}
%license LICENSE.txt LICENSE.LGPL3.txt dependencies/*/*/LICENSE.*
%{_sbindir}/%{name}
%{_bindir}/%{name}-root
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-root.1%{?ext_man}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/polkit-1/actions/org.gsmartcontrol.policy

%changelog
