#
# spec file for package python-ptyprocess
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
Name:           python-ptyprocess
Version:        0.6.0
Release:        0
Summary:        Run a subprocess in a pseudo terminal
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/pexpect/ptyprocess
Source:         https://files.pythonhosted.org/packages/source/p/ptyprocess/ptyprocess-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
%setup -q -n ptyprocess-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
