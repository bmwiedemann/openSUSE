#
# spec file for package cronie
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


%define cron_configs %{_sysconfdir}/pam.d/crond %{_sysconfdir}/crontab %{_sysconfdir}/cron.deny
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           cronie
Version:        1.6.1
Release:        0
Summary:        Cron Daemon
License:        BSD-3-Clause AND GPL-2.0-only AND MIT
Group:          System/Daemons
URL:            https://github.com/cronie-crond/%{name}
Source0:        https://github.com/cronie-crond/%{name}/archive/%{name}-%{version}.tar.gz
Source2:        run-crons
Source3:        sample.root
Source4:        deny.sample
Source7:        cron_to_cronie.README
Source8:        cron.service
Source9:        sysconfig.cron
# PATCH-FEATURE-OPENSUSE cronie-pam_config.diff added pam config file from old cron
Patch3:         cronie-pam_config.diff
# openSUSE set NHEADER_LINES to 3 - old openSUSE cron put three lines of comments
# in top of crontab file, so we want to hide this junk comments if user edit
# crontab file with crontab -e command, patch grabbed from old openSUSE cron
Patch4:         cronie-nheader_lines.diff
# we use cron.pid instead of crond.pid
Patch5:         cronie-crond_pid.diff
# PATCH-FIX-SUSE the first occurance of "/etc/anacrontab" was replaced by "/etc/crontab"
# in manpage file because the /etc/crontab is still used in SUSE.
Patch13:        fix-manpage-replace-anacrontab-with-crontab.patch
BuildRequires:  audit-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libselinux-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
Requires:       mail
Requires(post): %fillup_prereq
Requires(post): debianutils
Requires(post): permissions
Requires(pre):  cron
Suggests:       mailx
Conflicts:      cron <= 4.1
%{?systemd_requires}
# This is needed as cron subpkg has its own version
%{expand: %%define cronie_version %{version}}
%if 0%{?suse_version} >= 1330
Requires(pre):  group(trusted)
%endif

%description
cron automatically starts programs at specific times. Add new entries
with "crontab -e". (See "man 5 crontab" and "man 1 crontab" for
documentation.)

Under /etc, find the directories cron.hourly, cron.daily, cron.weekly,
and cron.monthly.  Scripts and programs that are located there are
started automatically.

%package -n cron
Version:        4.2
Release:        0
Summary:        Auxiliary package
Group:          System/Daemons
Requires:       %{name} = %{cronie_version}-%{release}
Requires(post): permissions

%description -n cron
Auxiliary package, needed for proper update from vixie-cron 4.1 to cronie 1.4.4

%package anacron
Summary:        Utility for running regular jobs
Group:          System/Base
Requires:       %{name} = %{cronie_version}

%description anacron
Anacron becames part of cronie. Anacron is used only for running regular jobs.
The default settings execute regular jobs by anacron, however this could be
overloaded in settings.

%prep
%setup -q -n %{name}-%{name}-%{cronie_version}
%patch3 -p1
%patch4
%patch5 -p1
cp %{SOURCE7} ./cron_to_cronie.README
%patch13 -p1

%build
# fill macro CRON_VERSION it is used in top three lines of crontab file,should be reworked
export CFLAGS="%{optflags} -DCRON_VERSION=\\\"%{version}\\\""
export LDFLAGS="-Wl,-z,relro,-z,now,-z,defs"
autoreconf -f -i
%configure \
	--with-audit \
	--enable-anacron \
	--with-pam \
	--with-selinux \
	--with-inotify \
	--enable-pie \
	SPOOL_DIR="%{_localstatedir}/spool/cron/tabs"
%make_build

%install
%make_install
mkdir -p -v %{buildroot}%{_localstatedir}/spool/cron/{tabs,lastrun}
mkdir -p -v %{buildroot}%{_sysconfdir}/cron.{d,hourly,daily,weekly,monthly}
install -v -m 600 %{SOURCE3} %{buildroot}%{_sysconfdir}/crontab
install -v -m 600 %{SOURCE4} %{buildroot}%{_sysconfdir}/cron.deny
install -v -d %{buildroot}%{_libexecdir}/cron
install -v %{SOURCE2} %{buildroot}%{_libexecdir}/cron
ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rccron
install -v -d %{buildroot}/%{_unitdir}
install -v -m 644 %{SOURCE8} %{buildroot}/%{_unitdir}
install -m 644 contrib/anacrontab %{buildroot}%{_sysconfdir}/anacrontab
install -c -m755 contrib/0anacron %{buildroot}%{_sysconfdir}/cron.hourly/0anacron
mkdir -p %{buildroot}%{_localstatedir}/spool/anacron
mv %{buildroot}%{_sbindir}/crond %{buildroot}%{_sbindir}/cron
mkdir -p %{buildroot}%{_fillupdir}
cp %{SOURCE9} %{buildroot}%{_fillupdir}/

