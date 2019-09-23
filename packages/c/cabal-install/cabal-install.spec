#
# spec file for package cabal-install
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cabal-install
Version:        2.4.0.0
Release:        0
Summary:        The command-line interface for Cabal and Hackage
License:        BSD-3-Clause
Group:          Development/Libraries/Haskell
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{name}-%{version}/revision/2.cabal#/%{name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HTTP-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptohash-sha256-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-echo-devel
BuildRequires:  ghc-edit-distance-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hackage-security-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-resolv-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-tar-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-zip-archive-devel
BuildRequires:  ghc-zlib-devel
Suggests:       %{name}-bash-completion

%description
The 'cabal' command-line program simplifies the process of managing Haskell
software by automating the fetching, configuration, compilation and
installation of Haskell libraries and programs.

%package bash-completion
Summary:        Bash completion for cabal-install
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    packageand(%{name}:bash-completion)

%description bash-completion
Optional sub-package offering bash completion for cabal-install.

%prep
%setup -q
cp -p %{SOURCE1} %{name}.cabal
cabal-tweak-dep-ver zip-archive '< 0.4' '< 0.5'

%build
%ghc_bin_build

%install
%ghc_bin_install
install -D -m444 bash-completion/cabal %{buildroot}%{_datadir}/bash-completion/completions/cabal

%files
%license LICENSE
%doc README.md changelog
%{_bindir}/cabal
%{_mandir}/man1/cabal.1%{?ext_man}

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/cabal

%changelog
