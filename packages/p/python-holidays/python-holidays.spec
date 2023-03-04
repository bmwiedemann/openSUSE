#
# spec file for package python-holidays
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-holidays
Version:        0.20
Release:        0
Summary:        Python library for generating holidays on the fly
License:        MIT
URL:            https://github.com/dr-prodigy/python-holidays
Source:         https://github.com/dr-prodigy/python-holidays/archive/refs/tags/v.%{version}.tar.gz#/holidays-%{version}.tar.gz
BuildRequires:  %{python_module convertdate}
BuildRequires:  %{python_module hijri-converter >= 2.2}
BuildRequires:  %{python_module korean-lunar-calendar}
BuildRequires:  %{python_module pytest}
#BuildRequires:  %%{python_module lag_baomer}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-convertdate
Requires:       python-hijri-converter >= 2.2
Requires:       python-korean-lunar-calendar
#Requires:       python-lag_baomer
Requires:       python-python-dateutil
BuildArch:      noarch
%python_subpackages

%description
A Python library for generating country, province and state specific sets of holidays on the fly.
It makes determining whether a specific date is a holiday possible.

%prep
%setup -q -n python-holidays-v.%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGES README.rst
%{python_sitelib}/*

%changelog
