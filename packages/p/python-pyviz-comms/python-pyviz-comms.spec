#
# spec file for package python-pyviz-comms
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-pyviz-comms
Version:        2.2.1
Release:        0
Summary:        Tool to launch jobs, organize the output, and dissect the results
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pyviz/pyviz_comms
# For the bundled JS files
Source0:        https://files.pythonhosted.org/packages/source/p/pyviz_comms/pyviz_comms-%{version}.tar.gz
# For the tests
Source1:        https://github.com/holoviz/pyviz_comms/archive/refs/tags/v%{version}.tar.gz#/pyviz_comms-%{version}-gh.tar.gz
Source100:      python-pyviz-comms-rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-param
Provides:       python-pyviz_comms = %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module param}
# /SECTION
%python_subpackages

%description
PyViz-Comms offers a simple bidirectional communication architecture
for PyViz tools including support for Jupyter comms in both the
classic notebook and Jupyterlab.

%prep
%setup -q -n pyviz_comms-%{version}
tar -x -f %{SOURCE1} --strip-components=1 pyviz_comms-%{version}/pyviz_comms/tests/

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/pyviz_comms
%{python_sitelib}/pyviz_comms-%{version}.dist-info

%changelog
