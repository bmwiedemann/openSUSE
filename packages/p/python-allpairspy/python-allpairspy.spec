#
# spec file for package python-allpairspy
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
Name:           python-allpairspy
Version:        2.5.1
Release:        0
License:        MIT
Summary:        Pairwise test combinations generator
URL:            https://github.com/thombashi/allpairspy
Source:         https://github.com/thombashi/allpairspy/archive/v%{version}.tar.gz#/allpairspy-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Suggests:       python-twine
Suggests:       python-wheel
Suggests:       python-releasecmd >= 0.0.18
Suggests:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
Pairwise test combinations generator.

%prep
%autosetup -p1 -n allpairspy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/allpairspy
%{python_sitelib}/allpairspy-%{version}.dist-info

%changelog
