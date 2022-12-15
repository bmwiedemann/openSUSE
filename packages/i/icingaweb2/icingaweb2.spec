#
# spec file for package icingaweb2
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2013-2017 Icinga Development Team | GPLv2+
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


%define revision 1

Name:           icingaweb2
Version:        2.11.3
Release:        %{revision}%{?dist}
Summary:        Icinga Web 2
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT
Group:          System/Monitoring
URL:            https://icinga.com
Source0:        https://github.com/Icinga/icingaweb2/archive/v%{version}/%{name}-%{version}.tar.gz
Source90:       README.SUSE
Source99:       %{name}-rpmlintrc
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?fedora} || 0%{?rhel} || 0%{?amzn}
%if 0%{?rhel} == 7
%define php_scl         rh-php73
%endif

%if 0%{?el5}%{?el6}%{?amzn}
%define use_selinux 0
%else
%define use_selinux 1
%endif

%if 0%{?php_scl:1}
%define php_scl_prefix  %{php_scl}-
%define php_runtime     %{php_scl_prefix}php-fpm
%define php_bin         /opt/rh/%{php_scl}/root/usr/bin/php
%define php_fpm         1
%else
%define php_runtime     %{php}
%endif

%define php             %{?php_scl_prefix}php
%define php_cli         %{php}-cli
%define php_common      %{php}-common
%define wwwconfigdir    %{_sysconfdir}/httpd/conf.d
%define wwwuser         apache

# extra requirements on RHEL
Requires:       %{php}-ldap
Requires:       %{php}-mysqlnd
Requires:       %{php}-pgsql
%endif

# minimum required PHP version
%define php_version 7.3.0

# unsupported PHP version
%define php_unsupported_version 8.2

%if 0%{?suse_version}
%define wwwconfigdir    %{_sysconfdir}/apache2/conf.d
%define wwwuser         wwwrun
%define php             php
%define php_runtime     mod_php_any
%define php_common      %{php}
%define php_cli         %{php}
# extra requirements on openSUSE
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  config(krb5)
Requires:       %{php}-ldap
Requires:       %{php}-mysql
Requires:       %{php}-pgsql
# conflict with older PHP on SLES and openSUSE
Conflicts:      php < %{php_version}
Conflicts:      php5 < %{php_version}
Conflicts:      php53
%endif

%{?amzn:Requires(pre):          shadow-utils}
%{?fedora:Requires(pre):        shadow-utils}
%{?rhel:Requires(pre):          shadow-utils}
%{?suse_version:Requires(pre):  pwdutils}

Requires:       %{php_common} >= %{php_version}
Requires:       %{php_runtime} >= %{php_version}
Conflicts:      %{php_runtime} >= %{php_unsupported_version}
%if 0%{?suse_version}
Requires:       apache2
%endif

Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-vendor-HTMLPurifier = %{version}-%{release}
Requires:       %{name}-vendor-JShrink = %{version}-%{release}
Requires:       %{name}-vendor-Parsedown = %{version}-%{release}
Requires:       %{name}-vendor-dompdf = %{version}-%{release}
Requires:       %{name}-vendor-lessphp = %{version}-%{release}
Requires:       icinga-l10n >= 1.1.0
Requires:       icinga-php-library >= 0.9.0
Requires:       icinga-php-thirdparty >= 0.11.0
Requires:       icingacli = %{version}-%{release}
Requires:       php-Icinga = %{version}-%{release}

%define basedir         %{_datadir}/%{name}
%define bindir          %{_bindir}
%define storagedir      %{_sharedstatedir}/%{name}
%define configdir       %{_sysconfdir}/%{name}
%define logdir          %{_localstatedir}/log/%{name}
%define phpdir          %{_datadir}/php
%define icingawebgroup  icingaweb2
%define docsdir         %{_datadir}/doc/%{name}

%description
Icinga Web 2 is the monitoring web interface for icinga2.

It comes with a completely new design and many user-friendly enhancements to
find the relevant information even faster.

%package common
Summary:        Common files for Icinga Web 2 and the Icinga CLI
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT
Group:          System/Monitoring
%{?amzn:Requires(pre):          shadow-utils}
%{?fedora:Requires(pre):        shadow-utils}
%{?rhel:Requires(pre):          shadow-utils}
%{?suse_version:Requires(pre):  pwdutils}
%if 0%{?suse_version} > 1320
Requires(pre):  system-user-wwwrun
%endif

