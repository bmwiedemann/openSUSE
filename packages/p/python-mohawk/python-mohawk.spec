#
# spec file for package python-mohawk
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


Name:           python-mohawk
Version:        1.1.0
Release:        0
Summary:        Library for Hawk HTTP authorization
License:        MPL-2.0
URL:            https://github.com/kumar303/mohawk
Source:         https://files.pythonhosted.org/packages/source/m/mohawk/mohawk-%{version}.tar.gz
Patch0:         remove-nose.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Mohawk is an alternate Python implementation of the Hawk HTTP
authorization scheme.

%prep
%autosetup -p1 -n mohawk-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%files %{python_files}
%doc README.rst
%{python_sitelib}/mohawk
%{python_sitelib}/mohawk-%{version}*-info

%changelog
