#
# spec file for package octave-forge-signal
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


%define octpkg  signal
Name:           octave-forge-%{octpkg}
Version:        1.4.0
Release:        0
Summary:        Signal processing tools for Octave
License:        GPL-3.0-or-later AND SUSE-Public-Domain
Group:          Productivity/Scientific/Math
Url:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  octave-devel
Requires:       octave-cli >= 3.8.0
Requires:       octave-forge-control >= 2.4.5

%description
Signal processing tools, including filtering, windowing and display functions.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
# gripes.h replaced by errwarn.h (deprecated in 4.2, removed in 4.6)
sed -i -s -e 's/gripes.h/errwarn.h/' -e 's/gripe_/err_/g' %{octpkg}-%{version}/src/*.cc
sed -i -s -e 's/NINT/octave::math::nint/g' %{octpkg}-%{version}/src/*.cc
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
