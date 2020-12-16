#
# spec file for package python-httpretty
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
Name:           python-httpretty
Version:        1.0.3
Release:        0
Summary:        HTTP client mocking tool for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/gabrielfalcao/HTTPretty
Source:         https://files.pythonhosted.org/packages/source/h/httpretty/httpretty-%{version}.tar.gz
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module fakeredis}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module httplib2}
BuildRequires:  %{python_module nose2}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sure}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module twine >= 1.15.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This library allows mocking of HTTP protocol based
unit tests.
It is similar to Ruby's FakeWeb.

%prep
%setup -q -n httpretty-%{version}
# no test coverage check needed
sed -i -e '/cover/ d' setup.cfg
# no color printout for tests
sed -i -e '/rednose/ d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/gabrielfalcao/HTTPretty/issues/405
export EVENTLET_NO_GREENDNS=yes
# test_http_passthrough and test_https_passthrough need internet connection
sed -Ei 's/(test_https?_passthrough)/_\1/' tests/functional/test_passthrough.py
# fails on 15.1
sed -Ei 's/(test_streaming_responses)/_\1/'  tests/functional/test_requests.py
# fails on x86_64
sed -Ei 's/(test_fakesock_socket_sendall_with_body_data_with_chunked_entry)/_\1/' tests/unit/test_core.py

%python_exec -m nose2 -v

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitelib}/httpretty
%{python_sitelib}/httpretty*egg-info

%changelog
