#
# spec file for package octave-forge-linear-algebra
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


%define octpkg  linear-algebra
Name:           octave-forge-%{octpkg}
Version:        2.2.2
Release:        0
Summary:        Linear algebra package for Octave
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND BSD-2-Clause
Group:          Productivity/Scientific/Math
Url:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://sourceforge.net/p/octave/linear-algebra/ci/6f1b92de265128e5408f26067192bce213786754/
Patch0:         0001-CmplxGSVD-dbleGSVD-replace-include-config.h-with-oct.patch
# PATCH-FIX-UPSTREAM https://sourceforge.net/p/octave/linear-algebra/ci/6e1dfc22132a1a5701498c815e57fcab4a97c165/
Patch1:         0002-Remove-autotools-cruft-from-the-very-old-times-of-Oc.patch
BuildRequires:  blas-devel
BuildRequires:  gcc-c++
BuildRequires:  lapack-devel
BuildRequires:  octave-devel
Requires:       octave-cli >= 4.0.0

%description
Additional linear algebra code, including general SVD and matrix functions.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%patch0 -p1
%patch1 -p1
# remove generated file from the tarball
rm %{octpkg}/src/configure
# gripes.h replaced by errwarn.h (deprecated in 4.2, removed in 4.6)
sed -i -s -e 's/gripes.h/errwarn.h/' -e 's/gripe_/err_/g' %{octpkg}/src/*.cc
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
