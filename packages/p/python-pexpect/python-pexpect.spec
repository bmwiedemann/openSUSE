#
# spec file for package python-pexpect
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-pexpect
Version:        4.8.0
Release:        0
Summary:        Pure Python Expect-like module
License:        ISC
URL:            https://pexpect.readthedocs.org/en/latest/
Source:         https://files.pythonhosted.org/packages/source/p/pexpect/pexpect-%{version}.tar.gz
Patch0:         no-python-binary.patch
# Newer asyncio / python 3.11 support
Patch1:         https://github.com/pexpect/pexpect/pull/715.patch
Patch2:         https://github.com/pexpect/pexpect/pull/684.patch
BuildRequires:  %{python_module ptyprocess}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
# For test command calls
# For bash validation
BuildRequires:  bash
BuildRequires:  fdupes
# For man validation
BuildRequires:  man
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
Requires:       python-ptyprocess
BuildArch:      noarch
%python_subpackages

%description
Pexpect is a pure Python module for spawning child applications;
controlling them; and responding to expected patterns in their output.

%prep
%autosetup -p1 -n pexpect-%{version}

# Fix wrong-script-interpreter
find examples -type f -name "*.py" -exec sed -i "s|#!%{_bindir}/env python||" {} \;
find examples -type f -name "*.cgi" -exec sed -i "s|##!%{_bindir}/env python|##!%{_bindir}/python|" {} \;
# Mark example *.py as non-executable (we already patch the shebang out, so they can't be started anyway)
find examples -type f -name "*.py" -exec chmod 644 {} \;

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# test_bash https://github.com/pexpect/pexpect/issues/568
# test_large_stdout_stream - random
# test_pager_as_cat - needs manpages that would pull extra deps
%pytest -k "not test_bash and not test_large_stdout_stream and not test_pager_as_cat %{?qemu_user_space_build: and not test_spawn_uses_env}"

%files %{python_files}
%license LICENSE
%doc doc/
%doc examples/
%{python_sitelib}/pexpect/
%{python_sitelib}/pexpect-%{version}-py*.egg-info

%changelog
