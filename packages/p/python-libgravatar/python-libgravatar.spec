#
# spec file for package python-libgravatar
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-libgravatar
Version:        1.0.4
Release:        0
Summary:        A library that provides a Python 3 interface for the Gravatar API
License:        GPL-3.0
URL:            https://github.com/pabluk/libgravatar
Source:         https://files.pythonhosted.org/packages/source/l/libgravatar/libgravatar-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A library that provides a Python 3 interface for the Gravatar API.

%prep
%autosetup -p1 -n libgravatar-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/libgravatar
%{python_sitelib}/libgravatar-%{version}.dist-info

%changelog
