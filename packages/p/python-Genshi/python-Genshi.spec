#
# spec file for package python-Genshi
#
# Copyright (c) 2025 SUSE LLC
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


%define oldpython python
%{?sle15_python_module_pythons}
Name:           python-Genshi
Version:        0.7.9
Release:        0
Summary:        A toolkit for generation of output for the web
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://genshi.edgewall.org/
Source:         https://files.pythonhosted.org/packages/source/G/Genshi/Genshi-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM remove_six.patch gh#edgewall/genshi!92 mcepl@suse.com
# remove six
Patch0:         remove_six.patch
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
Requires:       python-Babel
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
%autosetup -p1 -n Genshi-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# remove accidentally installed source files
%python_expand find %{buildroot}%{$python_sitearch}/genshi -name '*.c' -delete
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest_arch -v genshi.tests.suite

%files %{python_files}
%license COPYING
%doc ChangeLog README.md
%{python_sitearch}/genshi/
%{python_sitearch}/[Gg]enshi-%{version}*-info

%files -n %{name}-doc
%doc doc
%doc examples

%changelog
