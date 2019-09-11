#
# spec file for package katacontainers
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define  runtime_commit         37c2872f29eb783a7d14119572acf949cd128ac6
%define  proxy_commit           bba9b0ea7f9aafe21e2446e6fd39779c7544f175
%define  shim_commit            638b83a8225ae278ee81db7e27318fd97e249c6d
%define  ksm_throttler_commit   8968863efe4a3bf65b87d0ad247b5cd8826479c6

%ifarch x86_64
%define QEMUCMD qemu-system-x86_64
%else
%ifarch ppc64le
%define QEMUCMD qemu-system-ppc
%else
%define QEMUCMD qemu-system-%{_arch}
%endif
%endif

%define configACRN %{_datarootdir}/defaults/kata-containers/configuration-acrn.toml
%define configFC   %{_datarootdir}/defaults/kata-containers/configuration-fc.toml
%define configNEMU %{_datarootdir}/defaults/kata-containers/configuration-nemu.toml
%define configQEMU %{_datarootdir}/defaults/kata-containers/configuration-qemu.toml
%ifarch x86_64
# Note: braces used for bash brace expansion
%define defaultConfigFiles \{%{configACRN},%{configFC},%{configNEMU},%{configQEMU}\}
%else
%define defaultConfigFiles %{configQEMU}
%endif

Name:           katacontainers
Version:        1.9.0~alpha0
Release:        <CI_CNT>.<B_CNT>
Summary:        Kata Containers core components
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/kata-containers
Source0:        runtime-%{version}.tar.gz
Source1:        proxy-%{version}.tar.gz
Source2:        shim-%{version}.tar.gz
Source3:        ksm-throttler-%{version}.tar.gz
Source4:        kata-fc
Source5:        kata-qemu
Source6:        katacontainers.rpmlintrc
BuildRequires:  fdupes
%if 0%{?suse_version}
BuildRequires:  golang(API) = 1.11
%else
BuildRequires:  go = 1.11
%endif
Requires:       katacontainers-image-initrd  = %{version}
Requires:       kernel-kvmsmall
# Requires: are also required for build, to correctly detect the kernel
# version to use
BuildRequires:  katacontainers-image-initrd  = %{version}
BuildRequires:  kernel-kvmsmall
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
    SKIP_GO_VERSION_CHECK=1 COMMIT=%{runtime_commit} QEMUCMD=%{QEMUCMD}

cd $HOME/go/src/%{kata_project}/proxy
make %{?_smp_mflags} COMMIT=%{proxy_commit}

cd $HOME/go/src/%{kata_project}/shim
make %{?_smp_mflags} COMMIT=%{shim_commit}

cd $HOME/go/src/%{kata_project}/ksm-throttler
make %{?_smp_mflags} COMMIT=%{ksm_throttler_commit} HAVE_SYSTEMD=yes all-installable

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
    COMMIT=%{runtime_commit} \
    QEMUCMD=%{QEMUCMD} \
    install

# Using initrd, so delete the image config line
sed -i -E -e '/^image =/d' %{buildroot}/%{defaultConfigFiles}

# Properly set libexec path
sed -i -E -e 's,/usr/libexec,%{_libexecdir},' %{buildroot}/%{defaultConfigFiles}

cd $HOME/go/src/%{kata_project}/proxy
make \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBEXECDIR=%{_libexecdir} \
    COMMIT=%{proxy_commit} \
    install

cd $HOME/go/src/%{kata_project}/shim
make \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBEXECDIR=%{_libexecdir} \
    COMMIT=%{shim_commit} \
    install

cd $HOME/go/src/%{kata_project}/ksm-throttler
make \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBEXECDIR=%{_libexecdir} \
    COMMIT=%{ksm_throttler_commit} \
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
# Set config to use a matching kernel and initrd version. This is done in %post,
# so that it is using whatever versions the user has installed on its system.
kversion=$(readlink "%{_datarootdir}/kata-containers/kata-containers-initrd.img" | sed -E -e "s,^.*kata-containers-initrd-(.+).img,\1,")
[ -n "${kversion}" ] || { echo "Failed to detect the initrd kernel version"; exit -1; }
ln -sf "/boot/vmlinuz-${kversion}" "%{_datarootdir}/kata-containers/vmlinuz"
sed -i -E -e "s,^kernel =.*$,kernel = \"%{_datarootdir}/kata-containers/vmlinuz\"," %{defaultConfigFiles}

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
# Default configs
%dir %{_datarootdir}/defaults
%dir %{_datarootdir}/defaults/kata-containers
%doc %{_datarootdir}/defaults/kata-containers/configuration-qemu.toml
%ifarch x86_64
%doc %{_datarootdir}/defaults/kata-containers/configuration-acrn.toml
%doc %{_datarootdir}/defaults/kata-containers/configuration-fc.toml
%doc %{_datarootdir}/defaults/kata-containers/configuration-nemu.toml
%endif
%doc %{_datarootdir}/defaults/kata-containers/configuration.toml
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
