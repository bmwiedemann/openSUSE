#
# spec file for package python-openstack.nose_plugin
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-openstack.nose_plugin
Version:        0.11
Release:        0
Summary:        Openstack run_testspy style output for nosetests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/jkoelker/openstack-nose
Source:         https://files.pythonhosted.org/packages/source/o/openstack.nose_plugin/openstack.nose_plugin-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  openstack-suse-macros
BuildRequires:  python-rpm-macros
Requires:       python-colorama
Requires:       python-nose
Requires:       python-termcolor

%python_subpackages

%description
openstack.nose_plugin provides a nose plugin that allow's nosetests output to
mimic the output of openstack's run_tests.py.

%prep
%setup -q -n openstack.nose_plugin-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%{python_sitelib}/*

%changelog
