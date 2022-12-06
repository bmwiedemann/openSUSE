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

%bcond_with debug

%define flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "full"
%define build_main 0
%define build_doc 1
%define name_suffix -%{flavor}-src
%else
%define build_main 1
%define build_doc 0
%define name_suffix %{nil}
%endif

#
%define enable_selinux 1
%define libpam_so_version 0.85.1
%define libpam_misc_so_version 0.82.1
%define libpamc_so_version 0.82.1
%if ! %{defined _distconfdir}
  %define _distconfdir %{_sysconfdir}
  %define config_noreplace 1
%endif
#
%{load:%{_sourcedir}/macros.pam}
#
Name:           pam%{name_suffix}
#
Version:        1.5.2
Release:        0
Summary:        A Security Tool that Provides Authentication for Applications
License:        GPL-2.0-or-later OR BSD-3-Clause
Group:          System/Libraries
URL:            http://www.linux-pam.org/
Source:         Linux-PAM-%{version}.tar.xz
Source1:        Linux-PAM-%{version}-docs.tar.xz
Source2:        macros.pam
Source3:        other.pamd
Source4:        common-auth.pamd
Source5:        common-account.pamd
Source6:        common-password.pamd
Source7:        common-session.pamd
Source9:        baselibs.conf
Source10:       unix2_chkpwd.c
Source11:       unix2_chkpwd.8
Source12:       pam-login_defs-check.sh
Source13:       pam.tmpfiles
Source14:       Linux-PAM-%{version}-docs.tar.xz.asc
Source15:       Linux-PAM-%{version}.tar.xz.asc
Source16:       tst-pam_env-retval.c
Patch1:         pam-limit-nproc.patch
Patch2:         pam-hostnames-in-access_conf.patch
Patch3:         pam-xauth_ownership.patch
Patch4:         pam-bsc1177858-dont-free-environment-string.patch
Patch10:        pam_xauth_data.3.xml.patch
Patch11:        pam-git.diff
Patch12:        pam_env_econf.patch
BuildRequires:  audit-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  xz
Requires(post): permissions
# All login.defs variables require support from shadow side.
# Upgrade this symbol version only if new variables appear!
# Verify by shadow-login_defs-check.sh from shadow source package.
Recommends:     login_defs-support-for-pam >= 1.5.2
%if 0%{?suse_version} > 1320
BuildRequires:  pkgconfig(libeconf)
%endif
%if %{enable_selinux}
BuildRequires:  libselinux-devel
%endif
Requires:       pam_unix.so
Suggests:       pam_unix
Recommends:     pam-manpages
%if 0%{?suse_version} >= 1330
Requires(pre):  group(shadow)
Requires(pre):  user(root)
%endif

%description
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

%package -n pam_unix
Summary:        PAM module for standard UNIX authentication
Group:          System/Libraries
Provides:       pam:/%{_lib}/security/pam_unix.so
Provides:       pam_unix.so
Conflicts:      pam_unix-nis

%description -n pam_unix
This package contains the pam_unix module, which does the standard
UNIX authentication against the passwd and shadow database. This
module does not contain NIS support.

%package extra
Summary:        PAM module to authenticate against a separate database
Group:          System/Libraries
BuildRequires:  libdb-4_8-devel
BuildRequires:  pam-devel

%description extra
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

This package contains useful extra modules eg pam_userdb which is
used to verify a username/password pair against values stored in
a Berkeley DB database.

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
BuildRequires:  docbook-xsl-stylesheets
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
%setup -q -n Linux-PAM-%{version} -b 1
cp -a %{SOURCE12} .
cp %{SOURCE16} ./modules/pam_env
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
bash ./pam-login_defs-check.sh
export CFLAGS="%{optflags}"
%if !%{with debug}
CFLAGS="$CFLAGS -DNDEBUG"
%endif
%configure \
	--includedir=%{_includedir}/security \
	--docdir=%{_docdir}/pam \
	--htmldir=%{_docdir}/pam/html \
	--pdfdir=%{_docdir}/pam/pdf \
	--enable-isadir=../..%{_pam_moduledir} \
	--enable-securedir=%{_pam_moduledir} \
	--enable-vendordir=%{_prefix}/etc \
%if %{with debug}
	--enable-debug
%endif

%make_build
gcc -fwhole-program -fpie -pie -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE %{optflags} -I%{_builddir}/Linux-PAM-%{version}/libpam/include %{SOURCE10} -o %{_builddir}/unix2_chkpwd -L%{_builddir}/Linux-PAM-%{version}/libpam/.libs -lpam

%if %{build_main}
%check
%make_build check
%endif

