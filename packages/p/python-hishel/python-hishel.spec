#
# spec file for package python-hishel
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-hishel
Version:        0.0.29
Release:        0
Summary:        Persistent cache implementation for httpx and httpcore
License:        BSD-3-Clause
URL:            https://github.com/karpetrosyan/hishel
Source:         https://github.com/karpetrosyan/hishel/archive/refs/tags/%{version}.tar.gz#/hishel-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module httpx >= 0.22.0}
BuildRequires:  %{python_module typing_extensions >= 4.8.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module trio}
BuildRequires:  %{pythons}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python
Requires:       python-httpx >= 0.22.0
Requires:       python-typing_extensions >= 4.8.0
Suggests:       python-pyyaml == 6.0.1
Suggests:       python-redis == 5.0.1
Suggests:       python-anysqlite >= 0.0.5
Suggests:       python-boto3 >= 1.15.0
BuildArch:      noarch
%python_subpackages

%description
Hishel (հիշել, remember) is a library that implements HTTP Caching for
HTTPX and HTTP Core libraries in accordance with RFC 9111, the most
recent caching specification.

%prep
%autosetup -p1 -n hishel-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --ignore tests/_async/test_storages.py --ignore tests/_sync/test_storages.py

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/hishel
%{python_sitelib}/hishel-%{version}.dist-info

%changelog
