#
# spec file for package python-python-akismet
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


Name:           python-python-akismet
Version:        0.4.3
Release:        0
Summary:        Akismet v1.1 module for Python
License:        MIT
URL:            https://github.com/Nekmo/python-akismet
Source:         https://files.pythonhosted.org/packages/source/p/python-akismet/python-akismet-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
Akismet v1.1 module for Python.

%prep
%autosetup -p1 -n python-akismet-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Unfortunately, tests require connection to the live instance of
# Akismet
# %%pyunittest -v akismet.tests

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/akismet
%{python_sitelib}/python[-_]akismet-%{version}*-info

%changelog
