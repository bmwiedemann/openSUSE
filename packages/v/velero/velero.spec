#
# spec file for package velero
#
# Copyright (c) 2022 SUSE LLC
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


%define goipath github.com/vmware-tanzu/velero
%define commit cdf3acab5aa562a7841ce733b964b0dc13d10c71
%define gitstate clean

Name:           velero
Version:        1.9.2
Release:        0
Summary:        Backup program with deduplication and encryption
License:        Apache-2.0
Group:          Productivity/Archiving/Backup
URL:            https://velero.io
Source0:        https://github.com/vmware-tanzu/velero/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.17

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
%goprep %{goipath}
export CGO_ENABLED=0
%gobuild -mod vendor -installsuffix "static" -ldflags "-X %{goipath}/pkg/buildinfo.Version=%{version} -X %{goipath}/pkg/buildinfo.GitSHA=%{commit} -X %{goipath}/pkg/buildinfo.GitTreeState=%{gitstate}" cmd/velero
%gobuild -mod vendor -installsuffix "static" -ldflags "-X %{goipath}/pkg/buildinfo.Version=%{version} -X %{goipath}/pkg/buildinfo.GitSHA=%{commit} -X %{goipath}/pkg/buildinfo.GitTreeState=%{gitstate}" cmd/velero-restic-restore-helper

%install
%goinstall
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions
%{buildroot}/%{_bindir}/%{name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d
%{buildroot}/%{_bindir}/%{name} completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{name}
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}/%{_bindir}/%{name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files
%doc README.md
%license LICENSE
%{_bindir}/velero
%{_bindir}/velero-restic-restore-helper

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
