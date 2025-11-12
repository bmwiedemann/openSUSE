#
# spec file for package python-Scrapy
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        2.13.3
Release:        0
Summary:        A high-level Python Screen Scraping framework
License:        BSD-3-Clause
URL:            https://scrapy.org
Source:         https://files.pythonhosted.org/packages/source/s/scrapy/scrapy-%{version}.tar.gz
# New test file added in the gh#scrapy/scrapy#7134, needed for Patch2
# related to CVE-2025-6176
Source1:        CVE-2025-6176-testfile-bomb-br-64GiB.bin
# PATCH-FIX-UPSTREAM gh#scrapy/scrapy#6922
Patch0:         remove-hoverxref.patch
# PATCH-FIX-OPENSUSE No sphinx-rtd-dark-mode
Patch1:         no-dark-mode.patch
# PATCH-FIX-UPSTREAM CVE-2025-6176.patch gh#scrapy/scrapy#7134
Patch2:         CVE-2025-6176.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
%if %{with test}
# Test requirements:
BuildRequires:  %{python_module Scrapy = %{version}}
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module Protego}
BuildRequires:  %{python_module PyDispatcher >= 2.0.5}
BuildRequires:  %{python_module Twisted >= 18.9.0}
BuildRequires:  %{python_module attrs}
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
BuildRequires:  %{python_module pyOpenSSL >= 21.0.0}
BuildRequires:  %{python_module pyftpdlib >= 1.5.8}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module queuelib >= 1.4.2}
BuildRequires:  %{python_module service_identity >= 18.1.0}
BuildRequires:  %{python_module sybil}
BuildRequires:  %{python_module testfixtures}
BuildRequires:  %{python_module tldextract}
BuildRequires:  %{python_module uvloop}
BuildRequires:  %{python_module w3lib >= 1.17.0}
BuildRequires:  %{python_module zope.interface >= 5.1.0}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinx-notfound-page
BuildRequires:  python3-sphinx_rtd_theme
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
pushd docs
%make_build html && rm -r build/html/.buildinfo
popd

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/scrapy
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
cp %{SOURCE1} tests/sample_data/compressed/bomb-br-64GiB.bin

# no color in obs chroot console
skiplist="test_pformat"
# no online connection to toscrapy.com
skiplist="$skiplist or CheckCommandTest or test_file_path"
# Flaky test gh#scrapy/scrapy#5703
skiplist="$skiplist or test_start_requests_laziness"
# Fails on 32 bit arches
skiplist="$skiplist or test_queue_push_pop_priorities"
%{pytest -x \
    -k "not (${skiplist})" \
    -W ignore::DeprecationWarning \
    tests}
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
