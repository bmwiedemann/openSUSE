#
# spec file for package python-hl7apy
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017-2020 Dr. Axel Braun <DocB@opensuse.org>
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

Name:           python-hl7apy
Version:        1.3.3
Release:        0
Summary:        A Python library to parse, create and handle HL7 v2x messages
License:        MIT
Group:          Development/Languages/Python
URL:            https://crs4.github.io/hl7apy/
Source:         https://files.pythonhosted.org/packages/source/h/hl7apy/hl7apy-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
HL7apy is a Python package to handle HL7 <http://www.hl7.org> v2
messages according to HL7 specifications.

The main features include:
 * Message parsing
 * Message creation
 * Message validation following the HL7 xsd specifications
 * Access to elements by name, long name or position
 * Support to all simple and complex datatypes
 * Encoding chars customization
 * Message encoding in ER7 format and compliant with MLLP protocol

%prep
%setup -q -n hl7apy-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%doc AUTHORS
%license LICENSE
%python3_only %{_bindir}/hl7apy_profile_parser
%{python_sitelib}/*

%changelog
