#
# spec file for package python-httpx-sse
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-httpx-sse
Version:        0.4.3
Release:        0
Summary:        Consume Server-Sent Event (SSE) messages with HTTPX
License:        MIT
URL:            https://github.com/florimondmanca/httpx-sse
Source:         https://files.pythonhosted.org/packages/source/h/httpx-sse/httpx_sse-%{version}.tar.gz
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sse-starlette}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-httpx
BuildArch:      noarch
%python_subpackages

%description
Consume Server-Sent Event (SSE) messages with HTTPX.

%prep
%autosetup -p1 -n httpx_sse-%{version}
# we don't need to run coverage
sed -i '/--cov/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/httpx_sse
%{python_sitelib}/httpx_sse-%{version}.dist-info

%changelog
