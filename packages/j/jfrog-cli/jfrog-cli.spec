#
# spec file for package jfrog-cli
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


%define executable_name jf

Name:           jfrog-cli
Version:        2.93.0
Release:        0
Summary:        A client that automates access to the JFrog products
License:        Apache-2.0
URL:            https://github.com/jfrog/jfrog-cli
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go1.25 >= 1.25.7
BuildRequires:  zsh
Provides:       %{executable_name} = %{version}

%description
JFrog CLI is a compact and smart client that provides a simple interface that
automates access to Artifactory and Mission Control through their respective
REST APIs. By using the JFrog CLI, you can greatly simplify your automation
scripts making them more readable and easier to maintain. Several features of
the JFrog CLI makes your scripts more efficient and reliable:

- Multithreaded upload and download of artifacts make builds run faster
- Checksum optimization reduces redundant file transfers
- Wildcards and regular expressions give you an easy way to collect all the
  artifacts you wish to upload or download.
- "Dry run" gives you a preview of file transfer operations before you actually
run them

%package -n %{name}-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description -n %{name}-bash-completion
Bash command line completion support for %{name}.

%package -n %{name}-fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description -n %{name}-fish-completion
Fish command line completion support for %{name}.

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
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   -o bin/%{executable_name}

%install
# Install the binary.
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{executable_name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{executable_name}
# delete the shebang
sed -i '1d' %{buildroot}%{_datarootdir}/bash-completion/completions/%{executable_name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{executable_name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{executable_name}.fish
# delete the shebang
sed -i '1d' %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{executable_name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/%{executable_name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{executable_name}
# delete the shebang
sed -i '1d' %{buildroot}%{_datarootdir}/zsh/site-functions/_%{executable_name}

%check
%{buildroot}/%{_bindir}/%{executable_name} --version
%{buildroot}/%{_bindir}/%{executable_name} --version | grep %{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/%{executable_name}

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{executable_name}.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{executable_name}

%changelog
