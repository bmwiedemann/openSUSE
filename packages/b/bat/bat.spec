#
# spec file for package bat
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           bat
Version:        0.26.0
Release:        0
Summary:        A cat(1) clone with syntax highlighting and Git integration
License:        Apache-2.0 OR MIT
URL:            https://github.com/sharkdp/bat
Source0:        https://github.com/sharkdp/bat/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.79
ExclusiveArch:  %{rust_arches}

%description
A cat(1) clone which supports syntax highlighting for a large number of
programming and markup languages. It has git integration and automatic paging.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%autosetup -a1 -p1 -n %{name}-%{version}

%build
%{cargo_build}

%install
install -D -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

install -D -m 0644 $(find target/release/build -name "%{name}.1") "%{buildroot}/%{_mandir}/man1/%{name}.1"

install -D -m 0644 $(find target/release/build -name "%{name}.bash") "%{buildroot}/%{_datadir}/bash-completion/completions/%{name}"
install -D -m 0644 $(find target/release/build -name "%{name}.fish") "%{buildroot}/%{_datadir}/fish/vendor_completions.d/%{name}.fish"
install -D -m 0644 $(find target/release/build -name "%{name}.zsh")  "%{buildroot}/%{_datadir}/zsh/site-functions/_%{name}"

%if %{with check}
%check
%{cargo_test}
%endif

%files
%doc README.md CONTRIBUTING.md CHANGELOG.md
%license LICENSE-MIT LICENSE-APACHE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
