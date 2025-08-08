#
# spec file for package python-tpm2-pytss
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


%define pythons python3
%define srcname tpm2-pytss
%bcond_with     test
Name:           python-%{srcname}
Version:        2.3.0
Release:        0
Summary:        Python bindings for TSS
License:        BSD-2-Clause
URL:            https://github.com/tpm2-software/tpm2-pytss
Source:         https://github.com/tpm2-software/%{srcname}/archive/refs/tags/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
#PATCH-FIX-UPSTREAM use-c99-for-preproccessing.patch from https://github.com/tpm2-software/tpm2-pytss/commit/61d00b4dcca131b3f03f674ceabf4260bdbd6a61
Patch:          use-c99-for-preproccessing.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module asn1crypto}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module pycparser}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with test}
%check
%pytest_arch
%endif

%files %{python_files}
%license LICENSE
%{python_sitearch}/tpm2_pytss
%{python_sitearch}/tpm2_pytss-%{version}.dist-info

%changelog
