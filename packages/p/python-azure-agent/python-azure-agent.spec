#
# spec file for package python-azure-agent
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-azure-agent
Summary:        Microsoft Azure Linux Agent
License:        Apache-2.0
Group:          System/Daemons
Version:        2.9.1.1
Release:        0
URL:            https://github.com/Azure/WALinuxAgent
Source0:        WALinuxAgent-%{version}.tar.gz
Patch1:         agent-no-auto-update.patch
Patch6:         paa_force_py3_sle15.patch
Patch7:         reset-dhcp-deprovision.patch
Patch8:         paa_12_sp5_rdma_no_ext_driver.patch
# PATCH-FIX-UPSTREAM gh#Azure/WALinuxAgent#2741
Patch9:         remove-mock.patch
Patch10:        agent-micro-is-sles.patch
BuildRequires:  dos2unix

BuildRequires:  distribution-release
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} > 1315
BuildRequires:  python3-distro
BuildRequires:  python3-setuptools
%else
BuildRequires:  python-setuptools
BuildRequires:  python-xml
%endif
BuildRequires:  pkgconfig(udev)
Requires:       eject
Requires:       grep
Requires:       iptables
Requires:       logrotate
Requires:       openssh
Requires:       openssl
Requires:       pwdutils
Requires:       systemd
Requires:       sysvinit-tools
%if 0%{?suse_version} <= 1500
Requires:       wicked
%endif
%if 0%{?suse_version} > 1315
Requires:       python3-distro
Requires:       python3-pyasn1
Requires:       python3-xml
%else
Requires:       python-pyasn1
Requires:       python-xml
%endif
Requires:       sudo
Requires:       util-linux

# Package renamed in SLE 12, do not remove Provides, Obsolete directives
# until after SLE 12 EOL
Provides:       WALinuxAgent = %{version}
Obsoletes:      WALinuxAgent < %{version}

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The azure-agent supports the provisioning and running of Linux
VMs in the Microsoft Azure Public Cloud and Microsoft Azure Stack private
cloud. This package should be installed on Linux disk
images that are built to run withing the Microsoft Azure or
Microsoft Azure Stack framework.

%package test
Summary:        Unit tests
Group:          Development/Languages/Python
Requires:       %{name} == %{version}
Requires:       openssl
%if 0%{?suse_version} > 1315
Requires:       python3-pytest
%else
Requires:       python-mock
Requires:       python-pytest
%endif

%description test
Unit tests for python-azure-agent.

%package config-default
Summary:        Default upstream configuration
Group:          Development/Languages/Python
Requires:       %{name} == %{version}
Provides:       waagent-config
Conflicts:      otherproviders(waagent-config)

%description config-default
The default configuration for the agent as supplied by upstream for SUSE

%package config-server
Summary:        SUSE specific configuration for server products
Group:          Development/Languages/Python
Requires:       %{name} == %{version}
Provides:       waagent-config
Conflicts:      otherproviders(waagent-config)

%description config-server
Modified waagent.conf file to meet SUSE policies and SUSE image build
setup

%package config-hpc
Summary:        SUSE specific configuration for HPC
Group:          Development/Languages/Python
Requires:       %{name} == %{version}
Provides:       waagent-config
Conflicts:      otherproviders(waagent-config)

%description config-hpc
Modified waagent.conf file to meet SUSE policies and SUSE image build
setup

%package config-micro
Summary:        SUSE specific configuration for Micro
Group:          Development/Languages/Python
Requires:       %{name} == %{version}
Provides:       waagent-config
Conflicts:      otherproviders(waagent-config)

%description config-micro
Modified waagent.conf file to meet SUSE policies and SUSE image build
setup

%prep
%setup -qn WALinuxAgent-%{version}
%patch -P 1
%if 0%{?suse_version} > 1315
%patch -P 6
%endif
%patch -P 7
%patch -P 8
%patch -P 9 -p1
%patch -P 10

%build
%if 0%{?suse_version} > 1315
python3 setup.py build
%else
python setup.py build
%endif

