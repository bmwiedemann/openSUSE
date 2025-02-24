#
# spec file for package python-unicodedata2
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


%{?sle15_python_module_pythons}
Name:           python-unicodedata2
Version:        16.0.0
Release:        0
Summary:        Python unicodedata backport/updates
License:        Apache-2.0 AND Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/fonttools/unicodedata2
Source:         https://github.com/fonttools/unicodedata2/archive/%{version}.tar.gz#/unicodedata2-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Unicodedata backport and updates for the latest unicode version.
The versions of this package match Unicode versions, so
unicodedata2==%{version} is data from Unicode %{version}.

%prep
%setup -q -n unicodedata2-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/unicodedata2.*.so
%{python_sitearch}/unicodedata2-%{version}*-info

%changelog
