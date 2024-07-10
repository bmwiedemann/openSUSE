#
# spec file for package fortune
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


%define CookieDir share/fortune

Name:           fortune
Version:        2.10.0
Release:        0
Summary:        Random Saying
License:        BSD-4-Clause
Group:          Amusements/Toys/Other
URL:            ftp://sunsite.unc.edu/pub/Linux/games/amusements/fortune/
Source:         https://github.com/shlomif/fortune-mod/archive/fortune-mod-%{version}.tar.gz
Patch0:         fortune-no-games.patch
Patch1:         fortune-avoid-rinutils.patch
BuildRequires:  cmake >= 3
BuildRequires:  gcc-c++
BuildRequires:  recode-devel
BuildRequires:  shlomif-cmake-modules

%description
Fortune displays a random text string from a set of files in a certain
format.

This occurs each time you start a login shell. To get this feature just
uncomment the respective lines in the user's .profile.

%prep
%autosetup -p1 -n %{name}-mod-%{name}-mod-%{version}/fortune-mod

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README Notes
%{_mandir}/man1/*
%{_mandir}/man6/*
%{_datadir}/fortune
%{_bindir}/*

%changelog
