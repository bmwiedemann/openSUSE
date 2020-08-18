#
# spec file for package python-tweepy
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
Name:           python-tweepy
Version:        3.8.0
Release:        0
Summary:        Twitter library for python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tweepy/tweepy
Source:         https://github.com/tweepy/tweepy/archive/v%{version}.tar.gz
BuildRequires:  %{python_module PySocks >= 1.5.7}
BuildRequires:  %{python_module mock >= 1.0.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.11.1}
BuildRequires:  %{python_module requests-oauthlib >= 0.7.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module vcrpy >= 1.0.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PySocks >= 1.5.7
Requires:       python-requests >= 2.11.1
Requires:       python-requests-oauthlib >= 0.7.0
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
A library for accessing the Twitter.com API. Supports OAuth, covers the entire
API, and streaming API.

%prep
%setup -q -n tweepy-%{version}
sed -i 's/from nose import SkipTest/from unittest import SkipTest/' tests/test_api.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export USE_REPLAY=1
# TweepyAuthTests, test_filter_track, test_sample, test_sitestream, test_userstream and test_exp_backoff fail due to network
%pytest -rs -k 'not (TweepyAuthTests or test_filter_track or test_sample or test_sitestream or test_userstream or test_exp_backoff)'

%files %{python_files}
%doc README.md CHANGELOG.md docs/*.rst
%license LICENSE
%{python_sitelib}/*

%changelog
