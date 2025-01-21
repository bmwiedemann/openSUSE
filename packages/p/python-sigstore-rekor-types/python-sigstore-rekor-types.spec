#
# spec file for package python-sigstore-rekor-types
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-sigstore-rekor-types
Version:        0.0.18
Release:        0
Summary:        Python models for Rekor's API types
License:        Apache-2.0
URL:            https://github.com/trailofbits/sigstore-rekor-types
Source:         https://files.pythonhosted.org/packages/source/s/sigstore_rekor_types/sigstore_rekor_types-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pydantic >= 2
BuildArch:      noarch
%python_subpackages

%description
Python models for Rekor's API types.

%prep
%autosetup -p1 -n sigstore_rekor_types-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/rekor_types
%{python_sitelib}/sigstore_rekor_types-%{version}.dist-info

%changelog
