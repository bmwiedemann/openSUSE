#
# spec file for package python-web_cache
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


%define skip_python2 1
Name:           python-web_cache
Version:        1.1.0
Release:        0
Summary:        Persistent cache storage python module
License:        LGPL-2.1-only
URL:            https://github.com/desbma/web_cache
Source:         https://github.com/desbma/web_cache/archive/%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
BuildArch:      noarch
%python_subpackages

%description
Python module for simple key-value storage backed up by sqlite3
database. The typical use case is a URL to HTTP data cache, but it can
also be used fo non web resources. It features different cache eviction
strategies and optional compression.

%prep
%setup -q -n web_cache-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/web_cache
%{python_sitelib}/web_cache-%{version}.dist-info

%changelog
