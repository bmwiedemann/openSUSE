#
# spec file for package python-spyder-terminal
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
# But we need the python3-spyder-terminal name, provided by the python_subpackages rewrite
%define pythons python3
Name:           python-spyder-terminal
Version:        0.5.0
Release:        0
Summary:        Operating system virtual terminal plugin for the Spyder IDE
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spyder-ide/spyder-terminal
# The PyPI tarfile is the official release but does not include the tests.
# The Github tarfile does not include the bundled nodejs dependencies in
# server/static/components.  Thus we use the PyPI release and add the testdir
# from the Github package.
Source0:        https://files.pythonhosted.org/packages/source/s/spyder-terminal/spyder-terminal-%{version}.tar.gz#/%{name}-%{version}-pypi.tar.gz
Source1:        https://github.com/spyder-ide/spyder-terminal/archive/v%{version}.tar.gz#/%{name}-%{version}-gh.tar.gz
# The bundled nodejs stuff has a few files tripping rpmlint
Source2:        %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python-coloredlogs
Requires:       python-pexpect
Requires:       python-requests
Requires:       python-terminado >= 0.9.1
Requires:       python-tornado
Requires:       spyder >= 4.2.0
# SECTION test requirements
BuildRequires:  python3-coloredlogs
BuildRequires:  python3-flaky
BuildRequires:  python3-pexpect
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-qt
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-pytest-xvfb
BuildRequires:  python3-requests
BuildRequires:  python3-terminado >= 0.9.1
BuildRequires:  python3-tornado
BuildRequires:  spyder >= 4.2.0
BuildRequires:  xdpyinfo
# /SECTION
BuildArch:      noarch
Provides:       spyder-terminal = %{version}-%{release}
Obsoletes:      spyder-terminal < %{version}-%{release}
Provides:       spyder3-terminal = %{version}-%{release}
Obsoletes:      spyder3-terminal < %{version}-%{release}
%python_subpackages

%description
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin for displaying a virtual terminal
(OS independent) inside the main Spyder window. It uses a nodejs
backend.

%prep
%setup -q -n spyder-terminal-%{version}
tar --strip-components=1 -xzf %{SOURCE1} \
    spyder-terminal-%{version}/conftest.py \
    spyder-terminal-%{version}/spyder_terminal/tests \
    spyder-terminal-%{version}/spyder_terminal/server/tests

# fix rpmlint non-executable-script
sed -i -e '/^#!\//, 1d' spyder_terminal/server/__main__.py
sed -i -e '/^#!\//, 1d' spyder_terminal/server/tests/print_size.py

%build
%python3_build

%install
%python3_install
%find_lang spyder_terminal
find %{buildroot}%{python3_sitelib}/spyder_terminal/locale -name '*.po*' -delete
%fdupes %{buildroot}%{python3_sitelib}

%check
# The unittests fail with a seccomp-bpf crash if the sandbox
# is not disabled on i586
export QTWEBENGINE_DISABLE_SANDBOX=1
# qtbot timeouts in OBS env
donttest="test_terminal_paste or test_new_terminal"
%pytest -k "not ($donttest)"

%files %{python_files} -f spyder_terminal.lang
%defattr(-,root,root,-)
%doc CHANGELOG.md README.rst
%license LICENSE.txt
%dir %{python_sitelib}/spyder_terminal
%{python_sitelib}/spyder_terminal/{*.py*,server,widgets}
%{python_sitelib}/spyder_terminal/__pycache__/
%dir %{python_sitelib}/spyder_terminal/locale
%dir %{python_sitelib}/spyder_terminal/locale/*
%dir %{python_sitelib}/spyder_terminal/locale/*/LC_MESSAGES
%exclude %{python_sitelib}/spyder_terminal/tests
%exclude %{python_sitelib}/spyder_terminal/server/tests
%{python_sitelib}/spyder_terminal-%{version}*-info

%changelog