%description common
Common files for Icinga Web 2 and the Icinga CLI.

%package -n php-Icinga
Summary:        Icinga Web 2 PHP library
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT
Group:          Development/Libraries/Other
Requires:       %{php_common} >= %{php_version}
Requires:       %{php}-gd %{php}-intl %{php}-mbstring
%if 0%{?sle_version} >= 150200
Requires:       %{php}-dom %{php}-curl %{php}-fileinfo
%endif
%{?rhel:Requires:           %{php}-pdo %{php}-xml}
%if 0%{?rhel} >= 8 || 0%{?fedora} >= 30
Requires:       %{php}-json
%endif rhel >= 8 || fedora >= 30
Requires:       %{name}-vendor-zf1 = %{version}-%{release}
%{?amzn:Requires:           %{php}-pecl-imagick}
%{?fedora:Requires:         php-pecl-imagick}
%{?suse_version:Requires:   %{php}-gettext %{php}-json %{php}-openssl %{php}-posix %{php}-ctype %{php}-pdo %{php}-xml %{php}-imagick %{php}-curl %{php}-fileinfo %{php}-dom}

%description -n php-Icinga
Icinga Web 2 PHP library.

%package -n icingacli
Summary:        Icinga CLI
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT
Group:          System/Monitoring
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{php_cli} >= %{php_version}
Requires:       bash-completion
Requires:       icinga-l10n >= 1.1.0
Requires:       icinga-php-library >= 0.9.0
Requires:       icinga-php-thirdparty >= 0.11.0
Requires:       php-Icinga = %{version}-%{release}
%if 0%{?suse_version}
# conflict with older PHP on SLES and openSUSE
Conflicts:      php < %{php_version}
Conflicts:      php5 < %{php_version}
Conflicts:      php53
Obsoletes:      %{name}-icingacli < %{version}
Provides:       %{name}-icingacli = %{version}
%endif

%description -n icingacli
Icinga CLI.


%if 0%{?use_selinux}
%define selinux_variants mls targeted

%package selinux
Summary:        SELinux policy for Icinga Web 2
License:        BSD-3-Clause AND GPL-2.0-or-later AND MIT
Group:          System/Base
BuildRequires:  checkpolicy
BuildRequires:  hardlink
BuildRequires:  selinux-policy-devel
Requires:       %{name} = %{version}-%{release}
Requires(post): policycoreutils
Requires(postun):policycoreutils

%description selinux
SELinux policy for Icinga Web 2.
%endif

%package vendor-dompdf
Summary:        Icinga Web 2 vendor library dompdf
License:        LGPL-2.1-only
Group:          Development/Libraries/Other
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{php_common} >= %{php_version}

%description vendor-dompdf
Icinga Web 2 vendor library dompdf.

%package vendor-HTMLPurifier
Summary:        Icinga Web 2 vendor library HTMLPurifier
License:        LGPL-2.1-only
Group:          Development/Libraries/Other
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{php_common} >= %{php_version}
# Need because of wrong version in very old icingaweb2 packages
Obsoletes:      %{name}-vendor-HTMLPurifier < %{version}
Obsoletes:      %{name}-vendor-HTMLPurifier > %{version}

%description vendor-HTMLPurifier
Icinga Web 2 vendor library HTMLPurifier.

%package vendor-JShrink
Summary:        Icinga Web 2 vendor library JShrink
License:        BSD-3-Clause
Group:          Development/Libraries/Other
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{php_common} >= %{php_version}

%description vendor-JShrink
Icinga Web 2 vendor library JShrink.

%package vendor-lessphp
Summary:        Icinga Web 2 vendor library lessphp
License:        MIT
Group:          Development/Libraries/Other
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{php_common} >= %{php_version}

%description vendor-lessphp
Icinga Web 2 vendor library lessphp.

%package vendor-Parsedown
Summary:        Icinga Web 2 vendor library Parsedown
License:        MIT
Group:          Development/Libraries/Other
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{php_common} >= %{php_version}

%description vendor-Parsedown
Icinga Web 2 vendor library Parsedown.

%package vendor-zf1
Summary:        Icinga Web 2's fork of Zend Framework 1
License:        BSD-3-Clause
Group:          Development/Libraries/Other
Requires:       %{php_common} >= %{php_version}
Obsoletes:      %{name}-vendor-Zend < 1.12.20
Provides:       %{name}-vendor-Zend = %{version}
Requires:       %{name}-common = %{version}-%{release}

