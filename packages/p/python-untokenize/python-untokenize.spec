#
# spec file for package python-untokenize
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-untokenize
Version:        0.1.1
Release:        0
Summary:        Python module to transform tokens into original source code
License:        MIT
URL:            https://github.com/myint/untokenize
Source0:        https://files.pythonhosted.org/packages/source/u/untokenize/untokenize-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/myint/untokenize/refs/heads/master/LICENSE
# PATCH-FIX-UPSTREAM gh#myint/untokenize#5
Patch0:         support-python314.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Untokenize transforms tokens into source code. Unlike the standard library's
tokenize.untokenize(), it preserves the original whitespace between tokens.

%prep
%autosetup -p1 -n untokenize-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test_untokenize.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/untokenize.py
%pycache_only %{python_sitelib}/__pycache__/untokenize.*.pyc
%{python_sitelib}/untokenize-%{version}.dist-info

%changelog
