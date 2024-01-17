#
# spec file for package python-retryrequests
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-retryrequests
Version:        0.2.0
Release:        0
License:        MIT
Summary:        Extend python requests with exponential back-off retry
URL:            https://github.com/thombashi/retryrequests
Group:          Development/Languages/Python
Source:         https://github.com/thombashi/retryrequests/archive/v%{version}.tar.gz#/retryrequests-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 38.3.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module requests >= 2.18.4}
# /SECTION
BuildRequires:  fdupes
Requires:       python-requests >= 2.18.4
Requires:       python-setuptools >= 38.3.0
BuildArch:      noarch
%python_subpackages

%description
A Python library for HTTP requests using requests package with
exponential back-off retry.

%prep
%setup -q -n retryrequests-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# Upstream does not ship any tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/retryrequests*

%changelog
