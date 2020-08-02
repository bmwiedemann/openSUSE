#
# spec file for package speedcrunch
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           speedcrunch
Version:        0.12
Release:        0
Summary:        Calculator with history display, keyboard-oriented
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
Url:            http://www.speedcrunch.org/
Source0:        https://bitbucket.org/heldercorreia/speedcrunch/get/release-%{version}.0.tar.bz2#/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5Help) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A keyboard-oriented desktop scientific calculator which shows results in a
scrollable display.

%prep
%setup -q -n heldercorreia-speedcrunch-ea93b21f9498

%build
%cmake ../src
%make_jobs

%install
%cmake_install ../src

# Recent AppStream versions require the appdata.xml files to be in /usr/share/metainfo
%if 0%{?suse_version} > 1320
mkdir -p %{buildroot}%{_datadir}/metainfo
mv %{buildroot}%{_datadir}/appdata/speedcrunch.appdata.xml %{buildroot}%{_datadir}/metainfo/
%endif

%files
%defattr(-,root,root,-)
%doc README.md doc/legacy/speedcrunch-manual.odt pkg/COPYING.rtf
%{_bindir}/speedcrunch
%{_datadir}/pixmaps/speedcrunch.png
%if 0%{?suse_version} > 1320
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/speedcrunch.appdata.xml
%else
%dir %{_datadir}/appdata
%{_datadir}/appdata/speedcrunch.appdata.xml
%endif
%{_datadir}/applications/speedcrunch.desktop

%changelog
