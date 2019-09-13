#
# spec file for package python-sphinxcontrib-newsfeed
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
Name:           python-sphinxcontrib-newsfeed
Version:        0.1.4
Release:        0
Summary:        News Feed extension for Sphinx
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.com/aio-libs/sphinxcontrib-newsfeed
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-newsfeed/sphinxcontrib-newsfeed-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
BuildArch:      noarch

%python_subpackages

%description
sphinxcontrib-newsfeed is a extension for adding a simple Blog, News or Announcements section to a Sphinx website.

Features:
 * Makes feed entries from Sphinx documents.
 * Generates a list of entries with teasers.
 * Saves the feed to a file in RSS format.
 * Supports comments via Disqus.

%prep
%setup -q -n sphinxcontrib-newsfeed-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README
%license LICENSE
%{python_sitelib}/sphinxcontrib/newsfeed.py*
%pycache_only %{python_sitelib}/sphinxcontrib/__pycache__
%{python_sitelib}/sphinxcontrib_newsfeed-%{version}-py*-nspkg.pth
%{python_sitelib}/sphinxcontrib_newsfeed-%{version}-py*.egg-info

%changelog
