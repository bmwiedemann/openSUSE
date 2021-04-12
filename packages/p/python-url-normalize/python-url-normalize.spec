#
# spec file for package python-url-normalize
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-url-normalize
Version:        1.4.3
Release:        0
Summary:        URL normalization for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/niksite/url-normalize
Source:         https://github.com/niksite/url-normalize/archive/refs/tags/%{version}.tar.gz#/url-normalize-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
URL normalization for Python.

%prep
%setup -q -n url-normalize-%{version}
rm tox.ini

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
