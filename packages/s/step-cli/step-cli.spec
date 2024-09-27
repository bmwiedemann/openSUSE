#
# spec file for package step-cli
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%define configdir /etc/step
%define certsdir  /etc/step/certs
%define services  cert-renewer.target ssh-cert-renewer.timer ssh-cert-renewer@.timer cert-renewer@.timer ssh-cert-renewer.service ssh-cert-renewer@.service cert-renewer@.service
%define executable_name step
%define pkg_name cli

Name:           step-cli
Version:        0.27.4
Release:        0
Summary:        Zero trust swiss army knife for working with X509, OAuth, JWT, OATH OTP, etc
License:        Apache-2.0
Group:          Productivity/Networking/Security
URL:            https://github.com/smallstep/cli
Source:         cli-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        series
Patch:          more-units.patch
Patch1:         add-missing-targets.patch
BuildRequires:  go >= 1.22
Conflicts:      step

%description
step is an easy-to-use CLI tool for building, operating, and automating Public
Key Infrastructure (PKI) systems and workflows. It's the client counterpart to
the step-ca online Certificate Authority (CA). You can use it for many common
crypto and X.509 operations—either independently, or with an online CA.

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
%autosetup -p 1 -a 1 -n %{pkg_name}-%{version}

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X main.Version=%{version} \
   -X main.BuildDate=$BUILD_DATE" \
   -o bin/%{executable_name} github.com/smallstep/cli/cmd/step

%install
# Install the binary.
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{executable_name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{executable_name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{executable_name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{executable_name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d/
%{buildroot}/%{_bindir}/%{executable_name} completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{executable_name}

for unit in %{services} ; do
install -D -m 0644 systemd/${unit} %{buildroot}%{_unitdir}/${unit}
done

install -D -d -m 0711 %{buildroot}%{configdir}/{certs,config}

%check
bin/%{executable_name} --version | grep %{version}

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
%{_bindir}/%{executable_name}
%{_unitdir}/ssh-cert-renewer.service
%{_unitdir}/ssh-cert-renewer.timer
%{_unitdir}/ssh-cert-renewer@.service
%{_unitdir}/ssh-cert-renewer@.timer
%{_unitdir}/cert-renewer@.service
%{_unitdir}/cert-renewer@.timer
%{_unitdir}/cert-renewer.target
%config(noreplace) %attr(-,root,root)    %{configdir}
%config(noreplace) %attr(640,root,root) %ghost    %{configdir}/config/defaults.json

%files -n %{name}-bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{executable_name}

%files -n %{name}-fish-completion
%dir %{_datarootdir}/fish
%dir %{_datarootdir}/fish/vendor_completions.d
%{_datarootdir}/fish/vendor_completions.d/%{executable_name}.fish

%files -n %{name}-zsh-completion
%defattr(-,root,root)
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{executable_name}

%changelog
