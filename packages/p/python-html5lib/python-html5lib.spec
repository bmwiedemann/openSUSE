#
# spec file for package python-html5lib
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
Name:           python-html5lib
Version:        1.0.1
Release:        0
Summary:        HTML parser based on the WHAT-WG Web Applications 1
License:        MIT
URL:            https://github.com/html5lib/html5lib-python
Source:         https://files.pythonhosted.org/packages/source/h/html5lib/html5lib-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pytest4-mhroncok.patch gh#html5lib/html5lib-python#429 mcepl@suse.com
# This patch makes testsuite pass with pytest4
Patch0:         pytest4-mhroncok.patch
Patch1:         collections-abc.patch
BuildRequires:  %{python_module Genshi}
BuildRequires:  %{python_module datrie}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest < 5.0}
BuildRequires:  %{python_module pytest-expect}
BuildRequires:  %{python_module setuptools >= 18.5}
BuildRequires:  %{python_module six >= 1.9}
BuildRequires:  %{python_module webencodings}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.9
Requires:       python-webencodings
Recommends:     python-Genshi
Recommends:     python-lxml
BuildArch:      noarch
%python_subpackages

%description
HTML parser designed to follow the HTML5
specification. The parser is designed to handle all flavours of HTML and
parses invalid documents using well-defined error handling rules compatible
with the behaviour of major desktop web browsers.

Output is to a tree structure; the current release supports output to
DOM, ElementTree, lxml and BeautifulSoup tree formats as well as a
simple custom format

%prep
%setup -q -n html5lib-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --tb=short

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/html5lib/
%{python_sitelib}/html5lib-%{version}-py%{python_version}.egg-info

%changelog
