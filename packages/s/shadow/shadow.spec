#
# spec file for package shadow
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


%if ! %{defined _distconfdir}
  %define _distconfdir %{_sysconfdir}
%else
  %define no_config 1
%endif
Name:           shadow
Version:        4.9
Release:        0
Summary:        Utilities to Manage User and Group Accounts
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/shadow-maint/shadow
Source:         https://github.com/shadow-maint/shadow/releases/download/v%{version}/shadow-%{version}.tar.xz
Source1:        pamd.tar.bz2
Source3:        useradd.local
Source4:        userdel-pre.local
Source5:        userdel-post.local
Source6:        shadow.service
Source7:        shadow.timer
Source42:       https://github.com/shadow-maint/shadow/releases/download/v%{version}/shadow-%{version}.tar.xz.asc
Source43:       %{name}.keyring
# SOURCE-FEATURE-SUSE shadow-login_defs-check.sh sbrabec@suse.com -- Supplementary script that verifies coverage of variables in shadow-login_defs-unused-by-pam.patch and other patches.
Source44:       shadow-login_defs-check.sh
# PATCH-FIX-SUSE shadow-login_defs-unused-by-pam.patch kukuk@suse.com -- Remove variables that have no use with PAM.
Patch0:         shadow-login_defs-unused-by-pam.patch
# PATCH-FEATURE-SUSE userdel-script.patch kukuk@suse.com -- Add support for USERDEL_PRECMD and USERDEL_POSTCMD.
Patch1:         userdel-script.patch
# PATCH-FEATURE-SUSE useradd-script.patch kukuk@suse.com -- Add support for USERADD_CMD.
Patch2:         useradd-script.patch
# PATCH-FEATURE-SUSE chkname-regex.patch kukuk@suse.com -- Username restriction by regex.
Patch3:         chkname-regex.patch
# PATCH-FEATURE-SUSE useradd-default.patch kukuk@suse.com -- Change useradd defaults group to 1000.
Patch4:         useradd-default.patch
# PATCH-FEATURE-SUSE shadow-util-linux.patch sbrabec@suse.com -- Add support for util-linux specific variables, delete shadow login, su runuser specific.
Patch5:         shadow-util-linux.patch
# PATCH-FEATURE-SUSE shadow-login_defs-comments.patch kukuk@suse.com -- Adjust login.defs comments.
Patch6:         shadow-login_defs-comments.patch
# PATCH-FEATURE-SUSE shadow-login_defs-suse.patch kukuk@suse.com -- Customize login.defs.
Patch7:         shadow-login_defs-suse.patch
# PATCH-FEATURE-SUSE Copy also skeleton files from /usr/etc/skel (boo#1173321)
Patch8:         useradd-userkeleton.patch
# PATCH-FIX-SUSE disable_new_audit_function.patch adam.majer@suse.de -- Disable newer libaudit functionality for older distributions.
Patch9:         disable_new_audit_function.patch
# PATCH-FIX-UPSTREAM libsubid-build-fix.patch mvetter@suse.de -- Fix build with libsubid (f4a84e, 537b8c, fa986b)
Patch10:        libsubid-build-fix.patch
# PATCH-FIX-UPSTREAM shadow-libeconf-include.patch mvetter@suse.de -- Include libeconf to new*idmap (c68470)
Patch11:        shadow-libeconf-include.patch
# PATCH-FIX-UPSTREAM shadow-fix-sigabrt.patch mvetter@suse.de -- Fix SIGABRT https://github.com/shadow-maint/shadow/issues/394
Patch12:        shadow-fix-sigabrt.patch
# PATCH-FIX-UPSTREAM shadow-passwd-handle-null.patch mvetter@suse.de -- Fix passwd NULL handling https://github.com/shadow-maint/shadow/pull/398
Patch13:        shadow-passwd-handle-null.patch
# PATCH-FIX-UPSTREAM shadow-4.9-sgent-free.patch mvetter@suse.de -- Fix double free (boo#1190145)
Patch14:        shadow-4.9-sgent-free.patch
# PATCH-FIX-UPSTREAM shadow-4.9-useradd-subuid.patch mvetter@suse.de -- Fix generating empty subid range and undeclared subid_count (boo#1190146)
Patch15:        shadow-4.9-useradd-subuid.patch
# PATCH-FIX-UPSTREAM shadow-4.9-newgrp-segfault.patch mvetter@suse.de -- Fix segfault in newgrp (gh#437)
Patch16:        shadow-4.9-newgrp-segfault.patch
# PATCH-FIX-UPSTREAM shadow-4.9-pwck-segfault.patch mvetter@suse.de -- Fix segfault in pwck (gh#445)
Patch17:        shadow-4.9-pwck-segfault.patch
BuildRequires:  audit-devel > 2.3
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsemanage-devel
BuildRequires:  libtool
BuildRequires:  pam-devel
BuildRequires:  xz
Requires:       login_defs >= %{version}
Requires(pre):  group(root)
Requires(pre):  group(shadow)
Requires(pre):  permissions
Requires(pre):  user(root)
Provides:       pwdutils = 3.2.20
Obsoletes:      pwdutils <= 3.2.19
Provides:       useradd_or_adduser_dep
# It should be %%if %%{defined no_config}, but OBS cannot handle it:
%if 0%{?suse_version} >= 1550
BuildRequires:  libeconf-devel
%endif

