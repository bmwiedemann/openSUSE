#
# spec file for package linssid
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           linssid
Version:        3.6
Release:        0
Summary:        Graphical wireless scanning for Linux
License:        GPL-3.0-only
Group:          System/Monitoring
Url:            http://sourceforge.net/projects/linssid/
Source0:        http://sourceforge.net/projects/linssid/files/LinSSID_%{version}/linssid_%{version}.orig.tar.gz
# PATCH-FIX-OPENSUSE linssid-icons.patch -- puts icons in the proper paths
Patch0:         linssid-icons.patch
# PATCH-FIX-OPENSUSE linssid-icons.patch linssid-use-shared-qwt-qt5.patch -- uses shared qwt6 as packaged on openSUSE
Patch1:         linssid-use-shared-qwt-qt5.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
%if 0%{?suse_version} > 1315
BuildRequires:  libboost_regex-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Qwt6)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5UiTools)
Requires:       iw

%description
LinSSID is graphically and functionally similar to Inssider (Microsoft™ Windows®).
It is written in C++ using Linux wireless tools and Qt5.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%qmake5
make %{?_smp_mflags}

%install
%qmake5_install
# create launcher
mkdir -pv %{buildroot}%{_bindir}
tee %{buildroot}/%{_bindir}/linssid_wrapper << "EOF"
#!/bin/bash
TMP_PATH=$PATH
PATH=$PATH:%{_sbindir}
%{_bindir}/xdg-su -c %{_sbindir}/linssid
PATH=$TMP_PATH
EOF
%fdupes -s %{buildroot}

%if 0%{?suse_version} <= 1315
%post
%desktop_database_post

%postun
%desktop_database_post
%endif

%files
%license linssid-app/license.txt
%{_sbindir}/linssid
%attr(755,root,root) %{_bindir}/linssid_wrapper
%{_datadir}/applications/linssid.desktop
%{_datadir}/linssid
%{_datadir}/pixmaps/linssid.svg

%changelog
