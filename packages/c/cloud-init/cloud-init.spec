#
# spec file for package cloud-init
#
# Copyright (c) 2023 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%if 0%{?suse_version} >= 1600
%define pythons %{primary_python}
%else
%define pythons python311
%endif
%global _sitelibdir %{%{pythons}_sitelib}


Name:           cloud-init
Version:        25.1.3
Release:        0
License:        GPL-3.0
Summary:        Cloud node initialization tool
Url:            https://github.com/canonical/cloud-init
Group:          System/Management
Source0:        %{name}-%{version}.tar.gz
Source1:        rsyslog-cloud-init.cfg
Source2:        hidesensitivedata
Patch1:        datasourceLocalDisk.patch
# FIXME (lp#1849296)
Patch2:        cloud-init-break-resolv-symlink.patch
# FIXME no proposed solution
Patch3:        cloud-init-sysconf-path.patch
# FIXME (lp#1860164)
Patch4:        cloud-init-no-tempnet-oci.patch
# FIXME https://github.com/canonical/cloud-init/issues/5152 and LP#1715241
Patch5:       cloud-init-no-openstack-guess.patch
# FIXME https://github.com/canonical/cloud-init/issues/5075
Patch6:       cloud-init-skip-rename.patch
# FIXME https://github.com/canonical/cloud-init/pull/6105
Patch7:       cloud-init-ssh-usrmerge.patch
# FIXME https://github.com/canonical/cloud-init/pull/6121
Patch8:       cloud-init-lint-set-interpreter.patch
Patch9:       cloud-init-lint-fix.patch
# FIXME https://github.com/canonical/cloud-init/blob/ubuntu/noble/debian/patches/no-single-process.patch
# We have an old version of netcat that does not support the necessary
# feature to support a single process for cloud-init. Once we have netcat
# 1.226 or later available we can get rid of this patch
# Maybe there is hope for 16 https://jira.suse.com/browse/PED-12810
Patch11:      cloud-init-no-single-process.patch
# FIXME https://github.com/canonical/cloud-init/pull/6214
Patch12:      cloud-init-needs-action.patch

BuildRequires:  fdupes
BuildRequires:  filesystem
# pkg-config is needed to find correct systemd unit dir
BuildRequires:  pkg-config
# needed for /lib/udev
BuildRequires:  pkgconfig(udev)
BuildRequires:  procps
BuildRequires:  python-rpm-macros
BuildRequires:  %{pythons}-devel
BuildRequires:  %{pythons}-setuptools
# Test requirements
BuildRequires:  %{pythons}-Jinja2
BuildRequires:  %{pythons}-PyYAML
BuildRequires:  %{pythons}-configobj >= 5.0.2
BuildRequires:  %{pythons}-flake8
BuildRequires:  %{pythons}-jsonpatch
BuildRequires:  %{pythons}-jsonschema
BuildRequires:  %{pythons}-oauthlib
BuildRequires:  %{pythons}-passlib
BuildRequires:  %{pythons}-pytest
BuildRequires:  %{pythons}-pytest-cov
BuildRequires:  %{pythons}-pytest-mock
BuildRequires:  %{pythons}-requests
BuildRequires:  %{pythons}-responses
BuildRequires:  %{pythons}-pyserial
BuildRequires:  system-user-nobody
BuildRequires:  distribution-release
BuildRequires:  util-linux
Requires:       bash
%if 0%{?suse_version} >= 1600
# Micro 6+ is identified in the Build Service with 1600 as SUSE version but
# it does not provide dhcpcd
Requires:       (dhcpcd or dhcp-client)
%else
Requires:       dhcp-client
%endif
Requires:       file
Requires:       growpart
Requires:       e2fsprogs
Requires:       net-tools
Requires:       openssh
Requires:       procps
Requires:       %{pythons}-configobj >= 5.0.2
Requires:       %{pythons}-Jinja2
Requires:       %{pythons}-jsonpatch
Requires:       %{pythons}-jsonschema
Requires:       %{pythons}-oauthlib
Requires:       %{pythons}-passlib
Requires:       %{pythons}-PyYAML
Requires:       %{pythons}-requests
Requires:       %{pythons}-serial
Requires:       %{pythons}-setuptools
Requires:       %{pythons}-xml
Requires:       sudo
Requires:       util-linux
Requires:       wget
%if 0%{?suse_version} && 0%{?suse_version} <= 1500
Requires:       wicked-service
%endif
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
%patch -P 1 -p0
%patch -P 2
%patch -P 3
%patch -P 4
%patch -P 5
%patch -P 6
%patch -P 7
%patch -P 8
%patch -P 9
%patch -P 11
%patch -P 12

