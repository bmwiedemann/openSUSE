#
# spec file for package python-httpx2
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
Name:           python-httpx2
Version:        2.5.0
Release:        0
Summary:        The next generation HTTP client
License:        BSD-3-Clause
URL:            https://github.com/pydantic/httpx2
Source:         https://github.com/pydantic/httpx2/archive/refs/tags/v%{version}.tar.gz#/httpx2-%{version}.tar.gz
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-dynamic-versioning >= 0.8.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 8.3}
BuildRequires:  %{python_module Werkzeug >= 3.1.6}
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module chardet >= 5.2.0}
BuildRequires:  %{python_module cryptography >= 46.0.7}
BuildRequires:  %{python_module h2}
BuildRequires:  %{python_module hpack}
BuildRequires:  %{python_module httpcore2 == %{version}}
BuildRequires:  %{python_module hyperframe}
BuildRequires:  %{python_module idna >= 3.18}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-httpbin >= 2.0.0}
BuildRequires:  %{python_module pytest-trio >= 0.8.0}
BuildRequires:  %{python_module rich >= 10}
BuildRequires:  %{python_module socksio}
BuildRequires:  %{python_module trio >= 0.31.0}
BuildRequires:  %{python_module trustme >= 1.2.1}
BuildRequires:  %{python_module truststore >= 0.10}
BuildRequires:  %{python_module uvicorn >= 0.35}
BuildRequires:  %{python_module zstandard}
# /SECTION
BuildRequires:  fdupes
Requires:       python-anyio
Requires:       python-httpcore2 == %{version}
Requires:       python-idna >= 3.18
Requires:       python-truststore >= 0.10
%if 0%{?python_version_nodots} < 313
Requires:       python-typing-extensions >= 4.5.0
%endif
Suggests:       python-brotli
Suggests:       python-click >= 8.0.0
Suggests:       python-pygments >= 2.0.0
Suggests:       python-rich >= 10
Suggests:       python-h2 >= 3
Suggests:       python-socksio >= 1.0.0
%if 0%{?python_version_nodots} < 314
Suggests:       python-zstandard >= 0.18.0
%endif
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
HTTPX2 is a fully featured HTTP client library for Python 3. It includes an
integrated command line client, has support for both HTTP/1.1 and HTTP/2,
and provides both sync and async APIs.

HTTPX2 is a continuation of the wonderful work started by
[lovelydinosaur](https://github.com/lovelydinosaur) and the broader HTTPX
community.

%prep
%autosetup -p1 -n httpx2-%{version}

cd src/httpx2
# replace version fallback with real version
# (https://github.com/ninoseki/uv-dynamic-versioning/blob/main/docs/tips.md#nix-and-other-sandboxed-build-environments)
sed -i "s|^fallback-version = \"0\.0\.0\"|fallback-version = \"%{version}\"|" pyproject.toml

%build
cd src/httpx2
%pyproject_wheel

%install
cd src/httpx2
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/httpx2
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k "not network"

%post
%python_install_alternative httpx2

%postun
%python_uninstall_alternative httpx2

%files %{python_files}
%doc README.md
%license LICENSE.md
%python_alternative %{_bindir}/httpx2
%{python_sitelib}/httpx2
%{python_sitelib}/httpx2-%{version}.dist-info

%changelog
