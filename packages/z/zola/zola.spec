#
# spec file for package zola
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


Name:           zola
Version:        0.19.1
Release:        0
Summary:        Fast static site generator
License:        MIT
URL:            https://github.com/getzola/zola
Source0:        https://github.com/getzola/zola/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  cargo > 1.77
BuildRequires:  cargo-packaging
BuildRequires:  libgcc_s1
BuildRequires:  pkg-config
BuildRequires:  zstd
ExclusiveArch:  %{rust_tier1_arches}

%description
Zola is a static site generator (SSG), similar to Hugo, Pelican, and Jekyll.
It is written in Rust and uses the Tera template engine, which is similar to
Jinja2, Django templates, Liquid, and Twig. Content is written in CommonMark,
a strongly defined, highly compatible specification of Markdown.

%prep
%autosetup -a1 -p1

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       zsh
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%package        bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%build
%if 0%{?sle_version} == 150400 && 0%{?is_opensuse}
export RUSTC_BOOTSTRAP=1
%endif
%{cargo_build}

%install
%if 0%{?sle_version} == 150400 && 0%{?is_opensuse}
export RUSTC_BOOTSTRAP=1
%endif

%{cargo_install}
export PATH=$PATH:%{buildroot}%{_bindir}
%{name} completion bash | install -Dm 0644 /dev/stdin %{buildroot}%{_datadir}/bash-completion/completions/%{name}.bash
%{name} completion fish | install -Dm 0644 /dev/stdin %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{name} completion zsh  | install -Dm 0644 /dev/stdin %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%check
%if 0%{?sle_version} == 150400 && 0%{?is_opensuse}
export RUSTC_BOOTSTRAP=1
%endif
%{cargo_test}

%files
%{_bindir}/zola
%license LICENSE
%doc docs README.md CHANGELOG.md

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/zola.bash

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/zola.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_zola

%changelog
