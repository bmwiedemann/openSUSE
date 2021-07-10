#
# spec file for package octave-forge-geometry
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


%define octpkg  geometry
Name:           octave-forge-%{octpkg}
Version:        4.0.0
Release:        0
Summary:        Computational Geometry for Octave
License:        GPL-3.0-or-later AND BSD-2-Clause
Group:          Productivity/Scientific/Math
URL:            https://octave.sourceforge.io/%{octpkg}/index.html
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         compile-with-g++-v11.patch
BuildRequires:  octave-devel >= 4.2.0
Requires:       octave-cli >= 4.0.1
Requires:       octave-forge-matgeom >= 1.0.0

%description
Library for geometric computing extending MatGeom functions.
Useful to create, transform, manipulate and display geometric
primitives.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
pushd %{octpkg}-%{version}
%patch0 -p1
popd
%octave_pkg_src

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_test

%post
%octave --eval "pkg rebuild"

%postun
%octave --eval "pkg rebuild"

%files
%defattr(-,root,root)
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}

%changelog
