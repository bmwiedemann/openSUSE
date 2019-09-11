#
# spec file for package python-twython
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-twython
Version:        3.7.0
Release:        0
License:        MIT
Summary:        Python wrapper for the Twitter API
Url:            https://github.com/ryanmcgrath/twython
Group:          Development/Languages/Python
Source:         https://github.com/ryanmcgrath/twython/archive/%{version}.tar.gz#/twython-%{version}.tar.gz
Patch:          get_oembed_tweet-endpoint.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module requests >= 2.1.0}
BuildRequires:  %{python_module requests-oauthlib >= 0.4.0}
BuildRequires:  %{python_module responses}
# PyJWT 1.4.2 isnt compatible with single-spec
BuildRequires:  %{python_module PyJWT > 1.4.2}
Requires:       python-requests >= 2.1.0
Requires:       python-requests-oauthlib >= 0.4.0
BuildArch:      noarch

%python_subpackages

%description
Twython is a Python library providing a way to access Twitter data.

Features include:

- Query data for:
    - User information
    - Twitter lists
    - Timelines
    - Direct Messages
    - and anything found in `the docs <https://dev.twitter.com/docs/api/1.1>`_
- Image Uploading:
    - Update user status with an image
    - Change user avatar
    - Change user background image
    - Change user banner image
- OAuth 2 Application Only (read-only) Support
- Support for Twitter's Streaming API
- Seamless Python 3 support!

%prep
%setup -q -n twython-%{version}
%patch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Five failing tests
%python_exec %{_bindir}/nosetests -e '(test_get_lastfunction_header_should_return_header|test_request_should_handle_(rate_limit|401|400_that_is_not_auth_related|400_for_missing_auth_data))'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