%description vendor-zf1
Icinga Web 2's fork of Zend Framework 1.

%prep
%setup -q -n %{name}-%{version}
%if 0%{?use_selinux}
mkdir selinux
cp -p packages/selinux/icingaweb2.{fc,if,te} selinux
%endif
%if 0%{?suse_version}
# rpmlint
find . -type f "(" -name "*.css" -o -name "*.html" -o -name "*.json" -o -name "*.svg" -o -name "*.txt" -o -name "README" ")" -exec chmod -x "{}" "+"
%endif

%build
%if 0%{?use_selinux}
cd selinux
for selinuxvariant in %{selinux_variants}
do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv icingaweb2.pp icingaweb2.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -
%endif

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/{%{basedir}/{modules,library/vendor,public},%{bindir},%{configdir}/modules,%{storagedir},%{logdir},%{phpdir},%{wwwconfigdir},%{_datadir}/bash-completion/completions,%{docsdir}}
cp -prv application doc %{buildroot}/%{basedir}
cp -pv etc/bash_completion.d/icingacli %{buildroot}/%{_datadir}/bash-completion/completions/icingacli
cp -prv modules/{monitoring,setup,doc,translation,migrate} %{buildroot}/%{basedir}/modules
cp -prv library/Icinga %{buildroot}/%{phpdir}
cp -prv library/vendor/{dompdf,HTMLPurifier*,JShrink,lessphp,Parsedown,Zend} %{buildroot}/%{basedir}/library/vendor
cp -prv public/{css,font,img,js,error_norewrite.html,error_unavailable.html} %{buildroot}/%{basedir}/public
%if 0%{?php_fpm:1}
cp -pv packages/files/apache/icingaweb2.fpm.conf %{buildroot}/%{wwwconfigdir}/icingaweb2.conf
%else
cp -pv packages/files/apache/icingaweb2.conf %{buildroot}/%{wwwconfigdir}/icingaweb2.conf
%endif
cp -pv packages/files/bin/icingacli %{buildroot}/%{bindir}
%if 0%{?php_bin:1}
sed -i '1 s~#!.*~#!%{php_bin}~' %{buildroot}/%{bindir}/icingacli
%endif
sed -i 's|\/usr\/bin\/env php|\/usr\/bin\/php|g' %{buildroot}/%{basedir}/library/vendor/lessphp/bin/lessc
cp -pv packages/files/public/index.php %{buildroot}/%{basedir}/public
cp -prv etc/schema %{buildroot}/%{docsdir}
cp -prv packages/files/config/modules/{setup,translation} %{buildroot}/%{configdir}/modules
%if 0%{?use_selinux}
cd selinux
for selinuxvariant in %{selinux_variants}
do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  install -p -m 644 icingaweb2.pp.${selinuxvariant} %{buildroot}%{_datadir}/selinux/${selinuxvariant}/icingaweb2.pp
done
cd -
# TODO: Fix build problems on Icinga, see https://github.com/Icinga/puppet-icinga_build/issues/11
#/usr/sbin/hardlink -cv %%{buildroot}%%{_datadir}/selinux
%endif
%if 0%{?suse_version}
%fdupes %{buildroot}/%{basedir}/library
%endif

%pre
getent group icingacmd >/dev/null || groupadd -r icingacmd
%if 0%{?suse_version} && 0%{?suse_version} < 01200
usermod -A icingacmd,%{icingawebgroup} %{wwwuser}
%else
usermod -a -G icingacmd,%{icingawebgroup} %{wwwuser}
%endif
exit 0

%post
# enable required apache modules
if [ -x %{_sbindir}/a2enmod ]; then
   echo "Info: adding rewrite to APACHE_MODULES..."
   %{_sbindir}/a2enmod rewrite >/dev/null || :
fi

%post -n php-Icinga
# enable required apache modules
if [ -x %{_sbindir}/a2enmod ]; then
  a2enmod -q version || a2enmod version
  # get installed php_version (5 or 7)
  # ap_mpm=$(awk '/Server MPM/ {print $3}' <<<$(start_apache2 -V))
  # php_version=$(awk -F[." "] '/cli/ {print $2}' <<< $(php -v))
  php_version=$(php -v | sed -n 's/^PHP\ \([[:digit:]]\+\)\..*$/\1/p')
  if [[ -n ${php_version} ]] && start_apache2 -V | grep -q prefork; then
    echo "Info: adding php${php_version} to APACHE_MODULES..."
    a2enmod -q "php${php_version}" || a2enmod "php${php_version}"
  fi
