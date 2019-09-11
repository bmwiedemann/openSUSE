#
# spec file for package python-betamax
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
Name:           python-betamax
Version:        0.8.1
Release:        0
Summary:        A VCR imitation for python-requests
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/sigmavirus24/betamax
Source:         https://pypi.io/packages/source/b/betamax/betamax-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
Betamax is a VCR_ imitation for requests. This will make mocking out requests
much easier.

%prep
%setup -q -n betamax-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
