#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%if 0%{suse_version} <= 1500 && 0%{?sle_version} <= 150300
# The requirements are not available in the correct versions
# remove this if you see the :flavor build succeeding
ExclusiveArch: donotbuild
%endif
%endif

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?!python_module:%define python_module() python3-%{**}}
%define         skip_python2 1
Name:           python-nbclient%{psuffix}
Version:        0.5.9
Release:        0
Summary:        A client library for executing notebooks
License:        BSD-3-Clause
URL:            https://github.com/jupyter/nbclient
Source:         https://files.pythonhosted.org/packages/source/n/nbclient/nbclient-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 38.6.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?python_version_nodots} < 37
Requires:       python-async_generator
%endif
Requires:       python-jupyter-client >= 6.1.5
Requires:       python-nbformat >= 5.0
Requires:       python-nest-asyncio
Requires:       python-traitlets >= 4.2
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module async_generator if %python-base < 3.7}
BuildRequires:  %{python_module ipython}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module jupyter-client >= 6.1.5}
BuildRequires:  %{python_module nbconvert}
BuildRequires:  %{python_module nbformat >= 5.0}
BuildRequires:  %{python_module nest-asyncio}
BuildRequires:  %{python_module pytest >= 4.1}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module traitlets >= 4.2}
BuildRequires:  %{python_module xmltodict}
%endif
%python_subpackages

%description
A client library for executing notebooks. Formally nbconvert's
ExecutePreprocessor.

NBClient is a tool for parameterizing andexecuting Jupyter Notebooks.

%prep
%setup -q -n nbclient-%{version}

%build
%python_build

%if ! %{with test}
%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/jupyter-execute
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export IPYKERNEL_CELL_NAME="<IPY-INPUT>"
# tests on parallel notebooks randomly fail (4 tests) - https://github.com/jupyter/nbclient/pull/74#issuecomment-635929953
%pytest -k 'not parallel_notebooks'
%endif

%if ! %{with test}
%pre
%python_libalternatives_reset_alternative jupyter-execute

%post
%python_install_alternative jupyter-execute

%postun
%python_uninstall_alternative jupyter-execute

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/jupyter-execute
%{python_sitelib}/nbclient
%{python_sitelib}/nbclient-%{version}*-info/
%endif

%changelog
