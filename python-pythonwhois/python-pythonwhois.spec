#
# spec file for package python-pythonwhois
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
%define commit 60adc3acc2d59627b2e32dc36d27802942e0820d/
Name:           python-pythonwhois
Version:        2.4.3
Release:        0
Summary:        Python whois library
License:        WTFPL
Group:          Development/Languages/Python
Url:            http://cryto.net/pythonwhois
#Source:         https://files.pythonhosted.org/packages/source/p/pythonwhois/pythonwhois-%%{version}.tar.gz
# github tarball includes docs and tests (which require network)
Source:         https://github.com/joepie91/python-whois/archive/%{commit}.zip#/%{name}-%{version}.zip
# PATCH-FIX-UPSTREAM remove_argparse_req.patch -- argparse is not a package
Patch0:         remove_argparse_req.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
%ifpython3
Conflicts:      perl-Net-Whois-Raw
%endif
BuildArch:      noarch

%python_subpackages

%description
Module for retrieving and parsing the WHOIS data for a domain.

%prep
%setup -q -n python-whois-%{commit}
%patch0 -p1
# https://github.com/joepie91/python-whois/issues/142
# boo#1129473
sed -i 's/\(\s*regex = re.sub(r"\\\\s.*\)r"\\s\(.*\)>\\S\(.*\)/\1r"\\\\s\2>\\\\S\3/' pythonwhois/parse.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone %{buildroot}%{_bindir}/pwhois

%files %{python_files}
%doc README.md doc/*.html
%license LICENSE.txt
%{_bindir}/pwhois-%{python_bin_suffix}
%python3_only %{_bindir}/pwhois
%{python_sitelib}/*

%changelog