fi

%files
%defattr(-,root,root)
%{basedir}/application/controllers
%{basedir}/application/fonts
%{basedir}/application/forms
%{basedir}/application/layouts
%{basedir}/application/views
%{basedir}/application/VERSION
%{basedir}/doc
%{basedir}/modules
%{basedir}/public
%if 0%{?suse_version}
# for lint on OBS
%dir %{dirname:%{wwwconfigdir}}
%dir %{wwwconfigdir}
%endif
%config(noreplace) %{wwwconfigdir}/icingaweb2.conf
%attr(0775,root,%{icingawebgroup}) %dir %{logdir}
%attr(0770,root,%{icingawebgroup}) %config(noreplace) %dir %{configdir}/modules/setup
%attr(0660,root,%{icingawebgroup}) %config(noreplace) %{configdir}/modules/setup/config.ini
%attr(0770,root,%{icingawebgroup}) %config(noreplace) %dir %{configdir}/modules/translation
%attr(0660,root,%{icingawebgroup}) %config(noreplace) %{configdir}/modules/translation/config.ini
%{docsdir}
%docdir %{docsdir}

%pre common
getent group %{icingawebgroup} >/dev/null || groupadd -r %{icingawebgroup}
exit 0

%files common
%defattr(-,root,root)
%dir %{basedir}
%dir %{basedir}/application
%dir %{basedir}/library
%dir %{basedir}/library/vendor
%dir %{basedir}/modules
%attr(0770,root,%{icingawebgroup}) %dir %{storagedir}
%attr(0770,root,%{icingawebgroup}) %config(noreplace) %dir %{configdir}
%attr(0770,root,%{icingawebgroup}) %config(noreplace) %dir %{configdir}/modules

%files -n php-Icinga
%defattr(-,root,root)
%if 0%{?suse_version}
# for lint on OBS
%dir %{phpdir}
%endif
%{phpdir}/Icinga

%files -n icingacli
%defattr(-,root,root)
%{basedir}/application/clicommands
%{_datadir}/bash-completion/completions/icingacli
%attr(0755,root,root) %{bindir}/icingacli

%if 0%{?use_selinux}
%post selinux
for selinuxvariant in %{selinux_variants}
do
  %{_sbindir}/semodule -s ${selinuxvariant} -i %{_datadir}/selinux/${selinuxvariant}/icingaweb2.pp &> /dev/null || :
done
%{_sbindir}/restorecon -R %{basedir} &> /dev/null || :
%{_sbindir}/restorecon -R %{configdir} &> /dev/null || :
%{_sbindir}/restorecon -R %{logdir} &> /dev/null || :
%{_sbindir}/restorecon -R %{storagedir} &> /dev/null || :

%postun selinux
if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}
  do
     %{_sbindir}/semodule -s ${selinuxvariant} -r icingaweb2 &> /dev/null || :
  done
  [ -d %{basedir} ] && %{_sbindir}/restorecon -R %{basedir} &> /dev/null || :
  [ -d %{configdir} ] && %{_sbindir}/restorecon -R %{configdir} &> /dev/null || :
  [ -d %{logdir} ] && %{_sbindir}/restorecon -R %{logdir} &> /dev/null || :
  [ -d %{storagedir} ] && %{_sbindir}/restorecon -R %{storagedir} &> /dev/null || :
fi

%files selinux
%defattr(-,root,root,0755)
%doc selinux/*
%{_datadir}/selinux/*/icingaweb2.pp
%endif

%files vendor-dompdf
%defattr(-,root,root)
%{basedir}/library/vendor/dompdf

%files vendor-HTMLPurifier
%defattr(-,root,root)
%{basedir}/library/vendor/HTMLPurifier
%{basedir}/library/vendor/HTMLPurifier.autoload.php
%{basedir}/library/vendor/HTMLPurifier.php

%files vendor-JShrink
%defattr(-,root,root)
%{basedir}/library/vendor/JShrink

%files vendor-lessphp
%defattr(-,root,root)
%{basedir}/library/vendor/lessphp

%files vendor-Parsedown
%defattr(-,root,root)
%{basedir}/library/vendor/Parsedown

%files vendor-zf1
%defattr(-,root,root)
%{basedir}/library/vendor/Zend

%changelog
