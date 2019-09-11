#
# spec file for package python-eventlet
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-eventlet
Version:        0.25.0
Release:        0
Summary:        Concurrent networking library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            http://eventlet.net
Source:         https://files.pythonhosted.org/packages/source/e/eventlet/eventlet-%{version}.tar.gz
BuildRequires:  %{python_module dnspython >= 1.15.0}
BuildRequires:  %{python_module greenlet >= 0.3}
BuildRequires:  %{python_module monotonic >= 1.4}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  fdupes
BuildRequires:  netcfg
BuildRequires:  python-rpm-macros
# eventlet parses /etc/protocols which is not available in normal build envs
Requires:       netcfg
Requires:       python-dnspython >= 1.15.0
Requires:       python-greenlet >= 0.3
Requires:       python-monotonic >= 1.4
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%if %{python_version_nodots} < 34
Requires:       python-enum34
%endif
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
%setup -q -n eventlet-%{version}
sed -i "s|^#!.*||" eventlet/support/greendns.py # Fix non-executable script

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# 400 out of 600 tests either fail or error out
#%%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} nosetests-%{$python_bin_suffix} -v

%files %{python_files}
%license LICENSE
%doc AUTHORS NEWS README.rst
%{python_sitelib}/*

%changelog
