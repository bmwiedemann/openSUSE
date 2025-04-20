#
# spec file for package python-calmjs.types
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
Name:           python-calmjs.types
Version:        1.0.1
Release:        0
Summary:        Types for the calmjs framework
License:        MIT
URL:            https://github.com/calmjs/calmjs.types
Source:         https://github.com/calmjs/calmjs.types/archive/%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
A collection of types (mostly exception classes) for use with |calmjs|_.

%prep
%autosetup -p1 -n calmjs.types-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/calmjs/types/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/calmjs
%{python_sitelib}/calmjs_types-%{version}.dist-info
%{python_sitelib}/calmjs.types-%{version}*-nspkg.pth

%changelog
