#
# spec file for package texmath
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global pkg_name texmath
%bcond_with ghc_prof
%bcond_with tests
Name:           %pkg_name
Version:        0.13.3.5
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Conversion between math formats
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-pandoc-types-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-show-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-typst-symbols-devel
BuildRequires:  ghc-xml-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-pandoc-types-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-pretty-show-prof
BuildRequires:  ghc-split-prof
BuildRequires:  ghc-syb-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-typst-symbols-prof
BuildRequires:  ghc-xml-prof
%endif
%if %{with tests}
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-golden-devel
%if %{with ghc_prof}
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-tasty-golden-prof
BuildRequires:  ghc-tasty-prof
%endif
%endif

%description
The texmath library provides functions to read and write TeX math, presentation
MathML, and OMML (Office Math Markup Language, used in Microsoft Office).
Support is also included for converting math formats to Gnu eqn, typst,
StarMath, and pandoc's native format (allowing conversion, via pandoc, to a
variety of different markup formats). The TeX reader supports basic LaTeX and
AMS extensions, and it can parse and apply LaTeX macros. (See
<https://johnmacfarlane.net/texmath here> for a live demo of bidirectional
conversion between LaTeX and MathML.)

The package also includes several utility modules which may be useful for
anyone looking to manipulate either TeX math or MathML. For example, a copy of
the MathML operator dictionary is included.

Use the 'executable' flag to install a standalone executable, 'texmath', that
converts formulas from one format to another. (Use the '--help' flag for a
description of all functionality).

Use the 'server' flag to install a web server, 'texmath-server', that exposes a
JSON API allowing conversion of individual formulas and batches of formulas.

%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Requires:       ghc-%{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

%package -n ghc-%pkg_name-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%pkg_name-doc
This package provides the Haskell %{pkg_name} library documentation.

%if %{with ghc_prof}
%package -n ghc-%pkg_name-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%pkg_name-devel = %{version}-%{release}
Supplements:    (ghc-%pkg_name-devel and ghc-prof)

%description -n ghc-%pkg_name-prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
%autosetup -p1

%build
%define cabal_configure_options -f-server -fexecutable
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %pkg_name-%{version}

%check
%cabal_test

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license LICENSE
%doc README.md changelog.md
%{_bindir}/%{name}

%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc README.md changelog.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
