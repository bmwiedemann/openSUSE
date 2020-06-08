#
# spec file for package python-pyviz-comms
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-pyviz-comms
Version:        0.7.4
Release:        0
Summary:        Tool to launch jobs, organize the output, and dissect the results
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pyviz/pyviz_comms
Source0:        https://files.pythonhosted.org/packages/source/p/pyviz-comms/pyviz_comms-%{version}.tar.gz
Source100:      python-pyviz-comms-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module param >= 1.6.0}
# /SECTION
Requires:       python-param >= 1.6.0
BuildArch:      noarch

%python_subpackages

%description
PyViz-Comms offers a simple bidirectional communication architecture
for PyViz tools including support for Jupyter comms in both the
classic notebook and Jupyterlab.

%prep
%setup -q -n pyviz_comms-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/*

%changelog
