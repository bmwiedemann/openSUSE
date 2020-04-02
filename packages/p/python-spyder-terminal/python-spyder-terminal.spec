#
# spec file for package python-spyder-terminal
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
Name:           python-spyder-terminal
Version:        0.3.0
Release:        0
Summary:        Operating system virtual terminal plugin for the Spyder IDE
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spyder-ide/spyder-terminal
Source:         https://files.pythonhosted.org/packages/source/s/spyder-terminal/spyder-terminal-%{version}.tar.gz
Source:         %{name}-rpmlintrc
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python3-coloredlogs
Requires:       python3-pexpect
Requires:       python3-requests
Requires:       python3-terminado
Requires:       python3-tornado
Requires:       spyder >= 4
# SECTION test requirements
BuildRequires:  %{python_module coloredlogs}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module terminado}
BuildRequires:  %{python_module tornado}
BuildRequires:  spyder >= 4
BuildRequires:  xdpyinfo
# /SECTION

%python_subpackages

%description
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin for displaying a virtual terminal
(OS independent) inside the main Spyder window.

%package     -n spyder-terminal
Summary:        Operating system virtual terminal plugin for the Spyder IDE
Group:          Development/Languages/Python
Provides:       spyder3-terminal = %{version}-%{release}   
Obsoletes:      spyder3-terminal < %{version}-%{release}

%description -n spyder-terminal
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin for displaying a virtual terminal
(OS independent) inside the main Spyder window.

%prep
%setup -q -n spyder-terminal-%{version}

# fix python call in unit test gh#spyder-ide/spyder-terminal#179
sed -i "s/python_exec = 'python /python_exec = 'python3 /" spyder_terminal/server/tests/test_server.py

# fix rpmlint non-executable-script
sed -i -e '/^#!\//, 1d' spyder_terminal/server/__main__.py
sed -i -e '/^#!\//, 1d' spyder_terminal/server/tests/print_size.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
# The unittests fail with a seccomp-bpf crash if the sandbox
# is not disabled on i586
%ifarch %ix86 
export QTWEBENGINE_DISABLE_SANDBOX=1
%endif
# not in DEV mode gh#spyder-ide/spyder-terminal#180
skiptests="test_output_redirection"
%pytest -k "not $skiptests"

%files -n spyder-terminal
%defattr(-,root,root,-)
%doc CHANGELOG.md README.rst
%license LICENSE.txt
%{python3_sitelib}/spyder_terminal
%{python3_sitelib}/spyder_terminal-%{version}-*.egg-info

%changelog
