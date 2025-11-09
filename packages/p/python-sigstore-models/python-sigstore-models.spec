#
# spec file for package python-sigstore-models
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-sigstore-models
Version:        0.0.5
Release:        0
Summary:        Pydantic based models for Sigstore's protobuf specifications
License:        MIT
URL:            https://github.com/astral-sh/sigstore-models
Source:         https://files.pythonhosted.org/packages/source/s/sigstore-models/sigstore_models-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-build >= 0.8.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pydantic >= 2.11.7}
BuildRequires:  %{python_module typing-extensions >= 4.14.1}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pydantic >= 2.11.7
Requires:       python-typing-extensions >= 4.14.1
BuildArch:      noarch
%python_subpackages

%description
Pydantic-based data models for Sigstore.

These models mirror the subset of the [protobuf-specs] that
are used by the [sigstore-python] library.

%prep
%autosetup -p1 -n sigstore_models-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%{python_sitelib}/sigstore_models
%{python_sitelib}/sigstore_models-%{version}.dist-info

%changelog
