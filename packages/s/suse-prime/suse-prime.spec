#
# spec file for package suse-prime
#
# Copyright (c) 2022 SUSE LLC
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


%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150300
# systemd-rpm-macros is wrong in 15.3 and below
%define _modprobedir /lib/modprobe.d
%endif
%global modprobe_d_files 09-nvidia-modprobe-bbswitch-G04.conf 09-nvidia-modprobe-pm-G05.conf

Name:           suse-prime
Version:        0.8.10
Release:        0
Summary:        GPU (nvidia/intel) selection for NVIDIA optimus laptops with bbswitch support
License:        SUSE-Public-Domain
Group:          System/X11/Utilities
URL:            https://github.com/openSUSE/SUSEPrime
Source0:        https://github.com/openSUSE/SUSEPrime/archive/%{version}.tar.gz#/SUSEPrime-%{version}.tar.gz
Recommends:     nvidia_driver
Supplements:    modalias(nvidia_driver:pci:v00008086d*sv*sd*bc03sc*i*)
Conflicts:      suse-prime-alt
Obsoletes:      suse-prime-bbswitch < %{version}
Provides:       suse-prime-bbswitch = %{version}
BuildRequires:  pkgconfig(systemd)
BuildArch:      noarch
Requires:       coreutils
Requires:       sudo
%{?systemd_ordering}

%description
A collection of shell scripts that makes it possible to use the
NVIDIA GPU on a Optimus Laptop. The switching is similar to
the feature provided by the nvidia-prime package in Ubuntu.
Uses bbswitch to switch on/of power of NVIDIA GPU.

%prep
%setup -n SUSEPrime-%{version}

%build
:

%install
mkdir -p %{buildroot}%{_datadir}/prime
install -m 0644 xorg-intel.conf  %{buildroot}%{_datadir}/prime/
install -m 0644 xorg-intel-intel.conf  %{buildroot}%{_datadir}/prime/
install -m 0644 xorg-nvidia.conf %{buildroot}%{_datadir}/prime/
install -m 0644 xorg-nvidia-prime-render-offload.conf %{buildroot}%{_datadir}/prime/
install -m 0644 xorg-amd.conf %{buildroot}%{_datadir}/prime/
mkdir -p %{buildroot}%{_modprobedir}
install -m 0644 09-nvidia-modprobe-bbswitch-G04.conf %{buildroot}%{_modprobedir}/
install -m 0644 09-nvidia-modprobe-pm-G05.conf %{buildroot}%{_modprobedir}/
%if 0%{?suse_version} >= 1550
mkdir -p %{buildroot}/usr/lib/dracut/dracut.conf.d/
install -m 0644 90-nvidia-dracut-G05.conf %{buildroot}/usr/lib/dracut/dracut.conf.d/
%else
mkdir -p %{buildroot}/etc/dracut.conf.d
install -m 0644 90-nvidia-dracut-G05.conf %{buildroot}/etc/dracut.conf.d
%endif
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 prime-select.service %{buildroot}%{_unitdir}/
install -D -m 0755 prime-select.sh %{buildroot}%{_sbindir}/prime-select
mkdir -p %{buildroot}/usr/lib/udev/rules.d
install -m 0644 90-nvidia-udev-pm-G05.rules %{buildroot}/usr/lib/udev/rules.d
mkdir -p %{buildroot}/usr/sbin
ln -snf service %{buildroot}/usr/sbin/rcprime-select

%pre
%service_add_pre prime-select.service
# Avoid restoring outdated stuff in posttrans
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -f "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}.rpmsave.old" || :
done

%post
%{?regenerate_initrd_post}
%service_add_post prime-select.service
systemctl enable prime-select.service

%preun
%service_del_preun prime-select.service
if [ "$1" -eq 0 ]; then
   # cleanup before uninstalling the package completely
   export PATH=$PATH:/usr/sbin
   %{_sbindir}/prime-select unset || true
fi

%postun
if [ "$1" -eq 0 ]; then
   true
   %{?regenerate_initrd_post}
   %service_del_postun prime-select.service
fi

%posttrans
# Migration of modprobe.conf files to _modprobedir
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -fv "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}" || :
done
%{?regenerate_initrd_posttrans}

%triggerin -- nvidia-gfxG05-kmp-default
# get rid of nvidia kernel modules in initrd
rm -f /etc/dracut.conf.d/50-nvidia-default.conf
%{?regenerate_initrd_post}

%files
%defattr(-,root,root)
%doc README.md
%if 0%{?suse_version} >= 1550
%dir /usr/lib/dracut/
%dir /usr/lib/dracut/dracut.conf.d/
%else
/etc/dracut.conf.d
%endif
%dir %{_datadir}/prime
%{_datadir}/prime/xorg-amd.conf
%{_datadir}/prime/xorg-intel.conf
%{_datadir}/prime/xorg-intel-intel.conf
%{_datadir}/prime/xorg-nvidia.conf
%{_datadir}/prime/xorg-nvidia-prime-render-offload.conf
%ghost %dir %{_sysconfdir}/prime
%ghost %config(noreplace) %{_sysconfdir}/prime/current_type
%{_sbindir}/prime-select
%{_sbindir}/rcprime-select
%dir %{_modprobedir}
%{_modprobedir}/09-nvidia-modprobe-bbswitch-G04.conf
%{_modprobedir}/09-nvidia-modprobe-pm-G05.conf
%if 0%{?suse_version} >= 1550
/usr/lib/dracut/dracut.conf.d/90-nvidia-dracut-G05.conf
%else
/etc/dracut.conf.d/90-nvidia-dracut-G05.conf
%endif
/usr/lib/udev/rules.d/90-nvidia-udev-pm-G05.rules
%{_unitdir}/prime-select.service

%changelog
