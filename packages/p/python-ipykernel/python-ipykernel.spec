#
# spec file for package python-ipykernel
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
%define         skip_python2 1
Name:           python-ipykernel
Version:        5.3.0
Release:        0
Summary:        IPython Kernel for Jupyter
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ipython/ipykernel
Source:         https://files.pythonhosted.org/packages/source/i/ipykernel/ipykernel-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
Requires:       jupyter-ipykernel = %{version}
Requires:       python-ipython >= 5.0.0
Requires:       python-jupyter-client
Requires:       python-jupyter-core
Requires:       python-tornado >= 4.2
Requires:       python-traitlets >= 4.1.0
Provides:       python-jupyter_ipykernel = %{version}
Obsoletes:      python-jupyter_ipykernel < %{version}
Provides:       %{python_module ipykernel-doc = %{version}}
Obsoletes:      %{python_module ipykernel-doc < %{version}}
Provides:       %{python_module jupyter_ipykernel-doc = %{version}}
Obsoletes:      %{python_module jupyter_ipykernel-doc < %{version}}
Provides:       %{python_module jupyter-ipykernel-doc = %{version}}
Obsoletes:      %{python_module jupyter-ipykernel-doc < %{version}}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module ipython >= 5.0.0}
BuildRequires:  %{python_module jupyter-client}
BuildRequires:  %{python_module jupyter-core}
BuildRequires:  %{python_module nose_warnings_filters}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tornado >= 4.2}
BuildRequires:  %{python_module traitlets >= 4.1.0}
# /SECTION
# typing is only built-in for later versions of python
%if 0%{?suse_version} <= 1320
BuildRequires:  %{python_module typing}
Requires:       python-typing
%endif
%python_subpackages

%description
This package provides the IPython kernel for Jupyter.

This package provides the python interface.

%package     -n jupyter-ipykernel
Summary:        IPython Kernel for Jupyter
Group:          Development/Languages/Python
Requires:       hicolor-icon-theme
Requires:       jupyter-jupyter-client
Requires:       python3-ipykernel = %{version}
Conflicts:      python3-jupyter_ipykernel < 5.1.1

%description -n jupyter-ipykernel
This package provides the IPython kernel for Jupyter.

This package provides the jupyter components.

%prep
%autosetup -p1 -n ipykernel-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md docs/changelog.rst
%license COPYING.md
%{python_sitelib}/ipykernel
%{python_sitelib}/ipykernel_launcher.py
%{python_sitelib}/ipykernel-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__

%files -n jupyter-ipykernel
%license COPYING.md
%{_jupyter_kernel_dir}/python3/

%changelog
