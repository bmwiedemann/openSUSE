#
# spec file for package python-discogs-client
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
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
Name:           python-discogs-client
Version:        2.2.2
Release:        0
Summary:        Official Python API client for Discogs
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/discogs/discogs_client
Source:         https://files.pythonhosted.org/packages/source/d/discogs-client/discogs-client-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/discogs/discogs_client/master/LICENSE
BuildRequires:  %{python_module oauthlib}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-oauthlib
Requires:       python-requests
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
This is the official Discogs API client for Python. It enables you to query the
Discogs database for information on artists, releases, labels, users,
Marketplace listings, and more. It also supports OAuth 1.0a authorization,
which allows you to change user data such as profile information, collections
and wantlists, inventory, and orders.

%prep
%setup -q -n discogs-client-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%{python_sitelib}/discogs_client/
%{python_sitelib}/discogs_client-%{version}-py*.egg-info

%changelog
