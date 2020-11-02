#
# spec file for package python-aiohttp
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-aiohttp
Version:        3.7.2
Release:        0
Summary:        Asynchronous HTTP client/server framework
License:        Apache-2.0
URL:            https://github.com/aio-libs/aiohttp
Source:         https://files.pythonhosted.org/packages/source/a/aiohttp/aiohttp-%{version}.tar.gz
Patch0:         unbundle-http-parser.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module async_timeout >= 3.0}
BuildRequires:  %{python_module attrs >= 17.3.0}
BuildRequires:  %{python_module chardet >= 2.0}
BuildRequires:  %{python_module devel >= 3.5.3}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module multidict >= 4.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  http-parser-devel
BuildRequires:  python-rpm-macros
Requires:       python >= 3.5.3
Requires:       python-async_timeout >= 3.0
Requires:       python-attrs >= 17.3.0
Requires:       python-brotlipy
Requires:       python-chardet >= 2.0
Requires:       python-gunicorn
Requires:       python-multidict >= 4.5
Requires:       python-typing_extensions >= 3.6.5
Requires:       python-yarl >= 1.0
Recommends:     python-aiodns
Recommends:     python-cChardet
Suggests:       %{name}-doc
%if 0%{?suse_version} < 1550
BuildRequires:  %{python_module idna_ssl >= 1.0}
Requires:       python-idna_ssl
%endif
# SECTION test requirements
BuildRequires:  %{python_module aiodns}
BuildRequires:  %{python_module async_generator}
BuildRequires:  %{python_module brotlipy}
BuildRequires:  %{python_module gunicorn}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module re-assert}
BuildRequires:  %{python_module trustme}
BuildRequires:  %{python_module typing_extensions >= 3.6.5}
BuildRequires:  %{python_module yarl >= 1.0}
# /SECTION
# SECTION docs
BuildRequires:  %{python_module MarkupSafe}
BuildRequires:  python3-Pygments >= 2.1
BuildRequires:  python3-Sphinx
BuildRequires:  python3-aiohttp-theme
BuildRequires:  python3-sphinxcontrib-asyncio
BuildRequires:  python3-sphinxcontrib-blockdiag
BuildRequires:  python3-sphinxcontrib-newsfeed
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
%setup -q -n aiohttp-%{version}
%patch0 -p1
# Prevent building with vendor version
rm vendor/http-parser/*.c

%build
export CFLAGS="%{optflags}"
%python_build
pushd docs
%make_build html
rm _build/html/.buildinfo
popd

%install
%python_install
%{python_expand %fdupes %{buildroot}%{$python_sitearch}
find %{buildroot}%{$python_sitearch} -name "*.c" -delete
}

%check
rm setup.cfg
mv aiohttp .aiohttp
%pytest_arch -rs -k 'not (test_aiohttp_request_coroutine or test_mark_formdata_as_processed or test_aiohttp_plugin_async)'
mv .aiohttp aiohttp

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst CONTRIBUTORS.txt README.rst
%{python_sitearch}/*

%files -n %{name}-doc
%doc docs/_build/html

%changelog
