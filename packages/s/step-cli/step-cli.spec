#
# spec file for package step-cli
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


%define configdir %{_sysconfdir}/step
%define certsdir  %{_sysconfdir}/step/certs
%define services  cert-renewer.target ssh-cert-renewer.timer ssh-cert-renewer@.timer cert-renewer@.timer ssh-cert-renewer.service ssh-cert-renewer@.service cert-renewer@.service
%define pkg_name cli
%define pkg_version %{version}
Name:           step-cli
Version:        0.28.3
Release:        0
Summary:        Zero trust swiss army knife for working with X509, OAuth, JWT, OATH OTP, etc
License:        Apache-2.0
URL:            https://smallstep.com/cli
# https://github.com/smallstep/cli/releases
Source:         https://github.com/smallstep/cli/archive/refs/tags/v%{pkg_version}.tar.gz#/%{pkg_name}-%{pkg_version}.tar.gz
Source1:        vendor.tar.xz
Source2:        series
Patch0:         more-units.patch
Patch1:         add-missing-targets.patch
BuildRequires:  fish
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig
BuildRequires:  zsh
BuildRequires:  golang(API) >= 1.19
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(systemd)
Conflicts:      step
%{?systemd_ordering}

%description
A zero trust swiss army knife for working with X509, OAuth, JWT, OATH OTP, etc.

%package bash-completion
Summary:        Bash Completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
fish shell completions for %{name}.

%package zsh-completion
Summary:        ZSH completion for %{name}
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
zsh shell completions for %{name}.

%prep
%autosetup -p1 -n %{pkg_name}-%{pkg_version} -a 1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build -buildmode=pie -mod=vendor -ldflags="-w -X 'main.Version=%{version}' -X 'main.BuildTime=${BUILD_DATE}'" ./cmd/...
for shell in bash zsh fish ; do
./step completion ${shell} > autocomplete/${shell}_autocomplete
done

%install
install -D -m 0755 step                           %{buildroot}%{_bindir}/step
# shell completions
install -D -m 0644 autocomplete/bash_autocomplete   %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -m 0644 autocomplete/zsh_autocomplete    %{buildroot}%{_sysconfdir}/zsh_completion.d/%{name}
install -D -m 0644 autocomplete/fish_autocomplete   %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

for unit in %{services} ; do
install -D -m 0644 systemd/${unit} %{buildroot}%{_unitdir}/${unit}
done

install -D -d -m 0711 %{buildroot}%{configdir}/{certs,config}

%check
./step --version | grep %{version}

%pre
%service_add_pre %{services}

%post
%service_add_post %{services}

%preun
%service_del_preun %{services}

%postun
%service_del_postun %{services}

%files
%doc README.md
%license LICENSE
%{_bindir}/step*
%{_unitdir}/ssh-cert-renewer.service
%{_unitdir}/ssh-cert-renewer.timer
%{_unitdir}/ssh-cert-renewer@.service
%{_unitdir}/ssh-cert-renewer@.timer
%{_unitdir}/cert-renewer@.service
%{_unitdir}/cert-renewer@.timer
%{_unitdir}/cert-renewer.target
%config(noreplace) %attr(-,root,root) %{configdir}
%config(noreplace) %attr(640,root,root) %ghost %{configdir}/config/defaults.json

%files bash-completion
%license LICENSE
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%license LICENSE
%config %{_sysconfdir}/zsh_completion.d/%{name}

%files fish-completion
%license LICENSE
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
