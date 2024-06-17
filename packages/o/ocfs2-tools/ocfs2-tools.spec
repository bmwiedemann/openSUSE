#
# spec file for package ocfs2-tools
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
  %define _fillupdir /var/adm/fillup-templates
%endif

#see bsc#1191084
%if 0%{?suse_version} < 1550
  # for SLEs
  %define sbindir /sbin
%else
  # for opensuse
  %define sbindir %{_sbindir}
%endif

#if run  "rpmbuild --with=ocfs2console"
#_with_ocfs2console will be automatically defined
%if %{defined _with_ocfs2console}
	%define _ocfs2console  1
%else
	%if 0%{?suse_version} >= 1500
		%define _ocfs2console 0
	%else
		%define _ocfs2console 1
	%endif
%endif

Name:           ocfs2-tools
Version:        1.8.8
Release:        0
Summary:        Oracle Cluster File System 2 Core Tools
License:        GPL-2.0-only
Group:          System/Filesystems
URL:            https://ocfs2.wiki.kernel.org/
Source:         ocfs2-tools-%{version}.tar.gz
Source1:        reflink.tar.bz2

# suse special patches
Patch001:       auto-setup-pcmk-stack-as-default-if-no-stack-is-setup.patch
Patch103:       debug-ocfs2_hb_ctl.patch
Patch105:       bug-470741-debug_start_failures.patch
Patch106:       ocfs2-devel.diff
Patch107:       reflink-no-syscall.patch
Patch202:       fix-configure-check-libs.patch
Patch204:       dont-use-var-lock-subsys.patch
Patch205:       ocfs2-tools-resource.patch
Patch225:       0004-mkfs.ocfs2-Abort-if-cluster-information-is-not-detec.patch
Patch228:       0007-Improve-error-message-if-DLM-service-is-unavailable.patch
Patch405:       0007-vendor-Add-vendor-files-for-sles12.patch
Patch406:       0008-ocfs2-tools-add-systemd-support-fix.patch
# upstream patches (start from Patch501)
Patch501:       mkfs.ocfs2-verify-the-number-of-clusters.patch
Patch502:       bsc1216834-fsck.ocfs2-add-the-ability-to-clear-jbd2-errno.patch
Patch503:       bsc1219224-debugfs.ocfs2-support-recording-gd-bg_contig_free_bi.patch

BuildRequires:  autoconf
BuildRequires:  e2fsprogs-devel
BuildRequires:  libaio-devel
BuildRequires:  libbz2-devel
BuildRequires:  libcorosync-devel
BuildRequires:  libdlm-devel
BuildRequires:  libxslt-devel
BuildRequires:  libz1
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
Requires(pre):  %fillup_prereq
Requires:       e2fsprogs
Requires:       glib2 >= 2.2.3
Requires:       libdlm
Requires:       modutils
Requires:       net-tools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Recommends:     ocfs2-kmp
%if 0%{?suse_version} >= 1315
%define systemd_enabled 1
%else
%define systemd_enabled 0
Requires(pre):  %insserv_prereq
%endif

%description
OCFS2 is the Oracle Cluster File System.

This package contains the core user-space tools needed for creating and
managing the file system.

%if 0%{_ocfs2console} == 1
%package -n ocfs2console
Summary:        Oracle Cluster Filesystem 2 GUI tools
Group:          System/Filesystems
BuildRequires:  python-devel
BuildRequires:  python-gtk-devel
Requires:       e2fsprogs
Requires:       glib2 >= 2.2.3
Requires:       ocfs2-tools = %{version}
Requires:       ocfs2-tools = %{version}
Requires:       python-gtk >= 1.99.16
Requires:       vte >= 0.11.10
Provides:       ocfs2-support = %{version}
Obsoletes:      ocfs2-support < %{version}

%description -n ocfs2console
OCFS2 is the Oracle Cluster Filesystem.

This package contains additional tools and a GUI (python-gtk).
%endif