%description
This package includes the necessary programs for converting plain
password files to the shadow password format and to manage user and
group accounts.

%package -n login_defs
Summary:        The login.defs configuration file
# Virtual provides for supported variables in login.defs.
# It prevents references to unknown variables.
# Upgrade them only if shadow-util-linux.patch or
# encryption_method_nis.patch has to be ported!
# Call shadow-login_defs-check.sh before!
Group:          System/Base
Provides:       login_defs-support-for-pam = 1.5.2
Provides:       login_defs-support-for-util-linux = 2.37
BuildArch:      noarch

%description -n login_defs
This package contains the default login.defs configuration file
as used by util-linux, pam and shadow.

%package -n libsubid3
Summary:        A library to manage subordinate uid and gid ranges
Group:          System/Base

%description -n libsubid3
Utility library that provides a way to manage subid ranges.

%package -n libsubid-devel
Summary:        Development files for libsubid3
Group:          System/Base
Requires:       libsubid3 = %{version}

%description -n libsubid-devel
Development files for libsubid3.

%prep
%setup -q -a 1
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%if 0%{?suse_version} < 1330
%patch9 -p1
%endif
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

iconv -f ISO88591 -t utf-8  doc/HOWTO > doc/HOWTO.utf8
mv -v doc/HOWTO.utf8 doc/HOWTO

%build
export CFLAGS="%{optflags} -fpie"
export LDFLAGS="-pie"

autoreconf -fvi
%configure \
  --enable-shadowgrp \
  --enable-account-tools-setuid \
  --with-audit \
  --with-libpam \
  --with-sha-crypt \
  --with-acl \
  --with-attr \
  --with-nscd \
  --with-selinux \
  --without-libcrack \
  --with-group-name-max-length=32 \
  --enable-vendordir=%{_distconfdir}
%make_build
#  --disable-shared \ currently doesn't build with this. See https://github.com/shadow-maint/shadow/issues/336

%install
%make_install gnulocaledir=%{buildroot}/%{_datadir}/locale MKINSTALLDIRS=`pwd`/mkinstalldirs
# Separate call to install man pages. See https://github.com/shadow-maint/shadow/issues/389
%make_install -C man install-man

# install useradd.local, userdel.local, ...
install -m 0755 %{SOURCE3} %{buildroot}/%{_sbindir}/
install -m 0755 %{SOURCE4} %{buildroot}/%{_sbindir}/
install -m 0755 %{SOURCE5} %{buildroot}/%{_sbindir}/
install -Dm644 %{SOURCE6} %{buildroot}%{_unitdir}/shadow.service
install -Dm644 %{SOURCE7} %{buildroot}%{_unitdir}/shadow.timer

