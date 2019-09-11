#
# spec file for package otrs
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           otrs

%define otrs_ver 6.0.20
%define itsm_ver 6.0.20
%define itsm_min 6
%define otrs_root /srv/%{name}
%define otrsdoc_dir_files AUTHORS* CHANGES* COPYING* CREDITS README* UPGRADING.SUSE doc
%define otrsdocs CHANGES* doc

Summary:        The Open Ticket Request System
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Email/Utilities
Version:        %{otrs_ver}
Release:        0
URL:            https://community.otrs.com/
AutoReqProv:    off
Source:         ftp://ftp.otrs.org/pub/otrs/%{name}-%{otrs_ver}.tar.bz2
Source1:        itsm-%{itsm_ver}.tar.bz2
Source2:        %{name}.rpmlintrc
Source3:        %{name}.permissions
# Used to update the itsm package
Source11:       sysconfig.%{name}
Source12:       %{name}.README.en
Source13:       %{name}.README.de
Source14:       itsm.README.en
Source15:       itsm.README.de
Source16:       ZZZAuto.pm
Source17:       UPGRADING.SUSE
Source20:       %{name}.service
Source21:       %{name}.service.helper.sh
#
Source99:       itsm-update.sh
# PATCH-FIX-OPENSUSE -- VARS for conf and fix for apache >= 2.4
Patch1:         %{name}-httpd_conf.patch
# PATCH-FIX-OPENSUSE -- don't test write permissions on bin/
Patch2:         otrs-perm_test.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(pre):  coreutils
Requires(pre):  permissions
Requires(pre):  shadow
Requires(post): %fillup_prereq 
Requires(post): apache2
Requires(post): coreutils
Requires(post): sed
Requires(post): shadow
BuildRequires:  fdupes
BuildRequires:  pwdutils
#
%if 0%{?suse_version} >= 1210
BuildRequires:  systemd
%{?systemd_requires}
%define has_systemd 1
%endif
#
Requires:       apache2-mod_perl
Requires:       fetchmail
Requires:       mysql
Requires:       mysql-client
Requires:       perl
Requires:       procmail
Requires:       perl(Archive::Tar)
Requires:       perl(Archive::Zip)
Requires:       perl(DBD::mysql)
Requires:       perl(DBI)
Requires:       perl(Date::Format)
Requires:       perl(DateTime)
Requires:       perl(Digest::SHA)
Requires:       perl(LWP::UserAgent)
Requires:       perl(List::Util::XS)
Requires:       perl(Net::DNS) >= 0.60
Requires:       perl(Template)
Requires:       perl(Template::Stash::XS)
Requires:       perl(Time::HiRes)
Requires:       perl(Time::Piece)
Requires:       perl(YAML::XS)
#
Recommends:     perl(Apache::DBI)
Recommends:     perl(Apache2::Reload)
Recommends:     perl(Authen::SASL)
Recommends:     perl(Crypt::Eksblowfish::Bcrypt)
Recommends:     perl(Crypt::SSLeay)
Recommends:     perl(GD)
Recommends:     perl(GD::Graph)
Recommends:     perl(GD::Text)
Recommends:     perl(IO::Socket::SSL)
Recommends:     perl(JSON::XS)
Recommends:     perl(Mail::IMAPClient) >= 3.22
Recommends:     perl(ModPerl::Util)
Recommends:     perl(Net::SSL)
Recommends:     perl(PDF::API2) >= 0.73
Recommends:     perl(SOAP::Lite)
Recommends:     perl(Text::CSV_XS)
Recommends:     perl(XML::LibXML)
Recommends:     perl(XML::LibXSLT)
Recommends:     perl(XML::Parser)
#
Suggests:       perl(Authen::NTML)
Suggests:       perl(DBD::ODBC)
Suggests:       perl(DBD::Oracle)
Suggests:       perl(DBD::Pg)
Suggests:       perl(Encode::HanExtra) >= 0.23
Suggests:       perl(Net::LDAP)
#
### Framework -> Crypt::SMIME
Recommends:     ca-certificates

