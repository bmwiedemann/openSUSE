#
# spec file for package sesdev
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           sesdev
Version:        1.8.0+1602174240.g45df4dd
Release:        1%{?dist}
Summary:        CLI tool to deploy and manage SES clusters
License:        MIT
URL:            https://github.com/SUSE/sesdev
Source0:        %{name}-%{version}.tar.gz
Source1:        checkin.sh
Source2:        README-checkin.txt
NoSource:       1
NoSource:       2

BuildArch:      noarch

%if 0%{?suse_version}
BuildRequires:  python-rpm-macros
%else
BuildRequires:  python3-devel
%endif
BuildRequires:  fdupes
BuildRequires:  python3-setuptools

%if 0%{?suse_version}
Requires:       python3-Jinja2 >= 2.10.1
Requires:       python3-libvirt-python >= 5.1.0
Requires:       python3-PrettyTable
Requires:       python3-PyYAML >= 3.13
%endif
%if 0%{?el8} || 0%{?fedora}
Requires:       python3-jinja2 >= 2.10.1
Requires:       python3-libvirt >= 5.1.0
Requires:       python3-prettytable
Requires:       python3-pyyaml >= 3.13
%endif
Requires:       python3-click >= 6.7
Requires:       python3-pycryptodomex >= 3.4.6
Requires:       python3-setuptools
Requires:       vagrant > 2.2.2
Requires:       vagrant-libvirt
Requires:       sesdev-qa

%if 0%{?el8} || 0%{?fedora}
%{?python_disable_dependency_generator}
%endif

%description
sesdev is a CLI tool for developers to help with deploying SES clusters.
This tool uses vagrant and libvirt to create VMs and install Ceph using
DeepSea. The tool is highly customizable and allows to choose different
versions of Ceph and SES, as well as, different versions of the openSUSE
based OS.

%package qa
Summary:    Integration test script for validating Ceph deployments

%description qa
Integration test script for validating Ceph clusters deployed
by sesdev

%prep
%autosetup -p1
%if 0%{?fedora} && 0%{?fedora} < 30
sed -i -e 's/^\s*lv.qemu_use_session = false$//g' seslib/templates/Vagrantfile.j2
%endif

%build
%py3_build

%install
%py3_install
%fdupes %{buildroot}%{python3_sitelib}
install -m 0755 -d %{buildroot}/%{_datadir}/%{name}/qa
install -m 0755 -d %{buildroot}/%{_datadir}/%{name}/qa/common
install -m 0755 qa/health-ok.sh %{buildroot}/%{_datadir}/%{name}/qa/health-ok.sh
install -m 0644 qa/common/common.sh %{buildroot}/%{_datadir}/%{name}/qa/common/common.sh
install -m 0644 qa/common/helper.sh %{buildroot}/%{_datadir}/%{name}/qa/common/helper.sh
install -m 0644 qa/common/json.sh %{buildroot}/%{_datadir}/%{name}/qa/common/json.sh
install -m 0644 qa/common/zypper.sh %{buildroot}/%{_datadir}/%{name}/qa/common/zypper.sh

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{python3_sitelib}/seslib*/
%{python3_sitelib}/sesdev*/
%{_bindir}/%{name}
%dir %{_datadir}/%{name}

%files qa
%{_datadir}/%{name}/qa

%changelog

