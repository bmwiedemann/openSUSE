#
# spec file for package python-subprocess-tee
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
Name:           python-subprocess-tee
Version:        0.4.0
Release:        0
Summary:        Captures the output of subprocesses in real-time
License:        MIT
URL:            https://github.com/pycontribs/subprocess-tee
Source:         https://files.pythonhosted.org/packages/source/s/subprocess-tee/subprocess-tee-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm_git_archive}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test
BuildRequires:  %{python_module enrich}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
This package provides a drop-in alternative to `subprocess.run` that
captures the output while still printing it in real-time, just the way
`tee` does.

Printing output in real-time while still capturing is valuable for
any tool that executes long-running child processes. For those, you do want
to provide instant feedback (progress) related to what is happening.

%prep
%setup -q -n subprocess-tee-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# program "molecule" is no available in openSUSE. But this test is platform-independent, so not required
%pytest -k 'not test_molecule and not test_rich_console_ex'

%files %{python_files}
%{python_sitelib}/subprocess_tee/
%{python_sitelib}/subprocess_tee-%{version}*-info
%doc README.md
%license LICENSE

%changelog
