#
# spec file for package python-twitter
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
Name:           python-twitter
Version:        1.19.6
Release:        0
Summary:        An API and command-line toolset for Twitter
License:        MIT
URL:            https://mike.verdone.ca/twitter/
Source:         https://github.com/python-twitter-tools/twitter/archive/refs/tags/twitter-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
# SECTION tests
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module certifi}
# /SECTION
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-generators
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
Conflicts:      python-python-twitter
BuildArch:      noarch
%{?python_enable_dependency_generator}
%python_subpackages

%description
A Python API for Twitter, a command-line tool for getting others'
tweets and setting your own tweet and an IRC bot that can announce Twitter
updates to an IRC channel.

%prep
%setup -q -n twitter-twitter-%{version}

sed -i 's/setup_requires=\["setuptools_scm"\]/version="%{version}"/' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/twitter
%python_clone -a %{buildroot}%{_bindir}/twitter-archiver
%python_clone -a %{buildroot}%{_bindir}/twitter-follow
%python_clone -a %{buildroot}%{_bindir}/twitter-log
%python_clone -a %{buildroot}%{_bindir}/twitter-stream-example
%python_clone -a %{buildroot}%{_bindir}/twitterbot

%post
%{python_install_alternative twitter twitter-archiver twitter-follow twitter-log twitter-stream-example twitterbot}

%postun
%python_uninstall_alternative twitter

%check
# skip the tests requiring internet access
%pytest -k 'not (test_TwitterHTTPError_raised_for_invalid_oauth or test_get_trends_3 or test_get_trends or test_search or test_metadata_multipic or test_API_set_unicode_tweet or test_API_set_tweet)'

%files %{python_files}
%{python_sitelib}/twitter*
%python_alternative %{_bindir}/twitter
%python_alternative %{_bindir}/twitter-archiver
%python_alternative %{_bindir}/twitter-follow
%python_alternative %{_bindir}/twitter-log
%python_alternative %{_bindir}/twitter-stream-example
%python_alternative %{_bindir}/twitterbot

%changelog
