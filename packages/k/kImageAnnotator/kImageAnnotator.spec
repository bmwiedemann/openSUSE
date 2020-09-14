#
# spec file for package kImageAnnotator
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


%define sover   0_3_2
%define libname libkImageAnnotator%{sover}
Name:           kImageAnnotator
Version:        0.3.2
Release:        0
Summary:        Tool for annotating images
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/ksnip/kImageAnnotator
Source:         https://github.com/ksnip/kImageAnnotator/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- Mark private link targets as such
Patch0:         0001-Make-link-against-X11-private.patch
Patch1:         0002-Make-kcolorpicker-link-private.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kColorPicker-devel >= 0.1.4
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(x11)
%lang_package

%description
kImageAnnotator is a tool for annotating images.

%package -n %{libname}
Summary:        Tool for annotating images
Group:          System/Libraries

%description -n %{libname}
kImageAnnotator is a tool for annotating images.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Development files for %{name} including headers and libraries

%prep
%autosetup -p1

%build
%cmake \
    -DBUILD_EXAMPLE=ON \
    -DCMAKE_INSTALL_DATAROOTDIR="share"

%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license LICENSE
%doc CHANGELOG.md README.md

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}
%{_includedir}/%{name}

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations

%changelog
