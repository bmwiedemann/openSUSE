#
# spec file for package python-url-normalize
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-url-normalize
Version:        1.4.3
Release:        0
Summary:        URL normalization for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/niksite/url-normalize
Source:         https://github.com/niksite/url-normalize/archive/refs/tags/%{version}.tar.gz#/url-normalize-%{version}.tar.gz
# PATCH-FIX-UPSTREAM url-normalize-pr28-poetry-core.patch gh#niksite/url-normalize#28
Patch0:         https://github.com/niksite/url-normalize/pull/28.patch#/url-normalize-pr28-poetry-core.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-url_normalize = %{version}-%{release}
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
URL normalization for Python.

%prep
%autosetup -p1 -n url-normalize-%{version}
rm tox.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/url_normalize
%{python_sitelib}/url_normalize-%{version}.dist-info

%changelog
