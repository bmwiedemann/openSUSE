#
# spec file for package octave-forge-statistics
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define octpkg  datatypes
Name:           octave-forge-%{octpkg}
Version:        1.2.1
Release:        0
Summary:        Extra data types for GNU Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gnu-octave.github.io/packages/%{octpkg}/
Source0:        https://github.com/pr0m1th3as/datatypes/releases/download/release-%{version}/datatypes-%{version}.tar.gz#/%{octpkg}-%{version}.tar.gz
# https://github.com/pr0m1th3as/datatypes/issues/38
Patch0:         0001-Extend-keyHash-tests-to-cover-more-inputs.patch
Patch1:         0002-keyHash-Force-char-signedness-to-fix-architecture-de.patch
BuildRequires:  octave-devel
Requires:       octave-cli >= 9.1.0

%description
The datatypes package is a collection of classdef Classes for
providing extra data types not available in core Octave.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
pushd %{octpkg}-release-%{version}
%autopatch -p1
popd
%octave_pkg_src

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%global octskiptests %{octskiptests}
echo "Skip tests requiring graphical toolkit: %{octskiptests}"
%octave_pkg_test

%post
%octave --eval "pkg rebuild"

%postun
%octave --eval "pkg rebuild"

%files
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}

%changelog
