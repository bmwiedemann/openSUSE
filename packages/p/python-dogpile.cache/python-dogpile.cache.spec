#
# spec file for package python-dogpile.cache
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
%global skip_python2 1
Name:           python-dogpile.cache
Version:        1.0.2
Release:        0
Summary:        A caching front-end based on the Dogpile lock
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sqlalchemy/dogpile.cache
Source:         https://files.pythonhosted.org/packages/source/d/dogpile.cache/dogpile.cache-%{version}.tar.gz
BuildRequires:  %{python_module Mako}
BuildRequires:  %{python_module decorator >= 4.0.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module stevedore}
Requires:       python-decorator >= 4.0.0
BuildRequires:  %{python_module six}
Requires:       python-six
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-dogpile.core = %{version}
Obsoletes:      python-dogpile.core < 0.4.1
BuildArch:      noarch
%python_subpackages

%description
A caching API built around the concept of a "dogpile lock", which allows
continued access to an expiring data value while a single thread generates a
new value.

%prep
%setup -q -n dogpile.cache-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/dogpile
%{python_sitelib}/dogpile.cache-%{version}-py%{python_version}.egg-info

%changelog
