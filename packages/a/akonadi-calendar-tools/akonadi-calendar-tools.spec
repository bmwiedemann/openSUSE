#
# spec file for package akonadi-calendar-tools
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           akonadi-calendar-tools
Version:        19.08.3
Release:        0
Summary:        Console applications and utilities for managing calendars
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-calendar-devel
BuildRequires:  akonadi-contact-devel
BuildRequires:  akonadi-server-devel >= %{_kapp_version}
BuildRequires:  calendarsupport-devel
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  kcalcore-devel
BuildRequires:  kcalutils-devel
BuildRequires:  kcontacts-devel
BuildRequires:  kdoctools-devel
BuildRequires:  libkdepim-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Console applications and utilities for managing calendars in Akonadi.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF
%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif

%files
%license COPYING*
%{_kf5_debugdir}/console.categories
%{_kf5_debugdir}/console.renamecategories
%doc %lang(en) %{_kf5_htmldir}/en/konsolekalendar/
%{_kf5_applicationsdir}/konsolekalendar.desktop
%{_kf5_bindir}/calendarjanitor
%{_kf5_bindir}/konsolekalendar
%{_kf5_iconsdir}/hicolor/*/apps/konsolekalendar.png

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
