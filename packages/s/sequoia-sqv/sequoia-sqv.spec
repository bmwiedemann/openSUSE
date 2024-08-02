#
# spec file for package sequoia-sqv
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

Name:           sequoia-sqv
Version:        1.2.1~0
Release:        0
Summary:        A simple signature verification program
License:        GPL-2.0-or-later
URL:            https://sequoia-pgp.org/
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.74
BuildRequires:  pkgconfig(nettle)
BuildRequires:  clang
BuildRequires:  fish
BuildRequires:  zsh
ExclusiveArch:  %{rust_tier1_arches}

%description
sqv verifies detached OpenPGP signatures. It is a replacement for gpgv.
Unlike gpgv, it can take additional constraints on the signature into account.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%{cargo_install}

install -Dm644 %{_builddir}/%{name}-%{version}/target/release/build/%{name}-*/out/shell-completions/sqv.bash %{buildroot}%{_datadir}/bash-completion/completions/sqv
install -Dm644 %{_builddir}/%{name}-%{version}/target/release/build/%{name}-*/out/shell-completions/_sqv %{buildroot}%{_datadir}/zsh/site-functions/_sqv
install -Dm644 %{_builddir}/%{name}-%{version}/target/release/build/%{name}-*/out/shell-completions/sqv.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/sqv.fish
install -Dm644 %{_builddir}/%{name}-%{version}/target/release/build/%{name}-*/out/man-pages/sqv*.1 -t %{buildroot}%{_mandir}/man1/

%check
%{cargo_test}

%files
%license LICENSE.txt
%{_bindir}/sqv
%{_mandir}/man1/sqv*

%files bash-completion
%{_datadir}/bash-completion/completions/sqv

%files zsh-completion
%{_datadir}/zsh/site-functions/_sqv

%files fish-completion
%{_datadir}/fish/vendor_completions.d/sqv.fish

%changelog
