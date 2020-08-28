#
# spec file for package ghc-turtle
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


%global pkg_name turtle
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.5.21
Release:        0
Summary:        Shell programming, Haskell-style
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-ansi-wl-pprint-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-clock-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-foldl-devel
BuildRequires:  ghc-hostname-devel
BuildRequires:  ghc-managed-devel
BuildRequires:  ghc-optional-args-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-system-fileio-devel
BuildRequires:  ghc-system-filepath-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-devel
%if %{with tests}
BuildRequires:  ghc-doctest-devel
%endif

%description
'turtle' is a reimplementation of the Unix command line environment in Haskell
so that you can use Haskell as both a shell and a scripting language.

Features include:

* Batteries included: Command an extended suite of predefined utilities

* Interoperability: You can still run external shell commands

* Portability: Works on Windows, OS X, and Linux

* Exception safety: Safely acquire and release resources

* Streaming: Transform or fold command output in constant space

* Patterns: Use typed regular expressions that can parse structured values

* Formatting: Type-safe 'printf'-style text formatting

* Modern: Supports 'text' and 'system-filepath'

Read "Turtle.Tutorial" for a detailed tutorial or "Turtle.Prelude" for a
quick-start guide

'turtle' is designed to be beginner-friendly, but as a result lacks certain
features, like tracing commands. If you feel comfortable using 'turtle' then
you should also check out the 'Shelly' library which provides similar
functionality.

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
%doc CHANGELOG.md

%changelog
