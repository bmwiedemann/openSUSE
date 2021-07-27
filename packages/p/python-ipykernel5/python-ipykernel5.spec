#
# spec file for package python-ipykernel
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%if %suse_version >= 1550
# python-ipykernel >= 6 provides the other flavors for python >= 3.7
%define         pythons python36
%else
%define skip_python2 1
%endif
Name:           python-ipykernel5
Version:        5.5.5
Release:        0
Summary:        IPython Kernel for Jupyter
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ipython/ipykernel
Source:         https://files.pythonhosted.org/packages/source/i/ipykernel/ipykernel-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  jupyter-jupyter_core-filesystem
BuildRequires:  python-rpm-macros
Requires:       python-ipython >= 5.0.0
Requires:       python-jupyter-client
Requires:       python-jupyter-core
Requires:       python-tornado >= 4.2
Requires:       python-traitlets >= 4.1.0
Provides:       python-ipykernel = %{version}-%{release}
Obsoletes:      python-ipykernel < %{version}-%{release}
Conflicts:      python-ipykernel >= 6
Provides:       python-jupyter_ipykernel = %{version}
Obsoletes:      python-jupyter_ipykernel < %{version}
Provides:       %{python_module ipykernel-doc = %{version}}
Obsoletes:      %{python_module ipykernel-doc < %{version}}
Provides:       %{python_module jupyter_ipykernel-doc = %{version}}
Obsoletes:      %{python_module jupyter_ipykernel-doc < %{version}}
Provides:       %{python_module jupyter-ipykernel-doc = %{version}}
Obsoletes:      %{python_module jupyter-ipykernel-doc < %{version}}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       jupyter-ipykernel = %{version}-%{release}
Obsoletes:      jupyter-ipykernel < %{version}-%{release}
%endif
%if "%{python_flavor}" == "python36"
# This shim is necessary until the python36-ipykernel = 5.5 binary requiring jupyter-ipykernel = 5.5 is wiped from the repositories
Provides:       jupyter-ipykernel = %{version}-%{release}
%endif
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module ipython >= 5.0.0}
BuildRequires:  %{python_module jupyter-client}
BuildRequires:  %{python_module jupyter-core}
BuildRequires:  %{python_module nose_warnings_filters}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tornado >= 4.2}
BuildRequires:  %{python_module traitlets >= 4.1.0}
BuildRequires:  %{python_module matplotlib if (%python-base without python36-base)}
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
# /SECTION
# typing is only built-in for later versions of python
%if 0%{?suse_version} <= 1320
BuildRequires:  %{python_module typing}
Requires:       python-typing
%endif
%python_subpackages

%description
This package provides the IPython kernel version 5 for Jupyter.
Version 5 is the last version to support Python 3.6

%prep
%autosetup -p1 -n ipykernel-%{version}

%build
%python_build

%install
%python_install
%if %suse_version >= 1550
%{python_expand # install kernelspecs for each flavor
PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -m ipykernel install \
    --prefix=%{buildroot}%{_prefix} \
    --name python%{$python_bin_suffix} \
    --display-name 'Python %{$python_bin_suffix} (ipykernel)'
}
# use the symlink for the default python3 flavor
sed -i "s|$(readlink -f %{__python3})|%{__python3}|" %{buildroot}%{_jupyter_kernel_dir}/python3/kernel.json
%endif
%python_expand %fdupes %{buildroot}%{$python_sitelib}


%check
# These tests expect jedi 0.17.2 return messages, but we use patches to support jedi 0.18 in ipython715
# and ipython 7.20 fixed its support for jedi 0.18 gh#ipython/ipykernel#578 gh#ipython/ipykernel#579
%pytest -ra -k "not (test_complete or test_inspect)"

%files %{python_files}
%doc README.md docs/changelog.rst
%license COPYING.md
%{python_sitelib}/ipykernel
%{python_sitelib}/ipykernel_launcher.py
%{python_sitelib}/ipykernel-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__/*.pyc
%if %suse_version >= 1550
%{_jupyter_kernel_dir}/python%{python_bin_suffix}
%endif
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
%{_jupyter_kernel_dir}/python3
%else
%exclude %{_jupyter_kernel_dir}/python3
%endif

%changelog
