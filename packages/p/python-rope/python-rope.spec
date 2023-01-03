#
# spec file for package python-rope
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


%define upname rope
Name:           python-rope
Version:        1.6.0
Release:        0
Summary:        A python refactoring library
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/python-rope/rope
Source:         https://files.pythonhosted.org/packages/source/r/rope/rope-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test
# Requires full stdlib
BuildRequires:  %{pythons}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module pytest >= 7.0.1}
BuildRequires:  %{python_module pytest-timeout >= 2.1.0}
BuildRequires:  %{python_module pytoolconfig-global >= 1.2.2}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Requires:       python-pytoolconfig-global >= 1.2.2
BuildArch:      noarch
%python_subpackages

%description
Rope is a python refactoring library.

* Rope aims to provide powerful and safe refactoring
* Rope is light on dependency, Rope only depends on Python itself
* Unlike PyRight or PyLance, Rope does not depend on Node.js
* Unlike PyLance or PyCharm, Rope is open source.
* Unlike PyRight and PyLance, Rope is written in Python itself,
  so if you experience problems, you would be able to debug and
  hack it yourself in a language that you are already familiar with
* In comparison to Jedi, Rope is focused on refactoring. While Jedi
  provides some basic refactoring capabilities, Rope supports many
  more advanced refactoring operations and options that Jedi does not.

%prep
%autosetup -p1 -n rope-%{version}

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# find ropetest from local source dir
export PYTHONPATH=":x"
# https://github.com/python-rope/rope/issues/478, we have a shuffled build directory and can't work around this
%pytest -k "not test_search_submodule"

%files %{python_files}
%license COPYING
%doc README.rst
%doc docs/
%{python_sitelib}/rope
%{python_sitelib}/rope-%{version}.dist-info

%changelog
