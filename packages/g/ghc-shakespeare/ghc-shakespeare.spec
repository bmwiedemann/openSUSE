#
# spec file for package ghc-shakespeare
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


%global pkg_name shakespeare
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2.0.25
Release:        0
Summary:        A toolkit for making compile-time interpolated templates
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-th-lift-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-hspec-devel
%endif

%description
Shakespeare is a family of type-safe, efficient template languages.
Shakespeare templates are expanded at compile-time, ensuring that all
interpolated variables are in scope. Variables are interpolated according to
their type through a typeclass.

Shakespeare templates can be used inline with a quasi-quoter or in an external
file.

Note there is no dependency on haskell-src-extras. Instead Shakespeare believes
logic should stay out of templates and has its own minimal Haskell parser.

Packages that use this: xml-hamlet

Please see the documentation at
<http://www.yesodweb.com/book/shakespearean-templates> for more details.

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
%doc ChangeLog.md

%changelog
