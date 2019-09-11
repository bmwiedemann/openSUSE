#
# spec file for package cobbler
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define www_path /srv/
%define apache_user wwwrun
%define apache_group www
%define apachedir apache2
%define _binaries_in_noarch_packages_terminate_build 0
%global debug_package %{nil}
Name:           cobbler
Version:        3.0.0
Release:        0
Summary:        Boot server configurator
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Boot/Servers
URL:            https://cobbler.github.io/
Source0:        cobbler-%{version}.tar.xz
# Manually generated AUTHORS file because the git repo is not included in the
# sources.
Source1:        AUTHORS
Source2:        logrotate_cobbler
Source3:        fence_ipmitool.template
Patch0:         fix_hardcoded_libpath_for_websession.patch
Patch1:         fix_shebang.patch
Patch2:         exclude_get-loaders_command.patch

BuildRequires:  python3-Cheetah3
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2 >= 2.4
BuildRequires:  distribution-release
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-base
BuildRequires:  python3-distro
BuildRequires:  python3-coverage
BuildRequires:  python3-future
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(systemd)
# Workaround so that /srv/tftpboot file exists during
# build, but is not owned by cobbler
BuildRequires:  tftp

Requires:       python3-Cheetah3
Requires:       acl
Requires:       apache2 >= 2.4
Requires:       apache2-mod_wsgi-python3
Requires:       fence-agents
Requires:       ipmitool
Requires:       logrotate
Requires:       mkisofs
Requires:       mod_wsgi
Requires:       python >= 3.0
Requires:       python3-PyYAML
Requires:       python3-base
Requires:       python3-distro
Requires:       python3-dnspython
Requires:       python3-future
Requires:       python3-ldap
Requires:       python3-netaddr
Requires:       python3-requests
Requires:       python3-simplejson
Requires:       rsync
Requires:       tftp(server)
Requires(post): apache2 >= 2.4
Requires(post): grub2
#Requires(post): grub2-x86_64-efi
#Requires(post): grub2-powerpc-ieee1275
Recommends:     grub2-x86_64-efi
Recommends:     grub2-i386-pc
Recommends:     grub2-arm64-efi
Recommends:     grub2-powerpc-ieee1275
BuildArch:      noarch
#Requires(post): grub2-arm64-efi
AutoReq:        no
%{?systemd_requires}
%ifarch %{ix86} x86_64 aarch64
Requires:       shim
Requires:       syslinux
%endif
%ifarch s390x
Requires:       syslinux-x86_64
%endif
%python_subpackages

%description

Cobbler is a network install server.  Cobbler supports PXE,
virtualized installs, and re-installing existing Linux machines.
There is also a web interface 'cobbler-web'.  Cobbler's
advanced features include importing distributions from DVDs and rsync
mirrors, kickstart templating, autoyast, integrated yum mirroring, and built-in
DHCP/DNS Management.  Cobbler has a XMLRPC API for integration with
other applications.

%package web
Summary:        Web interface for Cobbler
Group:          Productivity/Networking/Boot/Servers
Requires:       cobbler
Requires:       python3-django
Requires(post): openssl

%description web

Web interface for Cobbler that allows visiting
http://server/cobbler_web to configure the install server.

%prep
%setup -q -n cobbler-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%python_build
cp %{SOURCE1} AUTHORS

%install
%python_install

ln -sf service %{buildroot}%{_sbindir}/rccobblerd
rm -rf %{buildroot}%{_initddir}
mkdir -p %{buildroot}%{_unitdir}
mv %{buildroot}%{_sysconfdir}/cobbler/cobblerd.service %{buildroot}%{_unitdir}

mkdir -p %{buildroot}/srv/tftpboot/images
rm -f %{buildroot}%{_sysconfdir}/cobbler/cobblerd

# create logrote config
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/cobbler

# workaround to provide a ipmilanplus fence
ln -s fence_ipmilan %{buildroot}/%{_sbindir}/fence_ipmitool
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/cobbler/power/fence_ipmitool.template

%if 0%{?suse_version}
cp -r tests/ $RPM_BUILD_ROOT/usr/share/cobbler/
%endif

%fdupes %{buildroot}%{_prefix}

%pre
%service_add_pre cobblerd.service

%post
if [ ! -e /etc/genders ]; then
    touch /etc/genders
fi
if [ $1 -eq 1 ] ; then
    # Initial installation
        sysconf_addword %{_sysconfdir}/sysconfig/apache2 APACHE_MODULES proxy
        sysconf_addword %{_sysconfdir}/sysconfig/apache2 APACHE_MODULES proxy_http
        sysconf_addword %{_sysconfdir}/sysconfig/apache2 APACHE_MODULES proxy_connect
        sysconf_addword %{_sysconfdir}/sysconfig/apache2 APACHE_MODULES wsgi

