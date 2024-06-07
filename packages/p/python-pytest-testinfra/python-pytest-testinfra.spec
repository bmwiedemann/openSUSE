#
# spec file for package python-pytest-testinfra
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


%{?sle15_python_module_pythons}
Name:           python-pytest-testinfra
Version:        10.1.1
Release:        0
Summary:        Python module to test infrastructures
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pytest-dev/pytest-testinfra
Source:         https://files.pythonhosted.org/packages/source/p/pytest-testinfra/pytest-testinfra-%{version}.tar.gz
# PATCH-FIX-OPENSUSE testinfra-parametrize-backends-test.patch -- make backends deselectable which are not available for testing
Patch1:         testinfra-parametrize-backends-test.patch
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pywinrm}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado}
BuildRequires:  ansible
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-salt
Requires:       python-pytest >= 6.0
Provides:       python-testinfra = %{version}-%{release}
Obsoletes:      python-testinfra < %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
With Testinfra, one can write unit tests in Python to test the actual
state of servers configured by managements tools like Salt, Ansible,
Puppet, Chef and so on.

Testinfra is like a Serverspec equivalent in Python, and is written
as a plugin to the Pytest test engine.

%prep
%autosetup -p1 -n pytest-testinfra-%{version}
# register custom markers for test suite in order to avoid warning clutter
sed -i -e '/\[tool:pytest\]/ a markers = \
  testinfra_hosts\
  destructive' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/testinfra

%check
export LANG=en_US.UTF-8
donttest="donttestnonemptyprefix"
%{python_expand # salt is python3 primary flavor only
if [ "${python_flavor}" != "python3" -a "%{$python_provides}" != "python3" ]; then
   $python_donttest="or (test_backend_importables and salt)"
fi
}
%pytest -ra -k "not ($donttest ${$python_donttest})" test

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/testinfra
%{python_sitelib}/pytest_testinfra-%{version}*-info

%changelog
