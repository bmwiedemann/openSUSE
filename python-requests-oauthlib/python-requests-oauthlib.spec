#
# spec file for package python-requests-oauthlib
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
Name:           python-requests-oauthlib
Version:        1.2.0
Release:        0
Summary:        OAuthlib authentication support for Requests
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/requests/requests-oauthlib
Source:         https://files.pythonhosted.org/packages/source/r/requests-oauthlib/requests-oauthlib-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module oauthlib >= 3.0.0}
BuildRequires:  %{python_module requests >= 2.0.0}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-oauthlib >= 3.0.0
Requires:       python-requests >= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
This project provides first-class OAuth library support for Requests.

%prep
%setup -q -n requests-oauthlib-%{version}

%build
%python_build

%install
%python_install

#hardlink duplicated files
%fdupes %{buildroot}

%check
# Three tests initiate network traffic to httpbin.org
%python_exec -m nose -e '(testCanPostBinaryData|test_content_type_override|test_url_is_native_str)'

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst README.rst
%{python_sitelib}/*

%changelog
