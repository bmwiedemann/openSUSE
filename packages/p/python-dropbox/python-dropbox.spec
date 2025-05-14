#
# spec file for package python-dropbox
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
Name:           python-dropbox
Version:        12.0.2
Release:        0
Summary:        Official Dropbox API Client
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dropbox/dropbox-sdk-python
Source:         https://github.com/dropbox/dropbox-sdk-python/archive/refs/tags/v%{version}.tar.gz#/dropbox-%{version}.tar.gz
# PATCH-FIX-UPSTREAM remove_six.patch https://github.com/dropbox/dropbox-sdk-python/pull/493
Patch1:         remove_six.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.16.2
Requires:       python-stone
BuildArch:      noarch

%python_subpackages

%description
Official Dropbox API Client

%prep
%autosetup -p1 -n dropbox-sdk-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests require an access token

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/dropbox
%{python_sitelib}/dropbox-%{version}.dist-info

%check

%changelog
