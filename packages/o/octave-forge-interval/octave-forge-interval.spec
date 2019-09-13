#
# spec file for package octave-forge-interval
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define octpkg  interval
Name:           octave-forge-%{octpkg}
Version:        3.2.0
Release:        0
Summary:        Real-valued interval arithmetic for Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
Url:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  mpfr-devel >= 3.1.0
BuildRequires:  octave-devel
Requires:       octave-cli >= 3.8.2

%description
The interval package for real-valued interval arithmetic allows to
evaluate functions over subsets of their domain.  All results are verified,
because interval computations automatically keep track of any errors.

These concepts can be used to handle uncertainties, estimate arithmetic errors
and produce reliable results.  Also it can be applied to computer-assisted
proofs, constraint programming, and verified computing.

The implementation is based on interval boundaries represented by binary64
numbers and is conforming to IEEE Std 1788-2015, IEEE standard for interval
arithmetic.

This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%octave_pkg_src

%build
%octave_pkg_build

%install
%octave_pkg_install
# FIXME
# Remove documentation sources, building requires interval package installed
rm -r %{buildroot}%{octpackages_dir}/%{octpkg}-%{version}/doc

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
