#
# spec file for package python-pythonwhois
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


%define commit 60adc3acc2d59627b2e32dc36d27802942e0820d/
Name:           python-pythonwhois
Version:        2.4.3
Release:        0
Summary:        Python whois library
License:        WTFPL
URL:            http://cryto.net/pythonwhois
#Source:         https://files.pythonhosted.org/packages/source/p/pythonwhois/pythonwhois-%%{version}.tar.gz
# github tarball includes docs and tests (which require network)
Source:         https://github.com/joepie91/python-whois/archive/%{commit}.zip#/%{name}-%{version}.zip
# PATCH-FIX-UPSTREAM remove_argparse_req.patch -- argparse is not a package
Patch0:         remove_argparse_req.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
Conflicts:      perl-Net-Whois-Raw
%python_subpackages

%description
Module for retrieving and parsing the WHOIS data for a domain.

%prep
%autosetup -p1 -n python-whois-%{commit}
# https://github.com/joepie91/python-whois/issues/142
# boo#1129473
sed -i 's/\(\s*regex = re.sub(r"\\\\s.*\)r"\\s\(.*\)>\\S\(.*\)/\1r"\\\\s\2>\\\\S\3/' pythonwhois/parse.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pwhois
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pwhois

%postun
%python_uninstall_alternative pwhois

%files %{python_files}
%doc README.md doc/*.html
%license LICENSE.txt
%python_alternative %{_bindir}/pwhois
%{python_sitelib}/pythonwhois
%{python_sitelib}/pythonwhois-%{version}.dist-info

%changelog