# add empty /etc/sub{u,g}id files
touch %{buildroot}/%{_sysconfdir}/subuid
touch %{buildroot}/%{_sysconfdir}/subgid

# Remove binaries we don't use.
rm %{buildroot}/%{_bindir}/groups
rm %{buildroot}/%{_mandir}/man1/groups.*
rm %{buildroot}/%{_mandir}/*/man1/groups.*

rm %{buildroot}/%{_sbindir}/grpconv
rm %{buildroot}/%{_mandir}/man8/grpconv.*
rm %{buildroot}/%{_mandir}/*/man8/grpconv.*
rm %{buildroot}/%{_sbindir}/grpunconv
rm %{buildroot}/%{_mandir}/man8/grpunconv.*
rm %{buildroot}/%{_mandir}/*/man8/grpunconv.*

rm %{buildroot}/%{_sbindir}/groupmems
rm %{buildroot}/%{_mandir}/man8/groupmems.*
rm %{buildroot}/%{_mandir}/*/man8/groupmems.*
rm %{buildroot}%{_sysconfdir}/pam.d/groupmems

rm %{buildroot}/%{_bindir}/login
rm %{buildroot}/%{_mandir}/man1/login.*
rm %{buildroot}/%{_mandir}/*/man1/login.*
rm %{buildroot}%{_sysconfdir}/pam.d/login

rm %{buildroot}/%{_bindir}/su
rm %{buildroot}/%{_mandir}/man1/su.*
rm %{buildroot}/%{_mandir}/*/man1/su.*
rm %{buildroot}/%{_mandir}/man5/suauth.*
rm %{buildroot}/%{_mandir}/*/man5/suauth.*
rm %{buildroot}%{_sysconfdir}/pam.d/su

rm %{buildroot}/%{_bindir}/faillog
rm %{buildroot}/%{_mandir}/man5/faillog.*
rm %{buildroot}/%{_mandir}/*/man5/faillog.*
rm %{buildroot}/%{_mandir}/man8/faillog.*
rm %{buildroot}/%{_mandir}/*/man8/faillog.*

rm %{buildroot}/%{_sbindir}/logoutd
rm %{buildroot}/%{_mandir}/man8/logoutd.*
rm %{buildroot}/%{_mandir}/*/man8/logoutd.*
rm %{buildroot}/%{_sbindir}/nologin
rm %{buildroot}/%{_mandir}/man8/nologin.*
rm %{buildroot}/%{_mandir}/*/man8/nologin.*

rm %{buildroot}/%{_sbindir}/chgpasswd
rm %{buildroot}/%{_mandir}/man8/chgpasswd.*
rm %{buildroot}/%{_mandir}/*/man8/chgpasswd.*
rm %{buildroot}%{_sysconfdir}/pam.d/chgpasswd

