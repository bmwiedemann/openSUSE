#
# spec file for package tetragon
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

%define cli_binary_name tetra
%define cli_package_name tetragon-cli

Name:           tetragon
Version:        1.1.2
Release:        0
Summary:        eBPF-based Security Observability and Runtime Enforcement
License:        Apache-2.0
URL:            https://github.com/cilium/tetragon
Source:         tetragon-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  clang
BuildRequires:  go >= 1.22
BuildRequires:  llvm
BuildRequires:  make

%description
Cilium’s new Tetragon component enables powerful real-time, eBPF-based Security
Observability and Runtime Enforcement.

Tetragon detects and is able to react to security-significant events, such as

* Process execution events
* System call activity
* I/O activity including network & file access

When used in a Kubernetes environment, Tetragon is Kubernetes-aware - that is,
it understands Kubernetes identities such as namespaces, pods and so on - so
that security event detection can be configured in relation to individual
workloads.

%package -n %{cli_package_name}
Summary:        CLI for Tetragon
Provides:       tetra = %{version}

%description -n %{cli_package_name}
To interact with Tetragon, install the Tetragon client CLI tetra.

%package -n %{cli_package_name}-bash-completion
Summary:        Bash Completion for %{cli_package_name}
Group:          System/Shells
Requires:       %{cli_package_name} = %{version}
Requires:       bash-completion
Supplements:    (%{cli_package_name} and bash-completion)
BuildArch:      noarch

%description -n %{cli_package_name}-bash-completion
Bash command line completion support for %{cli_package_name}.

%package -n %{cli_package_name}-fish-completion
Summary:        Fish Completion for %{cli_package_name}
Group:          System/Shells
Requires:       %{cli_package_name} = %{version}
Supplements:    (%{cli_package_name} and fish)
BuildArch:      noarch

%description -n %{cli_package_name}-fish-completion
Fish command line completion support for %{cli_package_name}.

%package -n %{cli_package_name}-zsh-completion
Summary:        Zsh Completion for %{cli_package_name}
Group:          System/Shells
Requires:       %{cli_package_name} = %{version}
Supplements:    (%{cli_package_name} and zsh)
BuildArch:      noarch

%description -n %{cli_package_name}-zsh-completion
zsh command line completion support for %{cli_package_name}.

%prep
%autosetup -p 1 -a 1

%build
#
# tetragon
#
CGO_ENABLED=0 go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/cilium/tetragon/pkg/version.Version=%{version}" \
   -o bin/%{name} ./cmd/%{name}

# bpf stuff
# https://github.com/cilium/tetragon/blob/main/Makefile#L159
# https://github.com/cilium/tetragon/blob/main/bpf/Makefile
make -C ./bpf BPF_TARGET_ARCH=x86 %{?_smp_mflags}

#
# tetra cli
#
CGO_ENABLED=0 go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X github.com/cilium/tetragon/pkg/version.Version=%{version}" \
   -o bin/%{cli_binary_name} ./cmd/%{cli_binary_name}

%install
#
# tetragon
#
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}
install -D -m 0644 ./install/linux-tarball/systemd/tetragon.service %{buildroot}/%{_unitdir}/%{name}.service
sed -i 's#/local##' %{buildroot}/%{_unitdir}/%{name}.service
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf.d/
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/%{name}.tp.d/
install -D -m 0644 ./install/linux-tarball/usr/local/lib/tetragon/tetragon.conf.d/* %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf.d/
sed -i 's#/local##' %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf.d/*
sed -i 's#/lib/#/lib64/#' %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf.d/bpf-lib

install -d -m 0755 %{buildroot}/%{_libdir}/%{name}/
install -d -m 0755 %{buildroot}/%{_libdir}/%{name}/bpf
install -D -m 0644 ./bpf/objs/*.o  %{buildroot}/%{_libdir}/%{name}/bpf

#
# tetra cli
#
# Install the binary.
install -D -m 0755 bin/%{cli_binary_name} %{buildroot}/%{_bindir}/%{cli_binary_name}

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/%{cli_binary_name} completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/%{cli_binary_name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/%{cli_binary_name} completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{cli_binary_name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d/
%{buildroot}/%{_bindir}/%{cli_binary_name} completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_%{cli_binary_name}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%check

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%dir %attr(755,root, root) %{_sysconfdir}/%{name}/
%dir %attr(755,root, root) %{_sysconfdir}/%{name}/%{name}.conf.d/
%defattr(0644, root, root)
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf.d/*
%dir %attr(755,root, root) %{_libdir}/%{name}
%dir %attr(755,root, root) %{_libdir}/%{name}/bpf/
%attr(644,root, root) %{_libdir}/%{name}/bpf/*

%files -n %{cli_package_name}
%doc README.md
%license LICENSE
%{_bindir}/%{cli_binary_name}

%files -n %{cli_package_name}-bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/%{cli_binary_name}

%files -n %{cli_package_name}-fish-completion
%dir %{_datarootdir}/fish
%dir %{_datarootdir}/fish/vendor_completions.d
%{_datarootdir}/fish/vendor_completions.d/%{cli_binary_name}.fish

%files -n %{cli_package_name}-zsh-completion
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_%{cli_binary_name}

%changelog
