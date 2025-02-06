#
# spec file for package python-jupyter-server-ydoc
#
# Copyright (c) 2025 SUSE LLC
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

%define distversion 1.1
Name:           python-jupyter-server-ydoc%{psuffix}
Version:        1.1.0
Release:        0
Summary:        Jupyter server extension integrating collaborative shared models
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/jupyter-collaboration
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_server_ydoc/jupyter_server_ydoc-%{version}.tar.gz
BuildRequires:  %{python_module hatchling >= 1.4.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  jupyter-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       jupyter-server-ydoc = %{version}
Requires:       python-jsonschema >= 4.18.0
Requires:       python-jupyter_events >= 0.10.0
Requires:       python-jupyter_server >= 2.11.1
Requires:       python-jupyter_server_fileid >= 0.7.0
Requires:       python-jupyter_ydoc >= 2.1.2
Requires:       python-pycrdt
Requires:       python-pycrdt-websocket >= 0.15.0
Provides:       python-jupyter_server_ydoc = %{version}-%{release}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module jupyter-server-ydoc-test = %{version}}
%endif
%python_subpackages

%description
jupyter-server extension integrating collaborative shared models.

The collaborative shared models are used for both:
- real time collaboration, and
- server-side execution of notebooks

%package -n jupyter-server-ydoc
Summary:        Jupyter server extension integrating collaborative shared models
Requires:       python3dist(jupyter-server-ydoc) = %{distversion}
Suggests:       python3-jupyter-server-ydoc = %{version}

%description -n jupyter-server-ydoc
jupyter-server extension integrating collaborative shared models.

The collaborative shared models are used for both:
- real time collaboration, and
- server-side execution of notebooks

This package provides the common jupyter configuration file.

%package test
Summary:        The jupyter_server_ydoc[test] extra
Requires:       python-anyio
Requires:       python-dirty-equals
Requires:       python-httpx-ws >= 0.5.2
Requires:       python-jupyter-server-fileid
Requires:       python-jupyter-server-test >= 2.11.1
Requires:       python-jupyter-server-ydoc = %{version}
Requires:       python-pytest >= 7.0
Requires:       (python-importlib_metadata >= 4.8.3 if python-base < 3.10)

%description test
Metapackage for the jupyter_server_ydoc[test] extra requirements

%prep
%autosetup -p1 -n jupyter_server_ydoc-%{version}

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/jupyter_server_ydoc
%{python_sitelib}/jupyter_server_ydoc-%{version}.dist-info

%files -n jupyter-server-ydoc
%license LICENSE
%doc README.md
%{_jupyter_config} %{_jupyter_server_confdir}/jupyter_collaboration.json

%files %{python_files test}
%license LICENSE
%doc README.md
%endif

%changelog
