#
# spec file for package python-junos-eznc
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2017-2020, Martin Hauke <mardnh@gmx.de>
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


%define skip_python2 1
Name:           python-junos-eznc
Version:        2.7.1
Release:        0
Summary:        Junos 'EZ' automation for non-programmers
License:        Apache-2.0
URL:            https://www.github.com/Juniper/py-junos-eznc
Source:         https://github.com/Juniper/py-junos-eznc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# replace deprecated yamlordereddictloader by yamlloader
# https://github.com/Juniper/py-junos-eznc/pull/1078
Patch1:         python-junos-eznc-remove-yamlordereddictloader.patch
# https://github.com/Juniper/py-junos-eznc/issues/1176
Patch3:         python-junos-eznc-no-mock.patch
# PATCH-FIX-OPENSUSE python-311.patch gh#Juniper/py-junos-eznc#1236
Patch4:         python-311.patch
# PATCH-FIX-UPSTREAM gh#Juniper/py-junos-eznc#1307 Don't require six
Patch5:         no-six.patch
BuildRequires:  %{python_module Jinja2 >= 2.7.1}
BuildRequires:  %{python_module PyYAML >= 5.1}
BuildRequires:  %{python_module lxml >= 3.2.4}
BuildRequires:  %{python_module ncclient >= 0.6.15}
BuildRequires:  %{python_module nose2}
BuildRequires:  %{python_module ntc-templates}
BuildRequires:  %{python_module paramiko >= 1.15.2}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module pyserial}
BuildRequires:  %{python_module pytest-forked}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scp >= 0.7.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module transitions}
BuildRequires:  %{python_module yamlloader}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.7.1
Requires:       python-PyYAML >= 5.1
Requires:       python-lxml >= 3.2.4
Requires:       python-ncclient >= 0.6.15
Requires:       python-paramiko >= 1.15.2
Requires:       python-pyparsing
Requires:       python-pyserial
Requires:       python-scp >= 0.7.0
Requires:       python-transitions
BuildArch:      noarch
%python_subpackages

%description
Junos PyEZ is designed to provide the same capabilities as a user would have
on the Junos CLI, but in an environment built for automation tasks.
These capabilities include, but are not limited to:

 - Remote connectivity and management of Junos devices via NETCONF
 - Provide "facts" about the device
 - Retrieve "operational" or "run-state" information
 - Retrieve configuration information
 - Make configuration changes in unstructured and structured ways
 - Provide common utilities for tasks such as secure copy of files and
   software updates

%prep
%autosetup -p1 -n py-junos-eznc-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
donttest="nonemptydonttestprefix"
# https://github.com/Juniper/py-junos-eznc/issues/1109
python39_donttest=" or test_sw_put_ftp"
python310_donttest=" or test_sw_put_ftp"
donttest+=" or test_sw_install_multi_vc"
%pytest -m "not functional" --forked -k "not ($donttest ${$python_donttest})" tests/unit

%files %{python_files}
%license COPYRIGHT LICENSE
%doc README.txt README.md
%dir %{python_sitelib}/jnpr
%{python_sitelib}/jnpr/junos
%{python_sitelib}/junos_eznc-%{version}*-info
%{python_sitelib}/junos_eznc-%{version}*-nspkg.pth

%changelog
