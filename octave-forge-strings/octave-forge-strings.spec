#
# spec file for package octave-forge-strings
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


%define octpkg  strings
Name:           octave-forge-%{octpkg}
Version:        1.2.0
Release:        0
Summary:        Additional manipulation functions for Octave
License:        GPL-3.0-or-later AND BSD-2-Clause
Group:          Productivity/Scientific/Math
Url:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  octave-devel
BuildRequires:  pcre-devel
Requires:       octave-cli >= 3.8.0

%description
Additional manipulation functions.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
# gripes.h replaced by errwarn.h (deprecated in 4.2, removed in 4.6)
sed -i -s -e 's/gripes.h/errwarn.h/' -e 's/gripe_/err_/g' %{octpkg}-%{version}/src/*.cc
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
