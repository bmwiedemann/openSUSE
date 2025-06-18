#
# spec file for package python-python-openid-teams
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2018 Neal Gompa <ngompa13@gmail.com>.
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


Name:           python-python-openid-teams
Version:        1.1
Release:        0
Summary:        Teams extension for python-openid
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/puiterwijk/python-openid-teams
Source:         https://github.com/puiterwijk/python-openid-teams/archive/v%{version}/python-openid-teams-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-python3-openid
%python_subpackages

%description
Teams extension implementation for python-openid.

%prep
%setup -q -n python-openid-teams-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%license COPYING
%{python_sitelib}/openid_teams
%{python_sitelib}/python[-_]openid[-_]teams-%{version}*-info

%changelog
