#
# spec file for package octave-forge-symbolic
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


%define octpkg  symbolic
Name:           octave-forge-%{octpkg}
Version:        3.2.1
Release:        0
Summary:        Octave Symbolic Package using SymPy
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gnu-octave.github.io/packages/%{octpkg}/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  octave-devel
BuildRequires:  python3-sympy >= 1.4
Requires:       octave-cli >= 5.1
Requires:       python3-sympy >= 1.4

%description
Adds symbolic calculation features to GNU Octave.
These include common Computer Algebra System tools such as algebraic
operations, calculus, equation solving, Fourier and Laplace transforms,
variable precision arithmetic and and other features. Compatibility
with other symbolic toolboxes is a goal.
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

%changelog
