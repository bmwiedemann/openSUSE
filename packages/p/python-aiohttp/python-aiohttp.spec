#
# spec file for package python-aiohttp
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


%bcond_with docs
%{?sle15_python_module_pythons}
Name:           python-aiohttp
Version:        3.13.2
Release:        0
Summary:        Asynchronous HTTP client/server framework
License:        Apache-2.0
URL:            https://github.com/aio-libs/aiohttp
Source:         https://files.pythonhosted.org/packages/source/a/aiohttp/aiohttp-%{version}.tar.gz
# llhttp vendor tar ball manually created based on git submodule via:
# - yarn
# - make generate
# - tar cfvz vendor-llhttp.tar.gz vendor/
Source2:        vendor-llhttp.tar.gz
Patch0:         test_no_warnings_fix.patch
# PATCH-FIX-OPENSUSE remove-zlib-ng-test-dep.patch
Patch2:         remove-zlib-ng-test-dep.patch
# PATCH-FIX-OPENSUSE fix-vendoring.patch
Patch3:         fix-vendoring.patch
Requires:       python-aiohappyeyeballs >= 2.5.0
Requires:       python-aiosignal >= 1.4
Requires:       python-attrs >= 17.3.0
Requires:       python-frozenlist >= 1.1.1
Requires:       (python-charset-normalizer >= 2.0 with python-charset-normalizer < 4)
Requires:       (python-multidict >= 4.5 with python-multidict < 7)
Requires:       (python-yarl >= 1.17.0 with python-yarl < 2)
Recommends:     python-Brotli
Recommends:     python-aiodns
Recommends:     python-cChardet
Suggests:       %{name}-doc
# SECTION build requirements
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# /SECTION
# SECTION install requirements
BuildRequires:  %{python_module aiohappyeyeballs >= 2.5.0}
BuildRequires:  %{python_module aiosignal >= 1.4}
BuildRequires:  %{python_module attrs >= 17.3.0}
BuildRequires:  %{python_module charset-normalizer >= 2.0 with %python-charset-normalizer < 4}
BuildRequires:  %{python_module frozenlist >= 1.1.1}
BuildRequires:  %{python_module multidict >= 4.5 with %python-multidict < 7}
BuildRequires:  %{python_module yarl >= 1.17.0 with %python-yarl < 2}
# /SECTION
# SECTION test requirements
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module blockbuster}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module gunicorn}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module propcache}
BuildRequires:  %{python_module pytest >= 6.2.0}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module re-assert}
BuildRequires:  %{python_module time-machine}
BuildRequires:  %{python_module trustme}
# /SECTION
# SECTION docs
%if %{with docs}
BuildRequires:  python3-MarkupSafe
BuildRequires:  python3-Pygments >= 2.1
BuildRequires:  python3-Sphinx
BuildRequires:  python3-aiohttp-theme
BuildRequires:  python3-sphinxcontrib-asyncio
BuildRequires:  python3-sphinxcontrib-blockdiag
BuildRequires:  python3-sphinxcontrib-newsfeed
BuildRequires:  python3-sphinxcontrib-towncrier
%endif
# /SECTION
%python_subpackages

%description
Asynchronous HTTP client/server framework for Python.

- Supports both the client and server side of HTTP protocol.
- Supports both client and server WebSockets out-of-the-box.
- Web-server has middleware and pluggable routing.

%package -n %{name}-doc
Summary:        Documentation files for %{name}

%description -n %{name}-doc
HTML documentation on the API and examples for %{name}.

%prep
%autosetup -p1 -n aiohttp-%{version}

# don't check coverage
sed -i '/--cov/d' setup.cfg

# vendored llhttp
tar xfv %{S:2}
# prepare cython files manually for now
make cythonize

%build
export CFLAGS="%{optflags}"
%pyproject_wheel
%if %{with docs}
pushd docs
%make_build html
rm _build/html/.buildinfo
popd
%endif

%install
%pyproject_install
%{python_expand %fdupes %{buildroot}%{$python_sitearch}
find %{buildroot}%{$python_sitearch} -name '*.[ch]' -delete
rm -r %{buildroot}%{$python_sitearch}/aiohttp/.hash
}

%check
donttest="test_aiohttp_request_coroutine or test_mark_formdata_as_processed or test_aiohttp_plugin_async or test_secure_https_proxy_absolute_path"
# # flaky
# donttest+=" or test_https_proxy_unsupported_tls_in_tls"
# donttest+=" or test_shutdown_handler_cancellation_suppressed"
# https://github.com/aio-libs/aiohttp/issues/11113
donttest+=" or test_tcp_connector_ssl_shutdown_timeout"
# most probably https://github.com/cbornet/blockbuster/issues/47
donttest+=" or (test_cookie_jar and (heap or expire)) or test_treat_as_secure_origin_init"

# requires python-on-whales
rm -v tests/autobahn/test_autobahn.py
# uses proxy.py which is not maintained anymore
rm -v tests/test_proxy_functional.py
# Requires python-pytest-codspeed
rm -v tests/test_benchmarks_*

# randomly fails on xdist splits
single_runs="(test_run_app or test_web_runner)"
# breaks without threading
single_runs+=" and not test_shutdown_handler_cancellation_suppressed"
test -d aiohttp && mv aiohttp aiohttp.bkp
%pytest_arch tests -n 4 -k "not ($donttest or skip_blockbuster)"

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst CONTRIBUTORS.txt README.rst
%{python_sitearch}/aiohttp
%{python_sitearch}/aiohttp-%{version}.dist-info

%if %{with docs}
%if 0%{?suse_version} > 1500
%files -n %{name}-doc
%endif
%doc docs/_build/html
%endif

%changelog
