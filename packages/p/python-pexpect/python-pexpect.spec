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


%{?sle15_python_module_pythons}
Name:           python-pexpect
Version:        4.9.0
Release:        0
Summary:        Pure Python Expect-like module
License:        ISC
URL:            https://github.com/pexpect/pexpect
Source:         https://files.pythonhosted.org/packages/source/p/pexpect/pexpect-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module ptyprocess}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
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
# Remove shebang
sed -i '1 {/^#!/d}' pexpect/FSM.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
echo "set enable-bracketed-paste off" > .inputrc
export INPUTRC=$(readlink -f .inputrc) TRAVIS=true
# test_pager_as_cat - needs manpages that would pull extra deps
# test_interrupt, test_multiple_interrupts - hangs under linux-user emulation
# test_large_stdout_stream - seen failed on s390x,  [ assert 2 == 1 ]
# test_*interrupt hang or are too long [bsc#1209560]
# test_replwrap - seen failed on s390x, [ ValueError: Continuation prompt found - input was incomplete: ]
# test_pxssh - seen failed on s390x, [ pexpect.pxssh.ExceptionPxssh: could not synchronize with original prompt ]
# test_interact_exit_unicode - seen failed on s390x [ pexpect.exceptions.EOF: End Of File (EOF). Exception style platform. ]
# test_performance - random failures seen on aarch64 [ pexpect.exceptions.TIMEOUT: Timeout exceeded. ]
%pytest -k "not (test_large_stdout_stream or test_pager_as_cat or test_replwrap or test_pxssh or test_zsh or test_interrupt or test_multiple_interrupts or test_interact_exit_unicode or test_performance)"

%files %{python_files}
%license LICENSE
%doc doc examples
%{python_sitelib}/pexpect
%{python_sitelib}/pexpect-%{version}*-info

%changelog
