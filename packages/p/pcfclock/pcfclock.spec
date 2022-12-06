#
# spec file for package pcfclock
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
%global modprobe_d_files 50-pcfclock.conf

Name:           pcfclock
Version:        0.44
Release:        0
Summary:        Pcfclock kernel driver
License:        GPL-2.0-or-later
Group:          System/Kernel
URL:            http://www-stud.ims.uni-stuttgart.de/~voegelas/pcf.html
Source:         pcfclock-%{version}.tar.gz
Source1:        Makefile
Source2:        preamble
Source3:        pcfclock.conf
Patch0:         pcfclock-nomodule.patch
Patch1:         pcfclock-module_param.patch
Patch2:         pcfclock-no_devfs.patch
Patch3:         pcfclock-include.patch
Patch4:         pcfclock-linux-3.19.patch
Patch5:         pcfclock-linux-4.12.patch
Patch6:         pcfclock-linux-5.8.patch
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  kernel-source
BuildRequires:  kernel-syms
BuildRequires:  libelf-devel
BuildRequires:  module-init-tools
Requires:       pcfclock-kmp
# systemd-tmpfiles
Requires(post): systemd
ExcludeArch:    s390 s390x
%suse_kernel_module_package -p %_sourcedir/preamble kdump um xen xenpae iseries64

%description
The pcfclock(4) driver for GNU/Linux supports the parallel port radio
clock sold by Conrad Electronic under order number 967602. The radio
clock, which is put between your parallel port and your printer,
receives the legal German time, i.e. CET or CEST, from the DCF77
transmitter and uses it to set its internal quartz clock. The DCF77
transmitter is located near to Frankfurt/Main and covers a radius of
more than 1500 kilometers.

%package KMP
Summary:        Pcfclock kernel driver
Group:          System/Kernel

%description KMP
The pcfclock(4) driver for GNU/Linux supports the parallel port radio
clock sold by Conrad Electronic under order number 967602. The radio
clock, which is put between your parallel port and your printer,
receives the legal German time, i.e. CET or CEST, from the DCF77
transmitter and uses it to set its internal quartz clock. The DCF77
transmitter is located near to Frankfurt/Main and covers a radius of
more than 1500 kilometers.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
mkdir source
mkdir obj
cp -a linux/pcfclock.c %{SOURCE1} \
	source

%build
%configure --without-linux
make %{?_smp_mflags}
for flavor in %flavors_to_build; do
    rm -rf obj/$flavor
    cp -r source obj/$flavor
    make -C /usr/src/linux-obj/%_target_cpu/$flavor %{?linux_make_arch} modules \
         M=$PWD/obj/$flavor %{?_smp_mflags}
done

%install
%make_install
# install manpage
make -C linux install DESTDIR=%{buildroot}
# install kernel modules
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
for flavor in %flavors_to_build; do
    make -C /usr/src/linux-obj/%_target_cpu/$flavor %{?linux_make_arch} modules_install \
         M=$PWD/obj/$flavor
done
mkdir -p %{buildroot}%{_modprobedir}
echo "alias char-major-181 pcfclock" > %{buildroot}%{_modprobedir}/50-pcfclock.conf
%if 0%{?suse_version} > 1140
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}
%endif

%pre
# Avoid restoring outdated stuff in posttrans
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -f "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}.rpmsave.old" || :
done

%post
# Create devices nodes at installation time
systemd-tmpfiles --create %{_tmpfilesdir}/pcfclock.conf

%posttrans
# Migration of modprobe.conf files to _modprobedir
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -fv "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}" || :
done

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man4/pcfclock.4%{?ext_man}
%{_mandir}/man8/pcfdate.8%{?ext_man}
%{_sbindir}/pcfdate
%{_modprobedir}/50-pcfclock.conf
%if 0%{?suse_version} > 1140
%{_tmpfilesdir}/pcfclock.conf
%endif

%changelog
