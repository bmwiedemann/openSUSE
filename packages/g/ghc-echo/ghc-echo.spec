#
# spec file for package ghc-echo
#
# Copyright (c) 2019 SUSE LLC
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


%global pkg_name echo
Name:           ghc-%{pkg_name}
Version:        0.1.3
Release:        0
Summary:        A cross-platform, cross-console way to handle echoing terminal input
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros

%description
The 'base' library exposes the 'hGetEcho' and 'hSetEcho' functions for querying
and setting echo status, but unfortunately, neither function works with MinTTY
consoles on Windows. This is a serious issue, since 'hGetEcho' and 'hSetEcho'
are often used to disable input echoing when a program prompts for a password,
so many programs will reveal your password as you type it on MinTTY!

This library provides an alternative interface which works with both MinTTY and
other consoles. An example is included which demonstrates how one might prompt
for a password using this library. To build it, make sure to configure with the
'-fexample' flag.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%setup -q -n %{pkg_name}-%{version}
cp -p %{SOURCE1} %{pkg_name}.cabal

%build
%ghc_lib_build

%install
%ghc_lib_install

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%changelog
