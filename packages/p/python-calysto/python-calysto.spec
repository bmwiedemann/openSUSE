#
# spec file for package python-calysto
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
%define         skip_python2 1
%bcond_with     test
Name:           python-calysto
Version:        1.0.6
Release:        0
Summary:        Libraries and Languages for Jupyter
# The package license is listed as BSD-2-Clause but contains GPL-3.0 code for now, see https://github.com/Calysto/calysto/issues/11
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/Calysto/calysto
Source:         https://files.pythonhosted.org/packages/source/c/calysto/calysto-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       jupyter-calysto = %{version}
Requires:       python-CairoSVG
Requires:       python-ipython
Requires:       python-ipywidgets
Requires:       python-metakernel
Requires:       python-numpy
Requires:       python-svgwrite
Recommends:     python-Pillow
Recommends:     python-pexpect
Provides:       python-jupyter_calysto = %{version}
Obsoletes:      python-jupyter_calysto <= %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module CairoSVG}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module metakernel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module svgwrite}
%endif
%python_subpackages

%description
Libraries and Languages for Python and Jupyter.

This package provides the python interface.

%package     -n jupyter-calysto
Summary:        Libraries and Languages for Jupyter
Requires:       jupyter-ipython
Requires:       jupyter-ipywidgets
Requires:       jupyter-metakernel
Requires:       python3-calysto = %{version}

%description -n jupyter-calysto
Libraries and Languages for Python and Jupyter.

This package provides the jupyter components.

%prep
%setup -q -n calysto-%{version}

%build
%python_build

%install
%python_exec setup.py install -O1 --skip-build --force  --root=%{buildroot} --prefix=%{_prefix} --install-data=%{_datadir}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%files -n jupyter-calysto
%license LICENSE
%{_datadir}/calysto/

%changelog
