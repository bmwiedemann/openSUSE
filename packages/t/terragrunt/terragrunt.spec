#
# spec file for package terragrunt
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


Name:           terragrunt
Version:        0.99.3
Release:        0
Summary:        Thin wrapper for Terraform for working with multiple Terraform modules
License:        MIT
URL:            https://github.com/gruntwork-io/terragrunt
Source:         terragrunt-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        Makefile
Source3:        PACKAGING_README.md
BuildRequires:  bash-completion
BuildRequires:  zsh
BuildRequires:  golang(API) >= 1.25

%description
Terragrunt is a thin wrapper for Terraform that provides extra tools for
keeping your Terraform configurations DRY, working with multiple Terraform
modules, and managing remote state.

%package -n %{name}-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description -n %{name}-bash-completion
Bash command line completion support for %{name}.

%package -n %{name}-zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description -n %{name}-zsh-completion
zsh command line completion support for %{name}.

%prep
%autosetup -p1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/gruntwork-io/go-commons/version.Version=v%{version}"

%install
# Install the binary.
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

# create the shell completion files

rm -f ~/.bashrc ~/.zshrc
touch ~/.bashrc ~/.zshrc

%{buildroot}/%{_bindir}/%{name} --install-autocomplete
sed -i 's#%{buildroot}##g' ~/.bashrc ~/.zshrc

# install the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
install -m 0644 ~/.bashrc %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# install the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
install -m 0644 ~/.zshrc %{buildroot}%{_datarootdir}/zsh/site-functions/_%{name}

%check
%{buildroot}/%{_bindir}/%{name} --version | grep v%{version}

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/%{name}

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{name}

%changelog
