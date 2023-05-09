#
# spec file for package python-ansel
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
Name:           python-ansel
Version:        1.0.0
Release:        0
Summary:        Codecs for reading/writing documents in the ANSEL character set
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/haney/python-ansel
Source:         https://github.com/haney/python-ansel/archive/refs/tags/v1.0.0.tar.gz#/ansel-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pyfakefs}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Codecs for reading/writing documents in the ANSEL character set.

%prep
%setup -q -n python-ansel-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
