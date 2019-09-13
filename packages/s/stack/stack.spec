#
# spec file for package stack
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


%global pkg_name stack
%bcond_with tests
Name:           %{pkg_name}
Version:        2.1.3.1
Release:        0
Summary:        The Haskell Tool Stack
License:        BSD-3-Clause
Group:          Development/Libraries/Haskell
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch01:        enable-undecidable-instances-extension.patch
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-annotated-wl-pprint-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-colour-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptonite-conduit-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-echo-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filelock-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-fsnotify-devel
BuildRequires:  ghc-generic-deriving-devel
BuildRequires:  ghc-hackage-security-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hi-file-parser-devel
BuildRequires:  ghc-hpack-devel
BuildRequires:  ghc-hpc-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-download-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-mintty-devel
BuildRequires:  ghc-mono-traversable-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mustache-devel
BuildRequires:  ghc-neat-interpolation-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-open-browser-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-pantry-devel
BuildRequires:  ghc-path-devel
BuildRequires:  ghc-path-io-devel
BuildRequires:  ghc-persistent-devel
BuildRequires:  ghc-persistent-sqlite-devel
BuildRequires:  ghc-persistent-template-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-project-template-devel
BuildRequires:  ghc-regex-applicative-text-devel
BuildRequires:  ghc-resource-pool-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-retry-devel
BuildRequires:  ghc-rio-devel
BuildRequires:  ghc-rio-prettyprint-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-tar-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-terminal-size-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-metrics-devel
BuildRequires:  ghc-th-reify-many-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-tls-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-typed-process-devel
BuildRequires:  ghc-unicode-transforms-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-yaml-devel
BuildRequires:  ghc-zip-archive-devel
BuildRequires:  ghc-zlib-devel
Suggests:       docker
Suggests:       gcc
Suggests:       gmp-devel
Suggests:       make
Suggests:       tar
Suggests:       xz
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-raw-strings-qq-devel
BuildRequires:  ghc-smallcheck-devel
%endif

%description
Stack is a cross-platform program for developing Haskell projects. It is aimed
at Haskellers both new and experienced. It features:

* Installing GHC automatically, in an isolated location.
* Installing packages needed for your project.
* Building your project.
* Testing your project.
* Benchmarking your project.

Please see the documentation at <https://docs.haskellstack.org> for further
information.

%package -n ghc-%{name}
Summary:        Haskell %{name} library
Group:          System/Libraries

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Group:          Development/Libraries/Haskell
Requires:       ghc-%{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

%prep
%setup -q
%patch01 -p1

%build
%define cabal_configure_options -fdisable-git-info -fhide-dependency-versions -fsupported-build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}

%check
%cabal_test

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license LICENSE
%doc ChangeLog.md README.md doc
%{_bindir}/%{name}

%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc ChangeLog.md README.md doc

%changelog