%install
%if 0%{?suse_version} > 1315
python3 setup.py install --prefix=%{_prefix} --lnx-distro='suse' --root=%{buildroot}
%else
python setup.py install --prefix=%{_prefix} --lnx-distro='suse' --root=%{buildroot}
%endif

# Config file flavor setup
cp %{buildroot}%{_sysconfdir}/waagent.conf %{buildroot}%{_sysconfdir}/waagent.conf.default
# No autoupdate of binaries for any SUSE product
sed -i -e "s/# AutoUpdate.Enabled=y/AutoUpdate.Enabled=n/" %{buildroot}%{_sysconfdir}/waagent.conf
# Common settings for most SUSE products
# Generate all supported SSH host key types
sed -i -e "s/SshHostKeyPairType=rsa/SshHostKeyPairType=auto/" %{buildroot}%{_sysconfdir}/waagent.conf
# We use clod-init
sed -i -e "s/Provisioning.Agent=auto/Provisioning.Agent=cloud-init/" %{buildroot}%{_sysconfdir}/waagent.conf
# Leave the ephemeral disk handling to cloud-init
sed -i -e "s/ResourceDisk.Format=y/ResourceDisk.Format=n/" %{buildroot}%{_sysconfdir}/waagent.conf
cp %{buildroot}%{_sysconfdir}/waagent.conf %{buildroot}%{_sysconfdir}/waagent.conf.server
# HPC setup is addition to SUSE server configuration
# While there is no more specific driver we still need to enable
# RDMA to make the logic in the agent set up the IB interface
sed -i -e "s/# OS.EnableRDMA=y/OS.EnableRDMA=y/" %{buildroot}%{_sysconfdir}/waagent.conf
cp %{buildroot}%{_sysconfdir}/waagent.conf %{buildroot}%{_sysconfdir}/waagent.conf.hpc
# Micro setup
# Undo the HPC change
sed -i -e "s/OS.EnableRDMA=y/# OS.EnableRDMA=y/" %{buildroot}%{_sysconfdir}/waagent.conf
# Use Ignition/Afterburn in Micro
sed -i -e "s/Provisioning.Agent=cloud-init/Provisioning.Agent=disabled/" %{buildroot}%{_sysconfdir}/waagent.conf
# No extension support for transactional-upfdate systems
# There's an inherant bug in that root password reset is also treated via this
# switch
sed -i -e "s/Extensions.Enabled=y/Extensions.Enabled=n/" %{buildroot}%{_sysconfdir}/waagent.conf
mv %{buildroot}%{_sysconfdir}/waagent.conf %{buildroot}%{_sysconfdir}/waagent.conf.micro

ln -s service %{buildroot}%{_sbindir}/rcwaagent
mkdir -p %{buildroot}/%{_unitdir}