%package devel
Summary:        Oracle Cluster File System 2 Development files
Group:          Development/Libraries/C and C++
Requires:       libcom_err
Requires:       libcom_err-devel
Requires:       ocfs2-tools = %{version}

%description devel
OCFS2 is the Oracle Cluster File System.

This package contains the header files for developing low-level
OCFS2-aware applications.

%package devel-static
Summary:        Oracle Cluster File System 2 static libraries
Group:          Development/Libraries/C and C++
Requires:       libcom_err
Requires:       libcom_err-devel
Requires:       ocfs2-tools = %{version}

%description devel-static
OCFS2 is the Oracle Cluster File System.

This package contains the static libraries for developing low-level
OCFS2-aware applications.

%package o2cb
Summary:        Oracle Cluster File System 2 tools for the native o2cb stack
Group:          System/Filesystems
Requires:       ocfs2-tools = %{version}

%description o2cb
OCFS is the Oracle Cluster File System.

This package contains the tools to manage the native o2cb stack for the
OCFS2 filesystem.

%prep
%autosetup -p1 -a 1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export PROJECT="ocfs2-tools"
autoreconf -fi -I /usr/share/aclocal

%configure --disable-debug \
  %if 0%{_ocfs2console} == 1
  --enable-ocfs2console=yes \
  %endif
  --enable-dynamic-fsck=yes \
  --enable-dynamic-ctl=yes \
  %if 0%{?suse_version} < 1550
  # "do nothing"
  %else
  --with-root-prefix=/usr
  %endif

make OPTS="%{optflags}"

cd reflink
cp ../config.guess ../config.sub coreutils-6.9/build-aux/
%configure
make reflink
cd ..

%install
mkdir -p %{buildroot}%{sbindir}
mkdir -p %{buildroot}%{_prefix}/bin
mkdir -p %{buildroot}%{_fillupdir}
mkdir -p %{buildroot}%{_udevrulesdir}
cp -f vendor/common/51-ocfs2.rules %{buildroot}%{_udevrulesdir}
cp -f vendor/common/o2cb.sysconfig %{buildroot}%{_fillupdir}/sysconfig.o2cb

%if %{systemd_enabled}
    mkdir -p %{buildroot}/usr/lib/systemd/system
    cp -f vendor/common/o2cb.service  %{buildroot}/usr/lib/systemd/system/
    cp -f vendor/common/ocfs2.service %{buildroot}/usr/lib/systemd/system/
    cp -f vendor/common/o2cb.init     %{buildroot}%{sbindir}
    cp -f vendor/common/ocfs2.init    %{buildroot}%{sbindir}
%else
    mkdir -p %{buildroot}%{_sysconfdir}/init.d
    cp  -f vendor/common/o2cb.init       %{buildroot}%{_sysconfdir}/init.d/o2cb
    cp  -f vendor/common/ocfs2.init      %{buildroot}%{_sysconfdir}/init.d/ocfs2
    ln -sf ..%{_sysconfdir}/init.d/o2cb  %{buildroot}%{sbindir}/rco2cb
    ln -sf ..%{_sysconfdir}/init.d/ocfs2 %{buildroot}%{sbindir}/rcocfs2
%endif
make DESTDIR="%{buildroot}" install

cd reflink
make DESTDIR="%{buildroot}" install
cd ..

%if 0%{?suse_version} < 1550
mv %{buildroot}/{,/usr}/sbin/o2image
mv %{buildroot}/{,/usr}/sbin/debugfs.ocfs2
#mv %{buildroot}/{,/usr}/sbin/ocfs2_controld.pcmk
%endif
chmod a-x %{buildroot}/%{_libdir}/libo2cb.a
chmod a-x %{buildroot}/%{_libdir}/libo2dlm.a
chmod a-x %{buildroot}/%{_libdir}/libocfs2.a
%if 0%{_ocfs2console} == 1
python -c "import compileall; compileall.compile_dir('%{buildroot}/%{py_sitedir}/ocfs2interface', ddir='%{py_sitedir}/ocfs2interface')"
%endif

