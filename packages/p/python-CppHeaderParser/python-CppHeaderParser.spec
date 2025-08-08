#
# spec file for package python-CppHeaderParser
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-CppHeaderParser
Version:        2.7.4
Release:        0
Summary:        Parse C++ header files and generate a data structure representing the class
License:        BSD-3-Clause
URL:            https://github.com/senex/cppheaderparser
Source0:        https://files.pythonhosted.org/packages/source/C/CppHeaderParser/CppHeaderParser-%{version}.tar.gz
Source99:       python-CppHeaderParser.rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ply
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ply}
# /SECTION
%python_subpackages

%description
Parse C++ header files and generate a data structure representing
the class

%prep
%autosetup -p1 -n CppHeaderParser-%{version}

sed -E -i "1{/^#!\/usr\/bin.*python/d}" CppHeaderParser/CppHeaderParser.py \
	CppHeaderParser/examples/readSampleClass.py
chmod a-x CppHeaderParser/examples/readSampleClass.py

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/CppHeaderParser/doc
%fdupes %{buildroot}%{$python_sitelib}
}

%files %{python_files}
%doc README.html README.txt
%doc CppHeaderParser/doc/CppHeaderParser.html
%{python_sitelib}/CppHeaderParser
%{python_sitelib}/[Cc]pp[Hh]eader[Pp]arser-%{version}*-info

%changelog
