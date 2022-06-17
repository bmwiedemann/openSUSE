#
# spec file for package dog
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


Name:           dog
Version:        0.1.0
Release:        0
Summary:        A command-line DNS client
License:        EUPL-1.2
URL:            https://github.com/ogham/dog
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source3:        install.yml
BuildRequires:  cargo-packaging
BuildRequires:  git
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  rinstall
BuildRequires:  pkgconfig(openssl)
ExclusiveArch:  %{rust_tier1_arches}

%description
A command-line DNS client, like dig. It has colourful output, understands normal
command-line argument syntax, supports the DNS-over-TLS and DNS-over-HTTPS protocols,
and can emit JSON.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config
cp %{SOURCE3} .

%build
%{cargo_build}
# Generate manpage
pandoc --standalone -f markdown -t man man/dog.1.md > man/dog.1

%install
%{rinstall}

%check
%{cargo_test}

%files
%doc %{_datadir}/doc/dog/README.md
%dir %{_datadir}/doc/dog
%license %{_datadir}/licenses/dog/LICENCE
%dir %{_datadir}/licenses/dog
%{_bindir}/dog
%{_mandir}/man1/dog.1%{?ext_man}
%{_datadir}/bash-completion/completions/dog.bash
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/dog.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%dir %{_datadir}/zsh/site-functions/completions
%{_datadir}/zsh/site-functions/completions/_dog

%changelog
