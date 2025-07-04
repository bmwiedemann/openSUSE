#
# spec file for package pam
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

%if 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1550
# Enable livepatching support for SLE15-SP4 onwards. It requires
# compiler support introduced there.
%define livepatchable 1

# Set variables for livepatching.
%define _other %{_topdir}/OTHER
%define tar_basename pam-livepatch-%{version}-%{release}
%define tar_package_name %{tar_basename}.%{_arch}.tar.xz
%define clones_dest_dir %{tar_basename}/%{_arch}
%else
# Unsupported operating system.
%define livepatchable 0
%endif

%ifnarch x86_64
# Unsupported architectures must have livepatch disabled.
%define livepatchable 0
%endif

%bcond_without selinux

%define flavor @BUILD_FLAVOR@%{nil}

# List of config files for migration to /usr/etc
%define config_files pam.d/other pam.d/common-account pam.d/common-auth pam.d/common-password pam.d/common-session \\\
	security/faillock.conf security/group.conf security/limits.conf security/pam_env.conf security/access.conf \\\
	security/namespace.conf security/namespace.init security/sepermit.conf

%if "%{flavor}" == "full"
%define build_main 0
%define build_doc 1
%define build_extra 1
%define build_userdb 1
%define name_suffix -%{flavor}-src
%else
%define build_main 1
%define build_doc 0
%define build_extra 0
%define build_userdb 0
%define name_suffix %{nil}
%endif

#
%define libpam_so_version 0.85.1
%define libpam_misc_so_version 0.82.1
%define libpamc_so_version 0.82.1
%if ! %{defined _distconfdir}
  %define _distconfdir %{_sysconfdir}
%endif
#
%{load:%{_sourcedir}/macros.pam}
#
Name:           pam%{name_suffix}
#
Version:        1.7.1
Release:        0
Summary:        A Security Tool that Provides Authentication for Applications
License:        GPL-2.0-or-later OR BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/linux-pam/linux-pam
Source:         Linux-PAM-%{version}.tar.xz
Source1:        Linux-PAM-%{version}.tar.xz.asc
Source2:        macros.pam
Source3:        other.pamd
Source4:        common-auth.pamd
Source5:        common-account.pamd
Source6:        common-password.pamd
Source7:        common-session.pamd
Source9:        baselibs.conf
Source12:       pam-login_defs-check.sh
Source13:       pam.tmpfiles
Source20:       common-session-nonlogin.pamd
Source21:       postlogin-auth.pamd
Source22:       postlogin-account.pamd
Source23:       postlogin-password.pamd
Source24:       postlogin-session.pamd
Patch1:         pam-limit-nproc.patch
BuildRequires:  audit-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  meson >= 0.62.0
BuildRequires:  xz
Requires(post): permissions
# All login.defs variables require support from shadow side.
# Upgrade this symbol version only if new variables appear!
# Verify by shadow-login_defs-check.sh from shadow source package.
Recommends:     login_defs-support-for-pam >= 1.5.2
BuildRequires:  pkgconfig(libeconf)
%if %{with selinux}
BuildRequires:  libselinux-devel
%endif
Obsoletes:      pam_unix
Obsoletes:      pam_unix-nis
Recommends:     pam-manpages
Requires(pre):  group(shadow)
Requires(pre):  user(root)

%description
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

%if %{build_userdb}
%package -n pam-userdb
Summary:        PAM module to authenticate against a separate database
Group:          System/Libraries
Provides:       pam-extra:%{_pam_moduledir}/pam_userdb.so
BuildRequires:  libdb-4_8-devel
BuildRequires:  pam-devel

%description -n pam-userdb
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

This package contains pam_userdb which is used to verify a
username/password pair against values stored in a Berkeley DB database.
%endif


%if %{build_extra}
%package -n pam-extra
Summary:        PAM module with extended dependencies
Group:          System/Libraries
BuildRequires:  pkgconfig(libsystemd) >= 254
BuildRequires:  pam-devel
Provides:	pam:%{_sbindir}/pam_timestamp_check
Provides:       pam:%{_pam_moduledir}/pam_limits.so

