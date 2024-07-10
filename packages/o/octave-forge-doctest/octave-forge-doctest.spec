#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%define octpkg  doctest
Name:           octave-forge-%{octpkg}
Version:        0.8.0
Release:        0
Summary:        Octave-Forge documentation tests
License:        BSD-3-Clause AND GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://octave.sourceforge.io
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  octave-devel >= 4.2.0
Requires:       octave-cli >= 4.2.0
BuildArch:      noarch

%description
The Octave-Forge Doctest package finds specially-formatted blocks of example
code within documentation files. It then executes the code and confirms
the output is correct. This can be useful as part of a testing framework
or simply to ensure that documentation stays up-to-date during software development.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%octave_pkg_src

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
tar -zxvf %{octpkg}-%{version}.tar.gz
%octave_pkg_test

%post
%octave --eval "pkg rebuild"

%postun
%octave --eval "pkg rebuild"

%files
%defattr(-,root,root)
%{octpackages_dir}/%{octpkg}-%{version}

%changelog
