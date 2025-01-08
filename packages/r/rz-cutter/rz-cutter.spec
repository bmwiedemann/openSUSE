#
# spec file for package rz-cutter
#
# Copyright (c) 2025 SUSE LLC
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


Name:           rz-cutter
Version:        2.3.4
Release:        0
Summary:        GUI for Rizin reverse engineering framework
License:        GPL-3.0-only
URL:            https://github.com/rizinorg/cutter
Source0:        https://github.com/rizinorg/cutter/releases/download/v%{version}/Cutter-v%{version}-src.tar.gz
# FIX-UPSTREAM, https://github.com/rizinorg/cutter/commit/93a06f5edd6fe5d6dc74eab564b93b9b0968c6f8
Patch0:         Fix-build-failure-against-PySide-6.8.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(Clang)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(PySide6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Rizin)
BuildRequires:  cmake(Shiboken6)
BuildRequires:  pkgconfig(libgvc)
BuildRequires:  pkgconfig(python3)

%description
Cutter is a Qt and C++ GUI for Rizin. Its goal is making an advanced,
customizable and FOSS reverse-engineering platform while keeping the user
experience at mind. Cutter is created by reverse engineers for reverse
engineers.

%package devel
Summary:        Development files for the cutter-re package
Requires:       %{name} = %{version}

%description devel
Development files for the cutter-re package. See cutter-re package for more
information.

%prep
%autosetup -p1 -n Cutter-v%{version}

%build
%cmake \
	-DCUTTER_USE_BUNDLED_RIZIN=OFF \
	-DCUTTER_ENABLE_PYTHON=ON \
	-DCUTTER_ENABLE_PYTHON_BINDINGS=ON \
	-DCUTTER_ENABLE_GRAPHVIZ=ON \
	-DCUTTER_QT6=ON
%cmake_build

%install
%cmake_install

%check

%files
%license COPYING src/img/icons/Iconic-LICENSE
%doc README.md
%{_bindir}/cutter
%{_datadir}/applications/re.rizin.cutter.desktop
%{_datadir}/icons/hicolor/scalable/apps/cutter.svg
%dir %{_datadir}/rizin/cutter
%dir %{_datadir}/rizin/cutter/translations
%{_datadir}/rizin/cutter/translations/*.qm

%files devel
%{_includedir}/cutter
%dir %{_libdir}/cmake/Cutter
%{_libdir}/cmake/Cutter/*.cmake

%changelog
