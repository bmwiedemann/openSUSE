#
# spec file for package python-plumbum
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
Name:           python-plumbum
Version:        1.6.7
Release:        0
Summary:        Shell combinators library
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/tomerfiliba/plumbum
Source:         https://github.com/tomerfiliba/plumbum/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  openssh
BuildRequires:  sudo
# /SECTION
BuildArch:      noarch

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
# remote tests won't work in OBS
rm tests/test_remote.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
# the skipped tests need running local SSH server or root privs
%pytest -k 'not (test_iterdir or test_iter_lines_timeout or test_iter_lines_error or test_atomic_file2 or test_pid_file or test_atomic_counter or test_as_user or test_copy_move_delete)'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
