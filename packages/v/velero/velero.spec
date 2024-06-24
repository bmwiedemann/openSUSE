#
# spec file for package velero
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


Name:           velero
Version:        1.14.0
Release:        0
Summary:        Backup program with deduplication and encryption
License:        Apache-2.0
Group:          Productivity/Archiving/Backup
URL:            https://velero.io
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.22

%description
velero is a backup program. It supports verification, encryption,
snapshots and deduplication.

%package velero-restic-restore-helper
Summary:        Restic restore helper for %{name}
Group:          Productivity/Archiving/Backup
Requires:       %{name} = %{version}
Supplements:    packageand(velero:velero-restic-restore-helper)

%description velero-restic-restore-helper
Restic restore helper for %{name}.

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
%setup -q -a1

%build
go build \
   -installsuffix "static" \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/vmware-tanzu/%{name}/pkg/buildinfo.Version=%{version} \
   -X github.com/vmware-tanzu/%{name}/pkg/buildinfo.GitSHA=v%{version} \
   -X github.com/vmware-tanzu/%{name}/pkg/buildinfo.GitTreeState=clean" \
   -o bin/%{name} ./cmd/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
%{buildroot}/%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d
%{buildroot}/%{_bindir}/%{name} completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{name}

# create the fish completion file
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}/%{_bindir}/%{name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%files bash-completion
%defattr(-,root,root)
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{name}

%files zsh-completion
%defattr(-,root,root)
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{name}

%files fish-completion
%defattr(-,root,root)
%dir %{_datarootdir}/fish
%dir %{_datarootdir}/fish/vendor_completions.d
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%changelog
