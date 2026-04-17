#
# spec file for package python-griffelib
#
# Copyright (c) 2026 SUSE LLC
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

Name:           python-griffelib
Version:        2.0.2
Release:        0
Summary:        Signatures for entire Python programs (library)
License:        ISC
URL:            https://mkdocstrings.github.io/griffe/
Source0:        https://files.pythonhosted.org/packages/source/g/griffelib/griffelib-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE static-version.patch mcepl@suse.com
# Don't use uv-dynamic-versioning, just set it statically
Patch0:         static-version.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
Suggests:       python-pip >= 24.0
Suggests:       python-platformdirs >= 4.2
Suggests:       python-wheel >= 0.42
BuildArch:      noarch
%python_subpackages

%description
This is the library for griffe package.

%prep
%autosetup -p1 -n griffelib-%{version}

# set the version
sed -i -e '/^version =/s/@VERSION@/%{version}/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE LICENSE
%{python_sitelib}/griffe
%{python_sitelib}/griffelib-%{version}.dist-info

%changelog
