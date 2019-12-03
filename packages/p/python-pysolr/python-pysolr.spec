#
# spec file for package python-pysolr
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
%define skip_python2 1
Name:           python-pysolr
Version:        3.8.1
Release:        0
Summary:        Lightweight python wrapper for Apache Solr
License:        BSD-3-Clause
URL:            https://github.com/django-haystack/pysolr/
Source:         https://files.pythonhosted.org/packages/source/p/pysolr/pysolr-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.9.1
Suggests:       python-kazoo >= 2.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.9.1}
# /SECTION
%python_subpackages

%description
Lightweight python wrapper for Apache Solr.

%prep
%setup -q -n pysolr-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# TODO, requires solr server to run

%files %{python_files}
%doc AUTHORS CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
