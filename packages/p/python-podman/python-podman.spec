#
# spec file for package python-podman
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
Name:           python-podman
Version:        0.12.0
Release:        0
Summary:        A library to interact with a Podman server
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/containers/python-podman
Source:         https://files.pythonhosted.org/packages/source/p/podman/podman-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools >= 39}
BuildRequires:  %{python_module varlink}
# /SECTION
BuildRequires:  fdupes
Requires:       python-psutil
Requires:       python-python-dateutil
Requires:       python-setuptools >= 39
Requires:       python-varlink
Suggests:       python-fixtures
Suggests:       python-pbr
BuildArch:      noarch

%python_subpackages

%description
A library to interact with a Podman server

%prep
%setup -q -n podman-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc AUTHORS CHANGES.txt ChangeLog README.md
%license LICENSE LICENSE.txt
%{python_sitelib}/*

%changelog
