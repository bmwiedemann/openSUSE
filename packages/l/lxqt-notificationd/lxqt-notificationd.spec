#
# spec file for package lxqt-notificationd
#
# Copyright (c) 2020 SUSE LLC
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


Name:           lxqt-notificationd
Version:        0.16.0
Release:        0
Summary:        LXQt Notification daemon
License:        LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem) >= 5.36.0
BuildRequires:  pkgconfig(Qt5UiTools) >= 5.12.0
BuildRequires:  pkgconfig(Qt5Xdg)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lxqt) >= %{version}
Recommends:     %{name}-lang

%description
The LXQt Notification daemon

%lang_package

%prep
%setup -q
# Changing LXQt into X-LXQt in desktop files to be freedesktop compliant and shut rpmlint warnings
#find -name '*desktop.in*' -exec sed -ri 's/(LXQt;)/X-\1/' {} +

%build
%cmake -DPULL_TRANSLATIONS=No
make %{?_smp_mflags}

%install
%cmake_install
%fdupes -s %{buildroot}%{_datadir}

%find_lang %{name} --with-qt

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_bindir}/lxqt-config-notificationd
%{_datadir}/applications/lxqt-config-notificationd.desktop
%{_sysconfdir}/xdg/autostart/lxqt-notifications.desktop

%files lang -f %{name}.lang 
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/lxqt-notificationd
%{_datadir}/lxqt/translations/lxqt-config-notificationd
%{_datadir}/lxqt/translations/lxqt-notificationd/*

%changelog
