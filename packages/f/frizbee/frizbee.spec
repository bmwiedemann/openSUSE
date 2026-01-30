#
# spec file for package frizbee
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


Name:           frizbee
Version:        0.1.8
Release:        0
Summary:        Throw a tag at and it comes back with a checksum
License:        Apache-2.0
URL:            https://github.com/stacklok/frizbee
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.25

%description
Frizbee is a tool you may throw a tag at and it comes back with a checksum.

It's a command-line tool designed to provide checksums for GitHub Actions and
container images based on tags.

It also includes a set of libraries for working with tags and checksums.

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

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

# output of 'frizbee version' still partially broken/missing
# https://github.com/stacklok/frizbee/issues/148
go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   -tags=netgo \
   -ldflags=" \
   -X main.Version=%{version} \
   -X main.Commit=${COMMIT_HASH} \
   -X main.CommitDate=${BUILD_DATE} \
   -X main.TreeState=clean \
   -X github.com/stacklok/frizbee/internal/cli.CLIVersion=%{version}" \
   -o bin/%{name} main.go

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d/
%{buildroot}/%{_bindir}/%{name} completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%files -n %{name}-bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{name}

%files -n %{name}-fish-completion
%dir %{_datarootdir}/fish
%dir %{_datarootdir}/fish/vendor_completions.d
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files -n %{name}-zsh-completion
%defattr(-,root,root)
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{name}

%changelog
