#
# spec file for package python-drf-spectacular-sidecar
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


Name:           python-drf-spectacular-sidecar
Version:        2024.12.1
Release:        0
Summary:        Serve self-contained distribution builds of Swagger UI and Redoc with Django
License:        BSD-3-Clause
URL:            https://github.com/tfranzel/drf-spectacular-sidecar
Source:         https://files.pythonhosted.org/packages/source/d/drf-spectacular-sidecar/drf_spectacular_sidecar-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       python-Django >= 2.2
BuildArch:      noarch
%python_subpackages

%description
Serve self-contained distribution builds of Swagger UI and Redoc with Django

%prep
%autosetup -p1 -n drf_spectacular_sidecar-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no tests

%files %{python_files}
%{python_sitelib}/drf_spectacular_sidecar
%{python_sitelib}/drf_spectacular_sidecar-%{version}.dist-info

%changelog
