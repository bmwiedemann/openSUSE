#
# spec file for package restic
#
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
# nodebuginfo


%bcond_without run_tests

Name:           restic
Version:        0.18.1
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
Patch1:         build.patch
Patch2:         testsuite-use-python3.patch
BuildRequires:  bash-completion
BuildRequires:  golang-packaging
BuildRequires:  zsh
BuildRequires:  golang(API) >= 1.24
Recommends:     fuse
%if %{with run_tests}
# for the tesuite suite
BuildRequires:  fuse
BuildRequires:  python3
%endif

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
go run -mod=vendor build.go \
	--enable-cgo \
%ifnarch ppc64 s390x
	--enable-pie \
%endif
	--verbose

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
./%{name} generate --man %{buildroot}%{_mandir}/man1
install -Dm0644 doc/bash-completion.sh %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm0644 doc/zsh-completion.zsh %{buildroot}%{_sysconfdir}/zsh_completion.d/%{name}

rm doc/.gitignore
perl -p -i -e 's|\r\n|\n|g' doc/logo/font/OFL.txt

%if %{with run_tests}
%check
go test ./...
%endif

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
