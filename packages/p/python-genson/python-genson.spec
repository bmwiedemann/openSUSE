#
# spec file for package python-genson
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
Name:           python-genson
Version:        1.2.2
Release:        0
Summary:        Python JSON Schema generator
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/wolverdude/genson/
Source:         https://files.pythonhosted.org/packages/source/g/genson/genson-%{version}.tar.gz
# https://github.com/wolverdude/GenSON/pull/53
Source1:        https://raw.githubusercontent.com/wolverdude/GenSON/master/test/fixtures/cp1252.json
Source2:        https://raw.githubusercontent.com/wolverdude/GenSON/master/test/fixtures/utf-8.json
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module jsonschema}
# /SECTION
%python_subpackages

%description
GenSON is a JSON Schema generator.

Besides taking JSON objects and generating schemas that describe
them, this generator is able to merge schemas as well.

%prep
%setup -q -n genson-%{version}
mkdir test/fixtures
cp %{SOURCE1} %{SOURCE2} test/fixtures/
touch test/__init__.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/genson
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
mkdir ~/bin
export PATH=~/bin:$PATH
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
cp %{buildroot}/%{_bindir}/genson-%{$python_bin_suffix} ~/bin/genson
rm -f ~/bin/python
ln -s $(which $python) ~/bin/python
$python -m unittest -v
}

%post
%python_install_alternative genson

%postun
%python_uninstall_alternative genson

%files %{python_files}
%doc AUTHORS.rst README.rst HISTORY.rst
%license LICENSE
%python_alternative %{_bindir}/genson
%{python_sitelib}/*

%changelog
