#
# spec file for package python-dogpile.cache
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-dogpile.cache
Version:        1.3.3
Release:        0
%define modname dogpile.cache
%define modver  1_3_3
Summary:        A caching front-end based on the Dogpile lock
License:        BSD-3-Clause
URL:            https://github.com/sqlalchemy/dogpile.cache
Source:         https://github.com/sqlalchemy/%{modname}/archive/refs/tags/rel_%{modver}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module Mako}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module decorator >= 4.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 5}
BuildRequires:  %{python_module stevedore > 3.0.0}
BuildRequires:  %{python_module typing-extensions >= 4.0.1}
BuildRequires:  %{python_module wheel}
Requires:       python-decorator >= 4.0.0
Requires:       python-stevedore >= 3.0.0
%if 0%{?python_version_nodots} < 311
Requires:       python-typing-extensions >= 4.0.1
%endif
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
%setup -q -n %{modname}-rel_%{modver}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/dogpile
%{python_sitelib}/dogpile_cache-%{version}.dist-info

%changelog
