#
# spec file for package ghc-esqueleto
#
# Copyright (c) 2025 SUSE LLC
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


%global pkg_name esqueleto
%global pkgver %{pkg_name}-%{version}
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        3.6.0.0
Release:        0
Summary:        Type-safe EDSL for SQL queries on persistent backends
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/1.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-monad-logger-prof
BuildRequires:  ghc-persistent-devel
BuildRequires:  ghc-persistent-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-unliftio-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-hspec-core-devel
BuildRequires:  ghc-hspec-core-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-mysql-devel
BuildRequires:  ghc-mysql-prof
BuildRequires:  ghc-mysql-simple-devel
BuildRequires:  ghc-mysql-simple-prof
BuildRequires:  ghc-persistent-mysql-devel
BuildRequires:  ghc-persistent-mysql-prof
BuildRequires:  ghc-persistent-postgresql-devel
BuildRequires:  ghc-persistent-postgresql-prof
BuildRequires:  ghc-persistent-sqlite-devel
BuildRequires:  ghc-persistent-sqlite-prof
BuildRequires:  ghc-postgresql-simple-devel
BuildRequires:  ghc-postgresql-simple-prof
%endif

%description
'esqueleto' is a bare bones, type-safe EDSL for SQL queries that works with
unmodified 'persistent' SQL backends. Its language closely resembles SQL, so
you don't have to learn new concepts, just new syntax, and it's fairly easy to
predict the generated SQL and optimize it for your backend. Most kinds of
errors committed when writing SQL are caught as compile-time errors---although
it is possible to write type-checked 'esqueleto' queries that fail at runtime.

'persistent' is a library for type-safe data serialization. It has many kinds
of backends, such as SQL backends ('persistent-mysql', 'persistent-postgresql',
'persistent-sqlite') and NoSQL backends ('persistent-mongoDB'). While
'persistent' is a nice library for storing and retrieving records, including
with filters, it does not try to support some of the features that are specific
to SQL backends. In particular, 'esqueleto' is the recommended library for
type-safe 'JOIN's on 'persistent' SQL backends. (The alternative is using raw
SQL, but that's error prone and does not offer any composability.)

Currently, 'SELECT's, 'UPDATE's, 'INSERT's and 'DELETE's are supported.
Not all SQL features are available, but most of them can be easily added
(especially functions), so please open an issue or send a pull request if you
need anything that is not covered by 'esqueleto' on
<https://github.com/bitemyapp/esqueleto>.

The name of this library means "skeleton" in Portuguese and contains all three
SQL letters in the correct order =). It was inspired by Scala's Squeryl but
created from scratch.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%package -n ghc-%{pkg_name}-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%{pkg_name}-doc
This package provides the Haskell %{pkg_name} library documentation.

%package -n ghc-%{pkg_name}-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%{pkg_name}-devel = %{version}-%{release}
Supplements:    (ghc-%{pkg_name}-devel and ghc-prof)

%description -n ghc-%{pkg_name}-prof
This package provides the Haskell %{pkg_name} profiling library.

%prep
%autosetup -n %{pkg_name}-%{version}
cp -p %{SOURCE1} %{pkg_name}.cabal

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
%doc README.md changelog.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
