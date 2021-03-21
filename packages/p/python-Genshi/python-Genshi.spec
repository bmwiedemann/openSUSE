#
# spec file for package python-Genshi
#
# Copyright (c) 2021 SUSE LLC
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
%define oldpython python
Name:           python-Genshi
Version:        0.7.5
Release:        0
Summary:        A toolkit for generation of output for the web
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://genshi.edgewall.org/
Source:         https://files.pythonhosted.org/packages/source/G/Genshi/Genshi-%{version}.tar.gz
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
Requires:       python-Babel
Requires:       python-six
Requires:       python-xml
%ifpython2
Obsoletes:      %{oldpython}-genshi < %{version}
Provides:       %{oldpython}-genshi = %{version}
%endif
%python_subpackages

%description
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or
other textual content for output generation on the web. The major
feature is a template language, which is heavily inspired by Kid.

%package -n %{name}-doc
Summary:        A toolkit for generation of output for the web - Documentation
Group:          Development/Libraries/Python
Provides:       %{python_module Genshi-doc = %{version}}
BuildArch:      noarch

%description -n %{name}-doc
Genshi is a Python library that provides an integrated set of
components for parsing, generating, and processing HTML, XML or
other textual content for output generation on the web. The major
feature is a template language, which is heavily inspired by Kid.

This package contains documentation and examples.

%prep
%setup -q -n Genshi-%{version}

%build
%python_build

%install
%python_install
# remove accidentally installed source files
%python_expand find %{buildroot}%{$python_sitearch}/genshi -name '*.c' -delete
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# install (flavor-agnostic) examples
mkdir -p %{buildroot}%{_docdir}/%{name}-doc/
cp -r examples %{buildroot}%{_docdir}/%{name}-doc/
sed -i '1{s/env python.*/python3/}' %{buildroot}%{_docdir}/%{name}-doc/examples/tutorial/geddit/controller.py
%fdupes %{buildroot}%{_docdir}/%{name}-doc/

%check
%if %{suse_version} < 1550
# calling unittest directly fails on Leap
%python_exec setup.py test
%else
%pyunittest_arch -v genshi.tests.suite
%endif

%files %{python_files}
%license COPYING
%doc ChangeLog README.txt
%{python_sitearch}/genshi/
%{python_sitearch}/Genshi-%{version}-py%{python_version}.egg-info

%files -n %{name}-doc
%doc doc
%doc %{_docdir}/%{name}-doc/examples

%changelog
