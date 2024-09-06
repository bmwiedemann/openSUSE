#
# spec file for package python-rank-bm25
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
Name:           python-rank-bm25
Version:        0.2.2
Release:        0
Summary:        Various BM25 algorithms for document ranking
License:        Apache-2.0
URL:            https://github.com/dorianbrown/rank_bm25
Group:          Development/Libraries/Python
Source0:        https://files.pythonhosted.org/packages/source/r/rank-bm25/rank_bm25-%{version}.tar.gz
Source1:        https://github.com/dorianbrown/rank_bm25/archive/refs/tags/%{version}.tar.gz#/rank-bm25-%{version}-gh.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module numpy} 
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  %{python_module pytest} 
Requires:       python-numpy 
BuildArch:      noarch
%python_subpackages

%description
Rank-BM25: A two line search engine
A collection of algorithms for querying a set of documents and returning the ones most relevant to the query. The most common use case for these algorithms is, as you might have guessed, to create search engines.

%prep
%autosetup -p1 -n rank_bm25-%{version}
# version.py and tests are not included in the tarball from pypi
(cd ..; tar xf %{SOURCE1} rank_bm25-%{version}/{version.py,tests})
# Fix non-executable scripts
sed -i "s|^#!.*||" rank_bm25.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%license LICENSE
%{python_sitelib}/rank_bm25.*
%{python_sitelib}/rank_bm25-%{version}.dist-info
%pycache_only %{python_sitelib}/__pycache__/*.pyc
%changelog
