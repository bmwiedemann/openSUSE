#
# spec file for package cloud-init
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
# change this whenever config changes incompatible
%global configver 0.7

Name:           cloud-init
Version:        19.4
Release:        0
License:        GPL-3.0
Summary:        Cloud node initialization tool
Url:            http://launchpad.net/cloud-init/
Group:          System/Management
Source0:        %{name}-%{version}.tar.gz
Source1:        rsyslog-cloud-init.cfg
Patch0:         0001-Make-tests-work-with-Python-3.8-139.patch
# FIXME 
# python2 disables SIGPIPE, causing broken pipe errors in shell scripts (bsc#903449)
Patch20:        cloud-init-python2-sigpipe.patch
Patch21:        cloud-init-template-py2.patch
Patch29:        datasourceLocalDisk.patch
Patch34:        cloud-init-tests-set-exec.patch
# FIXME (lp#1801364)
Patch42:        cloud-init-ostack-metadat-dencode.patch
# FIXME (lp#1812117)
Patch43:        cloud-init-write-routes.patch
# FIXME (lp#1849296)
Patch52:        cloud-init-break-resolv-symlink.patch
# FIXME (lp#1858808)
Patch55:        cloud-init-mix-static-dhcp.patch
# FIXME no proposed solution
Patch56:        cloud-init-sysconf-path.patch
# FIXME (lp#1860164)
Patch57:        cloud-init-no-tempnet-oci.patch
Patch58:        cloud-init-use-different-random-src.diff
Patch59:        cloud-init-long-pass.patch

BuildRequires:  fdupes
BuildRequires:  filesystem
# pkg-config is needed to find correct systemd unit dir
BuildRequires:  pkg-config
# needed for /lib/udev
BuildRequires:  pkgconfig(udev)
%if 0%{?suse_version} > 1320
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# Test requirements
BuildRequires:  python3-Jinja2
BuildRequires:  python3-PyYAML
BuildRequires:  python3-configobj >= 5.0.2
BuildRequires:  python3-httpretty
BuildRequires:  python3-jsonpatch
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-oauthlib
BuildRequires:  python3-requests
#BuildRequires:  python3-testtools
%else
BuildRequires:  python-devel
BuildRequires:  python-Jinja2
BuildRequires:  python-PyYAML
BuildRequires:  python-requests
BuildRequires:  python-setuptools
BuildRequires:  python-six
%endif
%if 0%{?is_opensuse}
BuildRequires:  openSUSE-release
%else
BuildRequires:  sles-release
%endif
BuildRequires:  util-linux
Requires:       bash
Requires:       dhcp-client
Requires:       file
Requires:       growpart
Requires:       e2fsprogs
Requires:       net-tools
Requires:       openssh
%if 0%{?suse_version} > 1320
Requires:       python3-configobj >= 5.0.2
Requires:       python3-Jinja2
Requires:       python3-jsonpatch
Requires:       python3-jsonschema
Requires:       python3-oauthlib
Requires:       python3-pyserial
Requires:       python3-PyYAML
Requires:       python3-requests
Requires:       python3-setuptools
Requires:       python3-six
Requires:       python3-xml
%else
Requires:       python-argparse
Requires:       python-configobj >= 5.0.2
Requires:       python-Jinja2
Requires:       python-jsonpatch
Requires:       python-jsonschema
Requires:       python-oauthlib
Requires:       python-pyserial
Requires:       python-PyYAML
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-six
Requires:       python-xml
%endif
Requires:       sudo
Requires:       util-linux
Requires:       cloud-init-config = %configver
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define         docdir %{_defaultdocdir}/%{name}
%ifarch %ix86 x86_64
Requires:       dmidecode
%endif
%if 0%{?suse_version} && 0%{?suse_version} <= 1210
%define initsys sysvinit_suse
%else
%define initsys systemd
BuildRequires: pkgconfig(systemd)
%{?systemd_requires}
%if 0%{?suse_version} && 0%{?suse_version} == 1220
%define systemd_prefix /lib
%else
%define systemd_prefix /usr/lib
%endif
%endif
%if 0%{?suse_version} && 0%{?suse_version} >= 1315
Requires:      wicked-service
%else
Requires:      sysconfig-network
%endif

