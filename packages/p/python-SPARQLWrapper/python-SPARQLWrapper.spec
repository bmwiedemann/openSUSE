#
# spec file for package python-SPARQLWrapper
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-SPARQLWrapper
Version:        1.8.2
Release:        0
Summary:        SPARQL Endpoint interface to Python
License:        W3C
URL:            http://sparql-wrapper.sourceforge.net/
Source:         https://files.pythonhosted.org/packages/source/S/SPARQLWrapper/SPARQLWrapper-%{version}.tar.gz
# Only used during installation
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-tools
Requires:       python-rdflib >= 4.0
BuildArch:      noarch
%python_subpackages

%description
This is a wrapper around a SPARQL service. It helps in creating the
query URI and, possibly, convert the result into a more manageable
format.

%prep
%setup -q -n SPARQLWrapper-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if %{python3_version_nodots} > 34
# taken from https://github.com/RDFLib/sparqlwrapper/blob/master/run_tests_py3.sh
cp -r %{buildroot}%{python_sitelib}/SPARQLWrapper test/
2to3 -wn --no-diffs test
sed -i.bak s/urllib2._opener/urllib.request._opener/g test/wrapper_test.py
python3 -m pytest test
%else
python -m pytest test
%endif

%files %{python_files}
%license LICENSE.txt
%doc README.md AUTHORS.md
%{python_sitelib}/SPARQLWrapper/
%{python_sitelib}/SPARQLWrapper-%{version}-py*.egg-info

%changelog
