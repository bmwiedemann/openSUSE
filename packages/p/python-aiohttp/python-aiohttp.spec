#
# spec file for package python-aiohttp
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python2 1
# requires some unavailable modules
%bcond_with docs
Name:           python-aiohttp
Version:        3.8.3
Release:        0
Summary:        Asynchronous HTTP client/server framework
License:        Apache-2.0
URL:            https://github.com/aio-libs/aiohttp
Source:         https://files.pythonhosted.org/packages/source/a/aiohttp/aiohttp-%{version}.tar.gz
# PATCH-FIX-UPSTREAM aiohttp-pr7057-bump-charset-normalizer.patch gh#aio-libs/aiohttp#7057
Patch0:         aiohttp-pr7057-bump-charset-normalizer.patch
# PATCH-FIX-OPENSUSE py3109-compat.patch
Patch1:         py3109-compat.patch
# SECTION build requirements
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  http-parser-devel
BuildRequires:  python-rpm-macros
# /SECTION
# SECTION install requirements
BuildRequires:  %{python_module aiosignal >= 1.1.2}
BuildRequires:  %{python_module async_timeout >= 4.0 with %python-async_timeout < 5}
BuildRequires:  %{python_module asynctest = 0.13.0 if %python-base < 3.8}
BuildRequires:  %{python_module attrs >= 17.3.0}
BuildRequires:  %{python_module charset-normalizer >= 2.0 with %python-charset-normalizer < 4}
BuildRequires:  %{python_module frozenlist >= 1.1.1}
BuildRequires:  %{python_module idna_ssl >= 1.0 if %python-base < 3.7}
BuildRequires:  %{python_module multidict >= 4.5 with %python-multidict < 7}
BuildRequires:  %{python_module typing_extensions >= 3.7.4 if %python-base < 3.8}
BuildRequires:  %{python_module yarl >= 1.0 with %python-yarl < 2}
# /SECTION
Requires:       python-aiosignal >= 1.1.2
Requires:       python-attrs >= 17.3.0
Requires:       python-frozenlist >= 1.1.1
Requires:       (python-async_timeout >= 4.0 with python-async_timeout < 5)
Requires:       (python-asynctest = 0.13.0 if python-base < 3.8)
Requires:       (python-charset-normalizer >= 2.0 with python-charset-normalizer < 4)
Requires:       (python-idna_ssl >= 1.0 if python-base < 3.7)
Requires:       (python-multidict >= 4.5 with python-multidict < 7)
Requires:       (python-typing_extensions >= 3.7.4 if python-base < 3.8)
Requires:       (python-yarl >= 1.0 with python-yarl < 2)
Recommends:     python-aiodns
Recommends:     python-brotlipy
Recommends:     python-cChardet
Suggests:       %{name}-doc
# SECTION test requirements
BuildRequires:  %{python_module aiodns}
BuildRequires:  %{python_module brotlipy}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module gunicorn}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module proxy.py}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module re-assert}
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

%package -n %{name}-doc
Summary:        Documentation files for %{name}

%description
Asynchronous HTTP client/server framework for Python.

- Supports both the client and server side of HTTP protocol.
- Supports both client and server WebSockets out-of-the-box.
- Web-server has middleware and pluggable routing.

%description -n %{name}-doc
HTML documentation on the API and examples for %{name}.

%prep
%autosetup -p1 -n aiohttp-%{version}

# don't check coverage
sed -i '/--cov/d' setup.cfg

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
# no name resolution
donttest+=" or test_client_session_timeout_zero or test_requote_redirect_url_default"
# flaky
donttest+=" or test_https_proxy_unsupported_tls_in_tls"
# not running under pytest ?!
donttest+=" or test_no_warnings"
%if 0%{?python3_version_nodots} == 36
donttest+=" or test_read_boundary_with_incomplete_chunk"
%endif
# skip functional tests
# rm -v tests/test_proxy_functional.py
%pytest_arch tests -rsEf -k "not ($donttest)"

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst CONTRIBUTORS.txt README.rst
%{python_sitearch}/aiohttp
%{python_sitearch}/aiohttp-%{version}*-info

%if %{with docs}
%files -n %{name}-doc
%doc docs/_build/html
%endif

%changelog
