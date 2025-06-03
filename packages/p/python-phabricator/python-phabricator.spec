#
# spec file for package python-phabricator
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


Name:           python-phabricator
Version:        0.9.1
Release:        0
Summary:        Phabricator API Bindings
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/disqus/python-phabricator
Source:         https://github.com/disqus/python-phabricator/archive/refs/tags/%{version}.tar.gz#/phabricator-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.22
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module requests >= 2.22}
BuildRequires:  %{python_module responses >= 0.12}
# /SECTION
%python_subpackages

%description
Phabricator API Bindings

%prep
%setup -q -n python-phabricator-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/phabricator
%{python_sitelib}/phabricator-%{version}*-info

%changelog
