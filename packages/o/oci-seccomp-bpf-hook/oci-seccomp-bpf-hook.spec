#
# spec file for package oci-seccomp-bpf-hook
#
# Copyright (c) 2021 SUSE LLC
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


%define project github.com/containers/oci-seccomp-bpf-hook

# Define macros for further referenced sources
Name:           oci-seccomp-bpf-hook
Version:        1.2.1
Release:        0
Summary:        OCI hook to trace syscalls and generate a seccomp profile
License:        Apache-2.0
URL:            https://github.com/containers/oci-seccomp-bpf-hook
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  bcc-devel
BuildRequires:  glib2-devel-static
BuildRequires:  glibc-devel-static
BuildRequires:  go-go-md2man
BuildRequires:  golang-packaging
BuildRequires:  kernel-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libseccomp-devel
BuildRequires:  golang(API) = 1.15

# disable stripping of binaries
%{go_nostrip}

%description
This project provides an OCI hook to generate seccomp profiles by tracing the
syscalls made by the container. The generated profile would allow all the
syscalls made and deny every other syscall.

The syscalls are traced by launching a binary by using the prestart OCI hook.
The binary started spawns a child process which attaches function enter_trace
to the raw_syscalls:sys_enter tracepoint using eBPF. The function looks at all
the syscalls made on the system and writes the syscalls which have the same PID
namespace as the container to the perf buffer. The perf buffer is read by the
process in the userspace and generates a seccomp profile when the container
exits.

%prep
%setup -q

%build

# We can't use symlinks here because go-list gets confused by symlinks, so we
# have to copy the source to $HOME/go and then use that as the GOPATH.
export GOPATH=$HOME/go
mkdir -pv $HOME/go/src/%{project}
rm -rf $HOME/go/src/%{project}/*
cp -avr * $HOME/go/src/%{project}
cd $HOME/go/src/%{project}

%make_build

%install

# binary
cd $HOME/go/src/%{project}
install -D -m 0755 bin/%{name} %{buildroot}/%{_libexecdir}/oci/hooks.d/%{name}

# config
sed -i 's|HOOK_BIN_DIR|%{_libexecdir}/oci/hooks.d|g' oci-seccomp-bpf-hook.json
install -D -m 0644 %{name}.json %{buildroot}/%{_datadir}/containers/oci/hooks.d/%{name}.json

# docs
install -D -m 0644 docs/%{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files

# meta
%license LICENSE
%doc README.md

# binary
%dir %{_libexecdir}/oci
%dir %{_libexecdir}/oci/hooks.d
%{_libexecdir}/oci/hooks.d/%{name}

# config
%dir %{_datadir}/containers
%dir %{_datadir}/containers/oci
%dir %{_datadir}/containers/oci/hooks.d
%{_datadir}/containers/oci/hooks.d/%{name}.json

# docs
%{_mandir}/man1/%{name}.1*

%changelog
