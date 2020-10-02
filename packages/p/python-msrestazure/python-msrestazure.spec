#
# spec file for package python-msrestazure
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-msrestazure
Version:        0.6.4
Release:        0
Summary:        AutoRest swagger generator - Azure-specific module
License:        MIT
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/msrestazure
Source:         https://files.pythonhosted.org/packages/source/m/msrestazure/msrestazure-%{version}.tar.gz
Source1:        LICENSE.md
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-adal < 2.0.0
Requires:       python-adal >= 0.6.0
Requires:       python-msrest < 2.0.0
Requires:       python-msrest >= 0.6.0
Requires:       python-six
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
AutoRest swagger generator Python client runtime. Azure-specific module.

%prep
%setup -q -n msrestazure-%{version}
cp %{SOURCE1} LICENSE.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files  %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE.md
%{python_sitelib}/*

%changelog
