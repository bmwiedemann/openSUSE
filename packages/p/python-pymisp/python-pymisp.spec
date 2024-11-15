#
# spec file for package python-pymisp
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


%define skip_python2 1
%define misp_objects_revision 83271573312aebce971a0cf7ffbd04e784a58de3
Name:           python-pymisp
Version:        2.5.1
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
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-oletools
Requires:       python-Deprecated >= 1.2.14
Requires:       python-python-dateutil >= 2.8.2
Requires:       python-requests >= 2.31.0
Recommends:     %{name}-doc
Recommends:     python-extract-msg >= 0.28.0
Recommends:     python-magic >= 0.4.27
Recommends:     python-reportlab
Recommends:     python3-beautifulsoup4 >= 4.12.2
Recommends:     python3-publicsuffixlist
Recommends:     python3-urllib3
Recommends:     python3-validators >= 0.20.0
Suggests:       python-pydeep
# Other optional requirements which are unavailable in Tumbleweed
#extract_msg = {version = "^0.42.1", optional = true}
#RTFDE = {version = "^0.1.0", optional = true}
#pydeep2 = {version = "^0.5.1", optional = true}
#lief = {version = "^0.13.2", optional = true}
#pyfaup = {version = "^1.2", optional = true}
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module Deprecated >= 1.2.14}
BuildRequires:  %{python_module oletools}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.8.2}
BuildRequires:  %{python_module python-magic >= 0.4.27}
BuildRequires:  %{python_module reportlab}
BuildRequires:  %{python_module requests >= 2.31.0}
BuildRequires:  %{python_module requests-mock}
# /SECTION
# SECTION docs
BuildRequires:  python3-CommonMark
BuildRequires:  python3-Sphinx
BuildRequires:  python3-recommonmark >= 0.7.1
BuildRequires:  python3-sphinx-autodoc-typehints
# /SECTION
%python_subpackages
%{?python_enable_dependency_generator}

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
find examples pymisp/data/misp-objects pymisp/tools -name "*.py" -type f -exec chmod -x '{}' \+
# https://github.com/MISP/PyMISP/issues/1295
sed -i '/CHANGELOG.txt/d' pyproject.toml
# remove the date from python-publicsuffixlist's version. the package python-publicsuffixlist in openSUSE uses the suffix list from the package publicsuffixlist, not the list packaged by python-publicsuffixlist
sed -i -r '/publicsuffixlist/ s/(version *= *"\^[0-9]+\.[0-9]\.[0-9]+)\.[0-9]{8}/\1/' pyproject.toml

%build
%pyproject_wheel
pushd docs
export LANG=en_US.UTF-8
make %{?_smp_mflags} html
rm build/html/.buildinfo
popd

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# requires optional dependencies which we don't have (extract_msg, RTFDE etc.)
rm tests/test_emailobject.py
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pymisp/
%{python_sitelib}/pymisp-%{version}*-info

%files -n %{name}-doc
%doc examples docs/build/html

%changelog
