#
# spec file for package python-xmlschema
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
%define skip_python2 1
Name:           python-xmlschema
Version:        1.5.2
Release:        0
Summary:        An XML Schema validator and decoder
License:        MIT
URL:            https://github.com/sissaschool/xmlschema
Source:         https://files.pythonhosted.org/packages/source/x/xmlschema/xmlschema-%{version}.tar.gz
# PATCH-FIX-UPSTREAM remove_shebang.patch gh#sissaschool/xmlschema#210 mcepl@suse.com
# Remove superfluous shebang
Patch0:         remove_shebang.patch
BuildRequires:  %{python_module elementpath >= 2.1.2}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-elementpath >= 2.1.2
Requires:       python-lxml
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
The *xmlschema* library is an implementation of `XML Schema <http://www.w3.org/2001/XMLSchema>`_
for Python.

%prep
%autosetup -p1 -n xmlschema-%{version}

# do not hardcode versions
sed -i -e 's:~=:>=:' setup.py
# do not bother with memory validation
rm tests/check_memory.py
rm tests/test_memory.py

%build
export LANG="en_US.UTF8"
%python_build

%install
export LANG="en_US.UTF8"
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# Prepare for update-alternatives usage
for p in json2xml validate xml2json; do
    %python_clone -a %{buildroot}%{_bindir}/xmlschema-$p
done

%check
export LANG="en_US.UTF8"
%pytest tests/

%post
%python_install_alternative xmlschema-json2xml
%python_install_alternative xmlschema-validate
%python_install_alternative xmlschema-xml2json

%postun
%python_uninstall_alternative xmlschema-json2xml
%python_uninstall_alternative xmlschema-validate
%python_uninstall_alternative xmlschema-xml2json

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/xmlschema-json2xml
%python_alternative %{_bindir}/xmlschema-validate
%python_alternative %{_bindir}/xmlschema-xml2json

%changelog
