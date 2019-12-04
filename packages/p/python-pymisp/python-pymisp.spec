#
# spec file for package python-pymisp
#
# Copyright (c) 2019 SUSE LLC
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
Name:           python-pymisp
Version:        2.4.117.3
Release:        0
Summary:        Python API for MISP
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/MISP/PyMISP
Source:         https://files.pythonhosted.org/packages/source/p/pymisp/pymisp-%{version}.tar.gz
# Internal script for generating changelog
Source1:        changelog.sh
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jsonschema
Requires:       python-python-dateutil
Requires:       python-requests
Recommends:     %{name}-doc
Recommends:     python-magic
Suggests:       python-pydeep
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module Deprecated}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module python-magic}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module requests}
BuildRequires:  python2-cachetools
BuildRequires:  python2-enum34
BuildRequires:  python2-functools32
# /SECTION
# SECTION docs
BuildRequires:  python3-CommonMark
BuildRequires:  python3-Sphinx
BuildRequires:  python3-recommonmark
BuildRequires:  python3-sphinx-autodoc-typehints
# /SECTION
%ifpython2
Requires:       python2-cachetools
Requires:       python2-enum34
Requires:       python2-functools32
%endif
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
%setup -q -n pymisp-%{version}
find pymisp examples -name "*.py" -type f -exec sed -i '1s/^#!.*//' '{}' \+

%build
%python_build
pushd docs
export LANG=en_US.UTF-8
make %{?_smp_mflags} html
rm build/html/.buildinfo
popd

%install
%python_install
%{python_expand %fdupes %{buildroot}%{$python_sitelib}}

%check
# Requires internet access and a MISP-instance
rm tests/test.py
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%files -n %{name}-doc
%doc examples docs/build/html

%changelog
