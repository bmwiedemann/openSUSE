#
# spec file for package python-sphinxcontrib-asyncio
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_with     test
Name:           python-sphinxcontrib-asyncio
Version:        0.2.0
Release:        0
Summary:        Sphinx extension to support coroutines in markup
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/aio-libs/sphinxcontrib-asyncio
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-asyncio/sphinxcontrib-asyncio-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
Requires:       python-Sphinx
BuildArch:      noarch

%python_subpackages

%description
Sphinx extension for adding asyncio-specific markups

%prep
%setup -q -n sphinxcontrib-asyncio-%{version}

%build
%python_build
pushd docs
PYTHONPATH=.. make html
rm _build/html/.buildinfo
popd

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Remove sphinxcontrib namespace package files provided by python-Sphinx
%python_expand rm -f %{buildroot}%{$python_sitelib}/sphinxcontrib/__init__.py*
%python_expand rm -f %{buildroot}%{$python_sitelib}/sphinxcontrib/__pycache__/__init__*.py*

%files %{python_files}
%doc CHANGES.rst README.rst docs/_build/html
%{python_sitelib}/sphinxcontrib/asyncio.py*
%pycache_only %dir %{python_sitelib}/sphinxcontrib/__pycache__/
%pycache_only %{python_sitelib}/sphinxcontrib/__pycache__/asyncio*.py*
%{python_sitelib}/sphinxcontrib_asyncio-%{version}-py*.egg-info

%changelog
