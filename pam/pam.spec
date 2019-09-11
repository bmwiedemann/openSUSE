#
# spec file for package pam
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
%define enable_selinux 1

Name:           pam
Url:            http://www.linux-pam.org/
BuildRequires:  audit-devel
BuildRequires:  bison
BuildRequires:  cracklib-devel
BuildRequires:  flex
%if 0%{?suse_version} > 1320
BuildRequires:  libdb-4_8-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(libnsl)
BuildRequires:  pkgconfig(libtirpc)
%endif
%if %{enable_selinux}
BuildRequires:  libselinux-devel
%endif
%define libpam_so_version 0.84.2
%define libpam_misc_so_version 0.82.1
%define libpamc_so_version 0.82.1
#
Version:        1.3.1
Release:        0
Summary:        A Security Tool that Provides Authentication for Applications
License:        GPL-2.0-or-later OR BSD-3-Clause
Group:          System/Libraries
PreReq:         permissions
%if 0%{?suse_version} >= 1330
Requires(pre):  group(shadow)
Requires(pre):  user(root)
%endif
# All login.defs variables require support from shadow side.
# Upgrade this symbol version only if new variables appear!
# Verify by shadow-login_defs-check.sh from shadow source package.
# Recent symbol includes variable from encryption_method_nis.diff.
Requires:       login_defs-support-for-pam >= 1.3.1

#DL-URL:	https://fedorahosted.org/releases/l/i/linux-pam/
Source:         Linux-PAM-%{version}.tar.xz
Source1:        Linux-PAM-%{version}-docs.tar.xz
Source2:        securetty
Source3:        other.pamd
Source4:        common-auth.pamd
Source5:        common-account.pamd
Source6:        common-password.pamd
Source7:        common-session.pamd
Source8:        etc.environment
Source9:        baselibs.conf
Source10:       unix2_chkpwd.c
Source11:       unix2_chkpwd.8
Source12:       pam-login_defs-check.sh
Patch0:         fix-man-links.dif
Patch2:         pam-limit-nproc.patch
Patch3:         encryption_method_nis.diff
Patch4:         pam-hostnames-in-access_conf.patch
Patch5:         use-correct-IP-address.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libdb-4_8-devel
# Remove with next version update:
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.



%package doc
Summary:        Documentation for Pluggable Authentication Modules
Group:          Documentation/HTML
%if 0%{?suse_version} >= 1140
BuildArch:      noarch
%endif

%description doc
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

This package contains the documentation.



%package devel
Summary:        Include Files and Libraries for PAM-Development
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
cp -a %{S:12} .
%patch0 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p0
%patch5 -p1

%build
bash ./pam-login_defs-check.sh
autoreconf -fiv
export CFLAGS="%optflags -DNDEBUG"
%configure \
	--sbindir=/sbin \
	--includedir=%_includedir/security \
	--docdir=%{_docdir}/pam \
	--htmldir=%{_docdir}/pam/html \
	--pdfdir=%{_docdir}/pam/pdf \
        --libdir=/%{_lib} \
	--enable-isadir=../../%{_lib}/security \
        --enable-securedir=/%{_lib}/security
make %{?_smp_mflags}
%__cc -fwhole-program -fpie -pie -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE %{optflags} -I$RPM_BUILD_DIR/Linux-PAM-%{version}/libpam/include %{SOURCE10} -o $RPM_BUILD_DIR/unix2_chkpwd -L$RPM_BUILD_DIR/Linux-PAM-%{version}/libpam/.libs/ -lpam

%check
make %{?_smp_mflags} check

