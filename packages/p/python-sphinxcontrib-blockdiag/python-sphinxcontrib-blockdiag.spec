#
# spec file for package python-sphinxcontrib-blockdiag
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
# Test files missing
%bcond_with     test
Name:           python-sphinxcontrib-blockdiag
Version:        1.5.5
Release:        0
Summary:        Sphinx "blockdiag" extension
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/blockdiag/sphinxcontrib-blockdiag
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-blockdiag/sphinxcontrib-blockdiag-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx >= 0.6}
BuildRequires:  %{python_module blockdiag >= 1.5.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 0.6
Requires:       python-blockdiag >= 1.5.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module funcparserlib}
BuildRequires:  %{python_module sphinx-testing}
BuildRequires:  python-mock
%endif
%python_subpackages

%description
A sphinx extension for embedding block diagram using blockdiag.

%prep
%setup -q -n sphinxcontrib-blockdiag-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/sphinxcontrib/blockdiag.py*
%pycache_only %{python_sitelib}/sphinxcontrib/__pycache__
%{python_sitelib}/sphinxcontrib_blockdiag-%{version}-py*-nspkg.pth
%{python_sitelib}/sphinxcontrib_blockdiag-%{version}-py*.egg-info

%changelog
