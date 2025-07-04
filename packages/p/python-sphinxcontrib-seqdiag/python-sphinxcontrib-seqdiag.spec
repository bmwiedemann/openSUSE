#
# spec file for package python-sphinxcontrib-seqdiag
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


%bcond_with     test
Name:           python-sphinxcontrib-seqdiag
Version:        3.0.0
Release:        0
Summary:        Sphinx "seqdiag" extension
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/blockdiag/sphinxcontrib-seqdiag
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-seqdiag/sphinxcontrib-seqdiag-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx >= 0.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 0.6
Requires:       python-blockdiag >= 1.5.0
Requires:       python-seqdiag >= 0.9.3
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module blockdiag >= 1.5.0}
BuildRequires:  %{python_module seqdiag >= 0.9.3}
%endif
%python_subpackages

%description
A sphinx extension for embedding sequence diagram using seqdiag_.

This extension enables you to insert sequence diagrams into your document.

%prep
%setup -q -n sphinxcontrib-seqdiag-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# remove tests/ dir from global site-packages
%{python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
%fdupes %{buildroot}%{$python_sitelib}
}

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/sphinxcontrib/seqdiag.py*
%pycache_only %{python_sitelib}/sphinxcontrib/__pycache__
%{python_sitelib}/sphinxcontrib_seqdiag-%{version}-py*-nspkg.pth
%{python_sitelib}/sphinxcontrib_seqdiag-%{version}*-info

%changelog