%install
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
mkdir -p $RPM_BUILD_ROOT/usr/include/security
mkdir -p $RPM_BUILD_ROOT/%{_lib}/security
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p -m 755 $RPM_BUILD_ROOT%{_libdir}
make DESTDIR=$RPM_BUILD_ROOT install
/sbin/ldconfig -n $RPM_BUILD_ROOT/%{_lib}
# Install documentation
make -C doc install DESTDIR=$RPM_BUILD_ROOT
# install /etc/environment
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT/etc/environment
# install securetty
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/etc
%ifarch s390 s390x
echo "ttyS0" >> $RPM_BUILD_ROOT/etc/securetty
echo "ttyS1" >> $RPM_BUILD_ROOT/etc/securetty
echo "hvc0" >> $RPM_BUILD_ROOT/etc/securetty
echo "hvc1" >> $RPM_BUILD_ROOT/etc/securetty
echo "hvc2" >> $RPM_BUILD_ROOT/etc/securetty
echo "hvc3" >> $RPM_BUILD_ROOT/etc/securetty
echo "hvc4" >> $RPM_BUILD_ROOT/etc/securetty
echo "hvc5" >> $RPM_BUILD_ROOT/etc/securetty
echo "hvc6" >> $RPM_BUILD_ROOT/etc/securetty
echo "hvc7" >> $RPM_BUILD_ROOT/etc/securetty
echo "sclp_line0" >> $RPM_BUILD_ROOT/etc/securetty
echo "ttysclp0" >> $RPM_BUILD_ROOT/etc/securetty
%endif
# install /etc/security/namespace.d used by pam_namespace.so for namespace.conf iscript
install -d $RPM_BUILD_ROOT%{_sysconfdir}/security/namespace.d
# install other.pamd and common-*.pamd
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/other
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/common-auth
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT/etc/pam.d/common-account
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT/etc/pam.d/common-password
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT/etc/pam.d/common-session
rm $RPM_BUILD_ROOT/%{_lib}/libpam.so
ln -sf ../../%{_lib}/libpam.so.%{libpam_so_version} $RPM_BUILD_ROOT%{_libdir}/libpam.so
rm $RPM_BUILD_ROOT/%{_lib}/libpamc.so
ln -sf ../../%{_lib}/libpamc.so.%{libpamc_so_version} $RPM_BUILD_ROOT%{_libdir}/libpamc.so
rm $RPM_BUILD_ROOT/%{_lib}/libpam_misc.so
ln -sf ../../%{_lib}/libpam_misc.so.%{libpam_misc_so_version} $RPM_BUILD_ROOT%{_libdir}/libpam_misc.so
#
# Remove crap
#
rm -rf $RPM_BUILD_ROOT/%{_lib}/*.la $RPM_BUILD_ROOT/%{_lib}/security/*.la
for x in pam_unix_auth pam_unix_acct pam_unix_passwd pam_unix_session; do
  ln -f $RPM_BUILD_ROOT/%{_lib}/security/pam_unix.so $RPM_BUILD_ROOT/%{_lib}/security/$x.so
done
#
# Install READMEs of PAM modules
#
DOC=$RPM_BUILD_ROOT%{_defaultdocdir}/pam
mkdir -p $DOC/modules
(
  cd modules;
  for i in pam_*/README ; do
    cp -fpv ${i} $DOC/modules/README.`dirname ${i}`
  done
)
#
# pam_tally is deprecated since ages
#
rm -f $RPM_BUILD_ROOT/%{_lib}/security/pam_tally.so
rm -f $RPM_BUILD_ROOT/sbin/pam_tally
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/pam_tally.8*
rm -f $RPM_BUILD_ROOT%{_defaultdocdir}/pam/modules/README.pam_tally
# Install unix2_chkpwd
install -m 755 $RPM_BUILD_DIR/unix2_chkpwd $RPM_BUILD_ROOT/sbin/
install -m 644 $RPM_SOURCE_DIR/unix2_chkpwd.8 $RPM_BUILD_ROOT%{_mandir}/man8/
# Create filelist with translatins
%{find_lang} Linux-PAM

%verifyscript
%verify_permissions -e /sbin/unix_chkpwd
%verify_permissions -e /sbin/unix2_chkpwd

%post
/sbin/ldconfig
%set_permissions /sbin/unix_chkpwd
%set_permissions /sbin/unix2_chkpwd

%postun -p /sbin/ldconfig