%description -n pam-extra
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

This package contains extra modules eg pam_issue and pam_timestamp which
can have extended dependencies.
%endif

%if %{build_doc}

%package -n pam-doc
Summary:        Documentation for Pluggable Authentication Modules
Group:          Documentation/HTML
BuildArch:      noarch

%description -n pam-doc
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

This package contains the documentation.

%package -n pam-manpages
Summary:        Manualpages for Pluggable Authentication Modules
Group:          Documentation/HTML
Provides:       pam:/%{_mandir}/man8/PAM.8.gz
BuildArch:      noarch
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  elinks
BuildRequires:  xmlgraphics-fop

%description -n pam-manpages
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

This package contains the manual pages.

%endif

%package devel
Summary:        Include Files and Libraries for PAM Development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       pam = %{version}

%description devel
PAM (Pluggable Authentication Modules) is a system security tool which
allows system administrators to set authentication policy without
having to recompile programs which do authentication.

This package contains header files and static libraries used for
building both PAM-aware applications and modules for use with PAM.

%prep
%autosetup -p1 -n Linux-PAM-%{version}
cp -a %{SOURCE12} .

%build
bash ./pam-login_defs-check.sh
%if %{livepatchable}
CFLAGS="$CFLAGS -fpatchable-function-entry=16,14 -fdump-ipa-clones"
%endif

%meson -Dvendordir=%{_distconfdir} \
       -Ddocdir=%{_docdir}/pam \
       -Dhtmldir=%{_docdir}/pam/html \
       -Dpdfdir=%{_docdir}/pam/pdf \
       -Dsecuredir=%{_pam_moduledir} \
%if "%{flavor}" != "full"
       -Dlogind=disabled \
       -Dpam_userdb=disabled \
       -Ddocs=disabled \
%else
       -Dlogind=enabled \
%endif
       -Delogind=disabled \
       -Dexamples=false \
       -Dnis=disabled
%meson_build

%if %{livepatchable}

# Ipa-clones are files generated by gcc which logs changes made across
# functions, and we need to know such changes to build livepatches
# correctly. These files are intended to be used by the livepatch
# developers and may be retrieved by using `osc getbinaries`.
#
# Create list of ipa-clones.
find . -name "*.ipa-clones" ! -empty | sed 's/^\.\///g' | sort > ipa-clones.list

