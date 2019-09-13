#
# spec file for package python-jupyter_contrib_core
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
%bcond_without tests
Name:           python-jupyter_contrib_core
Version:        0.3.3
Release:        0
Summary:        Common utilities for jupyter-contrib projects
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/jupyter-contrib/jupyter_contrib_core
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_contrib_core/jupyter_contrib_core-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with tests}
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module notebook >= 4.0}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module traitlets}
BuildRequires:  python-mock
%endif
Requires:       python-jupyter_core
Requires:       python-notebook >= 4.0
Requires:       python-setuptools
Requires:       python-tornado
Requires:       python-traitlets
Provides:       python-jupyter_contrib_core = %{version}
Obsoletes:      python-jupyter_contrib_core <= %{version}
Requires:       jupyter-jupyter_contrib_core = %{version}
BuildArch:      noarch

%python_subpackages

%description
Common utilities for jupyter-contrib projects. Includes:

-   providing a notebook-4.2-compatible nbextension API in order to
    smooth over differences in versions 4.0 and 4.1
-   common application components and cli scripts
-   utility classes and functions for use in tests

This package provides the python interface.

%package     -n jupyter-jupyter_contrib_core
Summary:        Libraries and Languages for Jupyter
Group:          Development/Languages/Python
Requires:       jupyter-jupyter_core
Requires:       jupyter-notebook >= 4.0
Requires:       python3-jupyter_contrib_core = %{version}

%description -n jupyter-jupyter_contrib_core
Common utilities for jupyter-contrib projects. Includes:

-   providing a notebook-4.2-compatible nbextension API in order to
    smooth over differences in versions 4.0 and 4.1
-   common application components and cli scripts
-   utility classes and functions for use in tests

This package provides the jupyter components.

%prep
%setup -q -n jupyter_contrib_core-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with tests}
%check
export LANG=en_US.UTF-8
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
nosetests-%{$python_bin_suffix}
}
%endif

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/jupyter_contrib_core/
%{python_sitelib}/jupyter_contrib_core-%{version}-py*.egg-info

%files -n jupyter-jupyter_contrib_core
%license LICENSE.txt
%{_bindir}/jupyter-contrib

%changelog
