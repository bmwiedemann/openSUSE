#
# spec file for package python-Flask-Versioned
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
Name:           python-Flask-Versioned
Version:        0.9.4
Release:        0
Summary:        Add version info to file paths
License:        BSD-3-Clause
URL:            http://github.com/pilt/flask-versioned
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Versioned/Flask-Versioned-%{version}-20101221.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module Flask}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Flask
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
Add version info to file paths.

%prep
%autosetup -p1 -n Flask-Versioned-%{version}-20101221

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# no checks available upstream

%files %{python_files}
%if 0%{suse_version} >= 1600
%{python_sitelib}/Flask_Versioned-0.9.4.post20101221-py3.10-nspkg.pth
%else
%{python_sitelib}/Flask_Versioned-0.9.4.post20101221-py3.11-nspkg.pth
%endif
%dir %{python_sitelib}/flaskext/
%dir %{python_sitelib}/flaskext/versioned/
%{python_sitelib}/flaskext/versioned/__init__.py
%pycache_only %{python_sitelib}/flaskext/versioned/__pycache__/
%{python_sitelib}/Flask_Versioned-%{version}.*.dist-info

%changelog
