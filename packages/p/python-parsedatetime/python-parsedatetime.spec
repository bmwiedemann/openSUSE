#
# spec file for package python-parsedatetime
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
Name:           python-parsedatetime
Version:        2.6
Release:        0
Summary:        Python module to parse human-readable date/time text
License:        Apache-2.0
Group:          Development/Libraries/Python
URL:            https://github.com/regebro/parsedatetime
Source:         https://files.pythonhosted.org/packages/source/p/parsedatetime/parsedatetime-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python module to parse human-readable date/time strings.

%prep
%setup -q -n parsedatetime-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.txt CHANGES.txt README.rst
%{python_sitelib}/parsedatetime/
%{python_sitelib}/parsedatetime-%{version}-py*.egg-info

%changelog
