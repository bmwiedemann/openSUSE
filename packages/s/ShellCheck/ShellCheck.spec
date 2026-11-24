#
# spec file for package ShellCheck
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


%global pkg_name ShellCheck
%bcond_with ghc_prof
%bcond_without tests
Name:           %pkg_name
Version:        0.11.0
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Shell script analysis tool
License:        GPL-3.0-or-later
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-fgl-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-regex-tdfa-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-transformers-devel
BuildRequires:  pandoc-cli
Provides:       shellcheck = %{version}-%{release}
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-Diff-prof
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-fgl-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-regex-tdfa-prof
BuildRequires:  ghc-transformers-prof
%endif

%description
The goals of ShellCheck are:

* To point out and clarify typical beginner's syntax issues, that causes a
shell to give cryptic error messages.

* To point out and clarify typical intermediate level semantic problems, that
causes a shell to behave strangely and counter-intuitively.

* To point out subtle caveats, corner cases and pitfalls, that may cause an
advanced user's otherwise working script to fail under future circumstances.

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
cabal-tweak-dep-ver Diff '< 1.1' '< 3'
cabal-tweak-dep-ver QuickCheck '< 2.17' '< 2.20'

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %pkg_name-%{version}
pandoc -s -f markdown-smart -t man shellcheck.1.md -o shellcheck.1
install -Dpm 0644 shellcheck.1 %{buildroot}%{_mandir}/man1/shellcheck.1

%check
%cabal_test

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/shellcheck
%{_mandir}/man1/shellcheck.1%{?ext_man}

%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc CHANGELOG.md README.md

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license LICENSE

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
