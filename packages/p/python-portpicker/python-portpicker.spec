#
# spec file for package python-portpicker
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without libalternatives
Name:           python-portpicker
Version:        1.6.0
Release:        0
Summary:        A library to choose unique available network ports
License:        Apache-2.0
Group:          Development/Libraries/Python
URL:            https://github.com/google/python_portpicker
Source0:        https://files.pythonhosted.org/packages/source/p/portpicker/portpicker-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  net-tools-deprecated
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%python_subpackages

%description
Portpicker provides an API to find and return an available network port for
an application to bind to. Ideally suited for use from unittests or for test
harnesses that launch local servers.

%prep
%setup -q -n portpicker-%{version}
test -f setup.py || echo "import setuptools; setuptools.setup()" > setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/portserver.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python src/tests/portpicker_test.py

%pre
%python_libalternatives_reset_alternative portserver.py

%files %{python_files}
%license LICENSE
%doc CONTRIBUTING.md README.md
%{python_sitelib}/portpicker.py
%pycache_only %{python_sitelib}/__pycache__/portpicker*
%{python_sitelib}/portpicker-%{version}*-info
# import asyncio
%python_alternative %{_bindir}/portserver.py

%changelog