elif [ "$1" -ge "2" ]; then
    # backup config
    if [ -e %{_localstatedir}/lib/cobbler/distros ]; then
        cp %{_localstatedir}/lib/cobbler/distros*  %{_localstatedir}/lib/cobbler/backup 2>/dev/null
        cp %{_localstatedir}/lib/cobbler/profiles* %{_localstatedir}/lib/cobbler/backup 2>/dev/null
        cp %{_localstatedir}/lib/cobbler/systems*  %{_localstatedir}/lib/cobbler/backup 2>/dev/null
        cp %{_localstatedir}/lib/cobbler/repos*    %{_localstatedir}/lib/cobbler/backup 2>/dev/null
        cp %{_localstatedir}/lib/cobbler/networks* %{_localstatedir}/lib/cobbler/backup 2>/dev/null
    fi
    if [ -e %{_localstatedir}/lib/cobbler/config ]; then
        cp -a %{_localstatedir}/lib/cobbler/config    %{_localstatedir}/lib/cobbler/backup 2>/dev/null
    fi
    # upgrade older installs
    # move power and pxe-templates from %%{_sysconfdir}/cobbler, backup new templates to *.rpmnew
    for n in power pxe; do
      rm -f %{_sysconfdir}/cobbler/$n*.rpmnew
      find %{_sysconfdir}/cobbler -maxdepth 1 -name "$n*" -type f | while read f; do
        newf=%{_sysconfdir}/cobbler/$n/`basename $f`
        [ -e $newf ] &&  mv $newf $newf.rpmnew
        mv $f $newf
      done
    done
    # upgrade older installs
    # copy kickstarts from %%{_sysconfdir}/cobbler to %%{_prefix}/lib/cobbler/kickstarts
    rm -f %{_sysconfdir}/cobbler/*.ks.rpmnew
    find %{_sysconfdir}/cobbler -maxdepth 1 -name "*.ks" -type f | while read f; do
      newf=%{_localstatedir}/lib/cobbler/kickstarts/`basename $f`
      [ -e $newf ] &&  mv $newf $newf.rpmnew
      cp $f $newf
    done
    # remove mod_python from apache
    sysconf_addword -r %{_sysconfdir}/sysconfig/apache2 APACHE_MODULES python >/dev/null 2>&1
    /bin/systemctl try-restart cobblerd.service >/dev/null 2>&1 || :
fi

# Create bootloders into /var/lib/cobbler/loaders
%{_datadir}/%{name}/bin/mkgrub.sh >/dev/null 2>&1

%service_add_post cobblerd.service

%preun
%service_del_preun cobblerd.service

%postun
%service_del_postun cobblerd.service
if [ -e %{_localstatedir}/lib/cobbler/loaders/.cobbler_postun_cleanup ];then
   for file in $(cat %{_localstatedir}/lib/cobbler/loaders/.cobbler_postun_cleanup);do
       rm -f %{_localstatedir}/lib/cobbler/loaders/$file
   done
   rm -rf %{_localstatedir}/lib/cobbler/loaders/.cobbler_postun_cleanup
fi

%posttrans
%{apache_restart_if_needed}

%post  web
# Change the SECRET_KEY option in the Django settings.py file
# required for security reasons, should be unique on all systems
RAND_SECRET=$(openssl rand -base64 40 | sed 's/\//\\\//g')
sed -i -e "s/SECRET_KEY = ''/SECRET_KEY = \'$RAND_SECRET\'/" %{python_sitelib}/cobbler/web/settings.py

%files
%doc AUTHORS README.md
%license COPYING
/%{www_path}/www/cobbler
%{_bindir}/cobbler
%{_bindir}/cobbler-ext-nodes
%{_bindir}/cobblerd
%{_datadir}/%{name}/bin/mkgrub.sh
%{_datadir}/cobbler/web
%attr(750, root, root) %{_localstatedir}/log/cobbler
%{_mandir}/man1/cobbler.1%{?ext_man}
%{_sbindir}/tftpd.py*
%{_sbindir}/rccobblerd
%{_sbindir}/fence_ipmitool
%{_unitdir}/cobblerd.service

%{python_sitelib}/cobbler
%{python_sitelib}/cobbler*.egg-info

%config(noreplace) %{_sysconfdir}/cobbler
%config(noreplace) %{_localstatedir}/lib/cobbler
%config(noreplace) %{_sysconfdir}/%{apachedir}/conf.d/cobbler.conf
# ToDo: This is used by systemd service file:
# ExecStartPost=/usr/bin/touch /usr/share/cobbler/web/cobbler.wsgi
# Get this into cobbler-web somehow
%config %{_sysconfdir}/logrotate.d/cobbler

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin

# These are part of the test package
%exclude %dir %{_datadir}/%{name}/tests
%exclude %{_datadir}/%{name}/tests/*

%dir /srv/tftpboot/images

%files web
%license COPYING
%doc AUTHORS
%config(noreplace) %{_sysconfdir}/%{apachedir}/conf.d/cobbler_web.conf
%defattr(-,%{apache_user},%{apache_group},-)
/%{www_path}/www/cobbler_webui_content/


%if 0%{?suse_version}
%package -n cobbler-tests

Summary:        Unit tests for Cobbler
Group:          Productivity/Networking/Boot/Servers
Requires:       cobbler
Requires:       python3-pytest
Requires:       python3-pyflakes
Requires:       python3-pycodestyle

%description -n cobbler-tests

Unit test files from the Cobbler project

%files -n cobbler-tests
%doc %{_datadir}/%{name}/tests/README.md
%dir %{_datadir}/%{name}/tests
%{_datadir}/%{name}/tests/*
%endif #suse_version

%changelog
