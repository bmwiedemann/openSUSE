#
# spec file for package ghc-cmdargs
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


%global pkg_name cmdargs
Name:           ghc-%{pkg_name}
Version:        0.10.20
Release:        0
Summary:        Command line argument processing
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-transformers-devel

%description
This library provides an easy way to define command line parsers. Most users
will want to use the "System.Console.CmdArgs.Implicit" module, whose
documentation contains an example.

* "System.Console.CmdArgs.Explicit" provides a way to write command line
parsers for both single mode programs (most programs) and multiple mode
programs (e.g. darcs or cabal). Parsers are defined by constructing a data
structure.

* "System.Console.CmdArgs.Implicit" provides a way to concisely define command
line parsers, up to three times shorter than getopt. These parsers are
translated into the Explicit data type.

* "System.Console.CmdArgs.GetOpt" provides a wrapper allowing compatiblity with
existing getopt parsers, mapping to the Explicit data type.

For a general reference on what command line flags are commonly used, see
<http://www.faqs.org/docs/artu/ch10s05.html>.

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

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGES.txt README.md

%changelog
