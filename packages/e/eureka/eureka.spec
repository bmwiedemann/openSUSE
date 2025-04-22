#
# spec file for package eureka
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

Name:           eureka
Version:        2.0.2
Release:        0
Summary:        A map editor for Doom engine games
License:        GPL-2.0-or-later
URL:            https://eureka-editor.sourceforge.net/
Source:         eureka-editor-%{version}.tar.gz
# Both of these patches are from upstream and can be removed with the next version.
Patch0:         cmake-duplicate-cxxflags-fix.patch
Patch1:         check-system-return-value.patch
BuildRequires:  cmake >= 3.13
# Leap 15 requires a newer GCC to fix a bunch of std::optional-related errors
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  fltk-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)

%description
Eureka is a map editor for the classic DOOM games, and a few related games such as Heretic and Hexen.

%prep
%autosetup -p1 -n eureka-editor-%{version}

%build
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif

# Eureka wants to clone googletest via git, but build environments don't have internet access,
# and trying to force it to use the system gtest requires more patches and ends up causing more problems...
%cmake -DENABLE_UNIT_TESTS=OFF
%cmake_build

%install
%cmake_install

install -Dpm 0644 misc/eureka.desktop %{buildroot}%{_datadir}/applications/eureka.desktop
install -Dpm 0644 misc/eureka.xpm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/eureka.xpm

%files
%license GPL.txt
%doc README.txt
%{_bindir}/eureka
%dir %{_datadir}/eureka
%{_datadir}/eureka/*
%{_datadir}/applications/eureka.desktop
%{_datadir}/icons/hicolor/32x32/apps/eureka.xpm

%changelog

