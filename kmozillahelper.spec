#
# spec file for package kmozillahelper
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


# this is needed to match this package with the main package without the main package
# having a hard requirement on this package
%define helper_version 6
Name:           kmozillahelper
Version:        5.0.6
Release:        0
Summary:        Helper for KDE Firefox Integration
License:        MIT
Group:          System/GUI/KDE
URL:            https://github.com/openSUSE/kmozillahelper
Source:         https://github.com/openSUSE/kmozillahelper/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5WindowSystem)
Requires:       mozilla-kde4-version = %{helper_version}
Supplements:    packageand(MozillaFirefox:plasma5-desktop)
Supplements:    packageand(MozillaThunderbird:plasma5-desktop)
# make sure the package is not installed when there is still
# a user of the old api version
Conflicts:      mozilla-kde4-version < %{helper_version}
# package rename
Provides:       mozilla-xulrunner191-kde4 = %{version}-%{release}
Obsoletes:      mozilla-xulrunner191-kde4 < %{version}-%{release}
# functionality integrated here
Obsoletes:      MozillaFirefox-kde4-addon <= 0.3.0
Provides:       MozillaFirefox-kde4-addon = 0.3.1
Provides:       mozilla-kde4-integration = %{version}
Obsoletes:      mozilla-kde4-integration < %{version}

%description
Package providing integration of Mozilla applications with KDE.

%prep
%setup -q

%build
version=$(grep '#define HELPER_VERSION' main.cpp | cut -d ' ' -f 3)
if test "$version" != %{helper_version}; then
    echo fix the version in the .spec file
    exit 1
fi
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

%files
%license LICENSE
%dir %{_prefix}/lib/mozilla
%{_prefix}/lib/mozilla/kmozillahelper
%{_datadir}/knotifications5/kmozillahelper.notifyrc

%changelog
