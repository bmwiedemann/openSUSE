#
# spec file for package python-aiohttp
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
Name:           python-aiohttp
Version:        3.7.4
Release:        0
Summary:        Asynchronous HTTP client/server framework
License:        Apache-2.0
URL:            https://github.com/aio-libs/aiohttp
Source:         https://files.pythonhosted.org/packages/source/a/aiohttp/aiohttp-%{version}.tar.gz
Patch0:         unbundle-http-parser.patch
# PATCH-FIX-UPSTREAM stdlib-typing_extensions.patch gh#aio-libs/aiohttp#5374 mcepl@suse.com
# Fix typing_extensions imports.
Patch1:         stdlib-typing_extensions.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module async_timeout >= 3.0}
BuildRequires:  %{python_module attrs >= 17.3.0}
BuildRequires:  %{python_module chardet >= 2.0}
BuildRequires:  %{python_module devel >= 3.5.3}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module idna_ssl >= 1.0}
BuildRequires:  %{python_module multidict >= 4.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions >= 3.6.5 if %python-base < 3.8}
BuildRequires:  %{python_module yarl >= 1.0}
BuildRequires:  fdupes
BuildRequires:  http-parser-devel
BuildRequires:  python-rpm-macros
Requires:       python >= 3.6
Requires:       python-async_timeout >= 3.0
Requires:       python-attrs >= 17.3.0
Requires:       python-chardet >= 2.0
Requires:       python-gunicorn
Requires:       python-multidict >= 4.5
Requires:       python-yarl >= 1.0
Requires:       (python3-typing_extensions >= 3.6.5 if python3-base < 3.8)
Recommends:     python-aiodns
Recommends:     python-brotlipy
Recommends:     python-cChardet
Suggests:       %{name}-doc
%if 0%{?suse_version} < 1550 || "%{python_flavor}" == "python36"
Requires:       python-idna_ssl >= 1.0
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
%autosetup -p1 -n aiohttp-%{version}

# Prevent building with vendor version
rm vendor/http-parser/*.c

# Allow use with chardet v4
# https://github.com/aio-libs/aiohttp/pull/5333
sed -i 's/chardet>=2.0,<4.0/chardet>=2.0/' setup.py

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
find %{buildroot}%{$python_sitearch} -name '*.[ch]' -delete
rm -r %{buildroot}%{$python_sitearch}/aiohttp/.hash
}

%check
# ignore setup.cfg
touch pytest.ini
%define skiptest_allflavors test_aiohttp_request_coroutine or test_mark_formdata_as_processed or test_aiohttp_plugin_async
# we need it to be defined for all flavors for expansion inside pytest_arch to work. %%{?...} would expand too early.
%{lua: for p in string.gmatch(rpm.expand("%pythons"), "%S+") do rpm.define("skiptest_" .. p .. "_only %{nil}") end}
%if 0%{?python3_version_nodots} == 36
%define skiptest_python3_only or test_read_boundary_with_incomplete_chunk
%endif
%define skiptest_python36_only or test_read_boundary_with_incomplete_chunk
%pytest_arch --ignore ./aiohttp -rs -k 'not (%{skiptest_allflavors} %{skiptest_$python_only})'

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst CONTRIBUTORS.txt README.rst
%{python_sitearch}/aiohttp
%{python_sitearch}/aiohttp-%{version}*-info

%files -n %{name}-doc
%doc docs/_build/html

%changelog
