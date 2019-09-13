#
# spec file for package octave-forge-fits
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


%define octpkg  fits
Name:           octave-forge-%{octpkg}
Version:        1.0.7
Release:        0
Summary:        Octave functions for reading and writing FITS files
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
Url:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildRequires:  cfitsio-devel
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  octave-devel
BuildRequires:  pkg-config
Requires:       octave-cli >= 3.0.0

%description
Functions for reading and writing FITS (Flexible Image Transport System) files. 
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
sed -i -s -e 's/D_NINT/octave::math::x_nint/g' %{octpkg}-%{version}/src/*.cc
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
