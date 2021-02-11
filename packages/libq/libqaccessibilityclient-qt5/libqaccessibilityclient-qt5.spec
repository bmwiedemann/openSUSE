#
# spec file for package libqaccessibilityclient-qt5
#
# Copyright (c) 2021 SUSE LLC
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
%global sover 0
%global lname libqaccessibilityclient-qt5-%{sover}
Name:           libqaccessibilityclient-qt5
Version:        0.4.1
Release:        0
Summary:        Accessibilty tools helper library, used e.g. by screen readers
License:        LGPL-2.1-only OR LGPL-3.0-only
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/libqaccessibilityclient/libqaccessibilityclient-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/libqaccessibilityclient/libqaccessibilityclient-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5Core) >= 5.6.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

%description
This library is used when writing accessibility clients such as screen readers.
It comes with some examples demonstrating the API. These small helpers may be
useful when testing accessibility. One of them writes all accessibiliy
interfaces an application provides as text output. The other, more advanced
application shows a tree of objects and allows some interaction and
exploration.
	
%package -n %{lname}
Summary:        Accessibilty tools helper library, used e.g. by screen readers
Group:          System/Libraries

%description -n %{lname}
This library is used when writing accessibility clients such as screen readers.
It comes with some examples demonstrating the API. These small helpers may be
useful when testing accessibility. One of them writes all accessibiliy
interfaces an application provides as text output. The other, more advanced
application shows a tree of objects and allows some interaction and
exploration.

%package devel
Summary:        Accessibilty tools helper library, used e.g. by screen readers
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Core) >= 5.6.0
# Not coinstallable with other -devel versions
Conflicts:      cmake(QAccessibilityClient)

%description devel
This library is used when writing accessibility clients such as screen readers.
It comes with some examples demonstrating the API. These small helpers may be
useful when testing accessibility. One of them writes all accessibiliy
interfaces an application provides as text output. The other, more advanced
application shows a tree of objects and allows some interaction and
exploration.

%prep
%autosetup -p1 -n libqaccessibilityclient-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON
  %cmake_build

%install
  %kf5_makeinstall -C build
  # Unlike accessibleapps, not that useful for debugging
  rm %{buildroot}%{_kf5_bindir}/dumper
  %fdupes %{buildroot}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%{_kf5_libdir}/libqaccessibilityclient-qt5.so.%{sover}
%{_kf5_libdir}/libqaccessibilityclient-qt5.so.%{version}

%files devel
%doc README.md
%{_kf5_bindir}/accessibleapps
%{_kf5_libdir}/libqaccessibilityclient-qt5.so
%{_kf5_libdir}/cmake/QAccessibilityClient/
%{_includedir}/qaccessibilityclient/

%changelog