%install
mkdir -p %{buildroot}%{_pam_confdir}
mkdir -p %{buildroot}%{_pam_vendordir}
mkdir -p %{buildroot}%{_includedir}/security
mkdir -p %{buildroot}%{_pam_moduledir}
mkdir -p %{buildroot}/sbin
mkdir -p -m 755 %{buildroot}%{_libdir}
# For compat reasons
mkdir -p %{buildroot}%{_distconfdir}/pam.d
%make_install
/sbin/ldconfig -n %{buildroot}%{libdir}
# Install documentation
%make_install -C doc
# install /etc/security/namespace.d used by pam_namespace.so for namespace.conf iscript
install -d %{buildroot}%{_pam_secconfdir}/namespace.d
# install other.pamd and common-*.pamd
install -m 644 %{SOURCE3} %{buildroot}%{_pam_vendordir}/other
install -m 644 %{SOURCE4} %{buildroot}%{_pam_vendordir}/common-auth
install -m 644 %{SOURCE5} %{buildroot}%{_pam_vendordir}/common-account
install -m 644 %{SOURCE6} %{buildroot}%{_pam_vendordir}/common-password
install -m 644 %{SOURCE7} %{buildroot}%{_pam_vendordir}/common-session
mkdir -p %{buildroot}%{_prefix}/lib/motd.d
#
# Remove crap
#
find %{buildroot} -type f -name "*.la" -delete -print
for x in pam_unix_auth pam_unix_acct pam_unix_passwd pam_unix_session; do
  ln -f %{buildroot}%{_pam_moduledir}/pam_unix.so %{buildroot}%{_pam_moduledir}/$x.so
done
#
# Install READMEs of PAM modules
#
DOC=%{buildroot}%{_defaultdocdir}/pam
mkdir -p $DOC/modules
pushd modules
for i in pam_*/README; do
	cp -fpv "$i" "$DOC/modules/README.${i%/*}"
done
popd
# Install unix2_chkpwd
install -m 755 %{_builddir}/unix2_chkpwd %{buildroot}%{_sbindir}

# rpm macros
install -D -m 644 %{SOURCE2} %{buildroot}%{_rpmmacrodir}/macros.pam
# /run/motd.d
install -Dm0644 %{SOURCE13} %{buildroot}%{_tmpfilesdir}/pam.conf

mkdir -p %{buildroot}%{_distconfdir}/security
mv %{buildroot}%{_sysconfdir}/security/{limits.conf,faillock.conf,group.conf,pam_env.conf} %{buildroot}%{_distconfdir}/security/
mv %{buildroot}%{_sysconfdir}/environment %{buildroot}%{_distconfdir}/environment

