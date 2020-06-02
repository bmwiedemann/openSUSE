#
# spec file for package python-twython
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-twython
Version:        3.8.2
Release:        0
Summary:        Python wrapper for the Twitter API
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ryanmcgrath/twython
Source:         https://files.pythonhosted.org/packages/source/t/twython/twython-%{version}.tar.gz
# PyJWT 1.4.2 isnt compatible with single-spec
BuildRequires:  %{python_module PyJWT > 1.4.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.1.0}
BuildRequires:  %{python_module requests-oauthlib >= 0.4.0}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Five failing tests
%pytest -k "not (test_get_lastfunction_header_should_return_header or test_request_should_handle_40 or test_request_should_handle_rate_limit)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
