#
# spec file for package python-cmd2
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
%define         skip_python2 1
Name:           python-cmd2
Version:        2.4.3
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
Requires:       python-pyperclip >= 1.6
Requires:       python-wcwidth >= 0.1.7
BuildArch:      noarch
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib_metadata >= 1.6
Requires:       python-typing_extensions
%endif
# SECTION Test requirements
BuildRequires:  %{python_module attrs >= 16.3.0}
BuildRequires:  %{python_module importlib_metadata >= 1.6 if %python-base < 3.8}
BuildRequires:  %{python_module pyperclip >= 1.6}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions if %python-base < 3.8}
BuildRequires:  %{python_module wcwidth >= 0.1.7}
BuildRequires:  vim
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
sed -i '/--cov/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# -q: prevent to colorize the terminal from color commands in parametrized test names
%pytest -q

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%{python_sitelib}/cmd2
%{python_sitelib}/cmd2-%{version}*-info

%changelog
