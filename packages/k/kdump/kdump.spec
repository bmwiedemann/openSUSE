#
# spec file for package kdump
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

%define dracutlibdir %{_prefix}/lib/dracut

Name:           kdump
Version:        0.9.0
Release:        0
Summary:        Script for kdump
License:        GPL-2.0-or-later
Group:          System/Kernel
URL:            https://github.com/openSUSE/kdump
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
Patch18:        %{name}-preserve-white-space.patch
Patch19:        %{name}-Clean-up-the-use-of-current-vs-boot-network-iface.patch
Patch20:        %{name}-Use-a-custom-namespace-for-physical-NICs.patch
Patch21:        %{name}-clean-up-kdump-mount-points.patch
Patch22:        %{name}-skip-mounts-if-no-proc-vmcore.patch
Patch23:        %{name}-nss-modules.patch
Patch24:        %{name}-Add-force-option-to-KDUMP_NETCONFIG.patch
Patch25:        %{name}-Add-fence_kdump_send-when-fence-agents-installed.patch
Patch26:        %{name}-FENCE_KDUMP_SEND-variable.patch
Patch27:        %{name}-Document-fence_kdump_send.patch
Patch28:        %{name}-powerpc-no-reload-on-CPU-removal.patch
Patch29:        %{name}-prefer-by-path-and-device-mapper.patch
Patch30:        %{name}-calibrate-Update-values.patch
Patch31:        %{name}-activate-udev-rules-late-during-boot.patch
Patch32:        %{name}-make-sure-that-the-udev-runtime-directory-exists.patch
Patch33:        %{name}-make-sure-that-initrd.target.wants-directory-exists.patch
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
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
#!BuildIgnore:  fop
Requires:       /usr/bin/sed
Requires:       curl
Requires:       dracut
Requires:       kexec-tools
Requires:       makedumpfile
Requires:       openssh
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %fillup_prereq
PreReq:         /usr/bin/mkdir /usr/bin/rm /usr/bin/touch
Recommends:     cifs-utils
Recommends:     nfs-client
# update should detect the split-off from kexec-tools
Provides:       kexec-tools:%{_initddir}/kdump
ExcludeArch:    s390 ppc
%{?systemd_ordering}

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
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1

%build
export CXXFLAGS="%{optflags} -std=gnu++98"
%cmake

# for SLE_15
%if %{undefined cmake_build}
%define cmake_build make %{?_smp_mflags}
%define ctest cd build; ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags}
%define cmake_install DESTDIR=%{buildroot} make -C build %{?_smp_mflags} install
%endif

%cmake_build

%check
%ctest

%install
%cmake_install
# remove executable bit from non-binaries
chmod -x %{buildroot}/lib/kdump/setup-kdump.functions
# empty directory
mkdir -p %{buildroot}%{_localstatedir}/crash

# symlink for init script
rm %{buildroot}%{_initddir}/boot.kdump
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rckdump

%pre
%service_add_pre kdump.service
%service_add_pre kdump-early.service

%post
# change only permission if the file exists before /etc/sysconfig/kdump
# has been created from %%{_fillupdir}/sysconfig.kdump
change_permission=0
if [ ! -f %{_sysconfdir}/sysconfig/kdump ] ; then
    change_permission=1
fi
%{fillup_only -n kdump}
%service_add_post kdump.service
%service_add_post kdump-early.service
# ensure newly added kdump-early.service is-enabled matches prior state
if [ -x %{_bindir}/systemctl ] && %{_bindir}/systemctl is-enabled kdump.service &>/dev/null ; then
	%{_bindir}/systemctl reenable kdump.service || :
fi
if [ "$change_permission" = 1 ]; then
    chmod 0600 %{_sysconfdir}/sysconfig/kdump
fi
# if /var/log/dump is empty, make it a symlink to /var/crash
if test -d %{_localstatedir}/log/dump && rmdir %{_localstatedir}/log/dump >/dev/null 2>&1 ||
        ! test -d %{_localstatedir}/log/dump ; then
    ln -snf %{_localstatedir}/crash %{_localstatedir}/log/dump
fi

%preun
echo "Stopping kdump ..."
%service_del_preun kdump.service
%service_del_preun kdump-early.service

%postun
# force regeneration of kdumprd
touch %{_sysconfdir}/sysconfig/kdump
# delete symbolic link
rm %{_localstatedir}/log/dump >/dev/null 2>&1 || true
%service_del_postun kdump.service
%service_del_postun kdump-early.service

# Compatibility cruft
# there is no %%license prior to SLE12
%if %{undefined _defaultlicensedir}
%define license %doc
%else
# filesystem before SLE12 SP3 lacks /usr/share/licenses
%if 0%(test ! -d %{_defaultlicensedir} && echo 1)
%define _defaultlicensedir %{_defaultdocdir}
%endif
%endif
# End of compatibility cruft

%files
%defattr(-,root,root)
%license COPYING
%doc ChangeLog README NEWS
%{_sbindir}/kdumptool
%{_sbindir}/mkdumprd
%{_mandir}/man5/kdump.5%{?ext_man}
%{_mandir}/man7/kdump.7%{?ext_man}
%{_mandir}/man8/kdumptool.8%{?ext_man}
%{_mandir}/man8/mkdumprd.8%{?ext_man}
%{_fillupdir}/sysconfig.kdump
%dir %{dracutlibdir}
%dir %{dracutlibdir}/modules.d
%{dracutlibdir}/modules.d/99kdump/
%dir /lib/kdump
/lib/kdump/*
%dir /usr/lib/kdump
/usr/lib/kdump/70-kdump.rules
%{_unitdir}/kdump.service
%{_unitdir}/kdump-early.service
%{_sbindir}/rckdump

%changelog
