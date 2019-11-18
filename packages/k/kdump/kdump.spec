#
# spec file for package kdump
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


# on systemd distros, rpm-build requires systemd-rpm-macros,
# which in turn defines %systemd_requires
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define systemd_present %{defined systemd_requires}

%define dracutlibdir %{_prefix}/lib/dracut

%{!?_udevdir: %global _udevdir %(pkg-config --variable=udevdir udev)}
%if "%{_udevdir}" == ""
%if 0%{?suse_version} >= 1230
%global _udevdir /usr/lib/udev
%else
%global _udevdir /lib/udev
%endif
%endif
%define _udevrulesdir %{_udevdir}/rules.d

Name:           kdump
Version:        0.9.0
Release:        0
Summary:        Script for kdump
License:        GPL-2.0-or-later
Group:          System/Kernel
Url:            https://github.com/openSUSE/kdump
Source:         %{name}-%{version}.tar.bz2
Source2:        %{name}-rpmlintrc
Patch1:         %{name}-fillupdir-fixes.patch
Patch2:         %{name}-block-initrd-parse-etc.service.patch
Patch3:         %{name}-fadump-avoid-multipath-optimizations.patch
Patch4:         %{name}-split-cmdline-purpose-wise.patch
Patch5:         %{name}-fadump-fix-network-bring-up.patch
Patch6:         %{name}-fadump-add-udev-support.patch
Patch7:         %{name}-turn-off-NUMA-in-kdump-kernel.patch
Patch8:         %{name}-remove-noefi-and-acpi_rsdp-for-efi-firmware.patch
Patch9:         %{name}-use-pbl.patch
Patch10:        %{name}-on-error-option-yesno.patch
Patch11:        %{name}-Restore-only-static-routes-in-kdump-initrd.patch
Patch12:        %{name}-fallback-re-register-fadump-from-userspace.patch
Patch13:        %{name}-recover-from-missing-CRASHTIME.patch
Patch14:        %{name}-fix-multipath-user_friendly_names.patch
Patch15:        %{name}-Add-skip_balance-option-to-BTRFS-mounts.patch
Patch16:        %{name}-kdumprd-Look-for-boot-image-and-boot-Image.patch
Patch17:        %{name}-savedump-search-also-for-vmlinux.xz.patch
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libblkid-devel
BuildRequires:  libcurl-devel
BuildRequires:  libelf-devel
BuildRequires:  libesmtp-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  udev
BuildRequires:  zlib-devel
Requires:       curl
Requires:       kexec-tools
Requires:       makedumpfile
Requires:       openssh
PreReq:         %fillup_prereq
PreReq:         coreutils
PreReq:         sed
Recommends:     cifs-utils
Recommends:     nfs-client
#!BuildIgnore:  fop
# update should detect the split-off from kexec-tools
Provides:       kexec-tools:%{_initddir}/kdump
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 ppc
%if %{systemd_present}
BuildRequires:  pkgconfig(systemd)
%else
PreReq:         %insserv_prereq
%endif
PreReq:         dracut
%if %{systemd_present}
%systemd_requires
%endif

%description
kdump is a package that includes several scripts for kdump, including
the kdump service and configuration files

The kernel package and this package are all that are required for a
crash dump to occur. However, if you wish to debug the crash dump
yourself you will need several debugging packages installed for each
kernel flavor and release you wish to debug.

For example, if you are debugging kernel-default, you will need:
- kernel-default-debuginfo
- kernel-default-devel
- kernel-default-devel-debuginfo

These packages are not needed to create the dump and can be installed
after a crash dump has occured.

%prep
%setup -q
%if 0%{?suse_version} >= 1330
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags} -std=gnu++98"
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
make %{?_smp_mflags}
cd -

%check
cd build
make %{?_smp_mflags} test

