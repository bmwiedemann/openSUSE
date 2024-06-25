#
# spec file for package python-certbot
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
Name:           python-certbot
Version:        2.11.0
Release:        0
Summary:        ACME client
License:        Apache-2.0
URL:            https://github.com/certbot/certbot
Source0:        https://files.pythonhosted.org/packages/source/c/certbot/certbot-%{version}.tar.gz
BuildRequires:  %{python_module acme >= %{version}}
BuildRequires:  %{python_module configargparse >= 1.5.3}
BuildRequires:  %{python_module configobj >= 5.0.6}
BuildRequires:  %{python_module cryptography >= 3.2.1}
BuildRequires:  %{python_module distro >= 1.0.1}
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.10}
BuildRequires:  %{python_module importlib-resources if %python-base < 3.9}
BuildRequires:  %{python_module josepy >= 1.13.0}
BuildRequires:  %{python_module parsedatetime >= 2.4}
BuildRequires:  %{python_module pyRFC3339}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz >= 2019.3}
BuildRequires:  %{python_module setuptools >= 41.6.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-acme >= %{version}
Requires:       python-configargparse >= 1.5.3
Requires:       python-configobj >= 5.0.6
Requires:       python-cryptography >= 3.2.1
Requires:       python-distro >= 1.0.1
Requires:       python-josepy >= 1.9.0
Requires:       python-parsedatetime >= 2.4
Requires:       python-pyRFC3339
Requires:       python-pytz >= 2019.3
Requires:       python-setuptools >= 41.6.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
%if %{python_version_nodots} < 310
Requires:       python-importlib-metadata
%endif
%if %{python_version_nodots} < 39
Requires:       python-importlib-resources
%endif
Provides:       certbot = %{version}
Obsoletes:      certbot < %{version}
BuildArch:      noarch
%python_subpackages

%description
certbot is a free, automated certificate authority that aims
to lower the barriers to entry for encrypting all HTTP traffic on the internet.

%prep
%setup -q -n certbot-%{version}
%autopatch -p1

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
