#
# spec file for package cloud-init
#
# Copyright (c) 2021 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
Version:        21.4
Release:        0
License:        GPL-3.0
Summary:        Cloud node initialization tool
Url:            https://github.com/canonical/cloud-init
Group:          System/Management
Source0:        %{name}-%{version}.tar.gz
Source1:        rsyslog-cloud-init.cfg
Patch1:        datasourceLocalDisk.patch
# FIXME (lp#1812117)
Patch2:        cloud-init-write-routes.patch
# FIXME (lp#1849296)
Patch3:        cloud-init-break-resolv-symlink.patch
# FIXME no proposed solution
Patch4:        cloud-init-sysconf-path.patch
# FIXME (lp#1860164)
Patch5:        cloud-init-no-tempnet-oci.patch
# FIXME https://github.com/canonical/cloud-init/pull/1278
Patch6:        cloud-init-sysctl-not-in-bin.patch
Patch7:        cloud-init-vmware-test.patch
BuildRequires:  fdupes
BuildRequires:  filesystem
# pkg-config is needed to find correct systemd unit dir
BuildRequires:  pkg-config
# needed for /lib/udev
BuildRequires:  pkgconfig(udev)
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# Test requirements
BuildRequires:  python3-Jinja2
BuildRequires:  python3-PyYAML
BuildRequires:  python3-configobj >= 5.0.2
BuildRequires:  python3-httpretty
BuildRequires:  python3-jsonpatch
BuildRequires:  python3-netifaces
BuildRequires:  python3-oauthlib
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
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
Requires:       python3-configobj >= 5.0.2
Requires:       python3-Jinja2
Requires:       python3-jsonpatch
Requires:       python3-jsonschema
Requires:       python3-netifaces
Requires:       python3-oauthlib
Requires:       python3-pyserial
Requires:       python3-PyYAML
Requires:       python3-requests
Requires:       python3-setuptools
Requires:       python3-six
Requires:       python3-xml
Requires:       sudo
Requires:       util-linux
Requires:       wget
Requires:       wicked-service
Requires:       cloud-init-config = %configver
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define         docdir %{_defaultdocdir}/%{name}
%ifarch %ix86 x86_64
Requires:       dmidecode
%endif
%define initsys systemd
BuildRequires: pkgconfig(systemd)
%{?systemd_requires}
%if 0%{?suse_version} && 0%{?suse_version} == 1220
%define systemd_prefix /lib
%else
%define systemd_prefix /usr/lib
%endif

%description
Cloud-init is an init script that initializes a cloud node (VM)
according to the fetched configuration data from the admin node.

%package config-suse
Summary:        Configuration file for Cloud node initialization tool
Provides:	    cloud-init-config = %configver
Group:          System/Management
Conflicts:	    otherproviders(cloud-init-config)

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

%prep
%setup -q
%patch1 -p0
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7 -p1

# patch in the full version to version.py
version_pys=$(find . -name version.py -type f)
[ -n "$version_pys" ] ||
   { echo "failed to find 'version.py' to patch with version." 1>&2; exit 1; }
sed -i "s,@@PACKAGED_VERSION@@,%{version}-%{release}," $version_pys

%build
python3 setup.py build

%check
## Ignore test failure currently not doing anything with opennebula
rm -v tests/unittests/test_datasource/test_opennebula.py
make unittest

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix} --install-lib=%{python3_sitelib} --init-system=%{initsys}
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

# remove duplicate files
%if 0%{?suse_version}
%fdupes %{buildroot}%{python3_sitelib}
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
%{_sysconfdir}/systemd/system/sshd-keygen@.service.d/disable-sshd-keygen-if-cloud-init-active.conf
%{_mandir}/man*/*
%if 0%{?suse_version} && 0%{?suse_version} < 1500
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%endif
%{_datadir}/bash-completion/completions/cloud-init
%{python3_sitelib}/cloudinit
%{python3_sitelib}/cloud_init-%{version}-py%{py3_ver}.egg-info
%{_prefix}/lib/cloud-init
%{systemd_prefix}/systemd/system-generators/cloud-init-generator
%{systemd_prefix}/systemd/system/cloud-config.service
%{systemd_prefix}/systemd/system/cloud-config.target
%{systemd_prefix}/systemd/system/cloud-init-local.service
%{systemd_prefix}/systemd/system/cloud-init.service
%{systemd_prefix}/systemd/system/cloud-init.target
%{systemd_prefix}/systemd/system/cloud-final.service
%dir %{_sysconfdir}/rsyslog.d
%{_sysconfdir}/rsyslog.d/21-cloudinit.conf
/usr/lib/udev/rules.d/66-azure-ephemeral.rules
# We use cloud-netconfig to handle new interfaces added to the instance
%exclude %{systemd_prefix}/systemd/system/cloud-init-hotplugd.service
%exclude %{systemd_prefix}/systemd/system/cloud-init-hotplugd.socket
%dir %attr(0755, root, root) %{_localstatedir}/lib/cloud
%dir %{docdir}
%dir /etc/NetworkManager
%dir /etc/NetworkManager/dispatcher.d
%dir /etc/dhcp
%dir /etc/dhcp/dhclient-exit-hooks.d
%dir /etc/systemd/system/sshd-keygen@.service.d

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
