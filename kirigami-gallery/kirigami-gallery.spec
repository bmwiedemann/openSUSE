#
# spec file for package kirigami-gallery
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


%bcond_without lang
Name:           kirigami-gallery
Version:        19.08.1
Release:        0
Summary:        Gallery application built using Kirigami
License:        LGPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
Requires:       kirigami2
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols2
Recommends:     %{name}-lang

%description
Example application which uses all features from kirigami,
including links to the sourcecode, tips on how to use the
components and links to the corresponding HIG pages and
code examples on cgit

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%suse_update_desktop_file -G "Kirigami Gallery" org.kde.kirigami2.gallery GUIDesigner

%if %{with lang}
%find_lang kirigamigallery %{name}.lang --with-qt
%endif

%files
%license LICENSE.LGPL-2
%{_kf5_bindir}/kirigami2gallery
%{_kf5_applicationsdir}/org.kde.kirigami2.gallery.desktop

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
