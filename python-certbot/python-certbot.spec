#
# spec file for package python-certbot
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
Name:           python-certbot
Version:        0.36.0
Release:        0
Summary:        ACME client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/certbot/certbot
Source:         https://files.pythonhosted.org/packages/source/c/certbot/certbot-%{version}.tar.gz
BuildRequires:  %{python_module acme >= 0.29.0}
BuildRequires:  %{python_module configargparse >= 0.9.3}
BuildRequires:  %{python_module configobj}
BuildRequires:  %{python_module cryptography >= 1.2.3}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module josepy >= 1.1.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module parsedatetime >= 1.3}
BuildRequires:  %{python_module pyRFC3339}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.component}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-typing
Requires:       python-acme >= 0.29.0
Requires:       python-configargparse >= 0.9.3
Requires:       python-configobj
Requires:       python-cryptography >= 1.2.3
Requires:       python-future
Requires:       python-josepy >= 1.1.0
Requires:       python-mock
Requires:       python-parsedatetime >= 1.3
Requires:       python-pyRFC3339
Requires:       python-pytz
Requires:       python-setuptools
Requires:       python-zope.component
Requires:       python-zope.interface
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Requires:       python-typing
%endif
Provides:       certbot = %{version}
Obsoletes:      certbot < %{version}
%python_subpackages

%description
certbot is a free, automated certificate authority that aims
to lower the barriers to entry for encrypting all HTTP traffic on the internet.

%prep
%setup -q -n certbot-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/certbot
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative certbot
# migrate from old certbot to new certbot
if test ! -h %{_sysconfdir}/certbot -a -e %{_sysconfdir}/certbot; then
	echo "Migrating %{_sysconfdir}/certbot to %{_sysconfdir}/letsencrypt..."
	mv %{_sysconfdir}/letsencrypt %{_sysconfdir}/letsencrypt.empty
	mv %{_sysconfdir}/certbot %{_sysconfdir}/letsencrypt
	cd %{_sysconfdir} ; ln -s letsencrypt certbot
fi

%postun
%python_uninstall_alternative certbot

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*
%python_alternative %{_bindir}/certbot

%changelog
