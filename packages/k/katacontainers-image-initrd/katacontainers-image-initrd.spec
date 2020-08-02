#
# spec file for package katacontainers-image-initrd
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
%define kata_agent_project    github.com/kata-containers/agent

# Platforms that supports kvm specific kernels
%ifarch x86_64
%define kernel_flavor         kvmsmall
%else
%define kernel_flavor         default
%endif

%ifarch x86_64
%define kernel_basename       vmlinuz
%endif

%ifarch ppc64le
%define kernel_basename       vmlinux
%endif

%ifarch aarch64
%define kernel_basename       Image
%define kernel_compress       1
%endif

%ifarch s390x
%define kernel_basename       image
%endif

Name:           katacontainers-image-initrd
Version:        1.11.1
Release:        0
Summary:        Kata Containers image (initrd) and kernel
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/kata-containers/osbuilder
Source0:        osbuilder-%{version}.tar.xz
Source1:        agent-%{version}.tar.xz
ExclusiveArch:  x86_64 aarch64 ppc64le s390x
BuildRequires:  dracut
BuildRequires:  fdupes
BuildRequires:  kernel-%{kernel_flavor}
BuildRequires:  golang(API) >= 1.12
Provides:       katacontainers-image

%description
Kata Containers image (in initrd format) and kernel used for the ephemeral VMs
used to run containers.

%prep
%setup -q -n osbuilder-%{version} -b1

%build
export GOPATH=$HOME/go
rm -rf $HOME/go/src/%{kata_agent_project}
mkdir -pv $HOME/go/src/%{kata_agent_project}
cp -avr ../agent-%{version}/* $HOME/go/src/%{kata_agent_project}

kata_kmodules=(9p 9pnet 9pnet_virtio)

%if 0%{?suse_version} <= 1500 || %{kernel_flavor} != "kvmsmall"
kata_kmodules+=( \
virtio \
virtio_pci \
virtio_balloon \
virtio_blk \
virtio_console \
virtio_crypto \
virtio-gpu \
virtio_input \
virtio_net \
virtio-rng \
virtio_scsi \
vmw_vsock_virtio_transport \
vmw_vsock_virtio_transport_common \
)
%endif

# Minimal set of kernel modules to allow starting containers
echo "drivers=\"${kata_kmodules[@]}\"" > dracut/dracut.conf.d/10-drivers.conf
kversion="$(find /boot -name '%{kernel_basename}-*%{kernel_flavor}' | sed 's,/boot/%{kernel_basename}-,,' | sort | tail -n 1)"
echo "Found kernel version: ${kversion}"
echo "${kversion}" > %{_builddir}/kversion

make \
    BUILD_METHOD=dracut \
    DRACUT_KVERSION=${kversion} \
    clean initrd

%check
# (tested manually)

%install
read kversion < %{_builddir}/kversion
# image
install -m 0644 -D kata-containers-initrd.img %{buildroot}%{_datarootdir}/kata-containers/kata-containers-initrd-${kversion}.img
ln -sf kata-containers-initrd-${kversion}.img %{buildroot}%{_datarootdir}/kata-containers/kata-containers-initrd.img

#kernel
vmKernelDest="%{buildroot}%{_datarootdir}/kata-containers/%{kernel_basename}-${kversion}"
%if 0%{?kernel_compress}
gzip -c /boot/%{kernel_basename}-${kversion} > ${vmKernelDest}.gz
%else
install -m 0644 -D /boot/%{kernel_basename}-${kversion} ${vmKernelDest}
%endif
ln -sf "$(basename "${vmKernelDest}%{?kernel_compress:.gz}")" %{buildroot}%{_datarootdir}/kata-containers/vmlinuz

%fdupes %{buildroot}/%{_prefix}

%files
%defattr(-,root,root,-)
%dir %{_datarootdir}/kata-containers
%{_datarootdir}/kata-containers/kata-containers-initrd.img
%{_datarootdir}/kata-containers/kata-containers-initrd-*-%{kernel_flavor}.img
%{_datarootdir}/kata-containers/vmlinuz
%{_datarootdir}/kata-containers/%{kernel_basename}-*-%{kernel_flavor}%{?kernel_compress:.gz}
%license LICENSE

%changelog
