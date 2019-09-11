#
# spec file for package yum
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           yum
Version:        3.4.3
Release:        0
Summary:        RPM installer/updater
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            http://yum.baseurl.org/
Source:         %{name}-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}-updatesd.service
# PATCH-FIX-OPENSUSE
Patch1:         %{name}-3.4.3-license-to-confirm.patch
# PATCH-FIX-OPENSUSE
Patch2:         %{name}-3.4.3-suse-changelogs.patch
# PATCH-FIX-OPENSUSE
Patch3:         %{name}-3.4.3-suse-missing-tags.patch
# PATCH-FIX-OPENSUSE
Patch6:         %{name}-3.4.3-add-lib-cpp-file.patch
# PATCH-FIX-UPSTREAM
Patch7:         %{name}-3.4.3-updatesd-dbus-conf-syntax.patch
# PATCH-FIX-UPSTREAM
Patch8:         %{name}-3.4.3-speedup-bnc810074.patch
# PATCH-FIX-OPENSUSE
Patch9:         %{name}-3.4.3-fix-repo-tag.patch
# PATCH-FIX-UPSTREAM bnc#896844
Patch10:        %{name}-3.4.3-preserve-queryparams-in-urls.patch
# PATCH-FIX-OPENSUSE
Patch11:        %{name}-3.2.29-parse-restart_suggested.patch
# PATCH-FIX-UPSTREAM
Patch12:        yum-3.4.3-correct-rpmdb-path.patch
BuildRequires:  dbus-1
BuildRequires:  intltool
BuildRequires:  python2-gpgme
BuildRequires:  python2-iniparse
BuildRequires:  python2-nose
BuildRequires:  python2-rpm
BuildRequires:  python2-setuptools
BuildRequires:  python2-urlgrabber
BuildRequires:  systemd
Requires:       python2-yum = %{version}-%{release}
Requires:       rpm >= 4.4.0
Requires(pre):  %fillup_prereq
Requires(pre):  coreutils
Recommends:     %{name}-lang = %{version}
Suggests:       cron
Suggests:       logrotate
BuildArch:      noarch
%lang_package

%description
Yum is a utility that can check for and automatically download and
install updated RPM packages. Dependencies are obtained and downloaded
automatically prompting the user as necessary.

%package updatesd
Summary:        YUM update notification daemon
Group:          System/Packages
Requires:       %{name} = %{version}
Requires:       dbus-1-python
Requires:       python-gobject2
%{?systemd_requires}

%description updatesd
yum-updatesd provides a daemon which checks for available updates and
can notify you when they are available via email, syslog or dbus.

%package -n python2-yum
Summary:        YUM update notification daemon
Group:          Development/Languages/Python
Requires:       dbus-1-python
Requires:       python2-gobject2
Requires:       python2-gpgme
Requires:       python2-iniparse
Requires:       python2-pyliblzma
Requires:       python2-rpm
Requires:       python2-urlgrabber
Requires:       python2-xml
Requires:       yum-metadata-parser >= 1.1.0
Provides:       python-yum = %{version}-%{release}
Obsoletes:      python-yum < %{version}-%{release}
Provides:       yum-common = %{version}
Obsoletes:      yum-common < %{version}

%description -n python2-yum
Common libraries for YUM based programs

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11
%patch12 -p1

# Fix non-executable scripts rpmlint issue:
sed -i "s|#!.*%{_bindir}/python.*||" rpmUtils/{arch,__init__,miscutils,oldUtils,transaction,updates}.py
sed -i "s|#!.*%{_bindir}/python.*||" yum/{callbacks,comps,config,constants,depsolve,Errors,failover,history,i18n,__init__,logginglevels,mdparser,metalink,misc,packages,packageSack,parser,pgpmsg,pkgtag_db,plugins,repoMDObject,repos,rpmsack,rpmtrans,sqlitesack,sqlutils,transactioninfo,update_md,yumRepo}.py

%build
make %{?_smp_mflags}

%install
%make_install
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}/yum.conf

# install custom systemd service
install -Dm 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}-updatesd.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcyum-updatesd

# remove the original init
rm %{buildroot}%{_sysconfdir}/rc.d/init.d/yum-updatesd
rm -rf %{buildroot}%{_sysconfdir}/rc.d

mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/pluginconf.d/ \
         %{buildroot}%{_libexecdir}/yum-plugins/ \
         %{buildroot}%{_fillupdir}/
