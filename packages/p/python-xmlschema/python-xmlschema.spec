#
# spec file for package python-xmlschema
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
Name:           python-xmlschema
Version:        3.3.1
Release:        0
Summary:        An XML Schema validator and decoder
License:        MIT
URL:            https://github.com/sissaschool/xmlschema
Source:         https://files.pythonhosted.org/packages/source/x/xmlschema/xmlschema-%{version}.tar.gz
BuildRequires:  %{python_module elementpath >= 3.0.0}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-elementpath >= 3.0.0
Requires:       python-lxml
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
%pyproject_wheel

%install
export LANG="en_US.UTF8"
%pyproject_install
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
%{python_sitelib}/xmlschema
%{python_sitelib}/xmlschema-%{version}.dist-info
%python_alternative %{_bindir}/xmlschema-json2xml
%python_alternative %{_bindir}/xmlschema-validate
%python_alternative %{_bindir}/xmlschema-xml2json

%changelog
