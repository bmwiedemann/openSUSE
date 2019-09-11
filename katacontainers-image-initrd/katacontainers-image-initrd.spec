#
# spec file for package katacontainers-image-initrd
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
%define kata_agent_project    github.com/kata-containers/agent
%define kata_modules_required 9p 9pnet_virtio
%define kernel_flavor         kvmsmall

Name:           katacontainers-image-initrd
Version:        1.9.0~alpha0
Release:        0
Summary:        Kata Containers OSbuilder
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/kata-containers/osbuilder
Source0:        osbuilder-%{version}.tar.gz
Source1:        agent-%{version}.tar.gz
BuildRequires:  dracut
BuildRequires:  fdupes
BuildRequires:  kernel-%{kernel_flavor}
BuildRequires:  golang(API) = 1.11
Provides:       katacontainers-image

%description
initrd used as guest VM in Kata Containers, built using dracut.

%prep
%setup -q -n osbuilder-%{version} -b1

%build
export GOPATH=$HOME/go
rm -rf $HOME/go/src/%{kata_agent_project}
mkdir -pv $HOME/go/src/%{kata_agent_project}
cp -avr ../agent-%{version}/* $HOME/go/src/%{kata_agent_project}

# Minimal set of drivers to allow starting containers
echo 'drivers="%{kata_modules_required}"' > dracut/dracut.conf.d/10-drivers.conf
kversion="$(find /boot -name 'vmlinuz-*%{kernel_flavor}' | sed 's,/boot/vmlinuz-,,' | sort | tail -n 1)"
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
install -m 0644 -D kata-containers-initrd.img %{buildroot}%{_datarootdir}/kata-containers/kata-containers-initrd-${kversion}.img
ln -sf kata-containers-initrd-${kversion}.img %{buildroot}%{_datarootdir}/kata-containers/kata-containers-initrd.img

%fdupes %{buildroot}/%{_prefix}

%files
%defattr(-,root,root,-)
%dir %{_datarootdir}/kata-containers
%{_datarootdir}/kata-containers/kata-containers-initrd.img
%{_datarootdir}/kata-containers/kata-containers-initrd-*-%{kernel_flavor}.img
%license LICENSE

%changelog
