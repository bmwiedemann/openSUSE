#
# spec file for package python-ruamel.yaml
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


%{?sle15_python_module_pythons}
Name:           python-ruamel.yaml
Version:        0.18.10
Release:        0
Summary:        Python YAML parser
License:        MIT
URL:            https://sourceforge.net/p/ruamel-yaml
Source:         https://files.pythonhosted.org/packages/source/r/ruamel.yaml/ruamel.yaml-%{version}.tar.gz
Patch0:         0000-fix-big-endian-issues.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ruamel.yaml.clib >= 0.2.0
BuildArch:      noarch
%python_subpackages

%description
ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation
of comments, seq/map flow style, and map key order.

%prep
%autosetup -p1 -n ruamel.yaml-%{version}
rm -rf *egg-info

%build
%python_build

%install
%python_install --single-version-externally-managed
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc CHANGES README.md
%{python_sitelib}/ruamel
%{python_sitelib}/ruamel.yaml-%{version}*-info

%changelog
