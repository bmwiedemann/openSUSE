#
# spec file for package python-dropbox
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
Name:           python-dropbox
Version:        12.2.2
Release:        0
Summary:        Official Dropbox API Client
License:        MIT
URL:            https://github.com/dropbox/dropbox-sdk-python
Source:         https://github.com/dropbox/dropbox-sdk-python/archive/refs/tags/v%{version}.tar.gz#/dropbox-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#dropbox/dropbox-sdk-python#598
Patch0:         remove-mock.patch
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module requests >= 2.16.2}
BuildRequires:  %{python_module stone >= 3.5.3}
# /SECTION
Requires:       python-requests >= 2.16.2
Requires:       python-stone >= 3.5.3
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

%check
# Integration tests require real AWS credientials
%pytest --ignore test/integration

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/dropbox
%{python_sitelib}/dropbox-%{version}.dist-info

%changelog
