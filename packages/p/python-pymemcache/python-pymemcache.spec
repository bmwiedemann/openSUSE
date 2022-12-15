#
# spec file for package python-pymemcache
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2014 Thomas Bechtold <thomasbechtold@jpberlin.de>
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


%bcond_without python2
Name:           python-pymemcache
Version:        4.0.0
Release:        0
Summary:        A pure Python memcached client
License:        Apache-2.0
URL:            https://github.com/Pinterest/pymemcache
Source:         https://files.pythonhosted.org/packages/source/p/pymemcache/pymemcache-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  memcached
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module Faker}
BuildRequires:  %{python_module pylibmc}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zstd}
# /SECTION
%python_subpackages

%description
A pure-Python memcached client.

pymemcache supports the following features:

* Complete implementation of the memcached text protocol.
* Configurable timeouts for socket connect and send/recv calls.
* Access to the "noreply" flag, which can significantly increase the speed of writes.
* Flexible, simple approach to serialization and deserialization.
* The (optional) ability to treat network and memcached errors as cache misses.

%prep
%autosetup -p1 -n pymemcache-%{version}
# Disable pytest-cov
sed -i 's/tool:pytest/tool:ignore-pytest-cov/' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
if [ -f %{_sbindir}/memcached ]; then
  %{_sbindir}/memcached &
elif [ -f %{_bindir}/memcached ]; then
  %{_bindir}/memcached &
fi

cat << EOF > pytest.ini
[pytest]
markers =
	unit
	integration
	benchmark
EOF

# TLS tests depend on setting up a memcached equivalent to
# https://github.com/scoriacorp/docker-tls-memcached
donttest="tls"
# In i586 zlib.compress doesn't compress the CustomInt instance so these tests
# fails
donttest+=" or test_compressed_complex"
%pytest -rs -k "not (${donttest})" -m "unit or integration"

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/pymemcache
%{python_sitelib}/pymemcache-%{version}*-info

%changelog
