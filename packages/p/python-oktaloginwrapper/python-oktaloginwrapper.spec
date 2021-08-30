#
# spec file for package python-oktaloginwrapper
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


%define skip_python2 1
Name:           python-oktaloginwrapper
Version:        0.2.2
Release:        0
Summary:        Okta login without API token
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/eliroca/OktaLoginWrapper
Source:         https://github.com/eliroca/OktaLoginWrapper/archive/%{version}.tar.gz#/OktaLoginWrapper-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
This modules provides a way for scripts to access resources behind
an Okta SSO solution, without the need for an API token.

%prep
%autosetup -n OktaLoginWrapper-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*

%changelog
