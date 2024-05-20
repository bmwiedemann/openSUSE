#
# spec file for package syntax-highlighting
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


%define lname   libKF5SyntaxHighlighting5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           syntax-highlighting
Version:        5.116.0
Release:        0
Summary:        Syntax highlighting engine and library
License:        LGPL-2.1-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND MIT AND BSD-3-Clause AND Artistic-1.0
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt5_version}
BuildRequires:  cmake(Qt5Network) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5XmlPatterns) >= %{qt5_version}

%description
This is a tier1/functional version of the Kate syntax highlighting engine.
It's not tied to a particular output format or editor engine.

%package imports
Summary:        QML components for syntax-highlighting
Requires:       %{lname} = %{version}

%description imports
This package contains QML imports for syntax-highlighting.

%package -n %{lname}
Summary:        Syntax highlighting engine and library
Recommends:     %{name} = %{version}

%description -n %{lname}
This is a tier1/functional version of the Kate syntax highlighting engine.
It's not tied to a particular output format or editor engine.

%package devel
Summary:        Syntax highlighting engine and library
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5Core) >= %{qt5_version}
Requires:       cmake(Qt5Gui) >= %{qt5_version}

%description devel
This is a tier1/functional version of the Kate syntax highlighting engine.
It's not tied to a particular output format or editor engine.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang  syntaxhighlighting5 --with-qt --without-mo

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}-lang -f syntaxhighlighting5.lang

%files
%{_kf5_debugdir}/ksyntaxhighlighting.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_bindir}/kate-syntax-highlighter

%files imports
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/syntaxhighlighting/

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5SyntaxHighlighting.so.*

%files devel
%{_kf5_libdir}/libKF5SyntaxHighlighting.so
%{_kf5_libdir}/cmake/KF5SyntaxHighlighting/
%{_kf5_mkspecsdir}/qt_KSyntaxHighlighting.pri
%{_kf5_includedir}/

%changelog
