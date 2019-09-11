#
# spec file for package python-testinfra
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-testinfra
Version:        3.1.0
Release:        0
Summary:        Python module to test infrastructures
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://github.com/philpep/testinfra
Source:         https://files.pythonhosted.org/packages/source/t/testinfra/testinfra-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pywinrm}
BuildRequires:  %{python_module salt}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.4}
BuildRequires:  ansible > 2.8
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
Requires:       python-six >= 1.4
BuildArch:      noarch
%python_subpackages

%description
With Testinfra, one can write unit tests in Python to test the actual
state of servers configured by managements tools like Salt, Ansible,
Puppet, Chef and so on.

Testinfra is like a Serverspec equivalent in Python, and is written
as a plugin to the Pytest test engine.

%prep
%setup -q -n testinfra-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/testinfra

%check
export LANG=en_US.UTF-8
#ansible does not exist at python2
%pytest -k "not test_backend_importables"

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
