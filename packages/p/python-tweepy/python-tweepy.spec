#
# spec file for package python-tweepy
#
# Copyright (c) 2022 SUSE LLC
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
Version:        4.9.0
Release:        0
Summary:        Twitter library for python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tweepy/tweepy
Source:         https://github.com/tweepy/tweepy/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.27.0}
BuildRequires:  %{python_module requests-oauthlib >= 1.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vcrpy >= 1.10.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-generators
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%{?python_enable_dependency_generator}
%python_subpackages

%description
A library for accessing the Twitter.com API. Supports OAuth, covers the entire
API, and streaming API.

%prep
%setup -q -n tweepy-%{version}

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
%doc README.md docs/*.rst docs/*.md
%license LICENSE
%{python_sitelib}/tweepy*

%changelog
