#
# spec file for package kdump
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

%define dracutlibdir %{_prefix}/lib/dracut

Name:           kdump
Version:        0.9.1
Release:        0
Summary:        Script for kdump
License:        GPL-2.0-or-later
Group:          System/Kernel
URL:            https://github.com/openSUSE/kdump
Source:         %{name}-%{version}.tar.bz2
Source2:        %{name}-rpmlintrc
Patch1:         %{name}-fillupdir-fixes.patch
Patch9:         %{name}-use-pbl.patch
Patch10:        %{name}-on-error-option-yesno.patch
Patch11:        %{name}-mounts.cc-Include-sys-ioctl.h.patch
Patch12:        %{name}-Add-bootdev-to-dracut-command-line.patch
Patch13:        %{name}-do-not-iterate-past-end-of-string.patch
Patch14:        %{name}-fix-incorrect-exit-code-checking.patch
Patch15:        %{name}-avoid-endless-loop-on-EAI_AGAIN.patch
Patch16:        %{name}-install-real-resolv.conf.patch
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libblkid-devel
BuildRequires:  libcurl-devel
BuildRequires:  libelf-devel
BuildRequires:  libesmtp-devel
BuildRequires:  libmount-devel
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
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
export CXXFLAGS="%{optflags} -std=c++11"
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
