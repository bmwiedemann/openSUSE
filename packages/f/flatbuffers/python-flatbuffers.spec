#
# spec file for package python-flatbuffers
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
Name:           python-flatbuffers
Version:        1.12.0
Release:        0
Summary:        The FlatBuffers serialization format for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/google/flatbuffers
Source0:        https://github.com/google/flatbuffers/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-numpy
BuildArch:      noarch
%python_subpackages

%description
Python runtime library for use with the Flatbuffers serialization format.

%prep
%setup -q -n flatbuffers-%{version}/python

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license ../LICENSE.txt
%{python_sitelib}/*

%changelog
