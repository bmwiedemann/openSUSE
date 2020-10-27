#
# spec file for package ghc-hsyslog
#
# Copyright (c) 2020 SUSE LLC
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


%global pkg_name hsyslog
Name:           ghc-%{pkg_name}
Version:        5.0.2
Release:        0
Summary:        FFI interface to syslog(3) from POSIX.1-2001
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros

%description
A Haskell interface to 'syslog(3)' as specified in
<http://pubs.opengroup.org/onlinepubs/9699919799/functions/syslog.html
POSIX.1-2008>. The entire public API lives in "System.Posix.Syslog".
There is a set of exposed modules available underneath that one, which contain
various implementation details that may be useful to other developers who want
to implement syslog-related functionality. /Users/ of 'syslog', however, do not
need them.

An example program that demonstrates how to use this library is available in
the <https://github.com/peti/hsyslog/blob/master/example/Main.hs examples>
directory of this package.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%autosetup -n %{pkg_name}-%{version}
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

%changelog
