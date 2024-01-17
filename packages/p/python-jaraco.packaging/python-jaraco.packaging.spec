#
# spec file for package python-jaraco.packaging
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-jaraco.packaging
Version:        9.2.0
Release:        0
Summary:        Supplement packaging Python releases
License:        MIT
URL:            https://github.com/jaraco/jaraco.packaging
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.packaging/jaraco.packaging-%{version}.tar.gz
Source10:       https://files.pythonhosted.org/packages/py3/s/sampleproject/sampleproject-3.0.0-py3-none-any.whl
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module importlib-metadata if %python-version < 3.8}
BuildRequires:  %{python_module jaraco.context}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module virtualenv >= 20}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test
BuildRequires:  %{python_module pytest}
BuildRequires:  ca-certificates
# /SECTION
Requires:       python-build
Requires:       python-jaraco.context
# From build[virtualenv]
Requires:       python-virtualenv >= 20
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib-metadata
%endif
BuildArch:      noarch
%python_subpackages

%description
Tools to supplement packaging Python releases.

%prep
%autosetup -p1 -n jaraco.packaging-%{version}
rm -rf jaraco.packaging.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PIP_FIND_LINKS=$(dirname %{SOURCE10})
%pytest

%files %{python_files}
%license LICENSE
%doc docs/*.rst CHANGES.rst README.rst
%{python_sitelib}/jaraco.packaging-%{version}*-info
%dir %{python_sitelib}/jaraco
%{python_sitelib}/jaraco/packaging/

%changelog