rm %{buildroot}/%{_mandir}/man3/getspnam.*
rm %{buildroot}/%{_mandir}/*/man3/getspnam.*
rm %{buildroot}/%{_mandir}/man5/gshadow.5*
rm %{buildroot}/%{_mandir}/*/man5/gshadow.5*
rm %{buildroot}/%{_mandir}/man5/passwd.5*
rm %{buildroot}/%{_mandir}/*/man5/passwd.5*

rm -rf %{buildroot}%{_mandir}/{??,??_??}

rm %{buildroot}/%{_libdir}/libsubid.la

# Move /etc to /usr/etc
if [ ! -d %{buildroot}%{_distconfdir} ]; then
    mkdir -p %{buildroot}%{_distconfdir}
    mv %{buildroot}%{_sysconfdir}/{login.defs,pam.d} %{buildroot}%{_distconfdir}
    mkdir -p %{buildroot}%{_sysconfdir}/login.defs.d
fi

%find_lang shadow

%pre
%service_add_pre shadow.service shadow.timer
for i in pam.d/chage pam.d/chfn pam.d/chpasswd pam.d/chsh pam.d/groupadd pam.d/groupdel pam.d/groupmod pam.d/newusers pam.d/passwd pam.d/useradd pam.d/userdel pam.d/usermod; do
  test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%pre -n login_defs
test -f %{_sysconfdir}/login.defs.rpmsave && mv -v %{_sysconfdir}/login.defs.rpmsave %{_sysconfdir}/login.defs.rpmsave.old ||:

%post
%set_permissions %{_bindir}/chage
%set_permissions %{_bindir}/chfn
%set_permissions %{_bindir}/chsh
%set_permissions %{_bindir}/expiry
%set_permissions %{_bindir}/gpasswd
%set_permissions %{_bindir}/newgrp
%set_permissions %{_bindir}/passwd
%set_permissions %{_bindir}/newgidmap
%set_permissions %{_bindir}/newuidmap

%service_add_post shadow.service shadow.timer

%verifyscript
%verify_permissions %{_bindir}/chage
%verify_permissions %{_bindir}/chfn
%verify_permissions %{_bindir}/chsh
%verify_permissions %{_bindir}/expiry
%verify_permissions %{_bindir}/gpasswd
%verify_permissions %{_bindir}/newgrp
%verify_permissions %{_bindir}/passwd
%verify_permissions %{_bindir}/newgidmap
%verify_permissions %{_bindir}/newuidmap

%preun
%service_del_preun shadow.service shadow.timer

%postun
%service_del_postun shadow.service shadow.timer

%posttrans
%if %{defined no_config}
# Migration to /usr/etc
for i in pam.d/chage pam.d/chfn pam.d/chpasswd pam.d/chsh pam.d/groupadd pam.d/groupdel pam.d/groupmod pam.d/newusers pam.d/passwd pam.d/useradd pam.d/userdel pam.d/usermod; do
  test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%posttrans -n login_defs
# rpmsave file can be created by
# - change of owning package (SLE15 SP2->SP3, Leap 15.2->15.3)
# - Migration to /usr/etc (after SLE15 and Leap 15)
test -f %{_sysconfdir}/login.defs.rpmsave && mv -v %{_sysconfdir}/login.defs.rpmsave %{_sysconfdir}/login.defs ||:

%post -n libsubid3 -p /sbin/ldconfig
%postun -n libsubid3 -p /sbin/ldconfig

%files -f shadow.lang
%license COPYING
%doc NEWS doc/HOWTO README
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/subuid
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/subgid
%if %{defined no_config}
%{_distconfdir}/pam.d/chage
%{_distconfdir}/pam.d/chfn
%{_distconfdir}/pam.d/chsh
%{_distconfdir}/pam.d/passwd
%{_distconfdir}/pam.d/useradd
%{_distconfdir}/pam.d/chpasswd
%{_distconfdir}/pam.d/groupadd
%{_distconfdir}/pam.d/groupdel
%{_distconfdir}/pam.d/groupmod
%{_distconfdir}/pam.d/newusers
%{_distconfdir}/pam.d/useradd
%{_distconfdir}/pam.d/userdel
%{_distconfdir}/pam.d/usermod
%else
%config %{_sysconfdir}/pam.d/chage
%config %{_sysconfdir}/pam.d/chfn
%config %{_sysconfdir}/pam.d/chsh
%config %{_sysconfdir}/pam.d/passwd
%config %{_sysconfdir}/pam.d/chpasswd
%config %{_sysconfdir}/pam.d/groupadd
%config %{_sysconfdir}/pam.d/groupdel
%config %{_sysconfdir}/pam.d/groupmod
%config %{_sysconfdir}/pam.d/newusers
%config %{_sysconfdir}/pam.d/useradd
%config %{_sysconfdir}/pam.d/userdel
%config %{_sysconfdir}/pam.d/usermod
%endif
%verify(not mode) %attr(2755,root,shadow) %{_bindir}/chage
%verify(not mode) %attr(4755,root,shadow) %{_bindir}/chfn
%verify(not mode) %attr(4755,root,shadow) %{_bindir}/chsh
%verify(not mode) %attr(4755,root,shadow) %{_bindir}/expiry
%verify(not mode) %attr(4755,root,shadow) %{_bindir}/gpasswd
%verify(not mode) %attr(4755,root,root) %{_bindir}/newgrp
%verify(not mode) %attr(4755,root,shadow) %{_bindir}/passwd
%verify(not mode) %attr(4755,root,shadow) %{_bindir}/newgidmap
%verify(not mode) %attr(4755,root,shadow) %{_bindir}/newuidmap
%{_bindir}/lastlog
%{_bindir}/sg
%attr(0755,root,root) %{_sbindir}/groupadd
%attr(0755,root,root) %{_sbindir}/groupdel
%attr(0755,root,root) %{_sbindir}/groupmod
%{_sbindir}/grpck
%{_sbindir}/pwck
%attr(0755,root,root) %{_sbindir}/useradd
%attr(0755,root,root) %{_sbindir}/userdel
%attr(0755,root,root) %{_sbindir}/usermod
%{_sbindir}/pwconv
%{_sbindir}/pwunconv
%attr(0755,root,root) %{_sbindir}/chpasswd
%attr(0755,root,root) %{_sbindir}/newusers
%{_sbindir}/vipw
%{_sbindir}/vigr
%verify(not md5 size mtime) %config(noreplace) %{_sbindir}/useradd.local
%verify(not md5 size mtime) %config(noreplace) %{_sbindir}/userdel-pre.local
%verify(not md5 size mtime) %config(noreplace) %{_sbindir}/userdel-post.local
%{_mandir}/man1/chage.1%{?ext_man}
%{_mandir}/man1/chfn.1%{?ext_man}
%{_mandir}/man1/chsh.1%{?ext_man}
%{_mandir}/man1/expiry.1%{?ext_man}
%{_mandir}/man1/gpasswd.1%{?ext_man}
%{_mandir}/man1/newgrp.1%{?ext_man}
%{_mandir}/man1/passwd.1%{?ext_man}
%{_mandir}/man1/sg.1%{?ext_man}
%{_mandir}/man3/shadow.3%{?ext_man}
%{_mandir}/man5/shadow.5%{?ext_man}
%{_mandir}/man8/chpasswd.8%{?ext_man}
%{_mandir}/man8/groupadd.8%{?ext_man}
%{_mandir}/man8/groupdel.8%{?ext_man}
%{_mandir}/man8/groupmod.8%{?ext_man}
%{_mandir}/man8/grpck.8%{?ext_man}
%{_mandir}/man8/lastlog.8%{?ext_man}
%{_mandir}/man8/newusers.8%{?ext_man}
%{_mandir}/man8/pwck.8%{?ext_man}
%{_mandir}/man8/pwconv.8%{?ext_man}
%{_mandir}/man8/pwunconv.8%{?ext_man}
%{_mandir}/man8/useradd.8%{?ext_man}
%{_mandir}/man8/userdel.8%{?ext_man}
%{_mandir}/man8/usermod.8%{?ext_man}
%{_mandir}/man8/vigr.8%{?ext_man}
%{_mandir}/man8/vipw.8%{?ext_man}
%{_mandir}/man5/subuid.5%{?ext_man}
%{_mandir}/man5/subgid.5%{?ext_man}
%{_mandir}/man1/newgidmap.1%{?ext_man}
%{_mandir}/man1/newuidmap.1%{?ext_man}

%{_unitdir}/*

%files -n login_defs
%if %{defined no_config}
%dir %{_sysconfdir}/login.defs.d
%attr(0644,root,root) %{_distconfdir}/login.defs
%else
%attr(0644,root,root) %config %{_sysconfdir}/login.defs
%endif
%{_mandir}/man5/login.defs.5%{?ext_man}

%files -n libsubid3
%{_libdir}/libsubid.so.*

%files -n libsubid-devel
%dir %{_includedir}/shadow
%{_includedir}/shadow/subid.h
%{_libdir}/libsubid.so

%changelog
