#
# spec file for package python-qtconsole
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-qtconsole
Version:        5.4.1
Release:        0
Summary:        Jupyter Qt console
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/qtconsole
Source0:        https://files.pythonhosted.org/packages/source/q/qtconsole/qtconsole-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module jupyter-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gdb
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  update-desktop-files
# QtPy does note require or depend on one of the frameworks itself
Requires:       (python-qt5 or python-pyside2 or python-PyQt6 or python-pyside6)
Requires:       python-Pygments
Requires:       python-QtPy >= 2.0.1
Requires:       python-ipykernel >= 4.1
Requires:       python-ipython_genutils
Requires:       python-jupyter-client >= 4.1
Requires:       python-jupyter-core
Requires:       python-packaging
Requires:       python-pyzmq >= 17.1
Requires:       python-traitlets
Conflicts:      python-traitlets = 5.2.1
Conflicts:      python-traitlets = 5.2.2
Provides:       python-jupyter_qtconsole = %{version}
Obsoletes:      python-jupyter_qtconsole < %{version}
BuildArch:      noarch
%if "%{python_flavor}" == "%{primary_python}"
Provides:       jupyter-qtconsole = %{version}-%{release}
Obsoletes:      jupyter-qtconsole < %{version}-%{release}
%endif
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
# SECTION test requirements
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module QtPy >= 2.0.1}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module ipykernel >= 4.1}
BuildRequires:  %{python_module ipython_genutils}
BuildRequires:  %{python_module jupyter-client >= 4.1}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq >= 17.1}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module traitlets}
# /SECTION
%python_subpackages

%description
A rich Qt-based console for working with Jupyter kernels,
supporting rich media output, session export, and more.

%prep
%setup -q -n qtconsole-%{version}

%build
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/jupyter-qtconsole

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
%python_expand cp qtconsole/resources/icon/JupyterConsole.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/JupyterQtConsole-%{$python_bin_suffix}.svg

# Modify and install .desktop file
pushd examples
%{python_expand # clone desktop file for flavors
cp jupyter-qtconsole.desktop jupyter-qtconsole-%{$python_bin_suffix}.desktop
desktop-file-edit \
  --set-icon="JupyterQtConsole-%{$python_bin_suffix}" \
  --set-key=Exec --set-value="jupyter-qtconsole-%{$python_bin_suffix}" jupyter-qtconsole-%{$python_bin_suffix}.desktop
%suse_update_desktop_file -i -r jupyter-qtconsole-%{$python_bin_suffix} "System;TerminalEmulator;"
}
popd

%check
%pytest -ra

%pre
%python_libalternatives_reset_alternative jupyter-qtconsole

%post
%python_install_alternative jupyter-qtconsole

%postun
%python_uninstall_alternative jupyter-qtconsole

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/jupyter-qtconsole
%{_datadir}/applications/jupyter-qtconsole-%{python_bin_suffix}.desktop
%{_datadir}/icons/hicolor/scalable/apps/JupyterQtConsole-%{python_bin_suffix}.svg
%{python_sitelib}/qtconsole-%{version}*-info
%{python_sitelib}/qtconsole/

%changelog
