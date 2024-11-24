#
# spec file for package python-et_xmlfile
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


%{?sle15_python_module_pythons}
Name:           python-et_xmlfile
Version:        2.0.0
Release:        0
Summary:        An implementation of lxml.xmlfile for the standard library
License:        MIT
URL:            https://foss.heptapod.net/openpyxl/et_xmlfile
Source0:        https://foss.heptapod.net/openpyxl/et_xmlfile/-/archive/%{version}/et_xmlfile-%{version}.tar.gz
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jdcal
Requires:       python-lxml >= 3.4
BuildArch:      noarch
%python_subpackages

%description
et_xmlfile is a low memory library for creating large XML files.

It is based upon the xmlfile module from lxml with the aim of allowing code to
be developed that will work with both libraries. It was developed initially for
the openpyxl project but is now a standalone module.

%prep
%setup -q -n et_xmlfile-%{version}
rm -rf *.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest et_xmlfile/tests

%files %{python_files}
%license LICENCE.rst
%doc README.rst
%{python_sitelib}/et_xmlfile-%{version}*-info
%{python_sitelib}/et_xmlfile

%changelog
