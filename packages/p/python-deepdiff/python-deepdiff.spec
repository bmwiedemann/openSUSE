#
# spec file for package python-deepdiff
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
Name:           python-deepdiff
Version:        3.3.0
Release:        0
Summary:        Deep Difference and Search of any Python object/data
License:        MIT
URL:            https://github.com/seperman/deepdiff
Source:         https://github.com/seperman/deepdiff/archive/v%{version}.tar.gz
BuildRequires:  %{python_module jsonpickle}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jsonpickle
BuildArch:      noarch
%python_subpackages

%description
Deep Difference of dictionaries, iterables, strings and other objects.
Search for objects within other objects.
Hash any object based on their content.

%prep
%setup -q -n deepdiff-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover

%files %{python_files}
%license LICENSE
%doc README.txt
%{python_sitelib}/*

%changelog
