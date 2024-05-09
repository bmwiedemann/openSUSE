#
# spec file for package python-jupyterlab-pygments
#
# Copyright (c) 2024 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%define skip_python39 1
%else
%define psuffix %{nil}
%bcond_with test
%endif

%define distversion 0.3
Name:           python-jupyterlab-pygments%{psuffix}
Version:        0.3.0
Release:        0
Summary:        Pygments theme for jupyterlab
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyterlab/jupyterlab_pygments
Source:         https://files.pythonhosted.org/packages/source/j/jupyterlab-pygments/jupyterlab_pygments-%{version}.tar.gz
# Slightly modified from https://github.com/jupyterlab/jupyterlab_pygments/blob/0.2.2/notebooks/Example.ipynb
Source1:        Example.ipynb
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatch-jupyter-builder}
BuildRequires:  %{python_module hatch-nodejs-version}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       jupyter-jupyterlab-pygments = %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module jupyterlab-pygments = %{version}}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
This package contains a syntax coloring theme for pygments making use
of the JupyterLab CSS variables.

%package -n jupyter-jupyterlab-pygments
Summary:        Pygments theme for jupyterlab -- Jupyterlab extension files
Requires:       python3dist(jupyterlab-pygments) = %{distversion}

%description -n jupyter-jupyterlab-pygments
This package contains the Jupyterlab extension files for python-jupyterlab-pygments

%prep
%autosetup -p1 -n jupyterlab_pygments-%{version}

%build
%{pyproject_wheel}

%if !%{with test}
%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
find %{buildroot}%{_prefix} -path '*/site-packages/jupyterlab_pygments-%{version}.dist-info/licenses/LICENSE' -exec cp {} . ';' -quit
%endif

%if %{with test}
%check
%pytest --nbval-lax %{SOURCE1}
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%{python_sitelib}/jupyterlab_pygments
%{python_sitelib}/jupyterlab_pygments-%{version}.dist-info

%files -n jupyter-jupyterlab-pygments
%{_jupyter_labextensions_dir3}/jupyterlab_pygments
%endif

%changelog
