#
# spec file for package python
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Neal Gompa <ngompa13@gmail.com>.
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


%global short_name ordered-set
%global dir_name ordered_set
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{short_name}
Version:        3.1.1
Release:        0
Summary:        Custom MutableSet that remembers its order
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/LuminosoInsight/ordered-set
Source0:        https://pypi.python.org/packages/source/o/%{short_name}/%{short_name}-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
An OrderedSet is a custom MutableSet that remembers its order, so that every
entry has an index that can be looked up.

%prep
%autosetup -n %{short_name}-%{version} -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test.py

%files %{python_files}
%license MIT-LICENSE
%doc README.md
%{python_sitelib}/%{dir_name}-*
%{python_sitelib}/%{dir_name}.py*
%pycache_only %{python3_sitelib}/__pycache__/%{dir_name}.*

%changelog
