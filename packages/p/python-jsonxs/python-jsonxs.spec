#
# spec file for package python-jsonxs
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


Name:           python-jsonxs
Version:        0.6
Release:        0
Summary:        Get/set values in JSON and Python datastructures
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/fboender/jsonxs
#Git-Clone:     https://github.com/fboender/jsonxs.git
Source:         https://github.com/fboender/jsonxs/archive/v%{version}.tar.gz#/jsonxs-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
JSONxs is a Python library that uses a path expression string to get and
set values in JSON and Python datastructures. It's slightly similar to
JSONPath, but supports only simpler expressions and allows
modifications.
JSONxs is safe to use with untrusted input.

%prep
%setup -q -n jsonxs-%{version}
sed -i -e '/^#!\//, 1d' jsonxs/jsonxs.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec jsonxs/jsonxs.py -v

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/jsonxs
%{python_sitelib}/jsonxs-%{version}*-info

%changelog
