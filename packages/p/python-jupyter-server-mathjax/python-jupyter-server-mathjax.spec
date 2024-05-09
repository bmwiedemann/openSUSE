#
# spec file for package python-jupyter-server-mathjax
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


Name:           python-jupyter-server-mathjax
Version:        0.2.6
Release:        0
Summary:        MathJax resources as a Jupyter Server Extension
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/jupyter-server/jupyter_server_mathjax
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_server_mathjax/jupyter_server_mathjax-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module jupyter-packaging >= 0.10 with %python-jupyter-packaging < 2}
BuildRequires:  %{python_module jupyter-server >= 1.1}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  python-rpm-macros
Requires:       jupyter-server-mathjax = %{version}
Requires:       python-jupyter_server >= 1.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module jupyter-server-test if %python-base >= 3.10}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
MathJax resources as a Jupyter Server Extension.

%package -n jupyter-server-mathjax
Summary:        MathJax resources as a Jupyter Server Extension -- configuration

%description -n jupyter-server-mathjax
MathJax resources as a Jupyter Server Extension.
This package contains the jupyter server extension configuration common
to all python flavors.

%prep
%autosetup -p1 -n jupyter_server_mathjax-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
cp %{buildroot}%{python3_sitelib}/jupyter_server_mathjax-%{version}.dist-info/LICENSE .
cp %{buildroot}%{python3_sitelib}/jupyter_server_mathjax/static/LICENSE LICENSE-STATIC
%jupyter_move_config

%check
export PYTHONDONTWRITEBYTECODE=1
%{python_expand # don't test anything on python39: no jupyter-server-test anymore
export PYTHONPATH=%{buildroot}%{$python_sitelib}
if [ ${python_flavor} != "python39" ]; then
  $python -m pytest -v --pyargs jupyter_server_mathjax
fi
}

%files %{python_files}
%license LICENSE LICENSE-STATIC
%{python_sitelib}/jupyter_server_mathjax
%{python_sitelib}/jupyter_server_mathjax-%{version}.dist-info

%files -n jupyter-server-mathjax
%license LICENSE LICENSE-STATIC
%_jupyter_config %{_jupyter_server_confdir}/jupyter_server_mathjax.json

%changelog
