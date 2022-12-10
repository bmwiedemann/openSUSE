#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%define pythons python3
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define srcname tpm2-pytss
%bcond_with     test
Name:           python-%{srcname}
Version:        2.0.0
Release:        0
Summary:        Python bindings for TSS
License:        BSD-2-Clause
URL:            https://github.com/tpm2-software/tpm2-pkcs11
Source:         %{srcname}-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module asn1crypto}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module pycparser}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(tss2-esys)
BuildRequires:  pkgconfig(tss2-fapi)
Requires:       python3-PyYAML
Requires:       python3-asn1crypto
Requires:       python3-cffi
Requires:       python3-cryptography
Requires:       python3-packaging
Requires:       python3-setuptools
Requires:       pkgconfig(tss2-esys)
Requires:       pkgconfig(tss2-fapi)
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  swtpm
# /SECTION
%endif
%python_subpackages

%description
TPM2 TSS Python bindings for Enhanced System API (ESYS), Feature API
(FAPI), Marshaling (MU), TCTI Loader (TCTILdr) and RC Decoding
(rcdecode) libraries. It also contains utility methods for wrapping
keys to TPM 2.0 data structures for importation into the TPM,
unwrapping keys and exporting them from the TPM, TPM-less
makecredential command and name calculations, TSS2 PEM Key format
support, importing Keys from PEM, DER and SSH formats, conversion from
tpm2-tools based command line strings and loading tpm2-tools context
files.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
# Provides a PKG-INFO with "version" for setuptools_scm
cat <<EOF > PKG-INFO
Metadata-Version: 1.1
Version:        %{version}
EOF
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with test}
%check
%pytest_arch
%endif

%files %{python_files}
%license LICENSE
%{python_sitearch}/tpm2_pytss
%{python_sitearch}/tpm2_pytss-%{version}*-info

%changelog
