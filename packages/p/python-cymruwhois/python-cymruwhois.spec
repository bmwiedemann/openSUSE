#
# spec file for package python-cymruwhois
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without test
Name:           python-cymruwhois
Version:        1.6
Release:        0
Summary:        Client for the whois.cymrucom service
License:        MIT
Group:          Development/Languages/Python
URL:            https://packages.python.org/cymruwhois/
Source:         https://files.pythonhosted.org/packages/source/c/cymruwhois/cymruwhois-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/JustinAzoff/python-cymruwhois/master/docs/cymruwhois.1
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       cymruwhois
BuildArch:      noarch
%python_subpackages

%description
Perform lookups by ip address and return ASN, Country Code,
and Netblock Owner.

%prep
%setup -q -n cymruwhois-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
install -d -m0755 %{buildroot}%{_mandir}/man1/
install -m0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/
%python_clone -a %{buildroot}%{_mandir}/man1/cymruwhois.1
%python_clone -a %{buildroot}%{_bindir}/cymruwhois

%post
%python_install_alternative cymruwhois cymruwhois.1

%postun
%python_uninstall_alternative cymruwhois

%files %{python_files}
%{python_sitelib}/cymruwhois.py
%pycache_only %{python_sitelib}/__pycache__/cymruwhois.*.pyc
%{python_sitelib}/cymruwhois-%{version}.dist-info
%python_alternative %{_bindir}/cymruwhois
%python_alternative %{_mandir}/man1/cymruwhois.1%{ext_man}

%changelog
