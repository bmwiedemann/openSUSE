#
# spec file for package python-azure-agent
#
# Copyright (c) 2023 SUSE LLC
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
Version:        2.8.0.11
Release:        0
URL:            https://github.com/Azure/WALinuxAgent
Source0:        WALinuxAgent-%{version}.tar.gz
Patch1:         agent-no-auto-update.patch
Patch6:         paa_force_py3_sle15.patch
Patch7:         reset-dhcp-deprovision.patch
Patch8:         paa_12_sp5_rdma_no_ext_driver.patch
# PATCH-FIX-UPSTREAM gh#Azure/WALinuxAgent#2741
Patch9:         remove-mock.patch
BuildRequires:  dos2unix

BuildRequires:  distribution-release
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} && 0%{?suse_version} > 1315
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
Requires:       wicked
%if 0%{?suse_version} && 0%{?suse_version} > 1315
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
# We are only building against Python 3 for SLE15+, and we don't need mock.
%if 0%{?suse_version} && 0%{?suse_version} > 1315 && 0%{?suse_version} < 1500
Requires:       python3-mock
%endif
%if 0%{?suse_version} && 0%{?suse_version} > 1315
Requires:       python3-pytest
%else
Requires:       python-mock
Requires:       python-pytest
%endif

%description test
Unit tests for python-azure-agent.

%prep
%setup -qn WALinuxAgent-%{version}
%patch1
%if 0%{?suse_version} && 0%{?suse_version} > 1315
%patch6
%endif
%patch7
%patch8
%patch9 -p1

%build
%if 0%{?suse_version} && 0%{?suse_version} > 1315
python3 setup.py build
%else
python setup.py build
%endif

%install
%if 0%{?suse_version} && 0%{?suse_version} > 1315
python3 setup.py install --prefix=%{_prefix} --lnx-distro='suse' --root=%{buildroot}
%else
python setup.py install --prefix=%{_prefix} --lnx-distro='suse' --root=%{buildroot}
%endif

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
%if 0%{?suse_version} && 0%{?suse_version} > 1315
cp -r tests %{buildroot}/%{python3_sitelib}/azurelinuxagent
%else
cp -r tests %{buildroot}/%{python_sitelib}/azurelinuxagent
%endif

%pre
%service_add_pre waagent.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/waagent ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

%if 0%{?suse_version} > 1500
%posttrans
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

%files
%defattr(0644,root,root,0755)
%doc NOTICE README.md
%license LICENSE.txt
%{_sbindir}/rcwaagent
%attr(0755,root,root) %{_sbindir}/waagent
%attr(0755,root,root) %{_sbindir}/waagent2.0
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/waagent
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/waagent
%endif
%config(noreplace) %{_sysconfdir}/waagent.conf
%ghost %{_localstatedir}/log/waagent.log
%{_unitdir}/waagent.service
%if 0%{?suse_version} < 1230
/lib/udev/rules.d/66-azure-storage.rules
/lib/udev/rules.d/99-azure-product-uuid.rules
%else
/usr/lib/udev/rules.d/66-azure-storage.rules
/usr/lib/udev/rules.d/99-azure-product-uuid.rules
%endif
%if 0%{?suse_version} && 0%{?suse_version} > 1315
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
%if 0%{?suse_version} && 0%{?suse_version} > 1315
%{python3_sitelib}/azurelinuxagent/tests
%else
%{python_sitelib}/azurelinuxagent/tests
%endif

%changelog
