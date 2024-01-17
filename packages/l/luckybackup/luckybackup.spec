#
# spec file for package luckybackup
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


Name:           luckybackup
Version:        0.5.0
Release:        0
Summary:        A backup and sync tool
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Backup
URL:            http://luckybackup.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       polkit
Requires:       rsync
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

%description
luckyBackup is an application that backs-up and/or synchronizes any directories
with rsync.

It checks all declared directories before proceeding with any data
manipulation, and, by way of rsync, transfers only changes and not
all data.

%prep
%setup -q
# Fix permissions (fixes rpmlint errors "spurious-executable-perm" and "executable-docs")
chmod 644 manual/index.html

%build
%qmake5 QMAKE_CXXFLAGS+="%{optflags}" -config release luckybackup.pro
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

# Remove unneeded files
rm -rf %{buildroot}%{_datadir}/doc/luckybackup/
rm -rf %{buildroot}%{_datadir}/menu/

%if 0%{?suse_version}
%suse_update_desktop_file -r %{name} Qt Utility Archiving
%suse_update_desktop_file -r %{name}-su Qt Utility Archiving
%endif

%files
%doc license/ manual/ readme/*
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_bindir}/luckybackup*
%{_datadir}/applications/luckybackup*.desktop
%{_datadir}/luckybackup/
%{_datadir}/pixmaps/luckybackup.*
%{_datadir}/polkit-1/actions/net.luckybackup.su.policy
%{_mandir}/man8/luckybackup*.8%{?ext_man}

%changelog
