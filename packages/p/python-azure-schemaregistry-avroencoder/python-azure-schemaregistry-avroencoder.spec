#
# spec file for package python-azure-schemaregistry-avroencoder
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


%{?sle15_python_module_pythons}
Name:           python-azure-schemaregistry-avroencoder
Version:        1.0.0
Release:        0
Summary:        Microsoft Azure Schema Registry Avro Encoder Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-schemaregistry-avroencoder/azure-schemaregistry-avroencoder-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module azure-schemaregistry >= 1.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-avro >= 1.11.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-typing_extensions >= 4.0.1
Requires:       (python-azure-schemaregistry >= 1.0.0 with python-azure-schemaregistry < 2.0.0)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-schemaregistry-avroencoder < 1.0.0
%endif
BuildArch:      noarch

%python_subpackages

%description
Azure Schema Registry is a schema repository service hosted by Azure Event Hubs, providing
schema storage, versioning, and management. This package provides an Avro encoder capable
of encoding and decoding payloads containing Schema Registry schema identifiers and
Avro-encoded content.

%prep
%setup -q -n azure-schemaregistry-avroencoder-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-schemaregistry-avroencoder-%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/schemaregistry/encoder
%{python_sitelib}/azure_schemaregistry_avroencoder-*.dist-info

%changelog
