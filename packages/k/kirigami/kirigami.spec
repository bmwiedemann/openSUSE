#
# spec file for package kirigami
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_without lang
Name:           kirigami
Version:        1.1.0
Release:        0
Summary:        Set of QtQuick components
License:        LGPL-2.1+
Group:          Development/Libraries/KDE
Url:            http://www.kde.org/
Source:         http://download.kde.org/stable/kirigami/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= 0.0.8
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(Qt5Core) >= 5.5.0
BuildRequires:  cmake(Qt5Gui) >= 5.5.0
BuildRequires:  cmake(Qt5Quick) >= 5.5.0
BuildRequires:  cmake(Qt5Svg) >= 5.5.0
BuildRequires:  cmake(Qt5Test) >= 5.5.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{with lang}
BuildRequires:  cmake(Qt5LinguistTools) >= 5.5.0
%endif
%if %{with lang}
Recommends:     %{name}-lang = %{version}
%endif

%description
QtQuick plugins to build user interfaces based on the KDE UX guidelines.

%package devel
Summary:        Development package for kirigami
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}

%description devel
QtQuick plugins to build user interfaces based on the KDE UX guidelines.
Development files.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

%if %{with lang}
%find_lang libkirigamiplugin --with-qt --without-mo
%endif

%if %{with lang}
%files lang -f libkirigamiplugin.lang
%endif

%files
%defattr(-,root,root,-)
%doc LICENSE*
%{_kf5_qmldir}/

%files devel
%defattr(-,root,root)
%{_kf5_libdir}/cmake/KF5Kirigami/
%{_kf5_mkspecsdir}/qt_Kirigami.pri

%changelog
