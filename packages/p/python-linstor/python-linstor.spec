#
# spec file for package python-linstor
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


Name:           python-linstor
Version:        1.12.0
Release:        0
Summary:        Python API for Linstor
License:        GPL-3.0-only
Group:          Productivity/Clustering/HA
URL:            https://github.com/LINBIT/linstor-api-py
Source:         https://pkg.linbit.com//downloads/linstor/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A Python API for Linstor.

%prep
%setup -q

%build
make %{?_smp_mflags} gensrc
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest linstor_tests

%files %{python_files}
%doc README.md
%license COPYING
%{python_sitelib}/linstor
%{python_sitelib}/python_linstor-%{version}.dist-info

%changelog
