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
Version:        0.75.0
Release:        0
Summary:        CLI for nono capability-based sandbox
License:        Apache-2.0
URL:            https://github.com/nolabs-ai/nono/
Source0:        https://github.com/nolabs-ai/nono/archive/refs/tags/v%{version}.tar.gz
Source1:        vendor.tar.zst
ExcludeArch:    %ix86 %arm32 ppc ppc64le s390 s390x
BuildRequires:  bash-completion
BuildRequires:  ca-certificates-mozilla
BuildRequires:  cargo >= 1.97
BuildRequires:  cargo-packaging
BuildRequires:  fish
BuildRequires:  gcc-c++
BuildRequires:  zsh

%description
nono-cli is a capability-based sandboxing system for running untrusted AI
agents with OS-enforced isolation.

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
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
# Filter a warning incorrectly emitted to stdout; https://github.com/nolabs-ai/nono/issues/1777
install -d %{buildroot}%{_datadir}/bash-completion/completions
%{buildroot}%{_bindir}/nono completion bash | grep -v 'Ignoring invalid XDG_CONFIG_HOME' > %{buildroot}%{_datadir}/bash-completion/completions/nono
install -d %{buildroot}%{_datadir}/zsh/site-functions
%{buildroot}%{_bindir}/nono completion zsh | grep -v 'Ignoring invalid XDG_CONFIG_HOME' > %{buildroot}%{_datadir}/zsh/site-functions/_nono
install -d %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}%{_bindir}/nono completion fish | grep -v 'Ignoring invalid XDG_CONFIG_HOME' > %{buildroot}%{_datadir}/fish/vendor_completions.d/nono.fish

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