mkdir -p %{buildroot}%{_sysconfdir}/cron.d
mkdir -p %{buildroot}%{_sysconfdir}/cron.hourly
mkdir -p %{buildroot}%{_sysconfdir}/cron.daily
mkdir -p %{buildroot}%{_sysconfdir}/cron.weekly
mkdir -p %{buildroot}%{_sysconfdir}/cron.monthly

touch %{buildroot}%{_localstatedir}/spool/anacron/cron.daily
touch %{buildroot}%{_localstatedir}/spool/anacron/cron.weekly
touch %{buildroot}%{_localstatedir}/spool/anacron/cron.monthly

%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
mv %{buildroot}%{_sysconfdir}/pam.d/crond %{buildroot}%{_pam_vendordir}/
%endif

%pre
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in pam.d/crond ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif
%service_add_pre cron.service

%post
%set_permissions %{_sysconfdir}/crontab %{_bindir}/crontab
%{fillup_only -n cron}
%service_add_post cron.service
exit 0

%if 0%{?suse_version} > 1500
%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in pam.d/crond ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%verifyscript
%verify_permissions -e %{_sysconfdir}/crontab -e %{_bindir}/crontab

%preun
%service_del_preun cron.service

%postun
%service_del_postun cron.service

%post anacron
[ -e %{_localstatedir}/spool/anacron/cron.daily ] || touch %{_localstatedir}/spool/anacron/cron.daily
[ -e %{_localstatedir}/spool/anacron/cron.weekly ] || touch %{_localstatedir}/spool/anacron/cron.weekly
[ -e %{_localstatedir}/spool/anacron/cron.monthly ] || touch %{_localstatedir}/spool/anacron/cron.monthly

%verifyscript -n cron
%verify_permissions -e %{_sysconfdir}/cron.d/
%verify_permissions -e %{_sysconfdir}/cron.daily/
%verify_permissions -e %{_sysconfdir}/cron.hourly/
%verify_permissions -e %{_sysconfdir}/cron.monthly/
%verify_permissions -e %{_sysconfdir}/cron.weekly/

%post -n cron
%set_permissions %{_sysconfdir}/cron.d/
%set_permissions %{_sysconfdir}/cron.daily/
%set_permissions %{_sysconfdir}/cron.hourly/
%set_permissions %{_sysconfdir}/cron.monthly/
%set_permissions %{_sysconfdir}/cron.weekly/

%files
%license COPYING
%doc AUTHORS README ChangeLog
%dir %attr(700,root,root) %{_localstatedir}/spool/cron
%dir %attr(700,root,root) %{_localstatedir}/spool/cron/tabs
%dir %{_localstatedir}/spool/cron/lastrun
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/crond
%else
%config %{_sysconfdir}/pam.d/crond
%endif
%verify(not mode) %config(noreplace) %{_sysconfdir}/crontab
%config(noreplace) %{_sysconfdir}/cron.deny
%{_mandir}/man1/crontab.1%{?ext_man}
%{_mandir}/man5/crontab.5%{?ext_man}
%{_mandir}/man8/cron.8%{?ext_man}
%{_mandir}/man8/crond.8%{?ext_man}
%{_mandir}/man1/cronnext.1%{?ext_man}
%verify(not mode) %attr (4750,root,trusted) %{_bindir}/crontab
%attr (755,root,root) %{_sbindir}/cron
%attr (755,root,root) %{_bindir}/cronnext
%{_sbindir}/rccron
%{_libexecdir}/cron
%{_unitdir}/cron.service
%{_fillupdir}/sysconfig.cron

%files anacron
%{_sbindir}/anacron
%attr(0755,root,root) %{_sysconfdir}/cron.hourly/0anacron
%config(noreplace) %{_sysconfdir}/anacrontab
%dir %{_localstatedir}/spool/anacron
%ghost %verify(not md5 size mtime) %{_localstatedir}/spool/anacron/cron.daily
%ghost %verify(not md5 size mtime) %{_localstatedir}/spool/anacron/cron.weekly
%ghost %verify(not md5 size mtime) %{_localstatedir}/spool/anacron/cron.monthly
%{_mandir}/man5/anacrontab.5%{?ext_man}
%{_mandir}/man8/anacron.8%{?ext_man}

%files -n cron
%doc cron_to_cronie.README
%dir %attr(755,root,root) %{_sysconfdir}/cron.d
%dir %attr(755,root,root) %{_sysconfdir}/cron.hourly
%dir %attr(755,root,root) %{_sysconfdir}/cron.daily
%dir %attr(755,root,root) %{_sysconfdir}/cron.weekly
%dir %attr(755,root,root) %{_sysconfdir}/cron.monthly

%changelog
