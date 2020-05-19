#
# spec file for package python-Scrapy
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
%define skip_python2 1
Name:           python-Scrapy
Version:        2.0.1
Release:        0
Summary:        A high-level Python Screen Scraping framework
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://scrapy.org
Source:         https://files.pythonhosted.org/packages/source/S/Scrapy/Scrapy-%{version}.tar.gz
Patch0:         zope-exception-test_crawler.patch
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module Protego >= 0.1.15}
BuildRequires:  %{python_module PyDispatcher >= 2.0.5}
BuildRequires:  %{python_module Twisted >= 17.9.0}
BuildRequires:  %{python_module cryptography >= 2.0}
BuildRequires:  %{python_module cssselect >= 0.9.1}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module jmespath}
BuildRequires:  %{python_module lxml >= 3.5.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module parsel >= 1.5.0}
BuildRequires:  %{python_module pyOpenSSL >= 16.2.0}
BuildRequires:  %{python_module pytest-twisted}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module queuelib >= 1.4.2}
BuildRequires:  %{python_module service_identity >= 16.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sybil}
BuildRequires:  %{python_module testfixtures}
BuildRequires:  %{python_module w3lib >= 1.17.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Requires:       python-Protego >= 0.1.15
Requires:       python-PyDispatcher >= 2.0.5
Requires:       python-Twisted >= 17.9.0
Requires:       python-cryptography >= 2.0
Requires:       python-cssselect >= 0.9.1
Requires:       python-lxml >= 3.5.0
Requires:       python-parsel >= 1.5.0
Requires:       python-pyOpenSSL >= 16.2.0
Requires:       python-queuelib >= 1.4.2
Requires:       python-service_identity >= 16.0.0
Requires:       python-setuptools
Requires:       python-w3lib >= 1.17.2
Requires:       python-zope.interface >= 4.1.3
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
Group:          Documentation/HTML

%description -n %{name}-doc
Provides documentation for %{name}.

%prep
%setup -q -n Scrapy-%{version}
sed -i -e 's:= python:= python3:g' docs/Makefile
%autopatch -p1

%build
%python_build
pushd docs
%make_build html && rm -r build/html/.buildinfo
popd

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/scrapy
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# boto package is broken (boto.cacerts module removed, but resulting errors are not fixed)
skiplist="not S3AnonTestCase and not S3TestCase and not S3FeedStorageTest"
skiplist="$skiplist and not FilesPipelineTestCaseFields"
skiplist="$skiplist and not ImagesPipelineTestCaseFields"
skiplist="$skiplist and not CrawlerTestCase"
# tests/test_proxy_connect.py: requires mitmproxy == 0.10.1
%{python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} \
    --ignore tests/test_proxy_connect.py \
    -k "${skiplist}" \
    -W ignore::DeprecationWarning \
    tests}

%post
%python_install_alternative scrapy

%postun
%python_uninstall_alternative scrapy

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/*
%python_alternative %{_bindir}/scrapy

%files -n %{name}-doc
%doc docs/build/html

%changelog
