#
# spec file for package python-notebook
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
%else
%define psuffix %{nil}
%bcond_with test
BuildArch:      noarch
%endif

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-notebook%{psuffix}
Version:        7.3.1
Release:        0
Summary:        Jupyter Notebook interface
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/notebook
Source0:        https://files.pythonhosted.org/packages/source/n/notebook/notebook-%{version}.tar.gz
Source100:      python-notebook-rpmlintrc
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module hatch-jupyter-builder >= 0.2}
BuildRequires:  %{python_module hatchling >= 1.11}
BuildRequires:  %{python_module jupyterlab >= 4.3.2 with %python-jupyterlab < 4.4}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros >= 20210929
Requires:       jupyter-notebook = %{version}
Requires:       python-tornado >= 6.2
Requires:       (python-jupyter-server >= 2.4 with python-jupyter-server < 3)
Requires:       (python-jupyterlab >= 4.3.2 with python-jupyterlab < 4.4)
Requires:       (python-jupyterlab-server >= 2.27.1 with python-jupyterlab-server < 3)
Requires:       (python-notebook-shim >= 0.2 with python-notebook-shim < 0.3)
Provides:       python-jupyter_notebook = %{version}-%{release}
Obsoletes:      python-jupyter_notebook < %{version}-%{release}
%if !%{with test}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  jupyter-notebook-filesystem
BuildRequires:  update-desktop-files
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%endif
%if %{with test}
BuildRequires:  %{python_module importlib_resources >= 5 if %python-base < 3.10}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module jupyter-server-test >= 2.4.0 with %python-jupyter-server-test < 3}
BuildRequires:  %{python_module jupyterlab-server-test >= 2.27.1 with %python-jupyterlab-server-test < 3}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module notebook = %{version}}
BuildRequires:  %{python_module pytest >= 7.0}
BuildRequires:  %{python_module pytest-console-scripts}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-tornasync}
BuildRequires:  %{python_module requests}
%endif
%python_subpackages

%description
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package provides the python interface.

%package     -n jupyter-notebook
Summary:        Jupyter Notebook interface
Group:          Development/Languages/Python
Requires:       python3dist(notebook) = %{version}
Suggests:       python3-notebook = %{version}
Conflicts:      python3-jupyter_notebook < 5.7.8
Provides:       jupyter-notebook-doc = %{version}
Obsoletes:      jupyter-notebook-doc < %{version}

%description -n jupyter-notebook
The Jupyter HTML notebook is a web-based notebook environment for
interactive computing.

This package provides the jupyter components.

%prep
%autosetup -p1 -n notebook-%{version}
# We don't want to run selenium tests
rm -rf notebook/tests/selenium
sed -i 's/"--color=yes", //' pyproject.toml

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
rm %{buildroot}%{_jupyter_lab_dir}/schemas/@jupyter-notebook/*/package.json.orig
rm %{buildroot}%{_jupyter_labextensions_dir3}/@jupyter-notebook/lab-extension/schemas/@jupyter-notebook/lab-extension/package.json.orig
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/jupyter-notebook
%python_group_libalternatives jupyter-notebook
%suse_update_desktop_file jupyter-notebook
%endif

%if %{with test}
%check
export LANG=en_US.UTF-8
# test_launch_socket_collision: fails because there are still servers listening
pythonall_donttest="test_launch_socket_collision"
%{python_expand # these tests call the wrong interpreter somewhere deep in the stack
if [ "$python_" != "python3_" -a "%{$python_provides}" != "python3" ]; then
  python_$python_donttest+=" or (test_kernels_api and (test_connection or test_culling))"
fi
}
%pytest -v -k "not (${pythonall_donttest} ${python_$python_donttest})"
%endif

%if !%{with test}
%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative jupyter-notebook

%post
%python_install_alternative jupyter-notebook

%postun
%python_uninstall_alternative jupyter-notebook

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/jupyter-notebook
%{python_sitelib}/notebook-%{version}.dist-info
%{python_sitelib}/notebook/

%files -n jupyter-notebook
%license LICENSE
%{_datadir}/icons/hicolor/scalable/apps/notebook.svg
%{_datadir}/applications/jupyter-notebook.desktop
%dir %{_jupyter_lab_dir}/schemas
%{_jupyter_lab_dir}/schemas/@jupyter-notebook
%{_jupyter_labextensions_dir3}/@jupyter-notebook
%{_jupyter_config} %{_jupyter_server_confdir}/notebook.json
%endif

%changelog
