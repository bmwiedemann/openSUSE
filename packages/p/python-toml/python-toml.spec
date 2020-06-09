#
# spec file for package python-toml
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-toml
Version:        0.10.1
Release:        0
Summary:        Python module which parses and emits TOML
License:        MIT
URL:            https://github.com/uiri/toml
Source:         https://files.pythonhosted.org/packages/source/t/toml/toml-%{version}.tar.gz
# Untagged test data https://github.com/uiri/toml/issues/232
Source1:        https://github.com/BurntSushi/toml-test/archive/280497f.tar.gz#/toml-test-280497f.tar.gz
# Missing file https://github.com/uiri/toml/pull/231
Source2:        https://raw.githubusercontent.com/uiri/toml/%{version}/test.toml
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  coreutils
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python toml allows to parse and create toml configuration files.
See below the toml specification link.

Usage
toml.loads --- takes a string to be parsed as toml and returns
the corresponding dictionary
toml.dumps --- takes a dictionary and returns a string which
is the contents of the corresponding toml file.

There are other functions which can be used to dump and load various
fragments of toml but dumps and loads will cover most usage.

Current Version of TOML Specification
https://github.com/mojombo/toml/blob/v0.4.0/README.md

%prep
%setup -q -n toml-%{version}
tar -xzf %{SOURCE1}
ln -s toml-test*/ toml-test
cp %{SOURCE2} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
# See https://github.com/uiri/toml/issues/216 re change log
%license LICENSE
%doc README.rst
%{python_sitelib}

%changelog
