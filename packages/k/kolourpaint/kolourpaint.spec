#
# spec file for package kolourpaint
#
# Copyright (c) 2024 SUSE LLC
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kolourpaint
Version:        24.05.2
Release:        0
Summary:        Paint Program
# See boo#717722 for license details
# GPL-2.0 is the license of the Bulgarian translation
License:        LGPL-2.1-or-later AND GPL-2.0-only
URL:            https://apps.kde.org/kolourpaint
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# FIXME not ported or CMakeLists.txt error
# BuildRequires: cmake(KF5Sane)
Provides:       kolourpaint5 = %{version}
Obsoletes:      kolourpaint5 < %{version}

%description
Paint program by KDE

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%suse_update_desktop_file org.kde.kolourpaint RasterGraphics

%fdupes %{buildroot}%{_kf6_sharedir}

%ldconfig_scriptlets

%files
%license COPYING*
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/*/
%{_kf6_applicationsdir}/org.kde.kolourpaint.desktop
%{_kf6_appstreamdir}/org.kde.kolourpaint.appdata.xml
%{_kf6_bindir}/kolourpaint
%{_kf6_iconsdir}/hicolor/*/apps/kolourpaint.*
%{_kf6_libdir}/libkolourpaint_lgpl.so*
%{_kf6_sharedir}/kolourpaint/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/*/

%changelog
