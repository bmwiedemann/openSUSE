#
# spec file for package python-pyLibravatar
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        2.0.2
Release:        0
Summary:        Python module for Libravatar
License:        MIT
URL:            https://github.com/libravatar/pylibravatar
Source:         https://files.pythonhosted.org/packages/source/p/pyLibravatar/pylibravatar-%{version}.tar.gz
BuildRequires:  %{python_module dnspython >= 2.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dnspython >= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
PyLibravatar is a module for using federated Libravatar
avatar hosting service from within Python applications.

%prep
%setup -q -n pylibravatar-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license README.md
%doc README.md
%{python_sitelib}/libravatar.py
%{python_sitelib}/py[Ll]ibravatar-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/libravatar*

%changelog
