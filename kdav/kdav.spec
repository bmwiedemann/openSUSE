#
# spec file for package kdav
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


%bcond_without  lang
Name:           kdav
Version:        19.08.0
Release:        0
Summary:        DAV protocol implementation
License:        GPL-2.0-only
Group:          Productivity/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5XmlPatterns)
Recommends:     %{name}-lang

%description
kdav is a library providing a KJob-based implementation of DAV protocols such as
CardDAV, WebDAV, and CalDAV.

%package -n libKPimKDAV5
Summary:        Core library for kdav
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libKPimKDAV5
kdav is a library providing a KJob-based implementation of DAV protocols such as
CardDAV, WebDAV, and CalDAV.

%package devel
Summary:        Development package for kdav
Group:          Development/Libraries/KDE
Requires:       libKPimKDAV5 = %{version}

%description devel
This package contains development files needed to use kdav in other applications.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKPimKDAV5 -p /sbin/ldconfig
%postun -n libKPimKDAV5 -p /sbin/ldconfig

%files
%license COPYING
%doc README
%{_kf5_debugdir}/kdav.categories

%files -n libKPimKDAV5
%license COPYING
%doc README
%{_kf5_libdir}/libKPimKDAV.so.*

%files devel
%license COPYING
%doc README
%{_includedir}/KPim/
%{_kf5_libdir}/cmake/KPimKDAV/
%{_kf5_libdir}/libKPimKDAV.so
%{_kf5_mkspecsdir}/qt_kdav.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
