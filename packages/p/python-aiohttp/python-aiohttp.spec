#
# spec file for package python-aiohttp
#
# Copyright (c) 2023 SUSE LLC
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
%{?sle15_python_module_pythons}
Name:           python-aiohttp
Version:        3.8.5
Release:        0
Summary:        Asynchronous HTTP client/server framework
License:        Apache-2.0
URL:            https://github.com/aio-libs/aiohttp
Source:         https://files.pythonhosted.org/packages/source/a/aiohttp/aiohttp-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Update-update_query-calls-to-work-with-latest-yarl.patch gh#aio-libs/aiohttp#7260
Patch0:         Update-update_query-calls-to-work-with-latest-yarl.patch
# PATCH-FIX-OPENSUSE remove-re-assert.patch mcepl@suse.com
# We really don’t need beautifuly presented exceptions for our testing
Patch1:         remove-re-assert.patch
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
Recommends:     python-Brotli
Recommends:     python-aiodns
Recommends:     python-cChardet
Suggests:       %{name}-doc
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
# SECTION test requirements
BuildRequires:  %{python_module aiodns}
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module gunicorn}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module proxy.py}
BuildRequires:  %{python_module pytest >= 6.2.0}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-timeout}
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
%{python_expand # Does not work on python <= 3.6
if [ %{$python_version_nodots} -eq 36 ]; then
  #See https://github.com/openSUSE/python-rpm-macros#flavor-expansion for an explanation of this hack
  $python_donttest=" or test_read_boundary_with_incomplete_chunk"
fi
}

# Disable DeprecationWarning to avoid error with the latest setuptools
# and pkg_resources deprecation
%pytest_arch tests -rsEf -k "not ($donttest ${$python_donttest})" -W ignore::DeprecationWarning

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst CONTRIBUTORS.txt README.rst
%{python_sitearch}/aiohttp
%{python_sitearch}/aiohttp-%{version}*-info

%if %{with docs}
%if 0%{?suse_version} > 1500
%files -n %{name}-doc
%endif
%doc docs/_build/html
%endif

%changelog
