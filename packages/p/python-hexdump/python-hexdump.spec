#
# spec file for package python-hexdump
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


Name:           python-hexdump
Version:        3.3
Release:        0
Summary:        Python tool to dump binary data
License:        Unlicense
Group:          Development/Languages/Python
URL:            https://bitbucket.org/techtonik/hexdump/
Source0:        https://files.pythonhosted.org/packages/source/h/hexdump/hexdump-%{version}.zip
Source1:        https://bitbucket.org/techtonik/hexdump/raw/66325cb5fed890df4a345e25ea8f107fd31b60d8/UNLICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
%python_subpackages

%description
This utility converts between the raw representation and a
byte-based hexdump representation.

The display is equivalent to the output of the `hexdump -C` command, but
it requires a Python runtime.

%prep
%setup -q -c -n hexdump-%{version}
sed -i '/^#!/d' hexdump.py
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
# this folder is needed only for tests
rm -rf %{buildroot}%{_prefix}/data
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python hexdump.py --test

%files %{python_files}
%{python_sitelib}/hexdump.py
%{python_sitelib}/hexdump-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/hexdump*
%doc README.txt
%license UNLICENSE

%changelog
