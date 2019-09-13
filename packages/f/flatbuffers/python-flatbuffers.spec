#
# spec file for package python-flatbuffers
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-flatbuffers
Version:        1.10.0.20190321T162332.a746143
Release:        0
Summary:        The FlatBuffers serialization format for Python
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/google/flatbuffers
Source:         flatbuffers-%{version}.tar.xz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-numpy
BuildArch:      noarch

%python_subpackages

%description
Python runtime library for use with the Flatbuffers serialization format.

%prep
%setup -q -n flatbuffers-%{version}

%build
pushd python
%python_build
popd

%install
pushd python
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
popd

%files %{python_files}
%if 0%{?leap_version} >= 420200 || 0%{?suse_version} > 1320 
%license LICENSE.txt
%else
%doc LICENSE.txt
%endif
%{python_sitelib}/*

%changelog
