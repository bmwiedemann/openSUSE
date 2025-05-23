#
# spec file for package python-python-barcode
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2019-2024 Dr. Axel Braun <DocB@opensuse.org>
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

%define base_name python-barcode
Name:           python-%{base_name}
Version:        0.15.1
Release:        0
Summary:        Library to create Barcodes with Python
License:        MIT
URL:            https://github.com/WhyNotHugo/python-barcode
Source:         https://files.pythonhosted.org/packages/source/p/%{base_name}/%{base_name}-%{version}.tar.gz
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       dejavu-fonts
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-pyBarcode = %{version}-%{release}
Obsoletes:      python-pyBarcode < %{version}-%{release}
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
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/python-barcode
%python_expand %fdupes %{buildroot}%{$python_sitelib}
find %{buildroot} -type f -name "*.ttf" | while read i; do
	ln -fs "%{_datadir}/fonts/truetype/${i##*/}" "$i"
done
%{python_expand # copy docs for deduplication
mkdir -p %{buildroot}%{_docdir}
cp -r docs %{buildroot}%{_docdir}/$python-python-barcode
%fdupes %{buildroot}%{_docdir}/$python-python-barcode
}

%check
sed -i '/cov/d' setup.cfg
%pytest

%post
%python_install_alternative python-barcode

%postun
%python_uninstall_alternative python-barcode

%files %{python_files}
%license LICENCE
%doc %{_docdir}/%{python_flavor}-python-barcode
%{python_sitelib}/barcode
%{python_sitelib}/python_barcode-%{version}.dist-info
%python_alternative %{_bindir}/python-barcode

%changelog
