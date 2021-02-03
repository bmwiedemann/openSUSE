#
# spec file for package python-spyder-notebook
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


# Not really singlespec: Spyder is an app only for the primary python3 interpreter
# But we need the python3-spyder-notebook name, provided by the python_subpackages rewrite
%define pythons python3
Name:           python-spyder-notebook
Version:        0.3.2
Release:        0
Summary:        Jupyter notebook integration with Spyder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spyder-ide/spyder-notebook
# We need the bundled JavaScript stuff from the PyPI archive ...
Source0:        https://files.pythonhosted.org/packages/source/s/spyder-notebook/spyder-notebook-%{version}.tar.gz
# ... but only the GitHub archive provides the unit tests
Source1:        https://github.com/spyder-ide/spyder-notebook/archive/v%{version}.tar.gz#/spyder-notebook-%{version}-gh.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python-QtPy
Requires:       python-nbformat
Requires:       python-notebook >= 4.3
Requires:       python-psutil
Requires:       python-requests
Requires:       spyder >= 4.1
Provides:       spyder-notebook = %{version}-%{release}
Obsoletes:      spyder-notebook < %{version}-%{release}
Provides:       spyder3-notebook = %{version}-%{release}
Obsoletes:      spyder3-notebook < %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  python3-QtPy
BuildRequires:  python3-flaky
BuildRequires:  python3-nbformat
BuildRequires:  python3-notebook
BuildRequires:  python3-opengl
BuildRequires:  python3-psutil
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-qt
BuildRequires:  python3-pytest-xvfb
BuildRequires:  python3-requests
BuildRequires:  spyder >= 4.1
BuildRequires:  xdpyinfo
# /SECTION
%python_subpackages

%description
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to control
breakpoints.

%prep
%setup -q -n spyder-notebook-%{version}
tar --strip-components=1 -xzf %{SOURCE1} \
    spyder-notebook-%{version}/spyder_notebook/server/test.ipynb \
    spyder-notebook-%{version}/spyder_notebook/tests \
    spyder-notebook-%{version}/spyder_notebook/utils/tests \
    spyder-notebook-%{version}/spyder_notebook/widgets/tests
sed -i 's/\r$//' CHANGELOG.md README.md
chmod -x spyder_notebook/utils/templates/welcome-dark.html

%build
%python3_build

%install
%python3_install
%find_lang spyder_notebook
%fdupes %{buildroot}%{python3_sitelib}

%check
# The unittests fail with a seccomp-bpf crash if the sandbox
# is not disabled on i586
export QTWEBENGINE_DISABLE_SANDBOX=1
# import from source for test modules
export PYTHONPATH=":x"
# test_plugin::test_shutdown_notebook_kernel: session request is always empty
# rest of deselected test_plugin tests: passing but produces XIO errors with xvfb at the end
%pytest -k "not (test_plugin and (shutdown or register or close or save))"

%files %{python_files} -f spyder_notebook.lang
%doc CHANGELOG.md README.md
%license LICENSE
%dir %{python_sitelib}/spyder_notebook
%dir %{python_sitelib}/spyder_notebook/locale
%dir %{python_sitelib}/spyder_notebook/locale/*
%dir %{python_sitelib}/spyder_notebook/locale/*/LC_MESSAGES
%{python_sitelib}/spyder_notebook/*.py
%{python_sitelib}/spyder_notebook/{images,server,utils,widgets}
%{python_sitelib}/spyder_notebook/__pycache__
%{python_sitelib}/spyder_notebook-%{version}*-info

%changelog
