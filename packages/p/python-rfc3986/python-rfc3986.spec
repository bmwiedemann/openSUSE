#
# spec file for package python-rfc3986
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-rfc3986
Version:        1.3.2
Release:        0
Summary:        Python module for validating URI references per RFC 3986
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://rfc3986.rtfd.org
Source:         https://files.pythonhosted.org/packages/source/r/rfc3986/rfc3986-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
A Python implementation of `RFC 3986`_ including validation and authority
parsing. Coming soon: `Reference Resolution <http://tools.ietf.org/html/rfc3986#section-5>`_.

%prep
%setup -q -n rfc3986-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst README.rst
%{python_sitelib}/*

%changelog
