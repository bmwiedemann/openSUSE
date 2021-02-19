#
# spec file for package kseexpr
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


%define sover 4_0_1_0
%if %pkg_vcmp extra-cmake-modules >= 5.64
%bcond_without lang
%else
%bcond_with lang
%endif
Name:           kseexpr
Version:        4.0.1.0
Release:        0
Summary:        The embeddable expression engine fork for Krita
License:        GPL-3.0-or-later AND Apache-2.0 AND BSD-3-Clause AND MIT
Group:          Productivity/Graphics/Other
URL:            https://invent.kde.org/graphics/kseexpr/
Source0:        https://download.kde.org/stable/%{name}/4.0.1/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         Fix-translation-lookup-in-stock-Linux-deployments.patch
# PATCH-FIX-OPENSUSE
Patch1:         Fix-possible-compiler-error.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Widgets)

%description
This is the fork of Disney Animation's SeExpr expression
library (https://wdas.github.io/SeExpr), that is used in Krita.

SeExpr is an embeddable, arithmetic expression language
that enables flexible artistic control and customization
in creating computer graphics images. Example uses
include procedural geometry synthesis, image synthesis,
simulation control, crowd animation, and geometry deformation.

%package -n libKSeExpr%{sover}
Summary:        %{name} libraries
Group:          System/Libraries
# for the lang package to be installable
Provides:       %{name} = %{version}

%description  -n libKSeExpr%{sover}
Runtime libraries for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libKSeExpr%{sover} = %{version}

%description devel
Development headers and libraries for %{name}.

%lang_package

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%if %{with lang}
%find_lang seexpr2 %{name}.lang --with-qt
%endif

%post -n libKSeExpr%{sover} -p /sbin/ldconfig
%postun -n libKSeExpr%{sover} -p /sbin/ldconfig

%files -n libKSeExpr%{sover}
%license LICENSES/*
%{_libdir}/libKSeExpr.so.%{version}
%{_libdir}/libKSeExprUI.so.%{version}

%files devel
%{_datadir}/cmake/KSeExpr/
%{_datadir}/pkgconfig/kseexpr.pc
%{_includedir}/KSeExpr/
%{_includedir}/KSeExprUI/
%{_libdir}/libKSeExpr.so
%{_libdir}/libKSeExprUI.so

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
