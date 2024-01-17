#
# spec file for package python-requests-gssapi
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
Name:           python-requests-gssapi
Version:        1.2.3
Release:        0
Summary:        A GSSAPI authentication handler for python-requests
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/pythongssapi/requests-gssapi
Source:         https://files.pythonhosted.org/packages/source/r/requests-gssapi/requests-gssapi-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-gssapi
Requires:       python-requests >= 1.1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module gssapi}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 1.1.0}
# /SECTION
%python_subpackages

%description
A GSSAPI authentication handler for python-requests

%prep
%setup -q -n requests-gssapi-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