# Remove manual pages for main package
%if !%{build_doc}
rm -rf %{buildroot}%{_mandir}/man[58]/*
install -m 644 modules/pam_userdb/pam_userdb.8 %{buildroot}/%{_mandir}/man8/
%else
install -m 644 %{_sourcedir}/unix2_chkpwd.8 %{buildroot}/%{_mandir}/man8/
# bsc#1188724
echo '.so man8/pam_motd.8' > %{buildroot}%{_mandir}/man5/motd.5
%endif
%if !%{build_main}
rm -rf %{buildroot}{%{_sysconfdir},%{_distconfdir},%{_sbindir},%{_pam_secconfdir},%{_pam_confdir},%{_datadir}/locale}
rm -rf %{buildroot}{%{_includedir},%{_libdir},%{_prefix}/lib}
rm -rf %{buildroot}%{_mandir}/man3/*
rm -rf %{buildroot}%{_mandir}/man8/pam_userdb.8*

%else

# Create filelist with translations
%find_lang Linux-PAM

%endif

%if %{build_main}

%verifyscript
%verify_permissions -e %{_sbindir}/unix_chkpwd
%verify_permissions -e %{_sbindir}/unix2_chkpwd

%post
/sbin/ldconfig
%set_permissions %{_sbindir}/unix_chkpwd
%set_permissions %{_sbindir}/unix2_chkpwd
%tmpfiles_create %{_tmpfilesdir}/pam.conf

%postun -p /sbin/ldconfig
%pre
for i in securetty pam.d/other pam.d/common-account pam.d/common-auth pam.d/common-password pam.d/common-session ; do
  test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/etc.
for i in securetty pam.d/other pam.d/common-account pam.d/common-auth pam.d/common-password pam.d/common-session ; do
  test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done

%files -f Linux-PAM.lang
%doc NEWS
%license COPYING
%exclude %{_defaultdocdir}/pam/html
%exclude %{_defaultdocdir}/pam/modules
%exclude %{_defaultdocdir}/pam/pdf
%exclude %{_defaultdocdir}/pam/*.txt
%dir %{_pam_confdir}
%dir %{_pam_vendordir}
%dir %{_pam_secconfdir}
%dir %{_pam_secconfdir}/limits.d
%dir %{_distconfdir}/security
# /usr/etc/pam.d is for compat reasons
%dir %{_distconfdir}/pam.d
%dir %{_prefix}/lib/motd.d
%if %{defined config_noreplace}
%config(noreplace) %{_pam_confdir}/other
%config(noreplace) %{_pam_confdir}/common-*
%else
%{_pam_vendordir}/other
%{_pam_vendordir}/common-*
%endif
%{_distconfdir}/environment
%config(noreplace) %{_pam_secconfdir}/access.conf
%{_distconfdir}/security/group.conf
%{_distconfdir}/security/faillock.conf
%{_distconfdir}/security/limits.conf
%{_distconfdir}/security/pam_env.conf
%if %{enable_selinux}
%config(noreplace) %{_pam_secconfdir}/sepermit.conf
%endif
%config(noreplace) %{_pam_secconfdir}/time.conf
%config(noreplace) %{_pam_secconfdir}/namespace.conf
%config(noreplace) %{_pam_secconfdir}/namespace.init
%dir %{_pam_secconfdir}/namespace.d
%{_libdir}/libpam.so.0
%{_libdir}/libpam.so.%{libpam_so_version}
%{_libdir}/libpamc.so.0
%{_libdir}/libpamc.so.%{libpamc_so_version}
%{_libdir}/libpam_misc.so.0
%{_libdir}/libpam_misc.so.%{libpam_misc_so_version}
%dir %{_pam_moduledir}
%{_pam_moduledir}/pam_access.so
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
%{_pam_moduledir}/pam_issue.so
%{_pam_moduledir}/pam_keyinit.so
%{_pam_moduledir}/pam_lastlog.so
%{_pam_moduledir}/pam_limits.so
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
%if %{enable_selinux}
%{_pam_moduledir}/pam_selinux.so
%{_pam_moduledir}/pam_sepermit.so
%endif
%{_pam_moduledir}/pam_setquota.so
%{_pam_moduledir}/pam_shells.so
%{_pam_moduledir}/pam_stress.so
%{_pam_moduledir}/pam_succeed_if.so
%{_pam_moduledir}/pam_time.so
%{_pam_moduledir}/pam_timestamp.so
%{_pam_moduledir}/pam_tty_audit.so
%{_pam_moduledir}/pam_umask.so
%{_pam_moduledir}/pam_usertype.so
%{_pam_moduledir}/pam_warn.so
%{_pam_moduledir}/pam_wheel.so
%{_pam_moduledir}/pam_xauth.so
%{_sbindir}/faillock
%{_sbindir}/mkhomedir_helper
%{_sbindir}/pam_namespace_helper
%{_sbindir}/pam_timestamp_check
%{_sbindir}/pwhistory_helper
%verify(not mode) %attr(4755,root,shadow) %{_sbindir}/unix_chkpwd
%verify(not mode) %attr(4755,root,shadow) %{_sbindir}/unix2_chkpwd
%attr(0700,root,root) %{_sbindir}/unix_update
%{_unitdir}/pam_namespace.service
%{_tmpfilesdir}/pam.conf

%files -n pam_unix
%defattr(-,root,root,755)
%{_pam_moduledir}/pam_unix.so
%{_pam_moduledir}/pam_unix_acct.so
%{_pam_moduledir}/pam_unix_auth.so
%{_pam_moduledir}/pam_unix_passwd.so
%{_pam_moduledir}/pam_unix_session.so

%files extra
%defattr(-,root,root,755)
%{_pam_moduledir}/pam_userdb.so
%{_mandir}/man8/pam_userdb.8%{?ext_man}

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/security
%{_mandir}/man3/pam*
%{_mandir}/man3/misc_conv.3%{?ext_man}
%{_includedir}/security/*.h
%{_libdir}/libpam.so
%{_libdir}/libpamc.so
%{_libdir}/libpam_misc.so
%{_rpmmacrodir}/macros.pam
%{_libdir}/pkgconfig/pam*.pc

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
%{_mandir}/man5/environment.5%{?ext_man}
%{_mandir}/man5/*.conf.5%{?ext_man}
%{_mandir}/man5/pam.d.5%{?ext_man}
%{_mandir}/man5/motd.5%{?ext_man}
%{_mandir}/man8/PAM.8%{?ext_man}
%{_mandir}/man8/faillock.8%{?ext_man}
%{_mandir}/man8/mkhomedir_helper.8%{?ext_man}
%{_mandir}/man8/pam.8%{?ext_man}
%{_mandir}/man8/pam_access.8%{?ext_man}
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
%{_mandir}/man8/pam_lastlog.8%{?ext_man}
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
%{_mandir}/man8/pam_selinux.8%{?ext_man}
%{_mandir}/man8/pam_sepermit.8%{?ext_man}
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
%{_mandir}/man8/unix2_chkpwd.8%{?ext_man}
%{_mandir}/man8/unix_chkpwd.8%{?ext_man}
%{_mandir}/man8/unix_update.8%{?ext_man}

%endif

%changelog
