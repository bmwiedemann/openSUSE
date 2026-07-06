#
# spec file for package python-sphinx-scrapy
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


# Enable libalternatives by default
%bcond_without libalternatives
Name:           python-sphinx-scrapy
Version:        0.8.6
Release:        0
Summary:        Sphinx extension for documentation in the Scrapy ecosystem
License:        BSD-3-Clause
URL:            https://github.com/scrapy/sphinx-scrapy
Source:         https://github.com/scrapy/sphinx-scrapy/archive/refs/tags/%{version}.tar.gz#/sphinx_scrapy-%{version}.tar.gz
BuildRequires:  %{python_module hatchling >= 1.27.0}
BuildRequires:  %{python_module pip}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-Sphinx
Requires:       python-packaging
Requires:       python-sphinx-llms-txt
Requires:       python-sphinx-markdown-builder
Requires:       python-sphinx-sitemap
Requires:       python-sphinxcontrib-copybutton
BuildArch:      noarch
%python_subpackages

%description
Sphinx extension for documentation in the Scrapy ecosystem.
-   Automatic configuration of intersphinx_ for Python_ and Scrapy_.
-   Automatic configuration of Sphinx roles of the Scrapy documentation, so
    that you can easily link to Scrapy settings, request metadata keys, signals
    and commands:

%prep
%autosetup -p1 -n sphinx-scrapy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/sphinx-scrapy

%files %{python_files}
%doc README.rst CHANGES.rst
%license LICENSE
%python_alternative %{_bindir}/sphinx-scrapy
%{python_sitelib}/sphinx_scrapy
%{python_sitelib}/sphinx_scrapy-%{version}.dist-info

%changelog
