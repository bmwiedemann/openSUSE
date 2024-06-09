#
# spec file for package kf6-syntax-highlighting
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


%define qt6_version 6.6.0

%define rname syntax-highlighting
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-syntax-highlighting
Version:        6.3.0
Release:        0
Summary:        Syntax highlighting engine and library
License:        LGPL-2.1-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND MIT AND BSD-3-Clause AND Artistic-1.0
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(xerces-c)

%description
This is a tier1/functional version of the Kate syntax highlighting engine.
It's not tied to a particular output format or editor engine.

%package imports
Summary:        QML components for syntax-highlighting
Requires:       libKF6SyntaxHighlighting6 = %{version}

%description imports
This package contains QML imports for syntax-highlighting.

%package -n libKF6SyntaxHighlighting6
Summary:        Syntax highlighting engine and library
Recommends:     kf6-syntax-highlighting = %{version}

%description -n libKF6SyntaxHighlighting6
This is a tier1/functional version of the Kate syntax highlighting engine.
It's not tied to a particular output format or editor engine.

%package devel
Summary:        Syntax highlighting engine and library
Requires:       kf6-extra-cmake-modules
Requires:       libKF6SyntaxHighlighting6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}

%description devel
This is a tier1/functional version of the Kate syntax highlighting engine.
It's not tied to a particular output format or editor engine.

%lang_package -n libKF6SyntaxHighlighting6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang syntaxhighlighting6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6SyntaxHighlighting6

%files -n libKF6SyntaxHighlighting6-lang -f syntaxhighlighting6.lang

%files
%{_kf6_bindir}/ksyntaxhighlighter6
%{_kf6_debugdir}/ksyntaxhighlighting.categories
%{_kf6_debugdir}/ksyntaxhighlighting.renamecategories

%files imports
%{_kf6_qmldir}/org/kde/syntaxhighlighting/

%files -n libKF6SyntaxHighlighting6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6SyntaxHighlighting.so.*

%files devel
%doc %{_kf6_qchdir}/KF6SyntaxHighlighting.*
%{_kf6_cmakedir}/KF6SyntaxHighlighting/
%{_kf6_includedir}/KSyntaxHighlighting/
%{_kf6_libdir}/libKF6SyntaxHighlighting.so

%changelog
