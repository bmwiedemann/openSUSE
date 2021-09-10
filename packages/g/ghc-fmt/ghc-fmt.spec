#
# spec file for package ghc-fmt
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


%global pkg_name fmt
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.6.3.0
Release:        0
Summary:        A new formatting library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-call-stack-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-formatting-devel
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-locale-compat-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-doctest-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-neat-interpolation-devel
BuildRequires:  ghc-vector-devel
%endif

%description
A new formatting library that tries to be simple to understand while still
being powerful and providing more convenience features than other libraries
(like functions for pretty-printing maps and lists, or a function for printing
arbitrary datatypes using generics).

A comparison with other libraries:

* 'printf' (from 'Text.Printf') takes a formatting string and uses some type
tricks to accept the rest of the arguments polyvariadically. It's very concise,
but there are some drawbacks – it can't produce 'Text' (you'd have to 'T.pack'
it every time) and it doesn't warn you at compile-time if you pass wrong
arguments or not enough of them.

* <https://hackage.haskell.org/package/text-format text-format> takes a
formatting string with curly braces denoting places where arguments would be
substituted (the arguments themselves are provided via a tuple). If you want to
apply formatting to some of the arguments, you have to use one of the provided
formatters. Like 'printf', it can fail at runtime, but at least the formatters
are first-class (and you can add new ones).

* <https://hackage.haskell.org/package/formatting formatting> takes a
formatting template consisting of pieces of strings interleaved with
formatters; this ensures that arguments always match their placeholders.
'formatting' provides lots of formatters and generally seems to be the most
popular formatting library here. Unfortunately, at least in my experience
writing new formatters can be awkward and people sometimes have troubles
understanding how 'formatting' works.

* <https://hackage.haskell.org/package/fmt fmt> (i.e. this library) provides
formatters that are ordinary functions, and a bunch of operators for
concatenating formatted strings; those operators also do automatic conversion.
There are some convenience formatters which aren't present in 'formatting'
(like ones for formatting maps, lists, converting to base64, etc).
Some find the operator syntax annoying, while others like it.

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
