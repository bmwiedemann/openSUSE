#
# spec file for package hscolour
#
# Copyright (c) 2023 SUSE LLC
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


%global pkg_name hscolour
%global pkgver %{pkg_name}-%{version}
Name:           %{pkg_name}
Version:        1.24.4
Release:        0
Summary:        Colourise Haskell code
License:        LGPL-2.1-or-later
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}

%description
Hscolour is a small Haskell script to colourise Haskell code. It currently has
six output formats: ANSI terminal codes (optionally XTerm-256colour codes),
HTML 3.2 with <font> tags, HTML 4.01 with CSS, HTML 4.01 with CSS and mouseover
annotations, XHTML 1.0 with inline CSS styling, LaTeX, and mIRC chat codes.

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
%autosetup

%build
%ghc_lib_build

%install
%ghc_lib_install

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license LICENCE-LGPL
%{_bindir}/HsColour
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/data
%{_datadir}/%{name}-%{version}/data/rgb24-example-.hscolour
%{_datadir}/%{name}-%{version}/hscolour.css

%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENCE-LGPL

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files

%files -n ghc-%{pkg_name}-doc -f ghc-%{pkg_name}-doc.files
%license LICENCE-LGPL

%files -n ghc-%{pkg_name}-prof -f ghc-%{pkg_name}-prof.files

%changelog
