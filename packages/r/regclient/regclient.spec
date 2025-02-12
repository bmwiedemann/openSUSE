#
# spec file for package regclient
#
# Copyright (c) 2025 SUSE LLC
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


Name:           regclient
Version:        0.8.1
Release:        0
Summary:        OCI Registry Client in Go and tooling using those libraries
License:        Apache-2.0
URL:            https://github.com/regclient/regclient
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  git
BuildRequires:  go >= 1.22
BuildRequires:  zsh

%description
Client interface for the registry API. This packages includes regctl for a
command line interface to manage registries.

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
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description -n %{name}-fish-completion
Fish command line completion support for %{name}.

%package -n %{name}-zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description -n %{name}-zsh-completion
zsh command line completion support for %{name}.

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

for executable in regctl regsync regbot
do
    go build \
       -mod=vendor \
       -buildmode=pie \
       -trimpath \
       -tags nolegacy \
       -buildvcs=false \
       -ldflags="-buildid= -X github.com/regclient/regclient/internal/version.vcsTag=%{version}" \
       -o bin/${executable} ./cmd/${executable}
done

%install

for executable in regctl regsync regbot
do

    # Install the binary.
    install -D -m 0755 bin/${executable} %{buildroot}/%{_bindir}/${executable}

    # create the bash completion file
    mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
    %{buildroot}/%{_bindir}/${executable} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/${executable}

    # create the fish completion file
    mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
    %{buildroot}/%{_bindir}/${executable} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/${executable}.fish

    # create the zsh completion file
    mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
    %{buildroot}/%{_bindir}/${executable} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_${executable}

done

%check

for executable in regctl regsync regbot
do
    %{buildroot}/%{_bindir}/${executable} version | grep %{version}
done

%files
%doc README.md
%license LICENSE
%{_bindir}/regbot
%{_bindir}/regctl
%{_bindir}/regsync

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/regbot
%{_datarootdir}/bash-completion/completions/regctl
%{_datarootdir}/bash-completion/completions/regsync

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/regbot.fish
%{_datarootdir}/fish/vendor_completions.d/regctl.fish
%{_datarootdir}/fish/vendor_completions.d/regsync.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_regbot
%{_datarootdir}/zsh/site-functions/_regctl
%{_datarootdir}/zsh/site-functions/_regsync

%changelog
