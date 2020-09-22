#
# spec file for package python-linstor
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
Name:           python-linstor
Version:        1.3.0
Release:        0
Summary:        Python API for Linstor
License:        GPL-3.0-only
Group:          Productivity/Clustering/HA
URL:            https://github.com/LINBIT/linstor-api-py
Source:         http://www.linbit.com/downloads/linstor/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  protobuf-devel
Requires:       %{python_module protobuf}
%python_subpackages

%description
A Python API for Linstor.

%prep
%setup -q

%build
make %{?_smp_mflags} gensrc
%python_build

%install
#python setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#files -f INSTALLED_FILES
%files %{python_files}
%{python_sitelib}

%changelog
