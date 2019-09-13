#
# spec file for package python-inflect
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-inflect
Version:        2.1.0
Release:        0
Summary:        Methods for working on numbers and nouns
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jazzband/inflect
Source0:        https://files.pythonhosted.org/packages/source/i/inflect/inflect-%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words.

%prep
%setup -q -n inflect-%{version}
rm -rf inflect.egg-info

%build
%python_build

%install
%python_install
%python_exec %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%{$python_bin_suffix}

%files %{python_files}
%license LICENSE
%doc CHANGES.txt README.rst
%{python_sitelib}/*

%changelog
