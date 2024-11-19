#
# spec file for package hyperfine
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


Name:           hyperfine
Version:        1.19.0
Release:        0
Summary:        Command-line benchmarking tool
License:        Apache-2.0 OR MIT
URL:            https://github.com/sharkdp/%{name}
Source0:        https://github.com/sharkdp/hyperfine/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.46
BuildRequires:  zstd
ExclusiveArch:  %{rust_tier1_arches}

%description
A command-line tool which runs benchmarks of other programs passed as arguments.
It includes:
  * Statistical analysis across multiple runs
  * Support for arbitrary shell commands
  * Constant feedback about the benchmark progress and current estimates
  * Warmup runs can be executed before the actual benchmark
  * Cache-clearing commands can be set up before each timing run
  * Statistical outlier detection to detect interference from other programs and caching effects
  * Export results to various formats: CSV, JSON, Markdown, AsciiDoc
  * Parameterized benchmarks (e.g. vary the number of threads)

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
The official bash completion script for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
The official fish completion script for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
The official zsh completion script for %{name}.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
mkdir -p  %{buildroot}%{_datadir}/bash-completion/completions \
          %{buildroot}%{_datadir}/fish/vendor_completions.d \
          %{buildroot}%{_datadir}/zsh/site-functions
%{cargo_install}
install -Dm644 doc/%{name}.1                                   %{buildroot}%{_mandir}/man1/%{name}.1

#%%if %{with check}
%check
%{cargo_test}
#%%endif

%files
%license LICENSE-APACHE LICENSE-MIT
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion

%files fish-completion
%{_datadir}/fish

%files zsh-completion
%{_datadir}/zsh

%changelog
