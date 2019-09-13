#
# spec file for package octave-forge-optim
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


%define octpkg  optim
Name:           octave-forge-%{octpkg}
Version:        1.6.0
Release:        0
Summary:        Non-linear optimization toolkit for Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
Url:            https://octave.sourceforge.io/optim/index.html
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildRequires:  blas-devel
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  lapack-devel
BuildRequires:  octave-devel
Requires:       octave-cli >= 3.6.0
Requires:       octave-forge-parallel >= 3.0.4
Requires:       octave-forge-statistics
Requires:       octave-forge-struct >= 1.0.12

%description
Non-linear optimization toolkit.
This is part of the Octave-Forge project.

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