# patch in the full version to version.py
version_pys=$(find . -name version.py -type f)
[ -n "$version_pys" ] ||
   { echo "failed to find 'version.py' to patch with version." 1>&2; exit 1; }
sed -i "s,@@PACKAGED_VERSION@@,%{version}-%{release}," $version_pys

%build
%python_build


%check
# Total HACK, we have no macro that expands the proper Python interpreter
# in a way that it can be used to set en environment variable
if [ -e /usr/bin/python3.13 ]; then
    export PYTHON=/usr/bin/python3.13
else
    export PYTHON=/usr/bin/python3.11
fi
make unittest
# Disable the flake checks and accept the bugs we may introduce with the
# patches. On SLE 15 SP5 flake dies with some weird internal error
#make lint

%install
%python_exec setup.py install --prefix=%{_prefix} --init-system=%{initsys} --distro=suse --root=%{buildroot}


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
mkdir -p %{buildroot}/%{systemd_prefix}/systemd/system/sshd-keygen@.service.d
mkdir -p %{buildroot}/%{_sysconfdir}/rsyslog.d
mkdir -p %{buildroot}/usr/lib/udev/rules.d/
cp -a %{SOURCE1} %{buildroot}/%{_sysconfdir}/rsyslog.d/21-cloudinit.conf
mkdir -p %{buildroot}%{_sbindir}
%if 0%{?suse_version} < 1600
install -m 755 %{SOURCE2} %{buildroot}%{_sbindir}
sed -i "s/python3/python3.11/" %{buildroot}%{_sbindir}/hidesensitivedata
%endif
# remove debian/ubuntu specific profile.d file (bnc#779553)
rm -f %{buildroot}%{_sysconfdir}/profile.d/Z99-cloud-locale-test.sh

# Remove non-SUSE templates
rm %{buildroot}/%{_sysconfdir}/cloud/templates/*.debian.*
rm %{buildroot}/%{_sysconfdir}/cloud/templates/*.redhat.*
rm %{buildroot}/%{_sysconfdir}/cloud/templates/*.ubuntu.*

# remove duplicate files
%if 0%{?suse_version}
%fdupes %{buildroot}%{_sitelibdir}
%endif

%if 0%{?suse_version} < 1600
%post
/usr/sbin/hidesensitivedata
%endif

%files
%defattr(-,root,root)
%dir %attr(0755, root, root) %{_localstatedir}/lib/cloud
%dir %{_sysconfdir}/cloud
%dir %{docdir}
%dir %{_sysconfdir}/rsyslog.d
%dir %{systemd_prefix}/systemd/system/sshd-keygen@.service.d
%license LICENSE LICENSE-GPLv3
%{_bindir}/cloud-id
%{_bindir}/cloud-init
%{_bindir}/cloud-init-per
%if 0%{?suse_version} < 1600
%{_sbindir}/hidesensitivedata
%endif
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg.d
%config(noreplace) %{_sysconfdir}/cloud/templates
%{systemd_prefix}/systemd/system/sshd-keygen@.service.d/disable-sshd-keygen-if-cloud-init-active.conf
%{_mandir}/man*/*
%if 0%{?suse_version} && 0%{?suse_version} < 1500
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%endif
%{_datadir}/bash-completion/completions/cloud-init
%{_sitelibdir}/cloudinit
%{_sitelibdir}/cloud_init-%{version}*.egg-info
%{_prefix}/lib/cloud-init
%{systemd_prefix}/systemd/system-generators/cloud-init-generator
%{systemd_prefix}/systemd/system/cloud-config.service
%{systemd_prefix}/systemd/system/cloud-config.target
%{systemd_prefix}/systemd/system/cloud-init-local.service
%{systemd_prefix}/systemd/system/cloud-init.service
%{systemd_prefix}/systemd/system/cloud-init-main.service
%{systemd_prefix}/systemd/system/cloud-init-network.service
%{systemd_prefix}/systemd/system/cloud-init.target
%{systemd_prefix}/systemd/system/cloud-final.service
%{_sysconfdir}/rsyslog.d/21-cloudinit.conf
%{_prefix}/lib/udev/rules.d/66-azure-ephemeral.rules
# We use cloud-netconfig to handle new interfaces added to the instance
%exclude %{systemd_prefix}/systemd/system/cloud-init-hotplugd.service
%exclude %{systemd_prefix}/systemd/system/cloud-init-hotplugd.socket




%files config-suse
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg

%files doc
%defattr(-,root,root)
%{docdir}/examples/*
%{docdir}/*.txt
%dir %{docdir}/examples

%changelog
