#
# spec file for package python-unicodecsv
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


Name:           python-unicodecsv
Version:        0.14.1
Release:        0
Summary:        Drop-in replacment for python's csv module with unicode support
License:        BSD-2-Clause
URL:            https://github.com/jdunck/python-unicodecsv
Source0:        https://pypi.io/packages/source/u/unicodecsv/unicodecsv-%{version}.tar.gz
# sdist does not ship a LICENSE
Source1:        https://raw.githubusercontent.com/jdunck/python-unicodecsv/refs/heads/master/LICENSE
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
Python 2's csv module doesn't easily deal with unicode strings,
leading to the dreaded "'ascii' codec can't encode characters
in position ..." exception.

The unicodecsv is a drop-in replacement for Python 2's csv module
which supports unicode strings without a hassle.

%prep
%setup -q -n unicodecsv-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/unicodecsv
%{python_sitelib}/unicodecsv-%{version}.dist-info

%changelog
