#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-nbclient%{psuffix}
Version:        0.7.2
Release:        0
Summary:        A client library for executing notebooks
License:        BSD-3-Clause
URL:            https://github.com/jupyter/nbclient
Source:         https://files.pythonhosted.org/packages/source/n/nbclient/nbclient-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling >= 1.10.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jupyter-client >= 6.1.12
Requires:       python-nbformat >= 5.1
Requires:       python-traitlets >= 5.3
Requires:       ((python-jupyter-core >= 4.12 with python-jupyter-core < 5) or python-jupyter-core >= 5.1)
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
%if %{with test}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module nbclient = %{version}}
BuildRequires:  %{python_module nbconvert >= 7}
BuildRequires:  %{python_module pytest >= 7}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module xmltodict}
%endif
%python_subpackages

%description
A client library for executing notebooks. Formally nbconvert's
ExecutePreprocessor.

NBClient is a tool for parameterizing andexecuting Jupyter Notebooks.

%prep
%setup -q -n nbclient-%{version}
sed -i 's/--color=yes//' pyproject.toml

%if ! %{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jupyter-execute
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export IPYKERNEL_CELL_NAME="<IPY-INPUT>"
# tests on parallel notebooks randomly fail (4 tests) - https://github.com/jupyter/nbclient/pull/74#issuecomment-635929953
donttest="parallel_notebooks"
# https://github.com/jupyter/nbclient/issues/189
donttest+=" or (test_run_all_notebooks and (opts6 or opts8 or opts9))"
# extra -v for more verbose error diffs
%pytest -v -k "not ($donttest)"
%endif

%if ! %{with test}
%pre
%python_libalternatives_reset_alternative jupyter-execute

%post
%python_install_alternative jupyter-execute

%postun
%python_uninstall_alternative jupyter-execute

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/jupyter-execute
%{python_sitelib}/nbclient
%{python_sitelib}/nbclient-%{version}.dist-info/
%endif

%changelog
