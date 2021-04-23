#
# spec file for package skanlite
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


Name:           skanlite
Version:        2.2.0
Release:        0
Summary:        Image Scanner Application
License:        LGPL-2.1-or-later
Group:          Hardware/Scanner
URL:            https://apps.kde.org/skanlite
Source0:        https://download.kde.org/stable/%{name}/2.2/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         Fix-compilation-with-Qt-before-5.14.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  libpng-devel
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Sane) >= 5.55.0
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     %{name}-lang = %{version}
Obsoletes:      %{name}-doc < %{version}

%description
Skanlite is an image scanner application by KDE.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --all-name
%{kf5_find_htmldocs}

# Fix rpmlint warning "script-without-shebang"
chmod 644 %{buildroot}%{_kf5_applicationsdir}/org.kde.skanlite.desktop

%files
%license src/COPYING
%doc src/TODO
%doc %lang(en) %{_kf5_htmldir}/en/skanlite
%{_kf5_applicationsdir}/org.kde.skanlite.desktop
%{_kf5_appstreamdir}/org.kde.skanlite.appdata.xml
%{_kf5_bindir}/skanlite

%files lang -f %{name}.lang

%changelog
