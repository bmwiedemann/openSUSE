#
# spec file for package python-httpretty
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
%if 0%{?suse_version} < 1550
%bcond_with boto3
%else
%bcond_without boto3
%endif
Name:           python-httpretty
Version:        1.1.4
Release:        0
Summary:        HTTP client mocking tool for Python
License:        MIT
URL:            https://github.com/gabrielfalcao/HTTPretty
Source:         https://files.pythonhosted.org/packages/source/h/httpretty/httpretty-%{version}.tar.gz
Patch0:         remove-mock.patch
# PATCH-FIX-UPSTREAM 453-fix-tests-pytest.patch gh#gabrielfalcao/HTTPretty#449 mcepl@suse.com
# Make tests compatible with pytest
Patch1:         453-fix-tests-pytest.patch
# PATCH-FIX-OPENSUSE test_double_slash may be replaced with / from stdlib
# gh#gabrielfalcao/HTTPretty#457
Patch2:         double-slash-paths.patch
#PATCH-FIX-UPSTREAM 460-fix-tests-two-miliseconds
Patch3:         460-miliseconds_tests.patch
# PATCH-FIX-OPENSUSE Relax the time for one test case from 2ms to 3ms.
Patch4:         relax-test-callback-response.patch
# PATCH-FIX-UPSTREAM https://github.com/gabrielfalcao/HTTPretty/pull/480
Patch5:         0001-Fix-test_417_openssl.py-if-pyOpenSSL-not-available.patch
%if %{with boto3}
BuildRequires:  %{python_module boto3}
%endif
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module fakeredis}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module httplib2}
BuildRequires:  %{python_module pytest-httpserver}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sure}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module urllib3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This library allows mocking of HTTP protocol based
unit tests.
It is similar to Ruby's FakeWeb.

%prep
%autosetup -p1 -n httpretty-%{version}
%if !%{with boto3}
rm tests/bugfixes/nosetests/test_416_boto3.py
%endif

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#gabrielfalcao/HTTPretty#405
export EVENTLET_NO_GREENDNS=yes
#  needs internet connection to httpbin.org
donttest="test_http_passthrough or test_https_passthrough"
# flaky (too slow) on obs
donttest="$donttest or test_httpretty_should_allow_forcing_headers_urllib2 or test_httpretty_should_allow_registering_regexes_with_streaming_responses or test_httpretty_provides_easy_access_to_querystrings"
# gh#gabrielfalcao/HTTPretty#457
donttest="$donttest or test_httpretty_should_handle_paths_starting_with_two_slashes"
%pytest -k "not (${donttest})"

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitelib}/httpretty
%{python_sitelib}/httpretty-%{version}*-info

%changelog
