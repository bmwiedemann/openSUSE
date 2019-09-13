#
# spec file for package octave-forge-generate_html
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


%define octpkg  generate_html
Name:           octave-forge-%{octpkg}
Version:        0.3.1
Release:        0
Summary:        Generate HTML web page from help texts
License:        GPL-3.0+
Group:          Productivity/Scientific/Math
Url:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  octave-devel
Requires:       makeinfo
Requires:       octave-cli >= 3.2.0

%description
This package provides functions for generating HTML pages that contain
the help texts for a set of functions. The package is designed to be
as general as possible, but also contains convenience functions for
generating a set of pages for entire packages.
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
%defattr(-,root,root)
%{octpackages_dir}/%{octpkg}-%{version}

%changelog
