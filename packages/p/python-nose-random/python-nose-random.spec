#
# spec file for package python-nose-random
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
Name:           python-nose-random
Version:        1.0.0
Release:        0
Summary:        Nose plugin to facilitate randomized unit testing
License:        MIT
URL:            https://github.com/xlwings/nose-random
Source:         https://github.com/xlwings/nose-random/archive/%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-nose
BuildArch:      noarch
%python_subpackages

%description
nose-random is designed to facilitate Monte-Carlo style unit testing. The idea is to improve testing by running your code against a large number of randomly generated input scenarios.

%prep
%setup -q -n nose-random-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%{$python_bin_suffix} examples/tests.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
