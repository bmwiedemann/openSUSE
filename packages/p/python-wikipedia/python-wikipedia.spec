#
# spec file for package python-wikipedia
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
Name:           python-wikipedia
Version:        1.4.0
Release:        0
Summary:        Wikipedia API for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/goldsmith/Wikipedia
Source:         https://files.pythonhosted.org/packages/source/w/wikipedia/wikipedia-%{version}.tar.gz
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-beautifulsoup4
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
Wikipedia is a Python library that makes it easy to access and parse
data from Wikipedia.

Search Wikipedia, get article summaries, get data like links and images
from a page, and more. Wikipedia wraps the `MediaWiki
API <https://www.mediawiki.org/wiki/API>`__ so you can focus on using
Wikipedia data, not getting it.

%prep
%setup -q -n wikipedia-%{version}

%build
%python_build

%install
%python_install

%check
ln -s tests/request_mock_data.py .
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
