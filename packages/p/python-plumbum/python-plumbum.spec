#
# spec file for package python-plumbum
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-plumbum
Version:        1.7.2
Release:        0
Summary:        Shell combinators library
License:        MIT
URL:            https://github.com/tomerfiliba/plumbum
Source:         https://github.com/tomerfiliba/plumbum/archive/v%{version}.tar.gz#/plumbum-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  openssh
BuildRequires:  sudo
# /SECTION
%python_subpackages

%description
Plumbum is a library for shell script-like programs in Python.

Apart from shell-like syntax and handy shortcuts, the library
provides local and remote command  execution (over SSH), local and
remote file-system paths, working-directory and environment
manipulation, and a programmatic Command-Line Interface (CLI)
application toolkit.

%prep
%setup -q -n plumbum-%{version}
sed -i '/addopts/d' setup.cfg

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%python_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
# timeouts too fast on obs
donttest="test_iter_lines_line_timeout"
%pytest --ignore tests/test_remote.py -k "not ($donttest)"

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/plumbum
%{python_sitelib}/plumbum-%{version}*-info

%changelog
