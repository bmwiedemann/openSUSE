#
# spec file for package python-treq
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
Name:           python-treq
Version:        18.6.0
Release:        0
Summary:        HTTP library inspired by python-requests
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/twisted/treq
Source:         https://files.pythonhosted.org/packages/source/t/treq/treq-%{version}.tar.gz
Patch0:         python37.patch
BuildRequires:  %{python_module Twisted >= 16.4.0}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module httpbin}
BuildRequires:  %{python_module incremental}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module requests >= 2.1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted >= 16.4.0
Requires:       python-attrs
Requires:       python-incremental
Requires:       python-requests >= 2.1.0
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
treq is an HTTP library inspired by requests but written on top of Twisted’s Agents.
It provides a simple, higher level API for making HTTP requests when using Twisted.

%prep
%setup -q -n treq-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/treq

%check
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} %{_bindir}/trial-%{$python_bin_suffix} treq

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/treq
%{python_sitelib}/treq-%{version}-py*.egg-info/

%changelog
