#
# spec file for package kmag
#
# Copyright (c) 2022 SUSE LLC
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kmag
Version:        22.12.0
Release:        0
Summary:        Screen Magnifier
License:        GPL-2.0-only
URL:            https://apps.kde.org/kmag
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  alsa-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  sbl
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      kmag5 < %{version}
Provides:       kmag5 = %{version}

%description
Magnifies a part of the screen.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file -r org.kde.kmag Utility Accessibility

%files
%license COPYING*
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_applicationsdir}/org.kde.kmag.desktop
%{_kf5_appstreamdir}/org.kde.kmag.appdata.xml
%{_kf5_bindir}/kmag
%{_kf5_iconsdir}/hicolor/*/apps/kmag.*
%{_kf5_mandir}//man1/kmag.1*
%{_kf5_sharedir}/kmag/

%files lang -f %{name}.lang

%changelog
