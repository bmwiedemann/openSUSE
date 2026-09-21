#
# spec file for package nono-cli
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


Name:           nono-cli
Version:        0.77.0
Release:        0
Summary:        CLI for nono capability-based sandbox
# Legal-Review-Notice: licences of the Rust crates statically linked into the
# shipped nono binary: 351 crates (nono, nono-cli, nono-proxy and 348
# vendored), identical on x86_64 and aarch64, taken from cargo's unit graph;
# anything reached only through proc-macros or build scripts is build-time
# only. Where a crate offers a choice, Apache-2.0, else MIT, is elected:
#  - MPL-2.0: colored (direct dependency) and option-ext (via dirs-sys);
#    vendor.tar.zst in the source package provides their source.
#  - ISC: aws-lc-rs, aws-lc-sys, ring, rustls-webpki, untrusted.
#  - BSD-3-Clause: subtle, and the jitterentropy code bundled in aws-lc-sys,
#    for which AWS-LC expressly elects BSD-3-Clause over GPL-2.0.
#  - Unicode-3.0: icu_*, litemap, potential_utf, tinystr, writeable, yoke,
#    zerofrom, zerotrie, zerovec, and the Unicode tables in regex-syntax.
#  - CDLA-Permissive-2.0: webpki-roots.
#  - MIT: 67 crates that do not offer Apache-2.0.
#  - OpenSSL- and SSLeay-derived code in aws-lc-sys is Apache-2.0 per its
#    LICENSE.
#  - zlib-rs and foldhash (Zlib) are named in the binary's embedded
#    cargo-auditable dependency list but are not linked.
License:        Apache-2.0 AND BSD-3-Clause AND CDLA-Permissive-2.0 AND ISC AND MIT AND MPL-2.0 AND Unicode-3.0
URL:            https://github.com/nolabs-ai/nono/
Source0:        https://github.com/nolabs-ai/nono/archive/refs/tags/v%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  bash-completion
BuildRequires:  ca-certificates-mozilla
BuildRequires:  cargo >= 1.97
BuildRequires:  cargo-packaging
BuildRequires:  fish
BuildRequires:  gcc-c++
BuildRequires:  zsh
ExcludeArch:    %{ix86} %{arm32} ppc ppc64le s390 s390x

%description
nono-cli is a capability-based sandboxing system for running untrusted AI
agents with OS-enforced isolation.

%package bash-completion
Summary:        Bash Completion for %{name}
License:        Apache-2.0
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
License:        Apache-2.0
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
License:        Apache-2.0
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -p 1 -n nono-%{version} -a 1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 target/release/nono %{buildroot}%{_bindir}/nono
install -d %{buildroot}%{_datadir}/bash-completion/completions
%{buildroot}%{_bindir}/nono completion bash > %{buildroot}%{_datadir}/bash-completion/completions/nono
install -d %{buildroot}%{_datadir}/zsh/site-functions
%{buildroot}%{_bindir}/nono completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/_nono
install -d %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}%{_bindir}/nono completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/nono.fish

%check
# would be nice, currently failing
#{cargo_test}

%files
%doc README.md
%license LICENSE
%{_bindir}/nono

%files bash-completion
%{_datadir}/bash-completion/completions/nono

%files zsh-completion
%{_datadir}/zsh/site-functions/_nono

%files fish-completion
%{_datadir}/fish/vendor_completions.d/nono.fish

%changelog
