#
# spec file for package python-PyNamecheap
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-PyNamecheap
Version:        0.0.3
Release:        0
Summary:        Namecheap API client in Python
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/Bemmu/PyNamecheap
Source:         https://files.pythonhosted.org/packages/source/P/PyNamecheap/PyNamecheap-%{version}.tar.gz
Source1:        LICENSE.txt
Source2:        README.md
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
BuildArch:      noarch

%python_subpackages

%description
Namecheap API client in Python

%prep
%setup -q -n PyNamecheap-%{version}
cp %{SOURCE1} LICENSE.txt
cp %{SOURCE2} README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
