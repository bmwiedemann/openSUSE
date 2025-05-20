#
# spec file for package python-contexter
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


Name:           python-contexter
Version:        0.1.4
Release:        0
Summary:        A replacement of the contextlib module
License:        MIT
Group:          Development/Languages/Python
URL:            https://bitbucket.org/defnull/contexter
Source:         https://files.pythonhosted.org/packages/source/c/contexter/contexter-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Contexter is a full replacement of the contextlib standard library
module.

%prep
%setup -q -n contexter-%{version}
# Remove executable bits
rm -r *egg-info*
chmod a-x README.rst

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%{python_sitelib}/contexter.py
%{python_sitelib}/contexter-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/contexter*

%changelog
