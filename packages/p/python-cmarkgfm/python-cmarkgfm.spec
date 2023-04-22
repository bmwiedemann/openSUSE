#
# spec file for package python-cmarkgfm
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
%{?sle15_python_module_pythons}
Name:           python-cmarkgfm
Version:        2022.10.27
Release:        0
Summary:        Minimal bindings to GitHub's fork of cmark
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jonparrott/cmarkgfm
Source:         https://files.pythonhosted.org/packages/source/c/cmarkgfm/cmarkgfm-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-cffi >= 1.0.0

%python_subpackages

%description
Minimal bindings to GitHub's fork of cmark

%prep
%autosetup -p1 -n cmarkgfm-%{version}

chmod a-x LICENSE.txt README.rst

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
find %{buildroot} -type f -name "*.h" -delete -print
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitearch}/cmarkgfm
%{python_sitearch}/cmarkgfm-%{version}*-info

%changelog
