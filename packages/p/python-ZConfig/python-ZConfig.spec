#
# spec file for package python-ZConfig
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
Name:           python-ZConfig
Version:        4.1
Release:        0
Summary:        Structured Configuration Library
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/ZConfig
Source:         https://files.pythonhosted.org/packages/source/Z/ZConfig/zconfig-%{version}.tar.gz
# PATCH-FIX-UPSTREAM: gh#zopefoundation/ZConfig#97
Patch1:         py313.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module manuel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zope.testrunner}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
ZConfig is a configuration library intended for general use. It supports a
hierarchical schema-driven configuration model that allows a schema to specify
data conversion routines written in Python. ZConfig's model is very different
from the model supported by the ConfigParser module found in Python's standard
library, and is more suitable to configuration-intensive applications.

ZConfig schema are written in an XML-based language and are able to "import"
schema components provided by Python packages. Since components are able to
bind to conversion functions provided by Python code in the package (or
elsewhere), configuration objects can be arbitrarily complex, with values that
have been verified against arbitrary constraints. This makes it easy for
applications to separate configuration support from configuration loading even
with configuration data being defined and consumed by a wide range of separate
packages.

%package        doc
Summary:        Structured Configuration Library
Requires:       %{name} = %{version}

%description    doc
This package contains documentation files for %{name}.

%prep
%autosetup -p1 -n zconfig-%{version}
rm -rf ZConfig.egg-info
rm docs/make.bat
# test works only in git repo
rm src/ZConfig/tests/test_readme.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/zconfig
%python_clone -a %{buildroot}%{_bindir}/zconfig_schema2html

%check
export LANG=en_US.UTF8
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} zope-testrunner-%{$python_bin_suffix} -v --test-path=src

%post
%python_install_alternative zconfig zconfig_schema2html

%postun
%python_uninstall_alternative zconfig

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst COPYRIGHT.txt PKG-INFO README.rst
%python_alternative %{_bindir}/zconfig
%python_alternative %{_bindir}/zconfig_schema2html
%{python_sitelib}/ZConfig
%{python_sitelib}/ZConfig-%{version}.dist-info

%files %{python_files doc}
%doc docs/

%changelog
