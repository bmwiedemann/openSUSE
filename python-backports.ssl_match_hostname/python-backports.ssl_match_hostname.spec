#
# spec file for package python-backports.ssl_match_hostname
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
Name:           python-backports.ssl_match_hostname
Version:        3.7.0.1
Release:        0
Summary:        The ssl.match_hostname() function from Python 3.7
License:        Python-2.0
Group:          Development/Languages/Python
URL:            http://bitbucket.org/brandon/backports.ssl_match_hostname
Source:         https://files.pythonhosted.org/packages/source/b/backports.ssl_match_hostname/backports.ssl_match_hostname-%{version}.tar.gz
# NOTE:
# %%{python_sitelib}/backports is a namespace package, and so under python 2 it must have a proper namespace __init__.py
# python-backports provides this __init__.py to prevent backports packages from conflicting.
# Please see:
#    https://pypi.python.org/pypi/backports/
#    https://www.python.org/dev/peps/pep-0420/%23namespace-packages-today
# If you need to link, the python-backports package is built as a subpackage of python-configparser
Source1:        https://bitbucket.org/brandon/backports.ssl_match_hostname/raw/312648aec6f01702e8704a99b54445ffc2458033/tests/test_ssl.py
BuildRequires:  %{python_module backports}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module unittest2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-backports
BuildArch:      noarch
%python_subpackages

%description
The Secure Sockets layer is only actually *secure*
if you check the hostname in the certificate returned
by the server to which you are connecting,
and verify that it matches to hostname
that you are trying to reach.

But the matching logic, defined in `RFC2818`_,
can be a bit tricky to implement on your own.
So the ``ssl`` package in the Standard Library of Python 3.2
and greater now includes a ``match_hostname()`` function
for performing this check instead of requiring every application
to implement the check separately.

This backport brings ``match_hostname()`` to users
of earlier versions of Python.
Simply make this distribution a dependency of your package,
and then use it like this::

    from backports.ssl_match_hostname import match_hostname, CertificateError
    ...
    sslsock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_SSLv3,
                              cert_reqs=ssl.CERT_REQUIRED, ca_certs=...)
    try:
        match_hostname(sslsock.getpeercert(), hostname)
    except CertificateError, ce:
        ...

%prep
%setup -q -n backports.ssl_match_hostname-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand rm %{buildroot}%{$python_sitelib}/backports/__init__.py*
%python_expand rm -rf %{buildroot}%{$python_sitelib}/backports/__pycache__/
%python_expand %fdupes %{buildroot}%{$python_sitelib}/backports/ssl_match_hostname/

%check
%python_exec -m unittest2 test_ssl.py

%files %{python_files}
%doc README.txt
%license LICENSE.txt
%{python_sitelib}/backports/ssl_match_hostname/
%{python_sitelib}/backports.ssl_match_hostname-%{version}-py*.egg-info

%changelog
