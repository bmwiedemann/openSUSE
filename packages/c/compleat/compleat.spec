#
# spec file for package compleat
#
# Copyright (c) 2022 SUSE LLC
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


Name:           compleat
Version:        1.0+git.20220402.ec8fccc
Release:        0%{?dist}
License:        MIT
Group:          System/Shells
Summary:        Generate command-line completions using a simple DSL
URL:            https://github.com/mbrubeck/compleat
Source:         %{name}-%{version}.tar.xz
# ghc is only built on these architectures
ExclusiveArch:  aarch64 %{arm} x86_64 ppc64 ppc64le riscv64 s390x
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-rpm-macros

%description

Generate tab completion for any shell command by specifying its usage in a familiar manpage-like format.

%package fish
Summary:        Files to use %{name} in the fish shell
Requires:       %{name}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish

Contains a script that is automatically loaded by the fish shell on startup to
setup the automatic completion by %{name}.

%package bash
Summary:        Files to use %{name} in the bash shell
Requires:       %{name}
Supplements:    (%{name} and bash)
BuildArch:      noarch

%description bash

Contains a script that is automatically loaded by the bash shell on startup to
setup the automatic completion by %{name}.

%prep
%autosetup

%build
%ghc_lib_build

%install
%ghc_bin_install
install -d %{buildroot}%{_datadir}/compleat.d
install -D -m 644 examples/*.usage %{buildroot}%{_datadir}/compleat.d
install -d %{buildroot}%{_sysconfdir}/profile.d
install -D -m 644 compleat_setup %{buildroot}%{_sysconfdir}/profile.d/compleat_setup.sh
install -D -m 644 compleat_setup.fish %{buildroot}%{_datadir}/fish/vendor_conf.d/compleat_setup.fish

%files
%defattr(-,root,root)
%{_bindir}/compleat
%{_datadir}/compleat-1.0
%doc README.markdown
%license README.markdown
%{_datadir}/compleat.d

%files bash
%config %{_sysconfdir}/profile.d/compleat_setup.sh

%files fish
%{_datadir}/fish

%changelog
