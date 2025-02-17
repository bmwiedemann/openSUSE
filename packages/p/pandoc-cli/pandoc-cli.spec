#
# spec file for package pandoc-cli
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


Name:           pandoc-cli
Version:        3.6.3
Release:        0
Summary:        Conversion between documentation formats
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-hslua-cli-devel
BuildRequires:  ghc-hslua-cli-prof
BuildRequires:  ghc-pandoc-devel
BuildRequires:  ghc-pandoc-lua-engine-devel
BuildRequires:  ghc-pandoc-lua-engine-prof
BuildRequires:  ghc-pandoc-prof
BuildRequires:  ghc-pandoc-server-devel
BuildRequires:  ghc-pandoc-server-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-prof
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-wai-extra-prof
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-warp-prof
Requires:       ghc-pandoc = %{version}
Provides:       pandoc = %{version}
Obsoletes:      pandoc < 3
ExcludeArch:    %{ix86}

%description
Pandoc-cli provides a command-line executable that uses the pandoc library to
convert between markup formats.

%prep
%autosetup

%build
%define cabal_configure_options -f+lua -f+server
%ghc_bin_build

%install
%ghc_bin_install

%files
%license COPYING.md
%{_bindir}/pandoc

%changelog
