#
# spec file for package python-Scrapy
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%endif
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%endif
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-Scrapy%{?psuffix}
Version:        2.20.0
Release:        0
Summary:        A high-level Python Screen Scraping framework
License:        BSD-3-Clause
URL:            https://scrapy.org
# SourceRepo:     https://github.com/scrapy/scrapy
Source:         https://files.pythonhosted.org/packages/source/s/scrapy/scrapy-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Do not require sphinx_reredirects
Patch0:         no-sphinx-reredicts.patch
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
%if %{with test}
# Test requirements:
BuildRequires:  %{python_module Scrapy = %{version}}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module botocore >= 1.4.87}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module httpx2}
BuildRequires:  %{python_module pexpect >= 4.8.1}
BuildRequires:  %{python_module pyftpdlib >= 2.0.1}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-twisted >= 1.14.3}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sybil >= 1.3.0}
BuildRequires:  %{python_module testfixtures}
BuildRequires:  %{python_module uvloop}
%endif
BuildRequires:  %{python_module w3lib >= 1.17.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinx-design
BuildRequires:  python3-sphinx-notfound-page
BuildRequires:  python3-sphinx-rtd-dark-mode
BuildRequires:  python3-sphinx-scrapy
Requires:       python-Brotli >= 1.2.0
Requires:       python-Protego >= 0.2.0
Requires:       python-PyDispatcher >= 2.0.5
Requires:       python-Twisted >= 23.10.0
Requires:       python-aiodns >= 3.3.0
Requires:       python-aioftp >= 0.26.1
Requires:       python-aiohttp >= 3.13.3
%if 0%{?python_version_nodots} < 314
Requires:       python-backports.zstd >= 1.3.0
%endif
Requires:       python-cryptography >= 41.0.5
Requires:       python-cssselect >= 1.2.0
Requires:       python-defusedxml >= 0.7.1
Requires:       python-formerly >= 0.1.0
Requires:       python-frostwork >= 0.2.2
Requires:       python-itemadapter >= 0.1.0
Requires:       python-itemloaders >= 1.0.5
Requires:       python-lxml >= 4.9.4
Requires:       python-packaging
Requires:       python-parsel >= 1.8.1
Requires:       python-platformdirs >= 2.0.0
Requires:       python-pyOpenSSL >= 24.3.0
Requires:       python-queuelib >= 1.8.0
Requires:       python-service_identity >= 24.2.0
Requires:       python-tldextract
Requires:       python-w3lib >= 2.6.0
Requires:       python-zope.interface >= 5.1.0
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
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

%if %{without test}
%build
%pyproject_wheel
set -e # fail the build if the docs fail
%make_build -C docs html && rm -r docs/build/html/.buildinfo

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/scrapy
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# no color in obs chroot console
skiplist="test_pformat"
# no online connection to toscrapy.com
skiplist="$skiplist or CheckCommandTest or test_file_path"
# Flaky test gh#scrapy/scrapy#5703
skiplist="$skiplist or test_start_requests_laziness"
# Fails on 32 bit arches
skiplist="$skiplist or test_queue_push_pop_priorities"
# Can not import tests module
skiplist="$skiplist or test_response_ip_address"
# needs online DNS lookups
skiplist="$skiplist or test_verify_certs or test_tls_logging or test_download or test_download_with_spider"
# OpenSSL 3.5+ natively reads SSLKEYLOGFILE in libssl even under python -E
skiplist="$skiplist or test_keylog_ignore_environment"
%pytest -k "not (${skiplist})" tests
%endif

%if %{without test}
%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative scrapy

%post
%python_install_alternative scrapy

%postun
%python_uninstall_alternative scrapy

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/scrapy
%{python_sitelib}/[Ss]crapy-%{version}.dist-info
%python_alternative %{_bindir}/scrapy

%files -n %{name}-doc
%doc docs/build/html
%endif

%changelog
