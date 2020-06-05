#
# spec file for package python-cmd2
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
%define         skip_python2 1
Name:           python-cmd2
Version:        0.8.9
Release:        0
Summary:        Extra features for standard library's cmd module
License:        MIT
URL:            https://github.com/python-cmd2/cmd2
Source:         https://files.pythonhosted.org/packages/source/c/cmd2/cmd2-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  vim
Requires:       python
Requires:       python-attrs >= 16.3.0
Requires:       python-colorama >= 0.3.7
Requires:       python-pyperclip >= 1.6
Requires:       python-wcwidth >= 0.1.7
BuildArch:      noarch
%if %{python3_version_nodots} < 35
Requires:       python-contextlib2
Requires:       python-typing
%endif
# SECTION Test requirements
BuildRequires:  %{python_module attrs >= 16.3.0}
BuildRequires:  %{python_module colorama >= 0.3.7}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pyperclip >= 1.6}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wcwidth >= 0.1.7}
# Required by tests.
BuildRequires:  vim
%if 0%{?suse_version} <= 1315
BuildRequires:  %{python_module contextlib2}
BuildRequires:  %{python_module typing}
%endif
# /SECTION
%python_subpackages

%description
Enhancements for standard library's cmd module.

Drop-in replacement adds several features for command-prompt tools:

    * Searchable command history (commands: "hi", "li", "run")
    * Load commands from file, save to file, edit commands in file
    * Multi-line commands
    * Case-insensitive commands
    * Special-character shortcut commands (beyond cmd's "@" and "!")
    * Settable environment parameters
    * Parsing commands with flags
    * > (filename), >> (filename) redirect output to file
    * < (filename) gets input from file
    * bare >, >>, < redirect to/from paste buffer
    * accepts abbreviated commands when unambiguous
    * `py` enters interactive Python console
    * test apps against sample session transcript (see example/example.py)

%prep
%setup -q -n cmd2-%{version}
# Fix spurious-executable-perm
chmod a-x README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm -v tests/test_transcript.py tests/test_parsing.py tests/test_cmd2.py
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md CODEOWNERS README.md
%{python3_sitelib}/*

%changelog
