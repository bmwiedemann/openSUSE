#
# spec file for package python-rdflib
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "doc"
%bcond_without doc
%define psuffix -doc
%else
%bcond_with doc
%define psuffix %{nil}
%endif

# Tests don't work and cause a dependency loop with python-SPARQLWrapper
%bcond_with tests
Name:           python-rdflib%{psuffix}
Version:        7.0.0
Release:        0
Summary:        A Python library for working with RDF
License:        BSD-3-Clause
URL:            http://rdflib.net/
Source:         https://files.pythonhosted.org/packages/source/r/rdflib/rdflib-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%if %{with tests}
BuildRequires:  %{python_module SPARQLWrapper}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pytest}
%endif

%if %{with doc}
BuildRequires:  %{python_module rdflib = %{version}}
BuildRequires:  python3-Sphinx
BuildRequires:  python3-myst-parser
BuildRequires:  python3-sphinx-autodoc-typehints
BuildRequires:  python3-sphinxcontrib-apidoc
Provides:       %{python_module rdflib-doc = %{version}}
%else
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module isodate}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xml}
Requires:       python-html5lib
Requires:       python-isodate
Requires:       python-pyparsing
%python_subpackages
%endif

%description
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information. The library contains an RDF/XML
parser/serializer that conforms to the RDF/XML Syntax Specification (Revised).
The library also contains both in-memory and persistent Graph backends.

%prep
%autosetup -p1 -n rdflib-%{version}
# remove unwanted shebang
find rdflib -name "*.py" | xargs sed -i '1 { /^#!/ d }'
chmod -x rdflib/plugins/parsers/notation3.py

%if %{without doc}
%build
%pyproject_wheel
%endif

%install
%if %{with doc}
# Build the docs, we need the module queryable
pushd docs
PYTHONPATH=%{buildroot}%{python3_sitelib} %make_build html

# Remove hidden file
rm -r _build/html/.buildinfo
popd
%fdupes docs/_build/html
%else

%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/rdfs2dot
%python_clone -a %{buildroot}%{_bindir}/rdfpipe
%python_clone -a %{buildroot}%{_bindir}/rdfgraphisomorphism
%python_clone -a %{buildroot}%{_bindir}/rdf2dot
%python_clone -a %{buildroot}%{_bindir}/csv2rdf
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with tests}
%check
%pytest
%endif

%if %{with doc}
%files -n %{name}
%doc docs/_build/html

%else

%post
%python_install_alternative rdfs2dot
%python_install_alternative rdfpipe
%python_install_alternative rdfgraphisomorphism
%python_install_alternative rdf2dot
%python_install_alternative csv2rdf

%postun
%python_uninstall_alternative rdfs2dot
%python_uninstall_alternative rdfpipe
%python_uninstall_alternative rdfgraphisomorphism
%python_uninstall_alternative rdf2dot
%python_uninstall_alternative csv2rdf

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/csv2rdf
%python_alternative %{_bindir}/rdf2dot
%python_alternative %{_bindir}/rdfgraphisomorphism
%python_alternative %{_bindir}/rdfpipe
%python_alternative %{_bindir}/rdfs2dot
%{python_sitelib}/rdflib
%{python_sitelib}/rdflib-%{version}.dist-info
%endif

%changelog
