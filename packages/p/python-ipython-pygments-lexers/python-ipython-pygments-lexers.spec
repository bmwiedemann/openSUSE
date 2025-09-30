#
# spec file for package python-ipython-pygments-lexers
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


Name:           python-ipython-pygments-lexers
Version:        1.1.1
Release:        0
Summary:        Pygments lexers for highlighting IPython code
License:        BSD-3-Clause
URL:            https://github.com/ipython/ipython-pygments-lexers
Source:         https://files.pythonhosted.org/packages/source/i/ipython_pygments_lexers/ipython_pygments_lexers-%{version}.tar.gz
Source99:       ipython_pygments_lexers.rpmlintrc
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pygments
Provides:       python-ipython_pygments_lexers = %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A Pygments plugin for IPython code & console sessions

IPython is an interactive Python shell. Among other features,
it adds some special convenience syntax, including `%%magics`, `!shell commands`
and `help?`. This package contains lexers for these, to use with the Pygments syntax
highlighting package.

- The `ipython` lexer should be used where only input code is highlighted
- The `ipythonconsole` lexer works for an IPython session, including code,
  prompts, output and tracebacks.

These lexers were previously part of IPython itself (in `IPython.lib.lexers`),
but have now been moved to a separate package.

%prep
%autosetup -p1 -n ipython_pygments_lexers-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/ipython_pygments_lexers.py
%pycache_only %{python_sitelib}/__pycache__/ipython_pygments_lexers*.pyc
%{python_sitelib}/ipython_pygments_lexers-%{version}.dist-info

%changelog
