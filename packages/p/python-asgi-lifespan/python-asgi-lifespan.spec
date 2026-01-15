#
# spec file for package python-asgi-lifespan
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
Name:           python-asgi-lifespan
Version:        2.1.0
Release:        0
Summary:        Programmatic startup/shutdown of ASGI apps
License:        MIT
URL:            https://github.com/florimondmanca/asgi-lifespan
Source:         https://files.pythonhosted.org/packages/source/a/asgi-lifespan/asgi-lifespan-%{version}.tar.gz
# PATCH-FIX-UPSTREAM as proposed in https://github.com/florimondmanca/asgi-lifespan/issues/65 AsyncClient.__init__() got an unexpected keyword argument 'app'
Patch0:         httpx028.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-sniffio
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 0.19.2}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sniffio}
BuildRequires:  %{python_module starlette}
# /SECTION
%python_subpackages

%description
Programmatic startup/shutdown of ASGI apps.

%prep
%autosetup -p1 -n asgi-lifespan-%{version}
# we don't need coverage
sed -i '/--cov/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# most of trio tests fail https://github.com/florimondmanca/asgi-lifespan/issues/63
%pytest -k "not trio"

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/asgi_lifespan
%{python_sitelib}/asgi_lifespan-%{version}.dist-info

%changelog
