#
# spec file for package python-sigstore-protobuf-specs
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


Name:           python-sigstore-protobuf-specs
Version:        0.3.2
Release:        0
Summary:        A library for serializing and deserializing Sigstore messages
License:        Apache-2.0
URL:            https://github.com/sigstore/protobuf-specs
Source:         https://files.pythonhosted.org/packages/source/s/sigstore-protobuf-specs/sigstore_protobuf_specs-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
# /SECTION
BuildRequires:  fdupes
Requires:       python-betterproto
BuildArch:      noarch
%python_subpackages

%description
A library for serializing and deserializing Sigstore messages

%prep
%autosetup -p1 -n sigstore_protobuf_specs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}/%{python_sitelib} $python -c "import sigstore_protobuf_specs"

%files %{python_files}
%{python_sitelib}/sigstore_protobuf_specs
%{python_sitelib}/sigstore_protobuf_specs-%{version}.dist-info

%changelog
