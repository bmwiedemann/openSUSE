#
# spec file for package octave-forge-database
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


%define octpkg  database
Name:           octave-forge-%{octpkg}
Version:        2.4.3
Release:        0
Summary:        Octave plugin interfacing PostgreSQL
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
Url:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         add_missing_iostream_include.patch
# PATCH-FIX-OPENSUSE -- boo#1120035, pg_config is no longer in the postgresql-devel package, use pkg-config instead
Patch1:         0001-Use-pkg-config-instead-of-pg_config.patch
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  octave-devel
BuildRequires:  pkg-config
BuildRequires:  postgresql-devel >= 8.3
Requires:       octave-cli >= 3.6.2
Requires:       octave-forge-struct >= 1.0.12

%description
Interface to PostgreSQL databases.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%patch0 -p1
pushd %{octpkg}-%{version}
%patch1 -p1
popd
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
