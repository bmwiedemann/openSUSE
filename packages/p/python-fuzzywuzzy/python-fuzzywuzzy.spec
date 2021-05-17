#
# spec file for package python-fuzzywuzzy
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
Name:           python-fuzzywuzzy
Version:        0.18.0
Release:        0
Summary:        Fuzzy string matching in python
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/seatgeek/fuzzywuzzy
Source:         https://files.pythonhosted.org/packages/source/f/fuzzywuzzy/fuzzywuzzy-%{version}.tar.gz
BuildRequires:  %{python_module Levenshtein}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-Levenshtein >= 0.12
BuildArch:      noarch
%python_subpackages

%description
Fuzzy string matching in python

%prep
%setup -q -n fuzzywuzzy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
