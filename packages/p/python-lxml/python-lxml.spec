#
# spec file for package python-lxml
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
Name:           python-lxml
Version:        5.2.2
Release:        0
Summary:        Pythonic XML processing library
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://lxml.de/
Source0:        https://files.pythonhosted.org/packages/source/l/lxml/lxml-%{version}.tar.gz
Source1:        https://lxml.de/lxmldoc-4.5.2.pdf
Source99:       python-lxml.rpmlintrc
# PATCH-FIX-OPENSUSE Skip a test under libxml2 2.10.4+
# https://bugs.launchpad.net/lxml/+bug/2016939
Patch1:         skip-test-under-libxml2-2.10.4.patch
# PATCH-FIX-OPENSUSE Skip a test under libxml2 2.11.1+
# https://bugs.launchpad.net/lxml/+bug/2018522
Patch2:         skip-test-under-libxml2-2.11.1.patch
BuildRequires:  %{python_module Cython >= 3.0.7}
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module cssselect >= 0.9.1}
BuildRequires:  %{python_module setuptools >= 18.0.1}
BuildRequires:  fdupes
%if 0%{?suse_version} == 1500
# Assume the best that the old libxml2 in SLE15 is patched for  https://gitlab.gnome.org/GNOME/libxml2/-/issues/378 (CVE-2022-2309)
BuildRequires:  libxml2-devel
%else
BuildRequires:  libxml2-devel >= 2.10.2
%endif
BuildRequires:  libxslt-devel >= 1.1.27
BuildRequires:  python-rpm-macros
Requires:       python-cssselect >= 0.9.1
%python_subpackages

%description
lxml is a Pythonic binding for the libxml2 and libxslt libraries. It
provides convenient access to these libraries using the ElementTree
API. It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT and C14N.

%if 0%{?suse_version} > 1500
%package -n %{name}-doc
Summary:        Documentation for python-lxml, an XML processing library
Group:          Documentation/Other
BuildArch:      noarch

%description -n %{name}-doc
lxml is a Pythonic binding for the libxml2 and libxslt libraries. It
provides convenient access to these libraries using the ElementTree
API. It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT and C14N.

This package contains documentation for lxml (HTML and PDF).
%endif

%package devel
Summary:        Development files for python-lxml
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}

%description devel
lxml is a Pythonic binding for the libxml2 and libxslt libraries. It
provides convenient access to these libraries using the ElementTree
API. It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT and C14N.

This package contains header files needed to use lxml's C API.

%prep
%autosetup -p1 -n lxml-%{version}

cp %{SOURCE1} .

# remove generated files
find -name '*.c' -delete -print
rm src/lxml/lxml.etree.h
rm src/lxml/lxml.etree_api.h

%build
export CFLAGS="%{optflags}"
%python_build build_ext -i --with-cython

%check
# The tests fail on SLE 11 due to broken incremental parsing in libxml2
export CFLAGS="%{optflags}"
export LANG=en_US.UTF-8
export PYTHONUNBUFFERED=x
# cyclic dependency between html5lib and lxml
rm -v src/lxml/html/tests/test_html5parser.py
%python_exec test.py

%install
%python_install
%python_expand %fdupes %{buildroot}

%files %{python_files}
%license LICENSES.txt
%doc CHANGES.txt CREDITS.txt README.rst
%{python_sitearch}/lxml/
%{python_sitearch}/lxml-%{version}-py%{python_version}.egg-info
%exclude %{python_sitearch}/lxml/*.h
%exclude %{python_sitearch}/lxml/includes/*.h

%if 0%{?suse_version} > 1500
%files -n %{name}-doc
%license LICENSES.txt
%endif
%doc doc/html
%doc lxmldoc-*.pdf

%files %{python_files devel}
%license LICENSES.txt
%{python_sitearch}/lxml/*.h
%{python_sitearch}/lxml/includes/*.h

%changelog
