#
# spec file for package python-ptyprocess
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-ptyprocess
Version:        0.7.0
Release:        0
Summary:        Run a subprocess in a pseudo terminal
License:        ISC
URL:            https://github.com/pexpect/ptyprocess
Source:         https://files.pythonhosted.org/packages/source/p/ptyprocess/ptyprocess-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - gh/pexpect/ptyprocess#75 - Remove unittest.makeSuite, gone from Python 3.13
Patch1:         https://github.com/pexpect/ptyprocess/pull/75.patch#/remove-old-unittest-functions.patch
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Launch a subprocess in a pseudo terminal (pty), and interact with both the
process and its pty.

Sometimes, piping stdin and stdout is not enough. There might be a password
prompt that doesn't read from stdin, output that changes when it's going to a
pipe rather than a terminal, or curses-style interfaces that rely on a terminal.
If you need to automate these things, running the process in a pseudo terminal
(pty) is the answer.

%prep
%autosetup -p1 -n ptyprocess-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# Fix python-bytecode-inconsistent-mtime
pushd %{buildroot}%{python_sitelib}
find . -name '*.pyc' -exec rm -f '{}' ';'
python%python_bin_suffix -m compileall *.py ';'
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/ptyprocess
%{python_sitelib}/ptyprocess-%{version}.dist-info

%changelog
