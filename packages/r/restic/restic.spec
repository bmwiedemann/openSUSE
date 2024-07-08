#
# spec file for package restic
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
# nodebuginfo


%define import_path github.com/restic/restic

Name:           restic
Version:        0.16.5
Release:        0
Summary:        Backup program with deduplication and encryption
License:        BSD-2-Clause
Group:          Productivity/Archiving/Backup
URL:            https://restic.net
Source0:        https://github.com/restic/restic/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/restic/restic/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        vendor.tar.gz
Patch0:         disable-selfupdate.patch
BuildRequires:  bash-completion
BuildRequires:  golang-packaging
BuildRequires:  zsh
BuildRequires:  golang(API) >= 1.18

%description
restic is a backup program. It supports verification, encryption,
snapshots and deduplication.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (restic and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Supplements:    (restic and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%autosetup -p 1 -a 3

%build
# Set up GOPATH.
export GOPATH="$GOPATH:$HOME/go"
mkdir -p $HOME/go/src/%{import_path}
cp -rT $PWD $HOME/go/src/%{import_path}

# Build restic. We don't use build.go because it builds statically, uses go
# modules, and also restricts the Go version in cases where it's not actually
# necessary. We disable go modules because restic still provides a vendor/.
GO111MODULE=off go build -o %{name} \
%ifnarch ppc64 s390x
	-buildmode=pie \
%endif
	-ldflags "-s -w -X main.version=%{version}" \
	%{import_path}/cmd/restic

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
./%{name} generate --man %{buildroot}%{_mandir}/man1
install -Dm0644 doc/bash-completion.sh %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm0644 doc/zsh-completion.zsh %{buildroot}%{_sysconfdir}/zsh_completion.d/%{name}

%files
%defattr(-,root,root)
%doc *.md
%doc doc/
%license LICENSE
%{_bindir}/restic
%{_mandir}/man1/restic*.1*

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%config %{_sysconfdir}/zsh_completion.d/%{name}

%changelog