# Deal with logic embeded in the code that puts the unit file where we do not
# want it, sometimes (depending on teh build environment)
if [ -e %{buildroot}/lib/systemd/system ]; then
mv %{buildroot}/lib/systemd/system/* %{buildroot}/%{_unitdir}
fi

### udev rules
%if 0%{?suse_version} < 1230
mkdir -p %{buildroot}/lib/udev/rules.d
mv %{buildroot}%{_sysconfdir}/udev/rules.d/* %{buildroot}/lib/udev/rules.d/
%else
mkdir -p %{buildroot}/usr/lib/udev/rules.d
mv %{buildroot}%{_sysconfdir}/udev/rules.d/* %{buildroot}/usr/lib/udev/rules.d/
%endif
### log file ghost
mkdir -p  %{buildroot}/%{_localstatedir}/log
touch %{buildroot}/%{_localstatedir}/log/waagent.log
### permissinon fixes
chmod +x %{buildroot}/%{_sbindir}/waagent2.0
### naming issues
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
mv %{buildroot}/%{_sysconfdir}/logrotate.d/waagent.logrotate %{buildroot}/%{_distconfdir}/logrotate.d/waagent
%else
mv %{buildroot}/%{_sysconfdir}/logrotate.d/waagent.logrotate %{buildroot}/%{_sysconfdir}/logrotate.d/waagent
%endif

# install tests
%if 0%{?suse_version} > 1315
cp -r tests %{buildroot}/%{python3_sitelib}/azurelinuxagent
%else
cp -r tests %{buildroot}/%{python_sitelib}/azurelinuxagent
%endif

%pre
%service_add_pre waagent.service
# Handle the case when the -config-* package is not installed, we want to
# preserver the previousl config file that was flavor customized during
# image build
if [ -e /etc/waagent.conf ]; then
    cp -Z /etc/waagent.conf /etc/waagent.conf.bak
fi

%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/waagent ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%posttrans
# Do not clobber the config if it was installed from a config package, but
# put the oldfile back if we do not have another config file
if [ ! -e /etc/waagent.conf ]; then
    if [ -e /etc/waagent.conf.bak ]; then
        mv -Z /etc/waagent.conf.bak /etc/waagent.conf
    # Making the assumption that the rpmsave file was generated because of
    # of the previously broken package upgrade.
    elif [ -e /etc/waagent.conf.rpmsave ]; then
        cp -Z /etc/waagent.conf.rpmsave /etc/waagent.conf
    fi
fi
%if 0%{?suse_version} > 1500
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/waagent ; do
    test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post
%service_add_post waagent.service

%preun
%service_del_preun waagent.service

%postun
%restart_on_update waagent
%service_del_postun waagent.service

%post config-default
rm -rf %{_sysconfdir}/waagent.conf
ln -s %{_sysconfdir}/waagent.conf.default %{_sysconfdir}/waagent.conf

%post config-server
rm -rf %{_sysconfdir}/waagent.conf
ln -s %{_sysconfdir}/waagent.conf.server %{_sysconfdir}/waagent.conf

%post config-hpc
rm -rf %{_sysconfdir}/waagent.conf
ln -s %{_sysconfdir}/waagent.conf.hpc %{_sysconfdir}/waagent.conf

%post config-micro
rm -rf %{_sysconfdir}/waagent.conf
ln -s %{_sysconfdir}/waagent.conf.micro %{_sysconfdir}/waagent.conf

%files
%defattr(0644,root,root,0755)
%doc NOTICE README.md
%license LICENSE.txt
%exclude %{_sysconfdir}/waagent.conf*
%{_sbindir}/rcwaagent
%attr(0755,root,root) %{_sbindir}/waagent
%attr(0755,root,root) %{_sbindir}/waagent2.0
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/waagent
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/waagent
%endif
%ghost %{_localstatedir}/log/waagent.log
%{_unitdir}/waagent.service
%if 0%{?suse_version} < 1230
/lib/udev/rules.d/66-azure-storage.rules
/lib/udev/rules.d/99-azure-product-uuid.rules
%else
/usr/lib/udev/rules.d/66-azure-storage.rules
/usr/lib/udev/rules.d/99-azure-product-uuid.rules
%endif
%if 0%{?suse_version} > 1315
%dir %{python3_sitelib}/azurelinuxagent
%{python3_sitelib}
%exclude %{python3_sitelib}/azurelinuxagent/tests
%else
%dir %{python_sitelib}/azurelinuxagent
%{python_sitelib}
%exclude %{python_sitelib}/azurelinuxagent/tests
%endif

%files test
%defattr(0644,root,root,0755)
%if 0%{?suse_version} > 1315
%{python3_sitelib}/azurelinuxagent/tests
%else
%{python_sitelib}/azurelinuxagent/tests
%endif

%files config-default
%ghost %{_sysconfdir}/waagent.conf
%config(noreplace) %{_sysconfdir}/waagent.conf.default

%files config-server
%ghost %{_sysconfdir}/waagent.conf
%config(noreplace) %{_sysconfdir}/waagent.conf.server

%files config-hpc
%ghost %{_sysconfdir}/waagent.conf
%config(noreplace) %{_sysconfdir}/waagent.conf.hpc

%files config-micro
%ghost %{_sysconfdir}/waagent.conf
%config(noreplace) %{_sysconfdir}/waagent.conf.micro

%changelog
