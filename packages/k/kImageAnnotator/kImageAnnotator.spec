#
# spec file for package kImageAnnotator
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


%global qtver 0
%if "@BUILD_FLAVOR@" == ""
ExclusiveArch:  do_not_build
%endif
%if "@BUILD_FLAVOR@" == "qt5"
%global qtver 5
%endif
%if "@BUILD_FLAVOR@" == "qt6"
%global qtver 6
%endif

%define sover   0
%define libname libkImageAnnotator-Qt%{qtver}-%{sover}
%if %{qtver} == 0
Name:           kImageAnnotator
%else
Name:           kImageAnnotator-Qt%{qtver}
%endif
Version:        0.7.2
Release:        0
Summary:        Tool for annotating images
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/ksnip/kImageAnnotator
Source:         https://github.com/ksnip/kImageAnnotator/archive/v%{version}.tar.gz#/kImageAnnotator-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE
Patch0:         0001-Make-Qt5-and-Qt6-libraries-coinstallable-again.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt%{qtver}LinguistTools)
BuildRequires:  cmake(Qt%{qtver}Svg)
BuildRequires:  cmake(Qt%{qtver}Test)
BuildRequires:  cmake(Qt%{qtver}Widgets)
BuildRequires:  cmake(kColorPicker-Qt%{qtver})
BuildRequires:  pkgconfig(x11)

%description
kImageAnnotator is a tool for annotating images.

%package -n kImageAnnotator-lang
Summary:        Translations for package kImageAnnotator
Group:          System/Localization
BuildArch:      noarch

%description -n kImageAnnotator-lang
Provides translations for the "kImageAnnotator" package.

%package -n %{libname}
Summary:        Tool for annotating images
Group:          System/Libraries
# Used to be named kImageAnnotator-QtX-0
Provides:       kImageAnnotator-Qt%{qtver}-%{sover} = %{version}
Obsoletes:      kImageAnnotator-Qt%{qtver}-%{sover} < %{version}
Recommends:     kImageAnnotator-lang

%description -n %{libname}
kImageAnnotator is a tool for annotating images.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
%if %{qtver} == 5
Obsoletes:      kImageAnnotator-devel < %{version}
%endif

%description devel
Development files for %{name} including headers and libraries

%prep
%autosetup -p1 -n kImageAnnotator-%{version}

%build
%define opts -DBUILD_EXAMPLE=FALSE -DCMAKE_INSTALL_DATAROOTDIR="share"
%if %{qtver} == 6
    %cmake_qt6 -DBUILD_WITH_QT6=TRUE -DBUILD_SHARED_LIBS=TRUE %{opts}
    %qt6_build
%else
    %cmake %{opts}
    %cmake_build
%endif

%install
%if %{qtver} == 6
    %qt6_install
    rm -r %{buildroot}%{_datadir}/kImageAnnotator
%else
%cmake_install
# Both packages build and install the same locale files.
# Keep only the Qt 5 ones (for now).
%find_lang kImageAnnotator --with-qt
%endif

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSE
%{_libdir}/lib%{name}.so.%{sover}
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}
%{_includedir}/%{name}

%if %{qtver} == 5
%files -n kImageAnnotator-lang -f kImageAnnotator.lang
%dir %{_datadir}/kImageAnnotator
%dir %{_datadir}/kImageAnnotator/translations
%endif

%changelog
