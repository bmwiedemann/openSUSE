#
# spec file for package zot-registry
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

%define service_name zot
%define system_user_name zot
%define executable_name zot

# https://github.com/project-zot/zot/blob/main/Makefile#L28
%define zui_version commit-f870292

Name:           zot-registry
Version:        2.1.11
Release:        0
Summary:        Scale-out production-ready vendor-neutral OCI-native container image registry
License:        Apache-2.0
URL:            https://github.com/project-zot/zot/
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
#
Source2:        https://github.com/project-zot/zui/releases/download/%{zui_version}/zui.tgz
#
Source11:       config.json
Source12:       system-user-%{system_user_name}.conf
#
Source21:       Makefile
Source22:       PACKAGING_README.md
#
#
BuildRequires:  awk
BuildRequires:  bash-completion
BuildRequires:  coreutils
BuildRequires:  fish
BuildRequires:  git-core
BuildRequires:  go >= 1.23
BuildRequires:  sysuser-tools
BuildRequires:  zsh
#
BuildRequires:  dos2unix
BuildRequires:  fdupes

%description
Production-ready vendor-neutral OCI image registry - images stored in OCI image
format, distribution specification on-the-wire, that's it!

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

tar xzf %{SOURCE2} -C ./pkg/extensions

%build
%ifarch %{ix86} s390 s390x armv7l armv7hl armv7l:armv6l:armv5tel riscv64
    export CGO_ENABLED=1
    sed -i 's/CGO_ENABLED=0/CGO_ENABLED=1/g' Makefile
%else
    export CGO_ENABLED=0
%endif

# disable modtidy target as dependency for modcheck
sed -i '/^modcheck:/ s/modcheck:.*/modcheck:/g' Makefile

# disable ui target as dependency for binary
sed -i '/^binary:.*findstring ui/d' Makefile

# disable ui target as dependency for build-metadata
sed -i '/^build-metadata:.*findstring/ s/^build-metadata:.*/build-metadata:/' Makefile

# set the COMMIT manually, to avoid having "dirty" in it
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"
sed -i '/^COMMIT/ s/= .*$/= $(COMMIT_HASH)/' Makefile
make binary

%sysusers_generate_pre %{SOURCE12} %{system_user_name} system-user-%{system_user_name}.conf

#
dos2unix ./examples/config-policy.json

%install
# Install the binary (which has linux and the architecture in the name...
install -D -m 0755 bin/%{executable_name}* %{buildroot}/%{_bindir}/%{executable_name}

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{executable_name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{executable_name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{executable_name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{executable_name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
%{buildroot}/%{_bindir}/%{executable_name} completion zsh > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{executable_name}

# Configuration file in /etc/zot/
install -D -m644 %{SOURCE11} %{buildroot}/%{_sysconfdir}/%{service_name}/config.json

# directory in /var/lib/
install -d  %{buildroot}%{_localstatedir}/lib/%{name}

# sysusers configuration file
mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE12} %{buildroot}%{_sysusersdir}/

# systemd service
install -D -m 0644 examples/%{service_name}.service %{buildroot}%{_unitdir}/%{service_name}.service

%check
%{buildroot}/%{_bindir}/%{executable_name} --version
%{buildroot}/%{_bindir}/%{executable_name} --version 2>&1 | grep -q %{version}

%pre -f %{system_user_name}.pre
%service_add_pre %{service_name}.service

%post
%service_add_post %{service_name}.service

%preun
%service_del_preun %{service_name}.service

%postun
%service_del_postun %{service_name}.service

%files
%doc README.md examples
%license LICENSE
%{_bindir}/%{executable_name}
%{_sysusersdir}/system-user-%{system_user_name}.conf
%{_unitdir}/%{service_name}.service
%dir %{_sysconfdir}/%{service_name}/
%config(noreplace) %{_sysconfdir}/%{service_name}/config.json
%attr(-,%{system_user_name},%{system_user_name}) %{_localstatedir}/lib/%{name}

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/%{executable_name}

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{executable_name}.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{executable_name}

%changelog
