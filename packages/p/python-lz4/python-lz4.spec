#
# spec file for package python-lz4
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-lz4
Version:        4.3.2
Release:        0
Summary:        LZ4 Bindings for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python-lz4/python-lz4
Source:         https://files.pythonhosted.org/packages/source/l/lz4/lz4-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  liblz4-devel >= 1.7.5
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This package provides python bindings for the lz4 compression library.

%prep
%setup -q -n lz4-%{version}

%build
# not neccessary, but ensure we use system lib
rm -r lz4libs
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# lz4.stream is not compiled by default: https://github.com/python-lz4/python-lz4/issues/240
ignoretest="--ignore tests/stream"
%pytest_arch $ignoretest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/lz4/
%{python_sitearch}/lz4-%{version}.dist-info

%changelog
