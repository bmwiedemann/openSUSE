#
# spec file for package python-lxml
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


Name:           python-lxml
Version:        4.9.2
Release:        0
Summary:        Pythonic XML processing library
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://lxml.de/
Source0:        https://files.pythonhosted.org/packages/source/l/lxml/lxml-%{version}.tar.gz
Source1:        https://lxml.de/lxmldoc-4.5.2.pdf
Source99:       python-lxml.rpmlintrc
BuildRequires:  %{python_module Cython >= 0.29.7}
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module cssselect >= 0.9.1}
BuildRequires:  %{python_module setuptools >= 18.0.1}
BuildRequires:  fdupes
BuildRequires:  libxml2-devel >= 2.10.2
BuildRequires:  libxslt-devel >= 1.1.27
BuildRequires:  python-rpm-macros
Requires:       python-cssselect >= 0.9.1
%python_subpackages

%description
lxml is a Pythonic binding for the libxml2 and libxslt libraries. It
provides convenient access to these libraries using the ElementTree
API. It extends the ElementTree API significantly to offer support for XPath,
RelaxNG, XML Schema, XSLT and C14N.

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
%setup -q -n lxml-%{version}
cp %{SOURCE1} .

# remove generated files
find -name '*.c' -delete -print
rm src/lxml/lxml.etree.h
rm src/lxml/lxml.etree_api.h

%build
export CFLAGS="%{optflags}"
%python_build --with-cython

%check
# The tests fail on SLE 11 due to broken incremental parsing in libxml2
export CFLAGS="%{optflags}"
export LANG=en_US.UTF-8
export PYTHONUNBUFFERED=x
%if 0%{?have_python2}
%{python_expand # define python version for test:
export PYTHON="$python"
%make_build test
}
%endif
%if 0%{?have_python3}
%{python_expand # define python version for test:
export PYTHON3="$python"
%make_build test3
}
%endif

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

%files %{python_files devel}
%license LICENSES.txt
%{python_sitearch}/lxml/*.h
%{python_sitearch}/lxml/includes/*.h

%files -n %{name}-doc
%license LICENSES.txt
%doc doc/html
%doc lxmldoc-*.pdf

%changelog