# Create ipa-clones destination folder and move clones there.
mkdir -p ipa-clones/%{clones_dest_dir}
while read f; do
  _dest=ipa-clones/%{clones_dest_dir}/$f
  mkdir -p ${_dest%/*}
  cp $f $_dest
done < ipa-clones.list

# Create tar package with the clone files.
tar cfJ %{tar_package_name} -C ipa-clones %{tar_basename}

# Copy tar package to the OTHERS folder
cp %{tar_package_name} %{_other}

%endif # livepatchable

%if %{build_main}
%check
%meson_test
%endif

%install
%meson_install

mkdir -p %{buildroot}%{_pam_confdir}
mkdir -p %{buildroot}%{_pam_vendordir}

# install other.pamd and common-*.pamd
install -m 644 %{SOURCE3} %{buildroot}%{_pam_vendordir}/other
install -m 644 %{SOURCE4} %{buildroot}%{_pam_vendordir}/common-auth
install -m 644 %{SOURCE5} %{buildroot}%{_pam_vendordir}/common-account
install -m 644 %{SOURCE6} %{buildroot}%{_pam_vendordir}/common-password
install -m 644 %{SOURCE7} %{buildroot}%{_pam_vendordir}/common-session
install -m 644 %{SOURCE20} %{buildroot}%{_pam_vendordir}/common-session-nonlogin
install -m 644 %{SOURCE21} %{buildroot}%{_pam_vendordir}/postlogin-auth
install -m 644 %{SOURCE22} %{buildroot}%{_pam_vendordir}/postlogin-account
install -m 644 %{SOURCE23} %{buildroot}%{_pam_vendordir}/postlogin-password
install -m 644 %{SOURCE24} %{buildroot}%{_pam_vendordir}/postlogin-session
#
# Install READMEs of PAM modules
#
DOC=%{buildroot}%{_defaultdocdir}/pam
%if "%{flavor}" == "full"
mkdir -p $DOC/modules
cp -fpv %{_vpath_builddir}/modules/pam_*/pam_*.txt "$DOC/modules/"
%endif

# rpm macros
install -D -m 644 %{SOURCE2} %{buildroot}%{_rpmmacrodir}/macros.pam
# /run/motd.d
install -Dm0644 %{SOURCE13} %{buildroot}%{_tmpfilesdir}/pam.conf

mkdir -p %{buildroot}%{_pam_secdistconfdir}/{limits.d,namespace.d}

# Remove manual pages for main package
%if !%{build_doc}
rm -rf %{buildroot}%{_mandir}/man?/*
%else
# bsc#1188724
echo '.so man8/pam_motd.8' > %{buildroot}%{_mandir}/man5/motd.5
%endif

%if !%{build_main}
rm -rf %{buildroot}{%{_distconfdir}/environment,%{_pam_secdistconfdir}/{a,f,g,n,p,s,t}*}
rm -rf %{buildroot}{%{_sysconfdir},%{_sbindir}/{f*,m*,pam_n*,pw*,u*},%{_pam_secconfdir},%{_pam_confdir},%{_datadir}/locale}
rm -rf %{buildroot}{%{_includedir},%{_libdir}/{libpam*,pkgconfig},%{_pam_vendordir},%{_rpmmacrodir},%{_tmpfilesdir},%{_unitdir}/pam_namespace.service}
rm -rf %{buildroot}%{_pam_moduledir}/pam_{a,b,c,d,e,f,g,h,j,k,la,lis,lo,m,n,o,p,q,r,s,v,w,x,y,z,time.,tt,um,un,usertype}*
%else
# Delete files for extra package
rm -rf  %{buildroot}{%{_pam_moduledir}/pam_limits.so,%{_pam_secdistconfdir}/limits.conf,%{_pam_moduledir}/pam_issue.so,%{_pam_moduledir}/pam_timestamp.so,%{_sbindir}/pam_timestamp_check}

# Create filelist with translations
%find_lang Linux-PAM

%endif

%if %{build_main}

%verifyscript
%verify_permissions -e %{_sbindir}/unix_chkpwd

%post
/sbin/ldconfig
%set_permissions %{_sbindir}/unix_chkpwd
%tmpfiles_create %{_tmpfilesdir}/pam.conf

%postun -p /sbin/ldconfig
%pre
for i in securetty %{config_files} ; do
  test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/etc.
for i in securetty %{config_files} ; do
  test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done

%files -f Linux-PAM.lang
%doc NEWS
%license COPYING
%dir %{_pam_confdir}
%dir %{_pam_vendordir}
%dir %{_pam_secconfdir}
%dir %{_pam_secdistconfdir}
%{_pam_vendordir}/other
%{_pam_vendordir}/common-*
%{_pam_vendordir}/postlogin-*
%{_distconfdir}/environment
%{_pam_secdistconfdir}/access.conf
%{_pam_secdistconfdir}/group.conf
%{_pam_secdistconfdir}/faillock.conf
%{_pam_secdistconfdir}/pam_env.conf
%if %{with selinux}
%{_pam_secdistconfdir}/sepermit.conf
%endif
%{_pam_secdistconfdir}/time.conf
%{_pam_secdistconfdir}/namespace.conf
%{_pam_secdistconfdir}/namespace.init
%{_pam_secdistconfdir}/pwhistory.conf
%dir %{_pam_secdistconfdir}/namespace.d
%{_libdir}/libpam.so.0
%{_libdir}/libpam.so.%{libpam_so_version}
%{_libdir}/libpamc.so.0
%{_libdir}/libpamc.so.%{libpamc_so_version}
%{_libdir}/libpam_misc.so.0
%{_libdir}/libpam_misc.so.%{libpam_misc_so_version}
%dir %{_pam_moduledir}
%{_pam_moduledir}/pam_access.so
%{_pam_moduledir}/pam_canonicalize_user.so
%{_pam_moduledir}/pam_debug.so
%{_pam_moduledir}/pam_deny.so
%{_pam_moduledir}/pam_echo.so
%{_pam_moduledir}/pam_env.so
%{_pam_moduledir}/pam_exec.so
%{_pam_moduledir}/pam_faildelay.so
%{_pam_moduledir}/pam_faillock.so
%{_pam_moduledir}/pam_filter.so
%dir %{_pam_moduledir}/pam_filter
%{_pam_moduledir}//pam_filter/upperLOWER
%{_pam_moduledir}/pam_ftp.so
%{_pam_moduledir}/pam_group.so
%{_pam_moduledir}/pam_keyinit.so
%{_pam_moduledir}/pam_listfile.so
%{_pam_moduledir}/pam_localuser.so
%{_pam_moduledir}/pam_loginuid.so
%{_pam_moduledir}/pam_mail.so
%{_pam_moduledir}/pam_mkhomedir.so
%{_pam_moduledir}/pam_motd.so
%{_pam_moduledir}/pam_namespace.so
%{_pam_moduledir}/pam_nologin.so
%{_pam_moduledir}/pam_permit.so
%{_pam_moduledir}/pam_pwhistory.so
%{_pam_moduledir}/pam_rhosts.so
%{_pam_moduledir}/pam_rootok.so
%{_pam_moduledir}/pam_securetty.so
%if %{with selinux}
%{_pam_moduledir}/pam_selinux.so
%{_pam_moduledir}/pam_sepermit.so
%endif
%{_pam_moduledir}/pam_setquota.so
%{_pam_moduledir}/pam_shells.so
%{_pam_moduledir}/pam_stress.so
%{_pam_moduledir}/pam_succeed_if.so
%{_pam_moduledir}/pam_time.so
%{_pam_moduledir}/pam_tty_audit.so
%{_pam_moduledir}/pam_umask.so
%{_pam_moduledir}/pam_unix.so
%{_pam_moduledir}/pam_usertype.so
%{_pam_moduledir}/pam_warn.so
%{_pam_moduledir}/pam_wheel.so
%{_pam_moduledir}/pam_xauth.so
%{_sbindir}/faillock
%{_sbindir}/mkhomedir_helper
%{_sbindir}/pam_namespace_helper
%{_sbindir}/pwhistory_helper
%verify(not mode) %attr(4755,root,shadow) %{_sbindir}/unix_chkpwd
%attr(0700,root,root) %{_sbindir}/unix_update
%{_unitdir}/pam_namespace.service
%{_tmpfilesdir}/pam.conf

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/security
%{_includedir}/security/*.h
%{_libdir}/libpam.so
%{_libdir}/libpamc.so
%{_libdir}/libpam_misc.so
%{_rpmmacrodir}/macros.pam
%{_libdir}/pkgconfig/pam*.pc
%endif

%if %{build_userdb}
%files -n pam-userdb
%defattr(-,root,root,755)
%{_pam_moduledir}/pam_userdb.so
%{_mandir}/man8/pam_userdb.8%{?ext_man}
%endif

%if %{build_extra}
%files -n pam-extra
%defattr(-,root,root,755)
%dir %{_pam_secdistconfdir}
%dir %{_pam_secdistconfdir}/limits.d
%{_pam_secdistconfdir}/limits.conf
%{_pam_moduledir}/pam_limits.so
%{_pam_moduledir}/pam_issue.so
%{_pam_moduledir}/pam_timestamp.so
%{_sbindir}/pam_timestamp_check
%endif

%if %{build_doc}

%files -n pam-doc
%defattr(644,root,root,755)
%dir %{_defaultdocdir}/pam
%doc %{_defaultdocdir}/pam/html
%doc %{_defaultdocdir}/pam/modules
%doc %{_defaultdocdir}/pam/pdf
%doc %{_defaultdocdir}/pam/*.txt

%files -n pam-manpages
%{_mandir}/man3/pam*.3%{?ext_man}
%{_mandir}/man3/misc_conv.3%{?ext_man}
%{_mandir}/man5/environment.5%{?ext_man}
%{_mandir}/man5/*.conf.5%{?ext_man}
%{_mandir}/man5/pam.d.5%{?ext_man}
%{_mandir}/man5/motd.5%{?ext_man}
%{_mandir}/man8/PAM.8%{?ext_man}
%{_mandir}/man8/faillock.8%{?ext_man}
%{_mandir}/man8/mkhomedir_helper.8%{?ext_man}
%{_mandir}/man8/pam.8%{?ext_man}
%{_mandir}/man8/pam_access.8%{?ext_man}
%{_mandir}/man8/pam_canonicalize_user.8%{?ext_man}
%{_mandir}/man8/pam_debug.8%{?ext_man}
%{_mandir}/man8/pam_deny.8%{?ext_man}
%{_mandir}/man8/pam_echo.8%{?ext_man}
%{_mandir}/man8/pam_env.8%{?ext_man}
%{_mandir}/man8/pam_exec.8%{?ext_man}
%{_mandir}/man8/pam_faildelay.8%{?ext_man}
%{_mandir}/man8/pam_faillock.8%{?ext_man}
%{_mandir}/man8/pam_filter.8%{?ext_man}
%{_mandir}/man8/pam_ftp.8%{?ext_man}
%{_mandir}/man8/pam_group.8%{?ext_man}
%{_mandir}/man8/pam_issue.8%{?ext_man}
%{_mandir}/man8/pam_keyinit.8%{?ext_man}
%{_mandir}/man8/pam_limits.8%{?ext_man}
%{_mandir}/man8/pam_listfile.8%{?ext_man}
%{_mandir}/man8/pam_localuser.8%{?ext_man}
%{_mandir}/man8/pam_loginuid.8%{?ext_man}
%{_mandir}/man8/pam_mail.8%{?ext_man}
%{_mandir}/man8/pam_mkhomedir.8%{?ext_man}
%{_mandir}/man8/pam_motd.8%{?ext_man}
%{_mandir}/man8/pam_namespace.8%{?ext_man}
%{_mandir}/man8/pam_namespace_helper.8%{?ext_man}
%{_mandir}/man8/pam_nologin.8%{?ext_man}
%{_mandir}/man8/pam_permit.8%{?ext_man}
%{_mandir}/man8/pam_pwhistory.8%{?ext_man}
%{_mandir}/man8/pam_rhosts.8%{?ext_man}
%{_mandir}/man8/pam_rootok.8%{?ext_man}
%{_mandir}/man8/pam_securetty.8%{?ext_man}
%if %{with selinux}
%{_mandir}/man8/pam_selinux.8%{?ext_man}
%{_mandir}/man8/pam_sepermit.8%{?ext_man}
%endif
%{_mandir}/man8/pam_setquota.8%{?ext_man}
%{_mandir}/man8/pam_shells.8%{?ext_man}
%{_mandir}/man8/pam_stress.8%{?ext_man}
%{_mandir}/man8/pam_succeed_if.8%{?ext_man}
%{_mandir}/man8/pam_time.8%{?ext_man}
%{_mandir}/man8/pam_timestamp.8%{?ext_man}
%{_mandir}/man8/pam_timestamp_check.8%{?ext_man}
%{_mandir}/man8/pam_tty_audit.8%{?ext_man}
%{_mandir}/man8/pam_umask.8%{?ext_man}
%{_mandir}/man8/pam_unix.8%{?ext_man}
%{_mandir}/man8/pam_usertype.8%{?ext_man}
%{_mandir}/man8/pam_warn.8%{?ext_man}
%{_mandir}/man8/pam_wheel.8%{?ext_man}
%{_mandir}/man8/pam_xauth.8%{?ext_man}
%{_mandir}/man8/pwhistory_helper.8%{?ext_man}
%{_mandir}/man8/unix_chkpwd.8%{?ext_man}
%{_mandir}/man8/unix_update.8%{?ext_man}

%endif

%changelog
