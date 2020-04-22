#
# spec file for package python-spyder-notebook
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
%define skip_python2 1
Name:           python-spyder-notebook
Version:        0.2.3
Release:        0
Summary:        Jupyter notebook integration with Spyder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spyder-ide/spyder-notebook
Source:         https://files.pythonhosted.org/packages/source/s/spyder-notebook/spyder-notebook-%{version}.tar.gz
Requires:       python-QtPy
Requires:       python-nbformat
Requires:       python-notebook >= 4.3
Requires:       python-psutil
Requires:       python-requests
Requires:       spyder >= 4
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module nbformat}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  spyder >= 4
BuildRequires:  xdpyinfo
# /SECTION
%python_subpackages

%description
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to control
breakpoints.

%package    -n spyder-notebook
Summary:        Jupyter Notebook plugin for the Spyder IDE
Group:          Development/Languages/Python
Provides:       spyder3-notebook = %{version}
Obsoletes:      spyder3-notebook < %{version}

%description -n spyder-notebook
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to control
breakpoints.

%prep
%setup -q -n spyder-notebook-%{version}
sed -i 's/\r$//' CHANGELOG.md README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The unittests fail with a seccomp-bpf crash if the sandbox
# is not disabled on i586
%ifarch %ix86 
export QTWEBENGINE_DISABLE_SANDBOX=1
%endif
export PYTHONDONTWRITEBYTECODE=1
%pytest

%files -n spyder-notebook
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/spyder_notebook
%{python_sitelib}/spyder_notebook-%{version}-py*.egg-info

%changelog
