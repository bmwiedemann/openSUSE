#
# spec file for package bbswitch
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
%global modprobe_d_files 50-bbswitch.conf

Name:           bbswitch
Version:        0.8
Release:        0
Summary:        Bumblebee ACPI kernel module
License:        GPL-2.0-or-later
Group:          System/Kernel
URL:            http://github.com/Bumblebee-Project/bbswitch
Source0:        https://github.com/Bumblebee-Project/bbswitch/archive/v%{version}.tar.gz
Patch0:         bbswitch-fix-header-inclusion.patch
Patch1:         0001-Update-proc_create_call-for-5.6-kernel.patch
Patch2:         fix-deprecated-acpi_bus_get_device-in-5.18.patch
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  libelf-devel
BuildRequires:  pkgconfig(libsystemd)
Requires:       bbswitch-kmp
# DKMSing this module has no point for us so obsolete the package
# Remove this after 13.2 release
Provides:       bbswitch-dkms = %{version}
Obsoletes:      bbswitch-dkms < %{version}
Provides:       dkms-bbswitch = %{version}
Obsoletes:      dkms-bbswitch < %{version}
ExclusiveArch:  %{ix86} x86_64
%kernel_module_package

%description
bbswitch is a kernel module which automatically detects the required
ACPI calls for two kinds of Optimus laptops.

%prep
%setup -q
%patch0 -p1
%if %{?pkg_vcmp:%{pkg_vcmp kernel-devel >= 5.6.0}}%{!?pkg_vcmp:0}
%patch1 -p1
%endif
%if %{?pkg_vcmp:%{pkg_vcmp kernel-devel >= 5.18.1}}%{!?pkg_vcmp:0}
%patch2 -p1
%endif
set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
for flavor in %{flavors_to_build}; do
        rm -rf obj/$flavor
        cp -r source obj/$flavor
        make %{?_smp_mflags} -C %{kernel_source $flavor} %{?linux_make_arch} modules M=$PWD/obj/$flavor
done

%install
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
for flavor in %{flavors_to_build}; do
        make -C %{kernel_source $flavor} %{?linux_make_arch} modules_install M=$PWD/obj/$flavor
done
install -dm755 %{buildroot}%{_prefix}/lib/modules-load.d
echo "bbswitch" >> %{buildroot}%{_prefix}/lib/modules-load.d/bbswitch.conf
install -dm755 %{buildroot}%{_modprobedir}/
echo "options bbswitch load_state=0 unload_state=1" >> %{buildroot}%{_modprobedir}/50-bbswitch.conf

%pre
# Avoid restoring outdated stuff in posttrans
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -f "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}.rpmsave.old" || :
done

%posttrans
# Migration of modprobe.conf files to _modprobedir
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -fv "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}" || :
done

%files
%doc source/COPYING source/README.md source/NEWS
%dir %{_prefix}/lib/modules-load.d
%{_prefix}/lib/modules-load.d/bbswitch.conf
%{_modprobedir}/50-bbswitch.conf

%changelog
