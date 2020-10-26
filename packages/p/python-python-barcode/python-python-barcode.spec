#
# spec file for package python-python-barcode
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 Dr. Axel Braun
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
%define skip_python2 1
%define base_name python-barcode
Name:           python-%{base_name}
Version:        0.13.1
Release:        0
Summary:        Library to create Barcodes with Python
License:        MIT
URL:            https://github.com/WhyNotHugo/python-barcode
Source:         https://files.pythonhosted.org/packages/source/p/%{base_name}/%{base_name}-%{version}.tar.gz
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module pathlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       dejavu-fonts
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-pyBarcode
Obsoletes:      python-pyBarcode
BuildArch:      noarch
%python_subpackages

%description
Library to create standard barcodes with Python. No external modules needed (optional PIL support included).

%prep
%setup -q -n %{base_name}-%{version}
# Fix rpmlint warning about too many +x perms when these files get installed later.
find . -type f -exec chmod a-x {} +
# doc buildscripts we don't wanna ship
rm docs/Makefile

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/python-barcode
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}
find %{buildroot} -type f -name "*.ttf" | while read i; do
	ln -fs "%{_datadir}/fonts/truetype/${i##*/}" "$i"
done

%check
sed -i '/cov/d' setup.cfg
%pytest

%post
%python_install_alternative python-barcode

%postun
%python_uninstall_alternative python-barcode

%files %{python_files}
%doc docs/*
%license LICENCE
%{python_sitelib}/*
%python_alternative %{_bindir}/python-barcode

%changelog
