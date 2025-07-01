#
# spec file for package python-flatbuffers
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


%{?sle15_python_module_pythons}
Name:           python-flatbuffers
Version:        25.2.10
Release:        0
Summary:        The FlatBuffers serialization format for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://google.github.io/flatbuffers/
Source0:        https://github.com/google/flatbuffers/archive/v%{version}.tar.gz#/flatbuffers-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-numpy
BuildArch:      noarch
%python_subpackages

%description
Python runtime library for use with the Flatbuffers serialization format.

%prep
%setup -q -n flatbuffers-%{version}/python
ln ../LICENSE
sed -i 's|../LICENSE|LICENSE|g' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license ../LICENSE
%{python_sitelib}/flatbuffers
%{python_sitelib}/flatbuffers-%{version}.dist-info

%changelog
