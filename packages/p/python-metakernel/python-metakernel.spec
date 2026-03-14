#
# spec file for package python-metakernel
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-metakernel
Version:        0.32.0
Release:        0
Summary:        Metakernel for Jupyter
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Calysto/metakernel
Source:         https://files.pythonhosted.org/packages/source/m/metakernel/metakernel-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-comm > 0.1.0
Requires:       python-ipykernel >= 5.5.6
Requires:       python-jedi >= 0.18
Requires:       python-jupyter-core >= 4.9.2
Requires:       python-pexpect >= 4.8
Recommends:     python-ipyparallel
Recommends:     python-portalocker
Provides:       python-jupyter_metakernel = %{version}
Obsoletes:      python-jupyter_metakernel < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ipykernel >= 5.5.6}
BuildRequires:  %{python_module comm >= 0.1.0}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module jupyter-core >= 4.9.2}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module pexpect >= 4.8}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  coreutils-doc
BuildRequires:  man
# /SECTION
%if "%{python_flavor}" == "python3" || "%{?python_provides}"  == "python3"
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
sed -i '1{/env python/d}' tests/test_expect.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/metakernel
%{python_sitelib}/metakernel-%{version}.dist-info

%changelog
