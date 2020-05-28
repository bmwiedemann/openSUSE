#
# spec file for package python-fedmsg
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


%define commands announce check collectd config dg-replay gateway hub irc logger relay signing-relay tail trigger
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-fedmsg
Version:        1.1.1
Release:        0
Summary:        Fedora Messaging Client API
License:        LGPL-2.1-or-later
URL:            https://github.com/fedora-infra/fedmsg
# source from pypi is missing test fixtures
Source:         https://github.com/fedora-infra/fedmsg/archive/%{version}/fedmsg-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Requires:       python-kitchen
Requires:       python-pyzmq
Requires:       python-requests
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-M2Crypto
Recommends:     python-Pygments
Recommends:     python-arrow
Recommends:     python-click
Recommends:     python-cryptography >= 1.6
Recommends:     python-m2ext
Recommends:     python-moksha.hub >= 1.3.0
Recommends:     python-psutil
Recommends:     python-pyOpenSSL >= 16.1.0
Recommends:     python-service_identity
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module arrow}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module kitchen}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module moksha-hub}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module vcrpy}
BuildRequires:  gpg2
# /SECTION
%python_subpackages

%description
fedmsg (Federated Message Bus) is a library built on ZeroMQ using the PyZMQ Python bindings.
fedmsg connects services together using ZeroMQ publishers and
subscribers.

%package        -n %{name}-doc
Summary:        Documentation for fedmsg

%description    -n %{name}-doc
This package contains the documentation for the fedmsg library and CLI programs.

%package        -n %{name}-base
Summary:        Base files system layout for packages using fedmsg
Supplements:    %{python_module %{name}}

%description    -n %{name}-base
This package contains the common filesystem layout shared by the python2 and
python3 versions of the fedmsg package.

%prep
%setup -q -n fedmsg-%{version}

%build
%python_build

export PYTHONPATH=$(pwd)
export PYTHON=python3
%make_build -C doc SPHINXBUILD=sphinx-build html
rm doc/_build/html/.buildinfo
rm doc/_build/html/objects.inv

%check
%pytest fedmsg

%install
%python_install
for c in %{commands}; do
  %python_clone -a %{buildroot}%{_bindir}/fedmsg-$c
done
%{python_expand # first remove the tests
rm -r %{buildroot}%{$python_sitelib}/fedmsg/tests/
%fdupes %{buildroot}%{$python_sitelib}
}
# system wide "config" files for fedmsg-base
mkdir -p %{buildroot}%{_sysconfdir}/fedmsg.d/
cp fedmsg.d/*.py %{buildroot}%{_sysconfdir}/fedmsg.d/.

%post
for c in %{commands}; do
  %python_install_alternative fedmsg-$c
done

%postun
for c in %{commands}; do
  %python_uninstall_alternative fedmsg-$c
done

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*
%python_alternative %{_bindir}/fedmsg-announce
%python_alternative %{_bindir}/fedmsg-check
%python_alternative %{_bindir}/fedmsg-collectd
%python_alternative %{_bindir}/fedmsg-config
%python_alternative %{_bindir}/fedmsg-dg-replay
%python_alternative %{_bindir}/fedmsg-gateway
%python_alternative %{_bindir}/fedmsg-hub
%python_alternative %{_bindir}/fedmsg-irc
%python_alternative %{_bindir}/fedmsg-logger
%python_alternative %{_bindir}/fedmsg-relay
%python_alternative %{_bindir}/fedmsg-signing-relay
%python_alternative %{_bindir}/fedmsg-tail
%python_alternative %{_bindir}/fedmsg-trigger

%files -n %{name}-doc
%license LICENSE
%doc README.rst doc/_build/html

%files -n %{name}-base
%license LICENSE
%doc README.rst
%dir %{_sysconfdir}/fedmsg.d/
%config(noreplace) %{_sysconfdir}/fedmsg.d/*

%changelog
