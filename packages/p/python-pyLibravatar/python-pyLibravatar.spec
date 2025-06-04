#
# spec file for package python-pyLibravatar
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


Name:           python-pyLibravatar
Version:        1.7
Release:        0
Summary:        Python module for Libravatar
License:        MIT
URL:            https://launchpad.net/pylibravatar
Source:         https://files.pythonhosted.org/packages/source/p/pyLibravatar/pyLibravatar-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module py3dns}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-py3dns
BuildArch:      noarch
%python_subpackages

%description
PyLibravatar is a module for using federated Libravatar
avatar hosting service from within Python applications.

%prep
%setup -q -n pyLibravatar-%{version}
dos2unix *.txt

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license README.txt
%doc README.txt Changelog.txt
%{python_sitelib}/libravatar.py
%{python_sitelib}/py[Ll]ibravatar-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/libravatar*

%changelog
