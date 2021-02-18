#
# spec file for package python-Faker
#
# Copyright (c) 2021 SUSE LLC
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
%define oldpython python
%global skip_python2 1
Name:           python-Faker
Version:        6.3.0
Release:        0
Summary:        Python package that generates fake data
License:        MIT
URL:            https://github.com/joke2k/faker
Source:         https://files.pythonhosted.org/packages/source/F/Faker/Faker-%{version}.tar.gz
BuildRequires:  %{python_module UkPostcodeParser >= 1.1.1}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest >= 3.8.0}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module python-dateutil >= 2.4}
BuildRequires:  %{python_module random2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10}
BuildRequires:  %{python_module text-unidecode >= 1.3}
BuildRequires:  %{python_module validators >= 0.13.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 2.4
Requires:       python-setuptools
Requires:       python-six >= 1.10
Requires:       python-text-unidecode >= 1.3
Requires(post): update-alternatives
Requires(postun): update-alternatives
Obsoletes:      python3-fake-factory < %{version}
Provides:       python3-fake-factory = %{version}
BuildArch:      noarch
%python_subpackages

%description
Faker is a Python package that generates fake data. It helps with
database bootstrapping, creating XML documents, persistence stress
testing, and data anonymization from production services.

%prep
%setup -q -n Faker-%{version}
# Remove pre-existing bytecode files in the sdist
find . -name '*.py[co]' -delete
# do not hardcode versions
sed -i -e 's:==:>=:g' setup.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/faker
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative faker

%postun
%python_uninstall_alternative faker

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.md README.rst
%python_alternative %{_bindir}/faker
%{python_sitelib}/*

%changelog
