#
# spec file
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


#
%define modname odfpy
%define binaries csv2ods mailodf odf2mht odf2xhtml odf2xml odfimgimport odflint odfmeta odfoutline odfuserfield xml2odf
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{modname}
Version:        1.4.2
Release:        0
Summary:        Python API and tools to manipulate OpenDocument files
License:        Apache-2.0 OR GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/eea/odfpy
Source:         https://github.com/eea/odfpy/archive/refs/tags/release-%{version}.tar.gz
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-defusedxml
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
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
%setup -q -n %{modname}-release-%{version}
sed -i "1d" odf/{userfield,odf2xhtml,manifest,element,elementtypes,load,odfmanifest,thumbnail}.py # Fix non-executable scripts

%build
%python_build

%install
%python_install
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_mandir}/man1/$b.1
  %python_clone -a %{buildroot}%{_bindir}/$b
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
for b in %{binaries}; do
  %python_install_alternative $b $b.1
done

%postun
for b in %{binaries}; do
  %python_uninstall_alternative $b
done

%files %{python_files}
%license APACHE-LICENSE-2.0.txt GPL-LICENSE-2.txt
%python_alternative %{_bindir}/csv2ods
%python_alternative %{_bindir}/mailodf
%python_alternative %{_bindir}/odf2mht
%python_alternative %{_bindir}/odf2xhtml
%python_alternative %{_bindir}/odf2xml
%python_alternative %{_bindir}/odfimgimport
%python_alternative %{_bindir}/odflint
%python_alternative %{_bindir}/odfmeta
%python_alternative %{_bindir}/odfoutline
%python_alternative %{_bindir}/odfuserfield
%python_alternative %{_bindir}/xml2odf
%python_alternative %{_mandir}/man1/csv2ods.1%{ext_man}
%python_alternative %{_mandir}/man1/mailodf.1%{ext_man}
%python_alternative %{_mandir}/man1/odf2mht.1%{ext_man}
%python_alternative %{_mandir}/man1/odf2xhtml.1%{ext_man}
%python_alternative %{_mandir}/man1/odf2xml.1%{ext_man}
%python_alternative %{_mandir}/man1/odfimgimport.1%{ext_man}
%python_alternative %{_mandir}/man1/odflint.1%{ext_man}
%python_alternative %{_mandir}/man1/odfmeta.1%{ext_man}
%python_alternative %{_mandir}/man1/odfoutline.1%{ext_man}
%python_alternative %{_mandir}/man1/odfuserfield.1%{ext_man}
%python_alternative %{_mandir}/man1/xml2odf.1%{ext_man}
%{python_sitelib}/odf
%{python_sitelib}/%{modname}*

%changelog