%install
cd build
make %{?_smp_mflags} DESTDIR=%{buildroot} install
cd -
# move udev rules
mkdir -p %{buildroot}/%{_udevrulesdir}
mv %{buildroot}/%{_sysconfdir}/udev/rules.d/* %{buildroot}/%{_udevrulesdir}/
# remove executable bit from non-binaries
chmod -x %{buildroot}/lib/kdump/setup-kdump.functions
# empty directory
mkdir -p %{buildroot}/var/crash

# symlink for init script
%if %{systemd_present}
rm %{buildroot}%{_initddir}/boot.kdump
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rckdump
%else
rm %{buildroot}/usr/lib/systemd/system/kdump.service
rm %{buildroot}/usr/lib/systemd/system/kdump-early.service
ln -s ../..%{_initddir}/boot.kdump %{buildroot}%{_sbindir}/rckdump
%endif

%if %{systemd_present}
%pre
%service_add_pre kdump.service
%service_add_pre kdump-early.service
%endif

%post
# change only permission if the file exists before /etc/sysconfig/kdump
# has been created from %{_fillupdir}/sysconfig.kdump
change_permission=0
if [ ! -f %{_sysconfdir}/sysconfig/kdump ] ; then
    change_permission=1
fi
%if %{systemd_present}
%{fillup_only -n kdump}
%service_add_post kdump.service
%service_add_post kdump-early.service
# ensure newly added kdump-early.service is-enabled matches prior state
if [ -x /usr/bin/systemctl ] && /usr/bin/systemctl is-enabled kdump.service &>/dev/null ; then
	/usr/bin/systemctl reenable kdump.service || :
fi
%else
%{fillup_and_insserv -n kdump boot.kdump}
%endif
if [ "$change_permission" = 1 ]; then
    chmod 0600 %{_sysconfdir}/sysconfig/kdump
fi
# if /var/log/dump is empty, make it a symlink to /var/crash
if test -d /var/log/dump && rmdir /var/log/dump >/dev/null 2>&1 ||
        ! test -d /var/log/dump ; then
    ln -snf /var/crash /var/log/dump
fi

%preun
echo "Stopping kdump ..."
%if %{systemd_present}
%service_del_preun kdump.service
%service_del_preun kdump-early.service
%else
%stop_on_removal boot.kdump
%endif

%postun
# force regeneration of kdumprd
touch %{_sysconfdir}/sysconfig/kdump
# delete symbolic link
rm /var/log/dump >/dev/null 2>&1 || true
%if %{systemd_present}
%service_del_postun kdump.service
%service_del_postun kdump-early.service
%else
%restart_on_update boot.kdump
%insserv_cleanup
%endif

# Compatibility cruft
# there is no %license prior to SLE12
%if %{undefined _defaultlicensedir}
%define license %doc
%else
# filesystem before SLE12 SP3 lacks /usr/share/licenses
%if 0%(test ! -d %{_defaultlicensedir} && echo 1)
%define _defaultlicensedir %_defaultdocdir
%endif
%endif
# End of compatibility cruft

%files
%defattr(-,root,root)
%license COPYING
%doc ChangeLog README NEWS
%{_sbindir}/kdumptool
%{_sbindir}/mkdumprd
%{_mandir}/man5/kdump.5%{ext_man}
%{_mandir}/man7/kdump.7%{ext_man}
%{_mandir}/man8/kdumptool.8%{ext_man}
%{_mandir}/man8/mkdumprd.8%{ext_man}
%{_fillupdir}/sysconfig.kdump
%dir %{dracutlibdir}
%dir %{dracutlibdir}/modules.d
%{dracutlibdir}/modules.d/99kdump/
%dir /lib/kdump
/lib/kdump/*
%{_udevrulesdir}/70-kdump.rules
%if %{systemd_present}
%{_unitdir}/kdump.service
%{_unitdir}/kdump-early.service
%else
%{_sysconfdir}/init.d/boot.kdump
%endif
%{_sbindir}/rckdump

%changelog
