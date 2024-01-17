#
# spec file for package jsonnet
#
# Copyright (c) 2023 SUSE LLC
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


%global gitsha 5f8d7fd191ba22ff2b60c1106d7135bb9a335533
Name:           gl3w
Version:        2022.03.24
Release:        0
Summary:        OpenGL core profile loading
License:        Unlicense
URL:            https://github.com/skaslev/gl3w
Source:         https://github.com/skaslev/gl3w/archive/%{gitsha}.zip
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  unzip
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(glu)

%description
gl3w is a way to get at functionality offered by the
OpenGL core profile specification.

%package devel
Summary:        Header files for gl3w

%description devel
gl3w is a way to get at functionality offered by the
OpenGL core profile specification.

This package contains header files for gl3w.

%prep
%autosetup -n gl3w-%{gitsha}

%build
%cmake
mkdir -p include/{GL,KHR}
cp -p /usr/include/GL/glcorearb.h include/GL/glcorearb.h
cp -p /usr/include/KHR/khrplatform.h include/KHR/khrplatform.h
%cmake_build

%install
%cmake_install

%files devel
%license UNLICENSE
%{_includedir}/gl3w
%{_datadir}/gl3w

%changelog
