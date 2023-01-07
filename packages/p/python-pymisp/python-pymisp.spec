#
# spec file for package python-pymisp
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define misp_objects_revision 66a9b8eee70ce3ac7ff5f2225cd7f78fe4630143
Name:           python-pymisp
Version:        2.4.166
Release:        0
Summary:        Python API for MISP
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/MISP/PyMISP
Source0:        https://github.com/MISP/PyMISP/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# github tarball misses the misp-objects subproject data
Source1:        https://github.com/MISP/misp-objects/archive/%{misp_objects_revision}.tar.gz#/misp-objects.tar.gz
# pypi tarball missing some files: https://github.com/MISP/PyMISP/issues/554
#Source:         https://files.pythonhosted.org/packages/source/p/pymisp/pymisp-%%{version}.tar.gz
# packaging tool
Source2:        update-misp-objects.sh
Source3:        python-pymisp-doc-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jsonschema
Requires:       python-oletools
Requires:       python-python-dateutil
Requires:       python-requests
Recommends:     %{name}-doc
Recommends:     python-extract-msg >= 0.28.0
Recommends:     python-magic
Recommends:     python-reportlab
Suggests:       python-pydeep
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module Deprecated}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module oletools}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module python-magic}
BuildRequires:  %{python_module reportlab}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module requests}
# /SECTION
# SECTION docs
BuildRequires:  python3-CommonMark
BuildRequires:  python3-Sphinx
BuildRequires:  python3-recommonmark
BuildRequires:  python3-sphinx-autodoc-typehints
# /SECTION
Requires:       python-Deprecated
%python_subpackages

%package -n %{name}-doc
Summary:        Examples and Documentation for %{name}
Group:          Documentation/HTML

%description
PyMISP is a Python library to access MISP platforms via their REST API.

PyMISP allows you to fetch events, add or update events/attributes, add or update samples or search for attributes.

%description -n %{name}-doc
Examples and HTML documentation for %{name}.

%prep
%setup -q -n PyMISP-%{version}
%setup -T -D -b 1 -n PyMISP-%{version}
mv ../misp-objects-*/* pymisp/data/misp-objects/
find pymisp examples -name "*.py" -type f -exec sed -i '1s/^#!.*//' '{}' \+
find examples -name "*.py" -type f -exec chmod -x '{}' \+

%build
%python_build
pushd docs
export LANG=en_US.UTF-8
make %{?_smp_mflags} html
rm build/html/.buildinfo
popd

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# requires optional dependencies which we don't have (extract_msg, RTFDE etc.)
rm tests/test_emailobject.py
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%files -n %{name}-doc
%doc examples docs/build/html

%changelog
