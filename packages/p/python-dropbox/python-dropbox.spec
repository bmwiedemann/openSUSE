#
# spec file for package python-dropbox
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-dropbox
Version:        10.4.1
Release:        0
Summary:        Official Dropbox API Client
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dropbox/dropbox-sdk-python
Source:         https://files.pythonhosted.org/packages/source/d/dropbox/dropbox-%{version}.tar.gz
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.16.2}
BuildRequires:  %{python_module six >= 1.3.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-requests >= 2.16.2
Requires:       python-six >= 1.3.0
BuildArch:      noarch

%python_subpackages

%description
Official Dropbox API Client

%prep
%setup -q -n dropbox-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests require an access token

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
