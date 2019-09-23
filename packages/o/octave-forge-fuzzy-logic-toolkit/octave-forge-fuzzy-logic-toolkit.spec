#
# spec file for package octave-forge-fuzzy-logic-toolkit
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


%define octpkg  fuzzy-logic-toolkit
Name:           octave-forge-%{octpkg}
Version:        0.4.5
Release:        0
Summary:        Fuzzy logic toolkit for Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
Url:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://sourceforge.net/p/octave/fuzzy-logic-toolkit/ci/00e05af94b3762d2e051ad28fb436da089160f40/
Patch0:         inst-defuz.m-update-anonymous-funtion.diff
BuildArch:      noarch
BuildRequires:  octave-devel
Requires:       octave-cli >= 3.2.4

%description
A mostly MATLAB-compatible fuzzy logic toolkit.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%patch0 -p1
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
