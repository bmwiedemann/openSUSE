#
# spec file for package python-repoze.sphinx.autointerface
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


%global modname repoze.sphinx.autointerface
%{?sle15_python_module_pythons}
Name:           python-%{modname}
Version:        1.0.0
Release:        0
Summary:        Sphinx extension: auto-generates API docs from Zope interfaces
License:        SUSE-Repoze
Group:          Development/Languages/Python
URL:            http://www.repoze.org
Source:         https://files.pythonhosted.org/packages/source/r/repoze.sphinx.autointerface/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
Requires:       python-zope.interface
BuildArch:      noarch
%python_subpackages

%description
Thie package defines an extension for the Sphinx documentation system. The
extension allows generation of API documentation by introspection of
zope.interface instances in code.

%prep
%setup -q -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# do not install tests
%python_expand rm -rf %{buildroot}%{$python_sitelib}/repoze/sphinx/tests

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst COPYRIGHT.txt README.rst
%dir %{python_sitelib}/repoze
%dir %{python_sitelib}/repoze/sphinx
%{python_sitelib}/repoze/sphinx/autointerface.py
%{python_sitelib}/repoze[._]sphinx[._]autointerface-%{version}*-info
%{python_sitelib}/repoze[._]sphinx[._]autointerface-%{version}*nspkg.pth
%pycache_only %dir %{python_sitelib}/repoze/sphinx/__pycache__
%pycache_only %{python_sitelib}/repoze/sphinx/__pycache__/autointerface*

%changelog
