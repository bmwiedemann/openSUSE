#
# spec file for package python-qtconsole
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
Name:           python-qtconsole
Version:        4.5.2
%define doc_ver 4.5.1
Release:        0
Summary:        Jupyter Qt console
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jupyter/qtconsole
Source0:        https://files.pythonhosted.org/packages/source/q/qtconsole/qtconsole-%{version}.tar.gz
Source1:        https://media.readthedocs.org/pdf/qtconsole/%{doc_ver}/qtconsole.pdf
Source2:        https://media.readthedocs.org/htmlzip/qtconsole/%{doc_ver}/qtconsole.zip
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  %{python_module setuptools}
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  update-desktop-files
Requires:       python-Pygments
Requires:       python-ipykernel >= 4.1
Requires:       python-ipython_genutils
Requires:       python-jupyter_client >= 4.1
Requires:       python-jupyter_core
Requires:       python-sip
Requires:       python-traitlets
Provides:       python-jupyter_qtconsole = %{version}
Obsoletes:      python-jupyter_qtconsole < %{version}
Requires:       jupyter-qtconsole = %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module ipykernel >= 4.1}
BuildRequires:  %{python_module ipython_genutils}
BuildRequires:  %{python_module jupyter_client >= 4.1}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module sip}
BuildRequires:  %{python_module traitlets}
# /SECTION

%python_subpackages

%description
A rich Qt-based console for working with Jupyter kernels,
supporting rich media output, session export, and more.

This package provides the python components.

%package     -n jupyter-qtconsole
Summary:        Jupyter Qt console
Requires:       python3-qtconsole = %{version}
Requires:       jupyter-ipykernel >= 4.1
Requires:       jupyter-jupyter_client >= 4.1
Requires:       jupyter-jupyter_core
Conflicts:      python3-jupyter_qtconsole < 4.4.4

%description -n jupyter-qtconsole
A rich Qt-based console for working with Jupyter kernels,
supporting rich media output, session export, and more.

This package provides the jupyter components.

%package     -n jupyter-qtconsole-doc
Summary:        Documentation for the Jupyter Qt console
Group:          Documentation/Other
Provides:       python-qtconsole-doc = %{version}
Provides:       %{python_module qtconsole-doc = %{version}}
Provides:       %{python_module jupyter_qtconsole-doc = %{version}}
Obsoletes:      %{python_module jupyter_qtconsole-doc < %{version}}

%description -n jupyter-qtconsole-doc
Documentation and help files for Jupyter's Qt console.

%prep
%setup -q -n qtconsole-%{version}
cp %{SOURCE1} .
unzip %{SOURCE2} -d docs
mv docs/qtconsole-* docs/html
rm docs/html/.buildinfo

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

mkdir -p %{buildroot}%{_docdir}/jupyter-qtconsole

cp %{SOURCE1} %{buildroot}%{_docdir}/jupyter-qtconsole/
cp -r docs/html %{buildroot}%{_docdir}/jupyter-qtconsole/

%fdupes %{buildroot}%{_docdir}/jupyter-qtconsole/

%check
rm -rf build _build.*
%python_expand pytest-%{$python_bin_suffix}

%files %{python_files}
%license LICENSE
%{python_sitelib}/qtconsole-%{version}-py*.egg-info
%{python_sitelib}/qtconsole/

%files -n jupyter-qtconsole
%license LICENSE
%{_bindir}/jupyter-qtconsole
%{_datadir}/applications/jupyter-qtconsole.desktop
%{_datadir}/icons/hicolor/scalable/apps/JupyterQtConsole.svg

%files -n jupyter-qtconsole-doc
%license LICENSE
%dir %{_docdir}/jupyter-qtconsole/
%{_docdir}/jupyter-qtconsole/qtconsole.pdf
%{_docdir}/jupyter-qtconsole/html

%changelog
