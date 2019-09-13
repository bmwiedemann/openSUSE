#
# spec file for package python2-ipykernel
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
%define         skip_python3 1
%define         oldpython python
Name:           python2-ipykernel
Version:        4.10.1
Release:        0
Summary:        Python 2 IPython Kernel for Jupyter
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ipython/ipykernel
Source:         https://files.pythonhosted.org/packages/source/i/ipykernel/ipykernel-%{version}.tar.gz
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module ipython >= 4.0.0}
BuildRequires:  %{python_module jupyter_client}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado >= 4.0}
BuildRequires:  %{python_module traitlets >= 4.1.0}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       jupyter-ipykernel-python2 = %{version}
Requires:       hicolor-icon-theme
Requires:       python-certifi
Requires:       python-ipython >= 4.0.0
Requires:       python-jupyter_client
Requires:       python-tornado >= 4.0
Requires:       python-traitlets >= 4.1.0
Requires:       python-typing
Provides:       %{oldpython}-jupyter_ipykernel = %{version}
Obsoletes:      %{oldpython}-jupyter_ipykernel < %{version}
Provides:       python-jupyter_ipykernel = %{version}
Obsoletes:      python-jupyter_ipykernel < %{version}
Provides:       python2-jupyter_ipykernel = %{version}
Obsoletes:      python2-jupyter_ipykernel < %{version}
Provides:       %{oldpython}-ipykernel = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module nose_warnings_filters}
BuildRequires:  %{python_module nose}
BuildRequires:  python-mock
BuildRequires:  python-typing
# /SECTION

%python_subpackages

%description
This package provides the python2 IPython kernel
for Jupyter.

This package provides the python interface and
the jupyter components.

%package     -n jupyter-ipykernel-python2
Summary:        Python 2 IPython Kernel for Jupyter
Requires:       hicolor-icon-theme
Requires:       jupyter-jupyter_client
Requires:       python2-ipykernel = %{version}
Conflicts:      python2-jupyter_ipykernel < 4.10.1

%description -n jupyter-ipykernel-python2
This package provides the python2 IPython kernel
for Jupyter.

This package provides the jupyter components.

%prep
%setup -q -n ipykernel-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
nosetests-%{$python_bin_suffix}
}

%files %{python_files}
%license COPYING.md
%{python_sitelib}/*
%{_jupyter_kernel_dir}/python2/

%files -n jupyter-ipykernel-python2
%license COPYING.md
%{_jupyter_kernel_dir}/python2/

%changelog
