#
# spec file for package python-pytest-tornasync
#
# Copyright (c) 2020 SUSE LLC.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-pytest-tornasync
Version:        0.6.0.post2
Release:        0
License:        MIT
Summary:        PyTest plugin for testing Tornado code
Url:            https://github.com/eukaryote/pytest-tornasync
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pytest-tornasync/pytest-tornasync-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tornado >= 5.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-base >= 3.5
Requires:       python-pytest
Requires:       python-tornado >= 5.0
BuildArch:      noarch

%python_subpackages

%description
A pytest plugin that provides some fixtures for testing Tornado
apps and handling of plain (undecoratored) native coroutine tests.

%prep
%setup -q -n pytest-tornasync-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# We'll package this ourself
rm -f %{buildroot}%{_prefix}/LICENSE

# Tests are missing files
# See: https://github.com/eukaryote/pytest-tornasync/pull/8
# There are no tags on github:
# See: https://github.com/eukaryote/pytest-tornasync/issues/9
# %%check
# %%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
