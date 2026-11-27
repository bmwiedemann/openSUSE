#
# spec file for package python-jupyter-builder
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-jupyter-builder
Version:        1.3.0
Release:        0
Summary:        JupyterLab build tools
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/jupyter-builder
Source:         https://files.pythonhosted.org/packages/source/j/jupyter-builder/jupyter_builder-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatch-nodejs-version >= 0.3.2}
BuildRequires:  %{python_module hatchling >= 1.21.1}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
Requires(post): update-alternatives
Requires(postun): update-alternatives
# SECTION test requirements
BuildRequires:  %{python_module jupyter-core}
BuildRequires:  %{python_module traitlets}
BuildRequires:  %{python_module jinja2-time}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pytest >= 7.3}
BuildRequires:  %{python_module pytest-check-links >= 0.7}
# /SECTION
Requires:       python-jupyter-core
Requires:       python-traitlets
Suggests:       python-build
Suggests:       python-mypy
Suggests:       python-pre-commit
Suggests:       python-hatch
Suggests:       python-ruff == 0.17.3
Provides:       python-jupyter_builder = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
Build tools for JupyterLab extensions

%prep
%autosetup -p1 -n jupyter_builder-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jupyter-builder
%python_clone -a %{buildroot}%{_bindir}/jlpm
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# TODO: create copier package in order to run tests
#%%pytest
%{python_expand # import test
$python -c 'import jupyter_builder'
}

%post
%python_install_alternative jupyter-builder jlpm

%postun
%python_uninstall_alternative jupyter-builder

%files %{python_files}
%license LICENSE THIRD_PARTY_LICENSES/semver.LICENSE.txt THIRD_PARTY_LICENSES/yarn.js.LICENSE.txt THIRD_PARTY_LICENSES/yarn.js.third-party-licenses.json
%python_alternative %{_bindir}/jupyter-builder
%python_alternative %{_bindir}/jlpm
%{python_sitelib}/jupyter_builder
%{python_sitelib}/jupyter_builder-%{version}.dist-info

%changelog
