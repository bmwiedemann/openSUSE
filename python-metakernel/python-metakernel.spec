#
# spec file for package python-metakernel
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
Name:           python-metakernel
Version:        0.24.2
Release:        0
Summary:        Metakernel for Jupyter
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Calysto/metakernel
Source:         https://files.pythonhosted.org/packages/source/m/metakernel/metakernel-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipyparallel}
BuildRequires:  %{python_module pexpect >= 4.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  man
# /SECTION
Requires:       python-ipykernel
Requires:       python-ipyparallel
Requires:       python-pexpect >= 4.2
Provides:       python-jupyter_metakernel = %{version}
Obsoletes:      python-jupyter_metakernel < %{version}
BuildArch:      noarch
%ifpython3
Provides:       jupyter-metakernel = %{version}
%endif

%python_subpackages

%description
A Jupyter/IPython kernel template which includes core magic functions
(including help, command and file path completion, parallel and
distributed processing, downloads, and much more).

%prep
%setup -q -n metakernel-%{version}
touch ~/.bashrc

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/metakernel/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest metakernel/tests

%files %{python_files}
%doc CONTRIBUTORS.rst HISTORY.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
