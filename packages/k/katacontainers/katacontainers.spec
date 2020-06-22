#
# spec file for package katacontainers
#
# Copyright (c) 2020 SUSE LLC
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


#
%define  kata_project          github.com/kata-containers

%ifarch x86_64
%define QEMUCMD qemu-system-x86_64
%else
%ifarch ppc64le
%define QEMUCMD qemu-system-ppc
%else
%define QEMUCMD qemu-system-%{_arch}
%endif
%endif

%define configPath %{_datarootdir}/defaults/kata-containers/
%define configACRN configuration-acrn.toml
%define configFC   configuration-fc.toml
%define configQEMU configuration-qemu.toml
%ifarch x86_64
# Note: braces used for bash brace expansion
%define defaultConfigFiles \{%{configACRN},%{configFC},%{configQEMU}\}
%else
%define defaultConfigFiles %{configQEMU}
%endif

Name:           katacontainers
Version:        1.11.1
Release:        0
Summary:        Kata Containers OCI container runtime
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/kata-containers
Source0:        runtime-%{version}.tar.xz
Source1:        proxy-%{version}.tar.xz
Source2:        shim-%{version}.tar.xz
Source3:        ksm-throttler-%{version}.tar.xz
Source4:        kata-fc
Source5:        kata-qemu
Source6:        katacontainers.rpmlintrc
ExclusiveArch:  x86_64 aarch64 ppc64le s390x
BuildRequires:  fdupes
BuildRequires:  golang(API) >= 1.12
Requires:       katacontainers-image-initrd  = %{version}
# Requires: are also required for build, to correctly detect the kernel
# version to use
BuildRequires:  katacontainers-image-initrd  = %{version}
# Required for build to correctly detect the kernel version to use
%ifarch x86_64
Requires:       qemu-x86
Recommends:     firecracker
%endif
%ifarch aarch64
Requires:       qemu-arm
%endif
%ifarch ppc64le
Requires:       qemu-ppc
%endif

%description
Kata Containers is an open source container runtime, building lightweight
virtual machines that seamlessly plug into the containers ecosystem.

%prep
%setup -q -c -a1 -a2 -a3

%build
export GOPATH=$HOME/go
rm -rf $HOME/go/src

suffix="-%{version}*"
dirs=($(ls -d {proxy,runtime,shim,ksm-throttler}${suffix}))

for d in ${dirs[@]}; do
    pkg=${d%$suffix}
    dest="$HOME/go/src/%{kata_project}/$pkg"
    mkdir -pv "$dest"
    cp    -avr "$d"/* "$dest"
done

cd $HOME/go/src/%{kata_project}/runtime
make %{?_smp_mflags} \
    SKIP_GO_VERSION_CHECK=1 QEMUCMD=%{QEMUCMD}

cd $HOME/go/src/%{kata_project}/proxy
make %{?_smp_mflags}

cd $HOME/go/src/%{kata_project}/shim
make %{?_smp_mflags}

cd $HOME/go/src/%{kata_project}/ksm-throttler
make %{?_smp_mflags} HAVE_SYSTEMD=yes all-installable

%check
# No tests

%install
export GOPATH=$HOME/go

cd $HOME/go/src/%{kata_project}/runtime
make \
    SKIP_GO_VERSION_CHECK=1 \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBEXECDIR=%{_libexecdir} \
    QEMUCMD=%{QEMUCMD} \
    install

# Only initrd is supported: delete the "image =" entries only in files where
# both "image =" and "initrd =" is specified
for f in %{buildroot}%{configPath}/%{defaultConfigFiles}; do
  grep -q "^image =" "$f" && grep -q "^initrd = " "$f" && sed -i -E -e '/^image =/d' $f
done

# Replace /usr/libexec path with /usr/lib
sed -i -E \
    -e "s,/usr/libexec,%{_libexecdir}," \
    -e "s,^kernel =.*$,kernel = \"%{_datarootdir}/kata-containers/vmlinuz\"," \
    %{buildroot}%{configPath}/%{defaultConfigFiles}

install -m 644 -D %{buildroot}%{configPath}/configuration.toml %{buildroot}%{_sysconfdir}/kata-containers/configuration.toml

cd $HOME/go/src/%{kata_project}/proxy
make \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBEXECDIR=%{_libexecdir} \
    install

cd $HOME/go/src/%{kata_project}/shim
make \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBEXECDIR=%{_libexecdir} \
    install

cd $HOME/go/src/%{kata_project}/ksm-throttler
make \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBEXECDIR=%{_libexecdir} \
    HAVE_SYSTEMD=yes \
    UNIT_DIR=%{_unitdir} \
    V=1 \
    install

sed -i -E -e 's,/usr/libexec,%{_libexecdir},' \
    %{buildroot}/%{_unitdir}/kata-ksm-throttler.service \
    %{buildroot}/%{_unitdir}/kata-vc-throttler.service

# symlink /usr/sbin/rcFOO -> /usr/sbin/service
install -d %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rckata-ksm-throttler
ln -s service %{buildroot}%{_sbindir}/rckata-vc-throttler

# install kata runtime helpers
install -m 755 %{SOURCE4} %{buildroot}%{_bindir}/kata-fc
install -m 755 %{SOURCE5} %{buildroot}%{_bindir}/kata-qemu

%fdupes %{buildroot}/%{_prefix}

%pre
%service_add_pre kata-ksm-throttler.service
%service_add_pre kata-vc-throttler.service

%post
%service_add_post kata-ksm-throttler.service
%service_add_post kata-vc-throttler.service

%preun
%service_del_preun kata-ksm-throttler.service
%service_del_preun kata-vc-throttler.service

%postun
%service_del_postun kata-ksm-throttler.service
%service_del_postun kata-vc-throttler.service

%files
%defattr(-,root,root,-)
# Runtime
# Binaries
%{_bindir}/kata-runtime
%{_bindir}/kata-fc
%{_bindir}/kata-qemu
%{_bindir}/containerd-shim-kata-v2
%dir %{_libexecdir}/kata-containers
%{_libexecdir}/kata-containers/kata-netmon
%{_bindir}/kata-collect-data.sh
# Manpages
# Configs
%dir %{_sysconfdir}/kata-containers
%config(noreplace) %{_sysconfdir}/kata-containers/configuration.toml
# Default configs
%dir %{_datarootdir}/defaults
%dir %{_datarootdir}/defaults/kata-containers
%config %{_datarootdir}/defaults/kata-containers/configuration.toml
%config %{_datarootdir}/defaults/kata-containers/configuration-*.toml
# Completion
%{_datarootdir}/bash-completion/completions/kata-runtime

# proxy
# Binaries
%{_libexecdir}/kata-containers/kata-proxy

# shim
# Binaries
%{_libexecdir}/kata-containers/kata-shim

# ksm-throttler
%dir %{_libexecdir}/kata-ksm-throttler
%dir %{_libexecdir}/kata-ksm-throttler/trigger
%dir %{_libexecdir}/kata-ksm-throttler/trigger/virtcontainers
# Binaries
%{_libexecdir}/kata-ksm-throttler/kata-ksm-throttler
%{_libexecdir}/kata-ksm-throttler/trigger/virtcontainers/vc
%{_sbindir}/rckata-ksm-throttler
%{_sbindir}/rckata-vc-throttler
# systemd
%{_unitdir}/kata-ksm-throttler.service
%{_unitdir}/kata-vc-throttler.service

%license runtime-%{version}/LICENSE

%changelog
