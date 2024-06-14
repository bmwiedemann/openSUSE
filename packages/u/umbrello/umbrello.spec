#
# spec file for package umbrello
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


%ifarch %{arm} aarch64 %{ix86} x86_64 %{x86_64} %{riscv}
%bcond_without kdevelop
%endif
%bcond_without released
Name:           umbrello
Version:        24.05.1
Release:        0
Summary:        UML Modeller
License:        GPL-2.0-only AND GFDL-1.2-only AND GPL-3.0-or-later
URL:            https://apps.kde.org/umbrello
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
%if %{with kdevelop}
BuildRequires:  kdevelop5-pg-qt
BuildRequires:  kdevplatform-devel
%endif
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5ThreadWeaver)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Obsoletes:      umbrello5 < %{version}
Provides:       umbrello5 = %{version}

%description
Umbrello is a UML modelling application.

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
export CXXFLAGS="%{optflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"

%cmake_kf5 -d build -- -DBUILD_KF5=ON
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.umbrello Development Design

%files
%license COPYING COPYING.DOC
%doc README
%doc %lang(en) %{_kf5_htmldir}/en/umbrello
%{_kf5_applicationsdir}/org.kde.umbrello.desktop
%{_kf5_appstreamdir}/org.kde.umbrello.appdata.xml
%{_kf5_bindir}/po2xmi5
%{_kf5_bindir}/umbrello5
%{_kf5_bindir}/xmi2pot5
%{_kf5_iconsdir}/hicolor/*/*/umbrello*
%{_kf5_iconsdir}/hicolor/*/mimetypes/application-x-uml.png
%{_kf5_sharedir}/umbrello5/

%files lang -f %{name}.lang

%changelog
