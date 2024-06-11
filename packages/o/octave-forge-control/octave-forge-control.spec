#
# spec file for package octave-forge-control
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


%define octpkg  control
Name:           octave-forge-%{octpkg}
Version:        4.0.1
Release:        0
Summary:        Computer-Aided Control System Design (CACSD) Tools
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gnu-octave.github.io/packages/%{octpkg}/
Source0:        https://github.com/gnu-octave/pkg-control/releases/download/%{octpkg}-%{version}/%{octpkg}-%{version}.tar.gz
BuildRequires:  blas-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hdf5-devel
BuildRequires:  lapack-devel
BuildRequires:  octave-devel
Requires:       octave-cli >= 4.0.0

%description
Computer-Aided Control System Design (CACSD) Tools for GNU Octave, based
on the proven SLICOT Library.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
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
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}

%changelog