%description
Cloud-init is an init script that initializes a cloud node (VM)
according to the fetched configuration data from the admin node.

%package config-suse
Summary:        Configuration file for Cloud node initialization tool
Provides:	cloud-init-config = %configver
Group:          System/Management
Conflicts:	otherproviders(cloud-init-config)

%description config-suse
This package contains the product specific configuration file
for cloud-init.

%package doc
Summary:        Cloud node initialization tool - Documentation
Group:          System/Management
Recommends:     cloud-init = %{version}

%description doc
Cloud-init is an init script that initializes a cloud node (VM)
according to the fetched configuration data from the admin node.

Documentation and examples for cloud-init tools

#%package test
#Summary:        Cloud node initialization tool  - Testsuite
#Group:          System/Management
#Requires:       cloud-init = %{version}
#
#%description test
#Cloud-init is an init script that initializes a cloud node (VM)
#according to the fetched configuration data from the admin node.
#
#Unit tests for the cloud-init tools

%prep
%setup -q
%patch0 -p1
%if 0%{?suse_version} < 1315
%patch20
%patch21 
%endif
%patch29 -p0
%patch34
%patch42
%patch43
%patch52
%patch55 -p0
%patch56
%patch57
%patch58 -p1
%patch59

%build
%if 0%{?suse_version} && 0%{?suse_version} <= 1315
python setup.py build
%else
python3 setup.py build
%endif


#%if 0%{?suse_version} > 1320
#%check
## these tests are currently failing due to suse patches
#rm -v tests/unittests/test_distros/test_netconfig.py
#rm -v tests/unittests/test_net.py
## Ignore test failure currently not doing anything with opennebula
#rm -v tests/unittests/test_datasource/test_opennebula.py
## To be investigated
#rm -v tests/unittests/test_handler/test_handler_ntp.py
#make test
#%endif


%install
%if 0%{?suse_version} && 0%{?suse_version} <= 1315
python setup.py install --root=%{buildroot} --prefix=%{_prefix} --install-lib=%{python_sitelib} --init-system=%{initsys}
%else
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix} --install-lib=%{python3_sitelib} --init-system=%{initsys}
%endif
find %{buildroot} \( -name .gitignore -o -name .placeholder \) -delete
# from debian install script
for x in "%{buildroot}%{_bindir}/"*.py; do
   [ -f "${x}" ] && mv "${x}" "${x%.py}"
