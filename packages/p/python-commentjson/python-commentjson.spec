#
# spec file for package python-commentjson
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
Name:           python-commentjson
Version:        0.9.0
Release:        0
Summary:        Add Python and JavaScript style comments in your JSON files
License:        MIT
URL:            https://github.com/vaidik/commentjson
Source:         https://github.com/vaidik/commentjson/archive/v%{version}.tar.gz#/commentjson-%{version}.tar.gz
BuildRequires:  %{python_module lark >= 0.7.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module testsuite}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lark >= 0.7.1
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
`commentjson` (Comment JSON) is a Python package that helps you create JSON
files with Python and JavaScript style inline comments. Its API is very similar
to the Python standard library's `json` module.

%prep
%setup -q -n commentjson-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG="en_US.UTF8"
# the testsuite is quite messy, just stick the run to only the core functionality
%pytest commentjson/tests/test_commentjson.py

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%{python_sitelib}/*

%changelog