%files -f Linux-PAM.lang
%defattr(-,root,root)
%dir %{_sysconfdir}/pam.d
%dir %{_sysconfdir}/security
%dir %{_sysconfdir}/security/limits.d
%dir %{_defaultdocdir}/pam
%config(noreplace) %{_sysconfdir}/pam.d/other
%config(noreplace) %{_sysconfdir}/pam.d/common-*
%config(noreplace) %{_sysconfdir}/securetty
%config(noreplace) %{_sysconfdir}/environment
%config(noreplace) %{_sysconfdir}/security/access.conf
%config(noreplace) %{_sysconfdir}/security/group.conf
%config(noreplace) %{_sysconfdir}/security/limits.conf
%config(noreplace) %{_sysconfdir}/security/pam_env.conf
%if %{enable_selinux}
%config(noreplace) %{_sysconfdir}/security/sepermit.conf
%endif
%config(noreplace) %{_sysconfdir}/security/time.conf
%config(noreplace) %{_sysconfdir}/security/namespace.conf
%config(noreplace) %{_sysconfdir}/security/namespace.init
%dir  %{_sysconfdir}/security/namespace.d
%doc NEWS
%license COPYING
%doc %{_mandir}/man5/environment.5*
%doc %{_mandir}/man5/*.conf.5*
%doc %{_mandir}/man5/pam.d.5*
%doc %{_mandir}/man8/*
/%{_lib}/libpam.so.0
/%{_lib}/libpam.so.%{libpam_so_version}
/%{_lib}/libpamc.so.0
/%{_lib}/libpamc.so.%{libpamc_so_version}
/%{_lib}/libpam_misc.so.0
/%{_lib}/libpam_misc.so.%{libpam_misc_so_version}
%dir /%{_lib}/security
/%{_lib}/security/pam_access.so
/%{_lib}/security/pam_cracklib.so
/%{_lib}/security/pam_debug.so
/%{_lib}/security/pam_deny.so
/%{_lib}/security/pam_echo.so
/%{_lib}/security/pam_env.so
/%{_lib}/security/pam_exec.so
/%{_lib}/security/pam_faildelay.so
/%{_lib}/security/pam_filter.so
%dir /%{_lib}/security/pam_filter
/%{_lib}/security//pam_filter/upperLOWER
/%{_lib}/security/pam_ftp.so
/%{_lib}/security/pam_group.so
/%{_lib}/security/pam_issue.so
/%{_lib}/security/pam_keyinit.so
/%{_lib}/security/pam_lastlog.so
/%{_lib}/security/pam_limits.so
/%{_lib}/security/pam_listfile.so
/%{_lib}/security/pam_localuser.so
/%{_lib}/security/pam_loginuid.so
/%{_lib}/security/pam_mail.so
/%{_lib}/security/pam_mkhomedir.so
/%{_lib}/security/pam_motd.so
/%{_lib}/security/pam_namespace.so
/%{_lib}/security/pam_nologin.so
/%{_lib}/security/pam_permit.so
/%{_lib}/security/pam_pwhistory.so
/%{_lib}/security/pam_rhosts.so
/%{_lib}/security/pam_rootok.so
/%{_lib}/security/pam_securetty.so
%if %{enable_selinux}
/%{_lib}/security/pam_selinux.so
/%{_lib}/security/pam_sepermit.so
%endif
/%{_lib}/security/pam_shells.so
/%{_lib}/security/pam_stress.so
/%{_lib}/security/pam_succeed_if.so
/%{_lib}/security/pam_tally2.so
/%{_lib}/security/pam_time.so
/%{_lib}/security/pam_timestamp.so
/%{_lib}/security/pam_tty_audit.so
/%{_lib}/security/pam_umask.so
/%{_lib}/security/pam_unix.so
/%{_lib}/security/pam_unix_acct.so
/%{_lib}/security/pam_unix_auth.so
/%{_lib}/security/pam_unix_passwd.so
/%{_lib}/security/pam_unix_session.so
/%{_lib}/security/pam_userdb.so
/%{_lib}/security/pam_warn.so
/%{_lib}/security/pam_wheel.so
/%{_lib}/security/pam_xauth.so
/sbin/mkhomedir_helper
/sbin/pam_tally2
/sbin/pam_timestamp_check
%verify(not mode) %attr(4755,root,shadow) /sbin/unix_chkpwd
%verify(not mode) %attr(4755,root,shadow) /sbin/unix2_chkpwd
%attr(0700,root,root) /sbin/unix_update

%files doc
%defattr(644,root,root,755)
%dir %{_defaultdocdir}/pam
%doc %{_defaultdocdir}/pam/html
%doc %{_defaultdocdir}/pam/modules
%doc %{_defaultdocdir}/pam/pdf
%doc %{_defaultdocdir}/pam/*.txt

%files devel
%defattr(644,root,root,755)
%dir /usr/include/security
%doc %{_mandir}/man3/pam*
%doc %{_mandir}/man3/misc_conv.3*
%{_includedir}/security/*.h
%{_libdir}/libpam.so
%{_libdir}/libpamc.so
%{_libdir}/libpam_misc.so

%changelog
