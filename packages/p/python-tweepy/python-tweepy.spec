#
# spec file for package python-tweepy
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           python-tweepy
Version:        4.16.0
Release:        0
Summary:        Twitter library for python
License:        MIT
URL:            https://github.com/tweepy/tweepy
Source:         https://github.com/tweepy/tweepy/archive/v%{version}.tar.gz
# PATCH-FIX-OPENSUSE Decompress vcr cassette data, sourced from:
# https://github.com/kevin1024/vcrpy/issues/719#issuecomment-1811544263
Patch0:         support-urllib3-2.patch
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module async-lru}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
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
%autosetup -p1 -n tweepy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export USE_REPLAY=1
# TweepyAuthTests, test_filter_track, test_sample, test_sitestream, test_userstream and test_exp_backoff fail due to network
%pytest -rs -k 'not (TweepyAuthTests or test_filter_track or test_sample or test_sitestream or test_userstream or test_exp_backoff)'

%files %{python_files}
%doc README.md docs/*.rst docs/*.md
%license LICENSE
%{python_sitelib}/tweepy
%{python_sitelib}/tweepy-%{version}.dist-info

%changelog
