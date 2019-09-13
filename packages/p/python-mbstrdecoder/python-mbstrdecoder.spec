#
# spec file for package python-mbstrdecoder
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
Name:           python-mbstrdecoder
Version:        0.8.1
Release:        0
Summary:        Multi-byte character string decoder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/thombashi/mbstrdecoder
Source:         https://files.pythonhosted.org/packages/source/m/mbstrdecoder/mbstrdecoder-%{version}.tar.gz
BuildRequires:  %{python_module chardet >= 3.0.4}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-chardet >= 3.0.4
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Python library for multi-byte character string decoding.

%prep
%setup -q -n mbstrdecoder-%{version}
# De-vendor six
rm mbstrdecoder/_six.py
sed -i 's/\._six/six/' mbstrdecoder/_mbstrdecoder.py

find . -type f | xargs chmod -x

echo > requirements/test_requirements.txt

# Remove build alias
sed -i '/build =/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
