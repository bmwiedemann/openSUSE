#
# spec file for package python-itemloaders
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-itemloaders
Version:        1.0.4
Release:        0
Summary:        Base library for scrapy's ItemLoader
License:        BSD-3-Clause
URL:            https://github.com/scrapy/itemloaders
# Use Github archive, the PyPI sdist does not bundle the tests
Source:         https://github.com/scrapy/itemloaders/archive/refs/tags/v%{version}.tar.gz#/itemloaders-%{version}-gh.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-itemadapter >= 0.1.0
Requires:       python-jmespath >= 0.9.5
Requires:       python-parsel >= 1.5.0
Requires:       python-w3lib >= 1.17.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module itemadapter >= 0.1.0}
BuildRequires:  %{python_module jmespath >= 0.9.5}
BuildRequires:  %{python_module parsel >= 1.5.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module w3lib >= 1.17.0}
# /SECTION
%python_subpackages

%description
Library to populate items using XPath and CSS with a convenient API

%prep
%setup -q -n itemloaders-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/itemloaders
%{python_sitelib}/itemloaders-%{version}*-info

%changelog
