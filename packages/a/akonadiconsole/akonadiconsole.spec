#
# spec file for package akonadiconsole
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


%define kf5_version 5.28.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           akonadiconsole
Version:        19.08.2
Release:        0
Summary:        Management and debugging console for akonadi
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-contact-devel
BuildRequires:  akonadi-mime-devel
BuildRequires:  akonadi-search-devel
BuildRequires:  akonadi-server-devel >= %{_kapp_version}
BuildRequires:  calendarsupport-devel
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  kcalcore-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcontacts-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kitemmodels-devel
BuildRequires:  kmime-devel
BuildRequires:  kpimtextedit-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdepim-devel
BuildRequires:  libkleo-devel
BuildRequires:  libxapian-devel
BuildRequires:  messagelib-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5DBus) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Test) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.6.0
Obsoletes:      akonadi_resources < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Akonadi Console is a utility that can be used to explore or manage
Akonadi. This utility exposes Akonadi internals, and can be useful
for debugging.

%prep
%setup -q

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF
%make_jobs

%install
%kf5_makeinstall -C build
%suse_update_desktop_file -u org.kde.akonadiconsole Network  Email

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB COPYING.DOC
%{_kf5_debugdir}/akonadiconsole.categories
%{_kf5_debugdir}/akonadiconsole.renamecategories
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%{_kf5_applicationsdir}/org.kde.akonadiconsole.desktop
%{_kf5_bindir}/akonadiconsole
%{_kf5_iconsdir}/hicolor/*/apps/akonadiconsole.png
%{_kf5_libdir}/libakonadiconsole.so.*
%{_kf5_sharedir}/kconf_update/

%changelog
