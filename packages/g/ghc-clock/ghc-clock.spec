#
# spec file for package ghc-clock
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


%global pkg_name clock
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.8
Release:        0
Summary:        High-resolution clock functions: monotonic, realtime, cputime
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
%if %{with tests}
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
A package for convenient access to high-resolution clock and timer functions of
different operating systems via a unified API.

POSIX code and surface API was developed by Cetin Sert in 2009.

Windows code was contributed by Eugene Kirpichov in 2010.

FreeBSD code was contributed by Finn Espen Gundersen on 2013-10-14.

OS X code was contributed by Gerolf Seitz on 2013-10-15.

Derived 'Generic', 'Typeable' and other instances for 'Clock' and 'TimeSpec'
was contributed by Mathieu Boespflug on 2014-09-17.

Corrected dependency listing for 'GHC < 7.6' was contributed by Brian McKenna
on 2014-09-30.

Windows code corrected by Dimitri Sabadie on 2015-02-09.

Added 'timeSpecAsNanoSecs' as observed widely-used by Chris Done on 2015-01-06,
exported correctly on 2015-04-20.

Imported Control.Applicative operators correctly for Haskell Platform on
Windows on 2015-04-21.

Unit tests and instance fixes by Christian Burger on 2015-06-25.

Removal of fromInteger : Integer -> TimeSpec by Cetin Sert on 2015-12-15.

New Linux-specific Clocks: MonotonicRaw, Boottime, MonotonicCoarse,
RealtimeCoarse by Cetin Sert on 2015-12-15.

Reintroduction fromInteger : Integer -> TimeSpec by Cetin Sert on 2016-04-05.

Fixes for older Linux build failures introduced by new Linux-specific clocks by
Mario Longobardi on 2016-04-18.

Refreshment release in 2019-04 after numerous contributions.

[Version Scheme] Major-'/R/'-ewrite . New-'/F/'-unctionality .
'/I/'-mprovementAndBugFixes . '/P/'-ackagingOnly

* 'PackagingOnly' changes are made for quality assurance reasons.

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

%build
%ghc_lib_build

%install
%ghc_lib_install

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files

%changelog