done
mkdir -p %{buildroot}%{_localstatedir}/lib/cloud
# move documentation
mkdir -p %{buildroot}%{_defaultdocdir}
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_defaultdocdir}
# man pages
mkdir -p %{buildroot}%{_mandir}/man1
mv doc/man/* %{buildroot}%{_mandir}/man1
# copy the LICENSE
mkdir -p %{buildroot}%{_defaultlicensedir}/%{name}
cp LICENSE %{buildroot}%{_defaultlicensedir}/%{name}
cp LICENSE-GPLv3 %{buildroot}%{_defaultlicensedir}/%{name}
# Set the distribution indicator
%if 0%{?suse_version}
%if 0%{?is_opensuse}
sed -i s/suse/opensuse/ %{buildroot}/%{_sysconfdir}/cloud/cloud.cfg
%else
sed -i s/suse/sles/ %{buildroot}/%{_sysconfdir}/cloud/cloud.cfg
%endif
%endif
mkdir -p %{buildroot}/%{_sysconfdir}/rsyslog.d
mkdir -p %{buildroot}/usr/lib/udev/rules.d/
cp -a %{SOURCE1} %{buildroot}/%{_sysconfdir}/rsyslog.d/21-cloudinit.conf
mv %{buildroot}/lib/udev/rules.d/66-azure-ephemeral.rules %{buildroot}/usr/lib/udev/rules.d/

# remove debian/ubuntu specific profile.d file (bnc#779553)
rm -f %{buildroot}%{_sysconfdir}/profile.d/Z99-cloud-locale-test.sh

# Remove non-SUSE templates
rm %{buildroot}/%{_sysconfdir}/cloud/templates/*.debian.*
rm %{buildroot}/%{_sysconfdir}/cloud/templates/*.redhat.*
rm %{buildroot}/%{_sysconfdir}/cloud/templates/*.ubuntu.*

# move sysvinit scripts into the "right" place
%if 0%{?suse_version} && 0%{?suse_version} <= 1210
mkdir -p %{buildroot}/%{_initddir}
mkdir -p %{buildroot}/%{_sbindir}
pushd "%{buildroot}%{_initddir}"
for iniF in *; do
    ln -s "%{_initddir}/${iniF}" "%{buildroot}/%{_sbindir}/rc${iniF}"
done
popd
%endif

# remove duplicate files
%if 0%{?suse_version}
%if 0%{?suse_version} <= 1315
%fdupes %{buildroot}%{python_sitelib}
%else
%fdupes %{buildroot}%{python3_sitelib}
%endif
%endif

%if 0%{?suse_version} && 0%{?suse_version} <= 1210
%postun
%insserv_cleanup
%endif

%files
%defattr(-,root,root)
%license LICENSE LICENSE-GPLv3
%{_bindir}/cloud-id
%{_bindir}/cloud-init
%{_bindir}/cloud-init-per
%dir %{_sysconfdir}/cloud
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg.d
%config(noreplace) %{_sysconfdir}/cloud/templates
%{_sysconfdir}/dhcp/dhclient-exit-hooks.d/hook-dhclient
%{_sysconfdir}/NetworkManager/dispatcher.d/hook-network-manager
%{_mandir}/man*/*
%if 0%{?suse_version} && 0%{?suse_version} < 1500
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%endif
%{_datadir}/bash-completion/completions/cloud-init
%if 0%{?suse_version} && 0%{?suse_version} <= 1315
%{python_sitelib}/cloudinit
%{python_sitelib}/cloud_init-%{version}-py%{py_ver}.egg-info
%else
%{python3_sitelib}/cloudinit
%{python3_sitelib}/cloud_init-%{version}-py%{py3_ver}.egg-info
%endif
%{_prefix}/lib/cloud-init
%if 0%{?suse_version} && 0%{?suse_version} <= 1210
%{_sbindir}/rccloud-config
%{_sbindir}/rccloud-init
%{_sbindir}/rccloud-init-local
%{_sbindir}/rccloud-final
%attr(0755, root, root) %{_initddir}/cloud-config
%attr(0755, root, root) %{_initddir}/cloud-init
%attr(0755, root, root) %{_initddir}/cloud-init-local
%attr(0755, root, root) %{_initddir}/cloud-final
%else
%{systemd_prefix}/systemd/system-generators/cloud-init-generator
%{systemd_prefix}/systemd/system/cloud-config.service
%{systemd_prefix}/systemd/system/cloud-config.target
%{systemd_prefix}/systemd/system/cloud-init-local.service
%{systemd_prefix}/systemd/system/cloud-init.service
%{systemd_prefix}/systemd/system/cloud-init.target
%{systemd_prefix}/systemd/system/cloud-final.service
%endif
%if 0%{?suse_version} && 0%{?suse_version} > 1110
%dir %{_sysconfdir}/rsyslog.d
%{_sysconfdir}/rsyslog.d/21-cloudinit.conf
/usr/lib/udev/rules.d/66-azure-ephemeral.rules
# This if condition really distinquished between OBS and IBS.
# For SLE 12 builds in OBS owning the directories is not required, while
# SLE 12 builds in IBS require owning the directories
%else
/lib/udev/rules.d/66-azure-ephemeral.rules
%endif
%dir %attr(0755, root, root) %{_localstatedir}/lib/cloud
%dir %{docdir}
%dir /etc/NetworkManager
%dir /etc/NetworkManager/dispatcher.d
%dir /etc/dhcp
%dir /etc/dhcp/dhclient-exit-hooks.d

%files config-suse
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg

%files doc
%defattr(-,root,root)
%{docdir}/examples/*
%{docdir}/*.txt
%dir %{docdir}/examples

#%files test
#%defattr(-,root,root)
#%{python_sitelib}/tests

%changelog
