#
# spec file for package ghc-pandoc-server
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


%global pkg_name pandoc-server
%bcond_with ghc_prof
Name:           ghc-%pkg_name
Version:        0.1.4.3
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Pandoc document conversion as an HTTP servant-server
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-doctemplates-devel
BuildRequires:  ghc-pandoc-devel
BuildRequires:  ghc-pandoc-types-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-servant-server-devel
BuildRequires:  ghc-skylighting-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-unicode-collation-devel
BuildRequires:  ghc-wai-cors-devel
BuildRequires:  ghc-wai-devel
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-doctemplates-prof
BuildRequires:  ghc-pandoc-prof
BuildRequires:  ghc-pandoc-types-prof
BuildRequires:  ghc-servant-server-prof
BuildRequires:  ghc-skylighting-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-unicode-collation-prof
BuildRequires:  ghc-wai-cors-prof
BuildRequires:  ghc-wai-prof
%endif

%description
Pandoc-server provides pandoc's document conversion functions in an HTTP
server.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

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
%autosetup -p1 -n %pkg_name-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license COPYING.md

%files devel -f %{name}-devel.files

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license COPYING.md

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
