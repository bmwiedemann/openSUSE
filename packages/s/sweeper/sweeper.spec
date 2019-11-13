#
# spec file for package sweeper
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without	lang
Name:           sweeper
Version:        19.08.3
Release:        0
Summary:        KDE Privacy Utility
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  breeze5-icons
BuildRequires:  extra-cmake-modules
BuildRequires:  kactivities-stats-devel
BuildRequires:  kbookmarks-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Helps clean unwanted traces the user leaves on the system.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n sweeper-%{version}

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
%suse_update_desktop_file org.kde.sweeper Utility Security
mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/actions
mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/
cp %{_kf5_iconsdir}/breeze/actions/24/trash-empty.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/actions/
cp %{_kf5_iconsdir}/breeze/apps/48/sweeper.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/

%files
%license COPYING.LIB
%doc %lang(en) %{_kf5_htmldir}/en/sweeper/
%{_kf5_applicationsdir}/org.kde.sweeper.desktop
%{_kf5_appstreamdir}/org.kde.sweeper.appdata.xml
%{_kf5_bindir}/sweeper
%{_kf5_iconsdir}/hicolor/scalable/*/*
%{_kf5_kxmlguidir}/sweeper/
%{_kf5_sharedir}/dbus-1/interfaces/*.xml

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
