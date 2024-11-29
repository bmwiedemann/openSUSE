#
# spec file for package python-discogs-client
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-discogs-client
Version:        2.7.1
Release:        0
Summary:        Python API client for Discogs
License:        BSD-2-Clause
URL:            https://github.com/joalla/discogs_client/
Source:         https://github.com/joalla/discogs_client/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module oauthlib}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-oauthlib
Requires:       python-python-dateutil
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
This is the official Discogs API client for Python. It enables you to query the
Discogs database for information on artists, releases, labels, users,
Marketplace listings, and more. It also supports OAuth 1.0a authorization,
which allows you to change user data such as profile information, collections
and wantlists, inventory, and orders.

%prep
%autosetup -p1 -n discogs_client-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v discogs_client/tests

%files %{python_files}
%license LICENSE
%doc README.mkd
%{python_sitelib}/discogs_client
%{python_sitelib}/python3_discogs_client-%{version}.dist-info

%changelog
