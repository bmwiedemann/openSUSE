#
# spec file for package python-odfpy
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


#
%define modname odfpy
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{modname}
Version:        1.4.0
Release:        0
Summary:        Python API and tools to manipulate OpenDocument files
License:        GPL-2.0-or-later AND Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/eea/odfpy
Source:         https://files.pythonhosted.org/packages/source/o/odfpy/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-defusedxml
%python_subpackages

%description
Odfpy is a library to read and write OpenDocument v. 1.1 files.
The main focus has been to prevent the programmer from creating invalid
documents. It has checks that raise an exception if the programmer adds
an invalid element, adds an attribute unknown to the grammar, forgets to
add a required attribute or adds text to an element that doesn't allow it.

These checks and the API itself were generated from the RelaxNG
schema, and then hand-edited. Therefore the API is complete and can
handle all ODF constructions.

In addition to the API, there are a few scripts:

- csv2odf - Create OpenDocument spreadsheet from comma separated values
- mailodf - Email ODF file as HTML archive
- odf2xhtml - Convert ODF to (X)HTML
- odf2mht - Convert ODF to HTML archive
- odf2xml - Create OpenDocument XML file from OD? package
- odfimgimport - Import external images
- odflint - Check ODF file for problems
- odfmeta - List or change the metadata of an ODF file
- odfoutline - Show outline of OpenDocument
- odfuserfield - List or change the user-field declarations in an ODF file
- xml2odf - Create OD? package from OpenDocument in XML form

Visit https://github.com/eea/odfpy for documentation and examples.

%prep
%setup -q -n %{modname}-%{version}
sed -i "1d" odf/{userfield,odf2xhtml,manifest,element,elementtypes,load,odfmanifest,thumbnail}.py # Fix non-executable scripts

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_version} -v

%files %{python_files}
%license APACHE-LICENSE-2.0.txt GPL-LICENSE-2.txt
%python3_only %{_bindir}/*
%python3_only %{_mandir}/man1/*
%{python_sitelib}/odf
%{python_sitelib}/%{modname}*

%changelog