mv %{buildroot}%{_sysconfdir}/sysconfig/yum-cron %{buildroot}%{_fillupdir}/sysconfig.yum-cron
%find_lang %{name}

# The i18n module fails to initialize
#%check
#export PYTHONPATH=%{buildroot}%{python_sitelib}
#nosetests -v

%post
%fillup_only -n yum-cron
# if we are upgrading from older distros the config should be moved
# to the new place
CONFD="%{_sysconfdir}/yum"
OCONF="%{_sysconfdir}/yum.conf"
NCONF="${CONFD}/yum.conf"
NCONFB="${CONFD}/yum.conf.rpmsave"
if [ -e "$OCONF" ] ; then
#
# in worst case we will get:
# /etc/yum/yum.conf         - the old /etc/yum.conf
# /etc/yum/yum.conf.rpmnew  - the config of the newly installed package.
# /etc/yum/yum.conf.rpmsave - the old /etc/yum/yum.conf
#
    if [ ! -d "$CONFD" ] ; then
        mkdir "$CONFD"
    fi
#
# we dont need to handle the case that /etc/yum/yum.conf
# exists. rpm does that for us.
# it creates /etc/yum/yum.conf.rpmnew
#
    if [ -e "$NCONF" ] ; then
        mv "$NCONF" "$NCONFB"
        echo "warning: %{_sysconfdir}/yum/yum.conf backed up as %{_sysconfdir}/yum/yum.conf.rpmsave" >&2
    fi
    echo "warning: %{_sysconfdir}/yum.conf moved to %{_sysconfdir}/yum/yum.conf" >&2
    mv "$OCONF" "$NCONF"
fi
# migrate /etc/yum.repos.d to /etc/yum/repos.d/
if [ -d "%{_sysconfdir}/yum.repos.d" ] ; then
    if [ ! -d "%{_sysconfdir}/yum/repos.d" ] ; then
        mkdir "%{_sysconfdir}/yum/repos.d"
    fi
    if [ "%{_sysconfdir}/yum.repos.d/*" != '%{_sysconfdir}/yum.repos.d/*' ] ; then
    for i in %{_sysconfdir}/yum.repos.d/*;
    do
      NCONF="%{_sysconfdir}/yum/repos.d/`basename $i`"
      NCONFB="%{_sysconfdir}/yum/repos.d/`basename $i`.rpmsave"
      OCONF="%{_sysconfdir}/yum.repos.d/`basename $i`"
      if [ -e "$NCONF" ] ; then
          mv "$NCONF" "$NCONFB"
          echo "warning: $NCONF backed up as $NCONFB" >&2
      fi
      echo "warning: $OCONF moved to $NCONF" >&2
      mv "$OCONF" "$NCONF"
    done
    fi
fi

%pre updatesd
%service_add_pre %{name}-updatesd.service

%post updatesd
%service_add_post %{name}-updatesd.service

%preun updatesd
%service_del_preun %{name}-updatesd.service

%postun updatesd
%service_del_postun %{name}-updatesd.service

%files
%license COPYING
%doc README AUTHORS TODO PLUGINS
%dir %{_localstatedir}/cache/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/repos.d
%dir %{_sysconfdir}/%{name}/pluginconf.d
%dir %{_libexecdir}/yum-plugins
%config(noreplace) %{_sysconfdir}/%{name}/yum.conf
%config %{_sysconfdir}/logrotate.d/%{name}
%{_fillupdir}/sysconfig.yum-cron
%{_sysconfdir}/cron.daily/0yum.cron
%config %{_sysconfdir}/%{name}/yum-daily.yum
%config %{_sysconfdir}/%{name}/yum-weekly.yum
%config %{_sysconfdir}/bash_completion.d/yum.bash
%{_mandir}/*/*
%defattr(0755,root,root)
%{_datadir}/yum-cli
%{_bindir}/*
%exclude %{_mandir}/man*/yum-updatesd*

%files lang -f %{name}.lang

%files -n python2-yum
%{python_sitelib}/*

%files updatesd
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/yum-updatesd.conf
%{_unitdir}/%{name}-updatesd.service
%{_sbindir}/rcyum-updatesd
%attr(644,root,root) %config %{_sysconfdir}/dbus-1/system.d/yum-updatesd.conf
%config(noreplace) %{_sysconfdir}/%{name}/version-groups.conf
%{_sbindir}/yum-updatesd
%{_mandir}/man*/yum-updatesd*

%changelog
