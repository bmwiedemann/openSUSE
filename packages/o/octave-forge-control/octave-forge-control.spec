#
# spec file for package octave-forge-control
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define octpkg  control
Name:           octave-forge-%{octpkg}
Version:        3.0.0
Release:        0
Summary:        Computer-Aided Control System Design (CACSD) Tools
License:        GPL-3.0+
Group:          Productivity/Scientific/Math
Url:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM control-gcc-errors.patch -- Fix no return in non-void function
Patch1:         control-gcc-errors.patch
BuildRequires:  blas-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hdf5-devel
BuildRequires:  lapack-devel
BuildRequires:  octave-devel
Requires:       octave-cli >= 3.8.0

%description
Computer-Aided Control System Design (CACSD) Tools for GNU Octave, based
on the proven SLICOT Library.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%patch1 -p1
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
