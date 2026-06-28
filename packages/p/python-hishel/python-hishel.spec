#
# spec file for package python-hishel
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
Name:           python-hishel
Version:        1.3.0
Release:        0
Summary:        Persistent cache implementation for popular HTTP clients
License:        BSD-3-Clause
URL:            https://github.com/karpetrosyan/hishel
Source:         https://github.com/karpetrosyan/hishel/archive/refs/tags/%{version}.tar.gz#/hishel-%{version}.tar.gz
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module anyio >= 4.9.0}
BuildRequires:  %{python_module anysqlite >= 0.0.5}
BuildRequires:  %{python_module fakeredis}
BuildRequires:  %{python_module httpx >= 0.28.1}
BuildRequires:  %{python_module inline-snapshot}
BuildRequires:  %{python_module msgpack >= 1.1.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis >= 7.0.0}
BuildRequires:  %{python_module requests >= 2.32.5}
BuildRequires:  %{python_module time-machine}
BuildRequires:  %{python_module trio}
BuildRequires:  %{python_module typing_extensions >= 4.14.1}
BuildRequires:  %{pythons}
# /SECTION
BuildRequires:  fdupes
Requires:       python-msgpack >= 1.1.2
Requires:       python-typing_extensions >= 4.14.1
Suggests:       python-httpx >= 0.28.1
Suggests:       python-requests >= 2.32.5
Suggests:       python-redis >= 7.0.0
Suggests:       python-anysqlite >= 0.0.5
Suggests:       python-anyio >= 4.9.0
Suggests:       python-fastapi >= 0.119.1
BuildArch:      noarch
%python_subpackages

%description
Hishel (հիշել, to remember in Armenian) is a modern HTTP caching
library for Python that implements RFC 9111 specifications. It
provides seamless caching integration for popular HTTP clients with
minimal code changes.

%prep
%autosetup -p1 -n hishel-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Need network access
donttest="test_simple_caching or test_encoded_content_caching"
%pytest --ignore tests/_async/test_storages.py --ignore tests/_sync/test_storages.py -k "not ($donttest)"

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/hishel
%{python_sitelib}/hishel-%{version}.dist-info

%changelog
