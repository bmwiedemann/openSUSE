#
# spec file for package python-pydiffx
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-pydiffx
Version:        1.1
Release:        0
Summary:        Python reader/writer for the DiffX file format
License:        MIT
URL:            https://github.com/reviewboard/pydiffx
Source:         https://files.pythonhosted.org/packages/source/p/pydiffx/pydiffx-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pydiffx-assertRaisesRegex.patch -- assertRaisesRegexp removed in py3.12
Patch0:         pydiffx-assertRaisesRegex.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module kgb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
A Python implementation of a reader and writer for the DiffX file
format, an extension to the unified diff format that adds structured,
unambiguous metadata for multi-commit, multi-file diffs.

%prep
%autosetup -p1 -n pydiffx-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/pydiffx
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest pydiffx

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/pydiffx
%{python_sitelib}/pydiffx-%{version}.dist-info

%changelog
