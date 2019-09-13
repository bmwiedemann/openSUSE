#
# spec file for package python-Fabric3
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Fabric3
Version:        1.14.post1
Release:        0
Summary:        Pythonic tool for remote execution and deployment
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mathiasertl/fabric/
Source:         https://files.pythonhosted.org/packages/source/F/Fabric3/Fabric3-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module fudge}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module paramiko >= 2.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-paramiko >= 2.0
Requires:       python-six >= 1.10.0
Conflicts:      %{oldpython}-Fabric
Conflicts:      python-Fabric
BuildArch:      noarch
%python_subpackages

%description
Fabric3 is a fork of Fabric <http://fabfile.org> to provide compatility
with Python 3.4+. The port still works with Python 2.7.

Fabric3 is compatible with the original Fabric. Please file issues
for any differences you find. Known differences are documented on
github <https://github.com/mathiasertl/fabric/>.

%prep
%setup -q -n Fabric3-%{version}
# the utils test have issues with py3 and py2 compat a lot
rm tests/test_utils.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_connect_does_not_prompt_password_when_ssh_raises_channel_exception - seems fudge version issue not runtime issue
# upload_template - raises unicode error in test code
# test_nested_execution_with_explicit_ports - https://github.com/mathiasertl/fabric/issues/48
%python_expand nosetests-%{$python_bin_suffix} -v -e '(test_connect_does_not_prompt_password_when_ssh_raises_channel_exception|upload_template|test_nested_execution_with_explicit_ports)'

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%python3_only %{_bindir}/fab
%{python_sitelib}/*

%changelog
