#
# spec file for package python-rdflib
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
# Tests don't work and cause a dependency loop with python-SPARQLWrapper
%bcond_with tests
Name:           python-rdflib
Version:        4.2.2
Release:        0
Summary:        A Python library for working with RDF
License:        BSD-3-Clause
URL:            http://rdflib.net/
Source:         https://files.pythonhosted.org/packages/source/r/rdflib/rdflib-%{version}.tar.gz
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module isodate}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-2to3
BuildRequires:  python3-Sphinx
Requires:       python-SPARQLWrapper
Requires:       python-flake8
Requires:       python-html5lib
Requires:       python-isodate
Requires:       python-pyparsing
Requires:       python-xml
BuildArch:      noarch
%if %{with tests}
BuildRequires:  %{python_module SPARQLWrapper}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module nose}
%endif
%python_subpackages

%description
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information. The library contains an RDF/XML
parser/serializer that conforms to the RDF/XML Syntax Specification (Revised).
The library also contains both in-memory and persistent Graph backends.

%package -n %{name}-doc
Summary:        A Python library for working with RDF
Provides:       %{python_module rdflib-doc = %{version}}

%description -n %{name}-doc
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information. The library contains an RDF/XML
parser/serializer that conforms to the RDF/XML Syntax Specification (Revised).
The library also contains both in-memory and persistent Graph backends.

%prep
%setup -q -n rdflib-%{version}
# remove unwanted shebang
find rdflib -name "*.py" | xargs sed -i '1 { /^#!/ d }'

%build
%python_build

pushd docs
make %{?_smp_mflags} html
# Remove hidden file
rm -r _build/html/.buildinfo
popd

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%fdupes docs/_build/html

%if %{with tests}
%check
%python_exec setup.py -q test
%endif

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md CONTRIBUTORS README.md
%python3_only %{_bindir}/csv2rdf
%python3_only %{_bindir}/rdf2dot
%python3_only %{_bindir}/rdfgraphisomorphism
%python3_only %{_bindir}/rdfpipe
%python3_only %{_bindir}/rdfs2dot
%{python_sitelib}/rdflib/
%{python_sitelib}/rdflib-%{version}-py*.egg-info

%files -n %{name}-doc
%doc docs/_build/html

%changelog