%if %{systemd_enabled}
%pre o2cb
%service_add_pre ocfs2.service o2cb.service
%endif

%preun o2cb
%if %{systemd_enabled}
%service_del_preun ocfs2.service o2cb.service
%else
%stop_on_removal ocfs2
%stop_on_removal o2cb
%endif

%post o2cb
%fillup_only -n o2cb
%if %{systemd_enabled}
%service_add_post ocfs2.service o2cb.service
%endif

%postun o2cb
%if %{systemd_enabled}
%service_del_postun ocfs2.service o2cb.service
%else
%{insserv_cleanup}
%restart_on_update ocfs2
%restart_on_update o2cb
%endif

%files
%defattr(-,root,root)
%license COPYING
%doc CREDITS MAINTAINERS
%doc documentation/users_guide.txt
%dir /usr/lib/udev
%dir %{_udevrulesdir}
%{sbindir}/fsck.ocfs2
%{sbindir}/mkfs.ocfs2
%{sbindir}/mounted.ocfs2
%{sbindir}/tunefs.ocfs2
%{sbindir}/mount.ocfs2
%{sbindir}/ocfs2_hb_ctl
%{sbindir}/o2cluster
%{sbindir}/defragfs.ocfs2
%{_sbindir}/o2image
%{_sbindir}/debugfs.ocfs2
%{_sbindir}/o2hbmonitor
%{_bindir}/reflink
%{_bindir}/o2info
%{_udevrulesdir}/51-ocfs2.rules
%{_mandir}/man8/debugfs.ocfs2.8*
%{_mandir}/man8/fsck.ocfs2.8*
%{_mandir}/man8/fsck.ocfs2.checks.8*
%{_mandir}/man8/mkfs.ocfs2.8*
%{_mandir}/man8/tunefs.ocfs2.8*
%{_mandir}/man8/mounted.ocfs2.8*
%{_mandir}/man8/ocfs2_hb_ctl.8*
%{_mandir}/man8/mount.ocfs2.8*
%{_mandir}/man8/o2image.8.gz
%{_mandir}/man8/o2cluster.8.gz
%{_mandir}/man8/o2hbmonitor.8.gz
%{_mandir}/man8/defragfs.ocfs2.8*
%{_mandir}/man5/o2cb.sysconfig.5.gz
%{_mandir}/man5/ocfs2.cluster.conf.5.gz
%{_mandir}/man7/ocfs2.7.gz
%{_mandir}/man1/o2info.1.gz

%if 0%{_ocfs2console} == 1
%files -n ocfs2console
%defattr(-,root,root)
%{_sbindir}/ocfs2console
%{py_sitedir}/ocfs2interface
%{_mandir}/man8/ocfs2console.8*
%endif

%files o2cb
%defattr(-,root,root)
%doc README.O2CB
%{sbindir}/o2cb_ctl
%{sbindir}/o2cb

%if %{systemd_enabled}
    %{sbindir}/o2cb.init
    %{sbindir}/ocfs2.init
    /usr/lib/systemd/system/o2cb.service
    /usr/lib/systemd/system/ocfs2.service
%else
    %{sbindir}/rco2cb
    %{sbindir}/rcocfs2
    %{_sysconfdir}/init.d/o2cb
    %{_sysconfdir}/init.d/ocfs2
%endif

%{_mandir}/man8/o2cb_ctl.8*
%{_fillupdir}/sysconfig.o2cb
%{_mandir}/man7/o2cb.7.gz
%{_mandir}/man8/o2cb.8.gz

%files devel
%defattr(-,root,root)
%{_includedir}/o2cb
%{_includedir}/o2dlm
%{_includedir}/ocfs2
%{_includedir}/ocfs2-kernel
%{_libdir}/pkgconfig/o2cb.pc
%{_libdir}/pkgconfig/o2dlm.pc
%{_libdir}/pkgconfig/ocfs2.pc

%files devel-static
%defattr(-,root,root)
%{_libdir}/libo2cb.a
%{_libdir}/libo2dlm.a
%{_libdir}/libocfs2.a

%changelog
