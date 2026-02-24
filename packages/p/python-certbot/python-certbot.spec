#
# spec file for package python-certbot
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-certbot
Version:        5.3.1
Release:        0
Summary:        ACME client
License:        Apache-2.0
URL:            https://github.com/certbot/certbot
Source0:        https://files.pythonhosted.org/packages/source/c/certbot/certbot-%{version}.tar.gz
# https://github.com/certbot/certbot/pull/10576 Reset mock call count using reset_mock since new thread-safe implementation means it can no longer just be set to 0
Patch0:         reset-mock-call-count.patch
BuildRequires:  %{python_module acme >= %{version}}
BuildRequires:  %{python_module configargparse >= 1.5.3}
BuildRequires:  %{python_module configobj >= 5.0.6}
BuildRequires:  %{python_module cryptography >= 43.0.0}
BuildRequires:  %{python_module distro >= 1.0.1}
BuildRequires:  %{python_module josepy >= 2.0.0}
BuildRequires:  %{python_module parsedatetime >= 2.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyRFC3339}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 41.6.0}
BuildRequires:  %{python_module uv}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-acme >= %{version}
Requires:       python-configargparse >= 1.5.3
Requires:       python-configobj >= 5.0.6
Requires:       python-cryptography >= 43.0.0
Requires:       python-distro >= 1.0.1
Requires:       python-josepy >= 2.0.0
Requires:       python-parsedatetime >= 2.6
Requires:       python-pyRFC3339
Provides:       certbot = %{version}
Obsoletes:      certbot < %{version}
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
certbot is a free, automated certificate authority that aims
to lower the barriers to entry for encrypting all HTTP traffic on the internet.

%prep
%autosetup -p1 -n certbot-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/certbot
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_lock_order[renew] needs internet connection to check ARI
%pytest -k "not (test_lock_order and renew)"

%pre
%python_libalternatives_reset_alternative certbot

%post
%python_install_alternative certbot

%postun
%python_uninstall_alternative certbot

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/certbot
%{python_sitelib}/certbot-%{version}.dist-info
%python_alternative %{_bindir}/certbot

%changelog
