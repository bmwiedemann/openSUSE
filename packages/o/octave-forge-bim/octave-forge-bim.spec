#
# spec file for package octave-forge-bim
#
# Copyright (c) 2022 SUSE LLC
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


%define octpkg  bim
Name:           octave-forge-%{octpkg}
Version:        1.1.6
Release:        0
Summary:        PDE Solver using a Finite Element/Finite Volume approach
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gnu-octave.github.io/packages/%{octpkg}/
Source0:        https://github.com/carlodefalco/bim/archive/refs/tags/v%{version}.tar.gz#/%{octpkg}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  octave-devel
Requires:       octave-cli >= 3.8.0
Requires:       octave-forge-fpl
Requires:       octave-forge-msh

%description
Package for solving Diffusion Advection Reaction (DAR) Partial Differential Equations.
This is part of the Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%octave_pkg_src
cp %{octpkg}-%{version}/COPYING .

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
%license COPYING
%{octpackages_dir}/%{octpkg}-%{version}

%changelog
