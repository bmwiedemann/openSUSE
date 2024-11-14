#
# spec file for package python-pysolr
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
Name:           python-pysolr
Version:        3.10.0
Release:        0
Summary:        Lightweight python wrapper for Apache Solr
License:        BSD-3-Clause
URL:            https://github.com/django-haystack/pysolr/
Source:         https://files.pythonhosted.org/packages/source/p/pysolr/pysolr-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.9.1
Suggests:       python-kazoo >= 2.5.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.9.1}
# /SECTION
%python_subpackages

%description
Lightweight python wrapper for Apache Solr.

%prep
%setup -q -n pysolr-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# TODO, requires solr server to run

%files %{python_files}
%doc AUTHORS CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/__pycache__
%{python_sitelib}/pysolr.py
%{python_sitelib}/pysolr-%{version}.dist-info

%changelog
