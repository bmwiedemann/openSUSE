#
# spec file for package octave-forge-quaternion
#
# Copyright (c) 2021 SUSE LLC
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


%define octpkg  quaternion
Name:           octave-forge-%{octpkg}
Version:        2.4.0
Release:        0
Summary:        Quaternion class with overloaded operators for Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://octave.sourceforge.io/quaternion/index.html
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 0001-Fix-build-with-Octave-5.1.patch -- based on PR 1
Patch0:         0001-Fix-build-with-Octave-5.1.patch
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  octave-devel
Requires:       octave-cli >= 3.8.0

%description
Quaternion class with overloaded operators.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%patch0
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
