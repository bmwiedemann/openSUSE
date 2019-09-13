#
# spec file for package octave-forge-bim
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define octpkg  bim
Name:           octave-forge-%{octpkg}
Version:        1.1.5
Release:        0
Summary:        PDE Solver using a Finite Element/Finite Volume approach
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
Url:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
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
%defattr(-,root,root)
%doc COPYING
%{octpackages_dir}/%{octpkg}-%{version}

%changelog