%if "%_vendor" == "suse"
	%define	VENDOR SUSE
%else
	%define	VENDOR %_vendor
%endif

%description
OTRS is a Ticket Request System with many features to manage
customer telephone calls and e-mails.

Feature list: see README
Authors list: see CREDITS

%package doc
Summary:        OTRS Documentation
Group:          Documentation/Other

%description doc
This package contains the README, Changes and docs for OTRS

Authors list: see CREDITS

%package -n otrs-itsm
Summary:        ITIL focused IT service management
Group:          Productivity/Networking/Email/Utilities
Version:        %{itsm_ver}
Release:        0
Requires:       %{name} >= %{itsm_ver}
Provides:       OTRS::ITSM
Provides:       itsm = %{itsm_ver}

%description itsm
OTRS::ITSM implements ITIL focused IT service management.

You need a OTRS %{otrs_ver} (http://otrs.org/) installation.

Make sure your database accepts packages over 5 MB in size. A MySQL database
for example accepts packages up to 1 MB by default. In this case, the value for
max_allowed_packet must be increased. The recommended maximum size accepted is
20 MB.

for INSTALL see INSTALL-%{itsm_min}.ITSM
please see README.itsm for further details, which comes with otrs package

Required OTRS::ITSM modules can be found under %{otrs_root}/itsm

Authors list: see CREDITS

%prep
%setup -q -n %{name}-%{otrs_ver} -a 1
%patch1
%patch2

### Is this critical ? (https://bugs.otrs.org/show_bug.cgi?id=12889)
# rpmlint: pem-certificate /srv/otrs/Kernel/cpan-lib/Mozilla/CA/cacert.pem
#rm -f Kernel/cpan-lib/Mozilla/CA/cacert.pem

### UPGRADING.SUSE
rm -f CONTRIBUTING.md INSTALL.md UPDATING.md
cp %{S:17} .
# fix @OTRS_ROOT@
sed -i -e "s,@OTRS_ROOT@,%{otrs_root},g" UPGRADING.SUSE

### ZZZAuto.pm for OTRS::ITSM
pushd Kernel/Config/Files
cp %{S:16} .
# fix @OTRS_ROOT@
sed -i -e "s,@OTRS_ROOT@,%{otrs_root},g" ZZZAuto.pm
popd

# remove not needed files from scripts
rm -rf \
  scripts/*.spec \
  scripts/auto_build \
  scripts/redhat-* \
  scripts/suse-*rc*otrs*

# scripts/test [Kernel::System::Package::_FileInstall]

# fix old otrs_root (/opt)
sed -i -e "s,/opt/%{name},%{otrs_root},g" \
  bin/Cron.sh \
  i18n/otrs/otrs.*.po \
  Kernel/Config/Defaults.pm \
  Kernel/Config/Files/XML/Daemon.xml \
  Kernel/Config/Files/XML/Framework.xml \
  Kernel/Config.pm.dist \
  Kernel/Language/*.pm \
  Kernel/Modules/AdminDynamicFieldText.pm \
  Kernel/Output/HTML/Templates/Standard/AdminGenericInterfaceTransportHTTPSOAP.tt \
  Kernel/System/SysConfig.pm \
  Kernel/System/ACL/DB/ACL.pm \
  Kernel/System/Environment.pm \
  Kernel/System/ProcessManagement/DB/Process.pm \
  Kernel/System/UnitTest/Helper.pm \
  scripts/apache2-perl-startup.pl

# rpmlint: wrong-file-end-of-line-encoding
perl -p -i -e "s|\r\n|\n|" itsm-%{itsm_ver}/INSTALL-%{itsm_min}.ITSM

%build
# copy config file
cp -a Kernel/Config.pm.dist Kernel/Config.pm

# copy all crontab dist files
for file in var/cron/*.dist; do
mv $file var/cron/$(basename $file .dist)
done

%install
export DESTROOT="%{otrs_root}/"
install -d %{buildroot}/${DESTROOT}
install -d %{buildroot}/%{_sbindir}

# install OTRS base system
cp -a . %{buildroot}/${DESTROOT}

for configFile in .fetchmailrc .mailfilter .procmailrc; do
  touch %{buildroot}/${DESTROOT}/${configFile}
done
touch %{buildroot}${DESTROOT}var/log/TicketCounter.log

# install README
for lang in en de; do
  cp -p "%{_sourcedir}/%{name}.README.${lang}" "README.%{VENDOR}.${lang}"
  cp -p "%{_sourcedir}/itsm.README.${lang}" "README.itsm.%{VENDOR}.${lang}"
done

# fix @OTRS_ROOT@ in README.*
for r in $(ls -1 README.*); do
  sed -i -e "s,@OTRS_ROOT@,%{otrs_root},g" $r
done

# remove files that are part of the docdir
pushd %{buildroot}/${DESTROOT}
rm -rf %{otrsdoc_dir_files}
install -d doc
popd

# permissions
install -D -m 0644 %{S:3} %{buildroot}/etc/permissions.d/%{name}
# fix @OTRS_ROOT@
sed -i -e "s,@OTRS_ROOT@,%{otrs_root},g" %{buildroot}/etc/permissions.d/%{name}

# sysconfig
install -D -m 0644 %{S:11} %{buildroot}%{_fillupdir}/sysconfig.%{name}
# fix @OTRS_ROOT@
sed -i -e "s,@OTRS_ROOT@,%{otrs_root},g" %{buildroot}%{_fillupdir}/sysconfig.%{name}

# systemd
install -D -m 0644 %{S:20} %{buildroot}/%{_unitdir}/%{name}.service
ln -fs %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}
install -D -m 0755 %{S:21} %{buildroot}/%{_bindir}/%{name}.service.helper.sh
# fix @OTRS_ROOT@
sed -i -e "s,@OTRS_ROOT@,%{otrs_root},g" "%{buildroot}/%{_unitdir}/%{name}.service"
sed -i -e "s,@OTRS_ROOT@,%{otrs_root},g" "%{buildroot}/%{_bindir}/%{name}.service.helper.sh"

otrs_apache_conf="scripts/apache2-httpd.include.conf"
install -D -m 0644 ${otrs_apache_conf} %{buildroot}/etc/apache2/conf.d/%{name}.conf
rm -f %{buildroot}/%{otrs_root}/scripts/apache*.conf
# fix @OTRS_ROOT@
sed -i -e "s,@OTRS_ROOT@,%{otrs_root},g" %{buildroot}/etc/apache2/conf.d/%{name}.conf

# OTRS::ITSM
# rename itsm-%{itsm_ver} to itsm
pushd %{buildroot}/${DESTROOT}
mv itsm-%{itsm_ver} itsm
popd

%if 0%{?suse_version} > 1020
%fdupes %{buildroot}/%{otrs_root}/scripts/test
%fdupes %{buildroot}/%{otrs_root}/var
%fdupes %{buildroot}/%{otrs_root}/Kernel/cpan-lib
%endif

%if 0%{?suse_version}
%verifyscript
%verify_permissions -e %{otrs_root}/var/tmp/
%endif

%pre
# on `rpm -ivh` PARAM is 1
# on `rpm -Uvh` PARAM is 2
if [ -z  "`%{_bindir}/getent group %{name} 2>/dev/null`" ]; then
  %{_sbindir}/groupadd -g 88 -r %{name}
else
  if [ `%{_bindir}/id -g %{name}` != 88 ]; then
    %{_sbindir}/groupmod -g 88 %{name}
  fi
fi 
if [ -z "`%{_bindir}/getent passwd %{name} 2>/dev/null`" ]; then
  %{_sbindir}/useradd -c "OTRS User" -d %{otrs_root} -G %{name},www -g %{name} -u 88 -r -s /bin/false %{name}
else
  if [ `%{_bindir}/id -u %{name}` != 88 ]; then
    %{_sbindir}/usermod -c "OTRS User" -d %{otrs_root} -G %{name},www -g %{name} -u 88 %{name}
  fi
fi
# add wwwrun to otrs group
%{_sbindir}/usermod -G %{name} wwwrun
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%{fillup_only -n otrs}
%service_add_post %{name}.service
# set permissions
%set_permissions %{otrs_root}/var/tmp/
#
%if 0%{?suse_version}
  /usr/sbin/a2enmod perl >/dev/null
  /usr/sbin/a2enmod version >/dev/null
%endif
# Update ?
if [ $1 -gt 1 ]; then
  # OTRS_ROOT changed from /opt to /srv
  if [ -f /opt/%{name}/Kernel/Config.pm.rpmsave ]; then
    mv /opt/%{name}/Kernel/Config.pm.rpmsave %{otrs_root}/Kernel/
  fi
  %{_sbindir}/usermod -d %{otrs_root} %{name}
  #update sysconfig
  if [ -f /etc/sysconfig/%{name} ]; then
    sed -i -e "s,/opt/%{name},%{otrs_root},g" /etc/sysconfig/%{name}
  fi
fi
# if rpm is not in update mode
if ! [ $1 -gt 1 ]; then
	if [ -z "${YAST_IS_RUNNING}" ]; then
		if [ -n "$LC_ALL" ]; then
			lang="$LC_ALL"
		elif [ -n "$LC_MESSAGE" ]; then
			lang="$LC_MESSAGE"
		elif [ -n "$LANG" ]; then
			lang="$LANG"
		else
			lang=
		fi
		echo
		case "$lang" in
			de_*)
				echo "Hinweise zur Erstkonfiguration von OTRS finden Sie in"
				echo "/usr/share/doc/packages/otrs/README.%{VENDOR}.de"
				;;
			*)
				echo "About the initial setup of OTRS, please read"
				echo "/usr/share/doc/packages/otrs/README.%{VENDOR}.en"
				;;
		esac
		echo
	fi
fi
exit 0

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root,-)
%doc AUTHORS.md CHANGES.md COPYING* README* UPGRADING.SUSE
%{otrs_root}/ARCHIVE
%{otrs_root}/RELEASE
%{otrs_root}/.bash_completion
%dir %{_sysconfdir}/apache2
%dir %{_sysconfdir}/apache2/conf.d
%config(noreplace) %{_sysconfdir}/apache2/conf.d/%{name}.conf
# permissions
%config %{_sysconfdir}/permissions.d/%{name}
# systemd
%{_fillupdir}/sysconfig.%{name}
%{_unitdir}/%{name}.service
%{_bindir}/%{name}.service.helper.sh
%{_sbindir}/rc%{name}

# Custom
%dir %{otrs_root}/Custom
%{otrs_root}/Custom/README

# i18n
%dir %{otrs_root}/i18n
%{otrs_root}/i18n/*

# scripts/*
%{otrs_root}/scripts/contrib
%{otrs_root}/scripts/database
%{otrs_root}/scripts/DBUpdateTo6
%{otrs_root}/scripts/tools
%{otrs_root}/scripts/*.pl
%{otrs_root}/scripts/*.pm

# var/cron
%dir %{otrs_root}/var/cron
%config(noreplace) %attr(644,%{name},www) %{otrs_root}/var/cron/*

# var/fonts
%{otrs_root}/var/fonts

# var/processes
%{otrs_root}/var/processes

# var/webservices
%{otrs_root}/var/webservices

###############
## {root,www}
###############
#defattr(0770,root,www,0775)
%defattr(0750,root,www,0750)

# bin
%{otrs_root}/bin/*.pl
%{otrs_root}/bin/cgi-bin/app.psgi
%{otrs_root}/bin/cgi-bin/*.pl
%{otrs_root}/bin/Cron.sh
%{otrs_root}/bin/fcgi-bin/*.pl
%exclude %{otrs_root}/bin/%{name}.SetPermissions.pl

###############
## {otrs,otrs}
###############
# otrs HOME
%defattr(-,%{name},%{name})
%dir %{otrs_root}
%ghost %config(noreplace) %{otrs_root}/.fetchmailrc
%ghost %config(noreplace) %{otrs_root}/.mailfilter
%ghost %config(noreplace) %{otrs_root}/.procmailrc
%{otrs_root}/.fetchmailrc.dist
%{otrs_root}/.mailfilter.dist
%{otrs_root}/.procmailrc.dist

###############
## {otrs,www}
###############
%defattr(0644,%{name},www,0775)

# var
%dir %{otrs_root}/var
%{otrs_root}/var/logo-%{name}.png

# var/log
%dir %attr(0770,%{name},www) %{otrs_root}/var/log
%ghost %config(noreplace) %attr(660,%{name},www) %{otrs_root}/var/log/TicketCounter.log

# var/spool
%dir %attr(0770,%{name},www) %{otrs_root}/var/spool

###############
## {wwwrun,www}
###############

%defattr(0750,wwwrun,www,0750)
# bin
%dir %{otrs_root}/bin
%dir %{otrs_root}/bin/cgi-bin
%dir %{otrs_root}/bin/fcgi-bin

%defattr(0644,wwwrun,www,0755)

# doc (is empty), [Kernel::System::Package::_FileInstall]
%dir %{otrs_root}/doc

# scripts/*
%dir %{otrs_root}/scripts
# scripts/test, [Kernel::System::Package::_FileInstall]
%dir %{otrs_root}/scripts/test
%{otrs_root}/scripts/test/*

# var/httpd, [Kernel::System::Package::_FileInstall]
%{otrs_root}/var/httpd

# var/stats
%dir %{otrs_root}/var/stats
%{otrs_root}/var/stats/*

# var/tmp
%dir %{otrs_root}/var/tmp
%verify(not user group mode) %attr(2770,wwwrun,www) %dir %{otrs_root}/var/tmp

%defattr(0664,wwwrun,www,0775)

# Kernel DIR
%dir %{otrs_root}/Kernel
%dir %{otrs_root}/Kernel/Autoload
%{otrs_root}/Kernel/Autoload/Test.pm
%config(noreplace) %attr(0640,wwwrun,www) %{otrs_root}/Kernel/Config.pm
%{otrs_root}/Kernel/Config.pm.dist
%{otrs_root}/Kernel/Config.pod.dist
%dir %{otrs_root}/Kernel/Config
%{otrs_root}/Kernel/Config/Defaults.pm
%dir %{otrs_root}/Kernel/Config/Files
%dir %{otrs_root}/Kernel/Config/Files/XML/
%{otrs_root}/Kernel/Config/Files/XML/*.xml
%{otrs_root}/Kernel/GenericInterface
%{otrs_root}/Kernel/cpan-lib
%dir %{otrs_root}/Kernel/Language
%config(noreplace) %{otrs_root}/Kernel/Language/*.pm
%{otrs_root}/Kernel/Language.pm
%{otrs_root}/Kernel/Modules/
%dir %{otrs_root}/Kernel/Output
%dir %{otrs_root}/Kernel/Output/HTML
%{otrs_root}/Kernel/Output/HTML/*
%{otrs_root}/Kernel/Output/JavaScript
%dir %{otrs_root}/Kernel/Output/PDF
%{otrs_root}/Kernel/Output/PDF/*
%dir %{otrs_root}/Kernel/Output/Template
%{otrs_root}/Kernel/Output/Template/*
%{otrs_root}/Kernel/System/

%files doc
%defattr(644,root,root,755)
%doc %{otrsdocs}

%files itsm
%defattr(-,root,root,-)
%doc COPYING* README.itsm*
%doc itsm-%{itsm_ver}/INSTALL-%{itsm_min}.ITSM
%{otrs_root}/itsm
%config(noreplace) %attr(0664,wwwrun,www) %{otrs_root}/Kernel/Config/Files/ZZZAuto.pm

%changelog
