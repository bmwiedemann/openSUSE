#
# spec file for package python-paginate
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
Name:           python-paginate
Version:        0.5.6
Release:        0
Summary:        Divides large result sets into pages for easier browsing
License:        MIT
URL:            https://github.com/Signum/paginate
# PyPI tarball does not include tests...
Source:         https://github.com/Signum/paginate/archive/%{version}.tar.gz#/paginate-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Divides large result sets into pages for easier browsing

%prep
%autosetup -p1 -n paginate-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.txt README.md
%{python_sitelib}/paginate
%{python_sitelib}/paginate-%{version}.dist-info

%changelog
