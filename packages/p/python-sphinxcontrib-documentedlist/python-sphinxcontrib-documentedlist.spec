#
# spec file for package python-sphinxcontrib-documentedlist
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
Name:           python-sphinxcontrib-documentedlist
Version:        0.6
Release:        0
Summary:        Sphinx DocumentedList extension
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/chintal/sphinxcontrib-documentedlist
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-documentedlist/sphinxcontrib-documentedlist-%{version}.tar.gz
# https://github.com/sphinx-contrib/documentedlist/issues/5
Patch0:         python-sphinxcontrib-documentedlist-no-six.patch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 0.6
Requires:       python-six
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module six}
%endif
%python_subpackages

%description
Sphinx extension to convert a Python list into a table in the generated
documentation. The intended application of this extension is to document
the items of essentially list-like objects of immutable data (possibly
enums, though python 3.4 enums are not supported yet).

In the source code, each list item, instead of being just its native
data type, should be replaced by a tuple of two elements. In the
simplest application, the second element of the tuple should be a string
providing a description for the item.

%prep
%autosetup -p1 -n sphinxcontrib-documentedlist-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%{python_sitelib}/sphinxcontrib/documentedlist.py*
%pycache_only %{python_sitelib}/sphinxcontrib/__pycache__
%{python_sitelib}/sphinxcontrib_documentedlist-%{version}-py*-nspkg.pth
%{python_sitelib}/sphinxcontrib_documentedlist-%{version}*-info

%changelog
