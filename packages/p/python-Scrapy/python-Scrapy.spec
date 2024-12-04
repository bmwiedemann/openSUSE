#
# spec file for package python-Scrapy
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-Scrapy
Version:        2.12.0
Release:        0
Summary:        A high-level Python Screen Scraping framework
License:        BSD-3-Clause
URL:            https://scrapy.org
Source:         https://files.pythonhosted.org/packages/source/s/scrapy/scrapy-%{version}.tar.gz
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module Protego}
BuildRequires:  %{python_module PyDispatcher >= 2.0.5}
BuildRequires:  %{python_module Twisted >= 18.9.0}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module botocore >= 1.4.87}
BuildRequires:  %{python_module cryptography >= 36.0.0}
BuildRequires:  %{python_module cssselect >= 0.9.1}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module defusedxml >= 0.7.1}
BuildRequires:  %{python_module itemadapter >= 0.1.0}
BuildRequires:  %{python_module itemloaders >= 1.0.1}
BuildRequires:  %{python_module lxml >= 4.4.1}
BuildRequires:  %{python_module parsel >= 1.5.0}
BuildRequires:  %{python_module pexpect >= 4.8.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyOpenSSL >= 21.0.0}
BuildRequires:  %{python_module pyftpdlib >= 1.5.8}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module queuelib >= 1.4.2}
BuildRequires:  %{python_module service_identity >= 18.1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sybil}
BuildRequires:  %{python_module testfixtures}
BuildRequires:  %{python_module tldextract}
BuildRequires:  %{python_module uvloop}
BuildRequires:  %{python_module w3lib >= 1.17.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zope.interface >= 5.1.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Requires:       python-Protego >= 0.1.15
Requires:       python-PyDispatcher >= 2.0.5
Requires:       python-Twisted >= 18.9.0
Requires:       python-cryptography >= 36.0.0
Requires:       python-cssselect >= 0.9.1
Requires:       python-defusedxml >= 0.7.1
Requires:       python-itemadapter >= 0.1.0
Requires:       python-itemloaders >= 1.0.1
Requires:       python-lxml >= 4.4.1
Requires:       python-packaging
Requires:       python-parsel >= 1.5.0
Requires:       python-pyOpenSSL >= 21.0.0
Requires:       python-queuelib >= 1.4.2
Requires:       python-service_identity >= 18.1.0
Requires:       python-tldextract
Requires:       python-w3lib >= 1.17.2
Requires:       python-zope.interface >= 5.1.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Scrapy is a high level scraping and web crawling framework for writing spiders
to crawl and parse web pages for all kinds of purposes, from information
retrieval to monitoring or testing web sites.

%package -n %{name}-doc
Summary:        Documentation for %{name}

%description -n %{name}-doc
Provides documentation for %{name}.

%prep
%autosetup -p1 -n scrapy-%{version}

sed -i -e 's:= python:= python3:g' docs/Makefile

%build
%pyproject_wheel
pushd docs
%make_build html && rm -r build/html/.buildinfo
popd

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/scrapy
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no color in obs chroot console
skiplist="test_pformat"
# no online connection to toscrapy.com
skiplist="$skiplist or CheckCommandTest or test_file_path"
# Flaky test gh#scrapy/scrapy#5703
skiplist="$skiplist or test_start_requests_laziness"
%{pytest -x \
    -k "not (${skiplist})" \
    -W ignore::DeprecationWarning \
    tests}

%post
%python_install_alternative scrapy

%postun
%python_uninstall_alternative scrapy

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/scrapy
%{python_sitelib}/Scrapy-%{version}.dist-info
%python_alternative %{_bindir}/scrapy

%files -n %{name}-doc
%doc docs/build/html

%changelog
