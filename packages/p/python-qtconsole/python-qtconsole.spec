#
# spec file for package python-qtconsole
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-qtconsole
Version:        4.7.7
Release:        0
Summary:        Jupyter Qt console
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/qtconsole
Source0:        https://files.pythonhosted.org/packages/source/q/qtconsole/qtconsole-%{version}.tar.gz
Source100:      python-qtconsole-rpmlintrc
BuildRequires:  %{python_module jupyter-core}
BuildRequires:  %{python_module setuptools}
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gdb
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  update-desktop-files
Requires:       jupyter-qtconsole = %{version}
Requires:       python-Pygments
Requires:       python-QtPy
Requires:       python-ipykernel >= 4.1
Requires:       python-ipython_genutils
Requires:       python-jupyter-client >= 4.1
Requires:       python-jupyter-core
Requires:       python-traitlets
Provides:       python-jupyter_qtconsole = %{version}
Obsoletes:      python-jupyter_qtconsole < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module QtPy}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module ipykernel >= 4.1}
BuildRequires:  %{python_module ipython_genutils}
BuildRequires:  %{python_module jupyter-client >= 4.1}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module traitlets}
# /SECTION
%python_subpackages

%description
A rich Qt-based console for working with Jupyter kernels,
supporting rich media output, session export, and more.

This package provides the python components.

%package     -n jupyter-qtconsole
Summary:        Jupyter Qt console
Group:          Development/Languages/Python
Requires:       jupyter-ipykernel >= 4.1
Requires:       jupyter-jupyter-client >= 4.1
Requires:       jupyter-jupyter-core
Requires:       python3-jupyter-core
Requires:       python3-qtconsole = %{version}
Conflicts:      python3-jupyter_qtconsole < 4.4.4
Provides:       jupyter-qtconsole-doc = %{version}
Obsoletes:      jupyter-qtconsole-doc < %{version}
Provides:       %{python_module jupyter_qtconsole-doc = %{version}}
Provides:       %{python_module qtconsole-doc = %{version}}
Provides:       python-qtconsole-doc = %{version}
Obsoletes:      %{python_module jupyter_qtconsole-doc < %{version}}

%description -n jupyter-qtconsole
A rich Qt-based console for working with Jupyter kernels,
supporting rich media output, session export, and more.

This package provides the jupyter components.

%prep
%setup -q -n qtconsole-%{version}

%build
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp qtconsole/resources/icon/JupyterConsole.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/JupyterQtConsole.svg

# Modify and install .desktop file
pushd examples
desktop-file-edit --set-icon="JupyterQtConsole" jupyter-qtconsole.desktop
%suse_update_desktop_file -i -r jupyter-qtconsole "System;TerminalEmulator;"
popd

%python_clone -a %{buildroot}%{_bindir}/jupyter-qtconsole

%check
export QT_QPA_PLATFORM="offscreen"
# test skips: https://github.com/jupyter/qtconsole/issues/443
%pytest -k "not (test_00 and (test_scroll or test_debug))"

%post -n jupyter-qtconsole
%python_install_alternative jupyter-qtconsole

%postun -n jupyter-qtconsole
%python_uninstall_alternative jupyter-qtconsole

%files %{python_files}
%license LICENSE
%{python_sitelib}/qtconsole-%{version}-py*.egg-info
%{python_sitelib}/qtconsole/

%files -n jupyter-qtconsole
%license LICENSE
%python_alternative %{_bindir}/jupyter-qtconsole
%{_datadir}/applications/jupyter-qtconsole.desktop
%{_datadir}/icons/hicolor/scalable/apps/JupyterQtConsole.svg

%changelog
