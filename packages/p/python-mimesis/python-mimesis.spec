#
# spec file for package python-mimesis
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
%define         skip_python2 1
Name:           python-mimesis
Version:        3.3.0
Release:        0
Summary:        Fake data generator
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/lk-geimfari/mimesis
Source:         https://github.com/lk-geimfari/mimesis/archive/v%{version}.tar.gz#/mimesis-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-pytz
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
# /SECTION
%python_subpackages

%description
Mimesis is a package for Python, which helps generate big volumes of
fake data for a variety of purposes in a variety of languages. The
fake data could be used to populate a testing database, create JSON
and XML files, anonymize data taken from production and etc.

%prep
%setup -q -n mimesis-%{version}
chmod a-x LICENSE README.rst
chmod a-x mimesis/data/*/*.json

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
rm %{buildroot}%{_prefix}/LICENSE

%check
sed -i '/--\(flake8\|isort\)/d' setup.cfg
# some tests require a network connection
%pytest -k 'not (test_download_image or test_stock_image)'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/mimesis-%{version}-py*.egg-info
%{python_sitelib}/mimesis/

%changelog
