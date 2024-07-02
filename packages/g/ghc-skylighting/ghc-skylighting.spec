#
# spec file for package ghc-skylighting
#
# Copyright (c) 2024 SUSE LLC
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


%global pkg_name skylighting
%global pkgver %{pkg_name}-%{version}
Name:           ghc-%{pkg_name}
Version:        0.14.2
Release:        0
Summary:        Syntax highlighting library
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-pretty-show-devel
BuildRequires:  ghc-pretty-show-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-skylighting-core-devel
BuildRequires:  ghc-skylighting-core-prof
BuildRequires:  ghc-skylighting-format-ansi-devel
BuildRequires:  ghc-skylighting-format-ansi-prof
BuildRequires:  ghc-skylighting-format-blaze-html-devel
BuildRequires:  ghc-skylighting-format-blaze-html-prof
BuildRequires:  ghc-skylighting-format-context-devel
BuildRequires:  ghc-skylighting-format-context-prof
BuildRequires:  ghc-skylighting-format-latex-devel
BuildRequires:  ghc-skylighting-format-latex-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
ExcludeArch:    %{ix86}

%description
Skylighting is a syntax highlighting library with support for over one hundred
languages. It derives its tokenizers from XML syntax definitions used by KDE's
KSyntaxHighlighting framework, so any syntax supported by that framework can be
added. An optional command-line program is provided. Skylighting is intended to
be the successor to highlighting-kate. This package provides generated syntax
modules based on the KDE XML definitions provided by the 'skylighting-core'
package. As a result this package is licensed under the GPL.

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

%build
%define cabal_configure_options -fexecutable
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE
%{_bindir}/%{pkg_name}

%files devel -f %{name}-devel.files
%doc README.md changelog.md

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENSE

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
