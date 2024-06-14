#
# spec file for package python-eventlet
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
Name:           python-eventlet
Version:        0.36.1
Release:        0
Summary:        Concurrent networking library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://eventlet.net
Source:         https://files.pythonhosted.org/packages/source/e/eventlet/eventlet-%{version}.tar.gz
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       netcfg
Requires:       python-dnspython >= 1.15.0
Requires:       python-greenlet >= 1.0
BuildArch:      noarch
# SECTION TEST requirements
BuildRequires:  %{python_module dnspython >= 1.15.0}
BuildRequires:  %{python_module greenlet >= 1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
# eventlet parses /etc/protocols which is not available in normal build envs
BuildRequires:  netcfg
%if 0%{?suse_version} >= 1550
BuildRequires:  %{python_module pyOpenSSL}
%endif
# /SECTION
%python_subpackages

%description
Eventlet is a concurrent networking library for Python that allows
changing how code is run.

It uses epoll or libevent for scalable non-blocking I/O. Coroutines
ensure that the developer uses a blocking style of programming that is similar
to threading, but provide the benefits of non-blocking I/O. The event dispatch
is implicit, which means Eventlet can be used from the Python
interpreter, or as part of a larger application.

%prep
%autosetup -p1 -n eventlet-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# dnspython 1 and 2: backdoor tests fail with "take too long"
skiptests="(BackdoorTest and test_server)"
skiptests+=" or test_dns_methods_are_green or test_noraise_dns_tcp or test_clear"
# These are flaky inside the OBS environment
skiptests+=" or test_fork_after_monkey_patch or test_send_1k_req_rep or test_cpu_usage_after_bind"
# it is racy, see: https://lore.kernel.org/all/CADVnQy=AnJY9NZ3w_xNghEG80-DhsXL0r_vEtkr=dmz0ugcoVw@mail.gmail.com/ (bsc#1202188)
skiptests+=" or test_018b_http_10_keepalive_framing"
# gh#eventlet/eventlet#803
skiptests+=" or test_raise_dns_tcp"
# gh#eventlet/eventlet#821 bsc#1216858
skiptests+=" or test_full_duplex"

# https://github.com/eventlet/eventlet/issues/739
python310_skiptests+=" or test_017_ssl_zeroreturnerror"
%pytest -k "not ($skiptests ${$python_skiptests})" ${$python_pytest_param}

%files %{python_files}
%license LICENSE
%doc AUTHORS NEWS README.rst
%{python_sitelib}/eventlet
%{python_sitelib}/eventlet-%{version}.dist-info

%changelog
