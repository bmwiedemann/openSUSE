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

Name:           python-jupyter-server%{psuffix}
Version:        2.0.6
Release:        0
Summary:        The backend to Jupyter web applications
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://jupyter-server.readthedocs.io
# SourceRepository: https://github.com/jupyter-server/jupyter_server
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_server/jupyter_server-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatch-jupyter-builder >= 0.8.1}
BuildRequires:  %{python_module hatchling >= 1.11}
BuildRequires:  %{python_module pip}
# We need the full stdlib
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python >= 3.8
Requires:       python-Jinja2
Requires:       python-Send2Trash
Requires:       python-argon2-cffi
Requires:       python-jupyter-client >= 7.4.4
Requires:       python-jupyter_events >= 0.4.0
Requires:       python-jupyter_server_terminals
Requires:       python-nbconvert >= 6.4.4
Requires:       python-nbformat >= 5.3.0
Requires:       python-packaging
Requires:       python-prometheus_client
Requires:       python-pyzmq >= 24
Requires:       python-terminado >= 0.8.3
Requires:       python-tornado >= 6.2
Requires:       python-traitlets >= 5.6
Requires:       python-websocket-client
Requires:       ((python-jupyter-core >= 4.12 with python-jupyter-core < 5.0) or python-jupyter-core >= 5.1)
Requires:       (python-anyio >= 3.1.0 with python-anyio < 4)
Provides:       python-jupyter_server = %{version}-%{release}
Obsoletes:      python-jupyter_server < %{version}-%{release}
%if %{with test}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module jupyter-server-test = %{version}}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xdist}
%endif
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       jupyter-jupyter-server = %{version}-%{release}
Obsoletes:      jupyter-jupyter-server < %{version}-%{release}
BuildArch:      noarch
%endif
%python_subpackages

%description
The Jupyter Server is a web application that allows you to create and
share documents that contain live code, equations, visualizations, and
explanatory text. The Notebook has support for multiple programming
languages, sharing, and interactive widgets.

%package test
Summary:        The backend to Jupyter web applications - test requirements
Group:          Development/Languages/Python
Requires:       python-ipykernel
Requires:       python-jupyter-server = %{version}
Requires:       python-pytest >= 7
Requires:       python-pytest-console-scripts
Requires:       python-pytest-jupyter-server >= 0.4
Requires:       python-pytest-timeout
Requires:       python-requests

%description test
Metapackage for the jupyter_server[test] requirement specifier

%prep
%setup -q -n jupyter_server-%{version}
sed -i pyproject.toml \
  -e 's/--color=yes//' \
  -e '/filterwarnings/,/]/ {/error/ a \  "ignore:Module already imported so cannot be rewritten",
                           }'

%if ! %{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a  %{buildroot}%{_bindir}/jupyter-server
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export LANG=en_US.UTF-8
if [ -e ~/.local/share/jupyter ]; then
    echo "WARNING: Not a clean test environment."
    echo "You might need to delete ~/.local/share/jupyter in order to avoid test failures."
fi
# pytest-xdist for process control so that the worker does not indefinitely hang after success, no parallel tests
%pytest --timeout 60 --force-flaky --max-runs=3 --no-flaky-report -n 1
%endif

%if ! %{with test}
%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative jupyter-server

%post
%python_install_alternative jupyter-server

%postun
%python_uninstall_alternative jupyter-server

%files %{python_files}
%doc README.md
%license COPYING.md
%python_alternative %{_bindir}/jupyter-server
%{python_sitelib}/jupyter_server
%{python_sitelib}/jupyter_server-%{version}*-info

%files %{python_files test}
%license COPYING.md
%endif

%changelog
