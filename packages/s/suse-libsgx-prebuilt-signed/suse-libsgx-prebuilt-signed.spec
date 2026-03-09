#
# spec file for package suse-libsgx-prebuilt-signed
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


%global  _buildshell /bin/bash
Name:           suse-libsgx-prebuilt-signed
Version:        1
Release:        0
Summary:        SGX libraries built and signed by Intel
License:        BSD-3-Clause
URL:            https://download.01.org/intel-sgx/sgx-dcap/1.24/linux/
ExclusiveArch:  x86_64
Source0:        prebuilt_ae_2.25.tar.gz
Source1:        prebuilt_dcap_1.24.tar.gz
Source123:      suse-libsgx-prebuilt-signed.rpmlintrc

%description
Libraries which will be verified and loaded at application runtime.

%package -n suse-libsgx-ae-epid
Summary:        Intel(R) SGX QE and PvE
Conflicts:      libsgx-ae-epid
Requires:       %name = %version-%release
%description -n suse-libsgx-ae-epid
Intel(R) Software Guard Extensions QE and PvE
%files -n suse-libsgx-ae-epid
%_libdir/libsgx_provision_enclave.signed.so.1
%_libdir/libsgx_qe.signed.so.1

%package -n suse-libsgx-ae-id-enclave
Summary:        Intel(R) SGX ID enclave
Conflicts:      libsgx-ae-id-enclave
Requires:       %name = %version-%release
%description -n suse-libsgx-ae-id-enclave
Intel(R) Software Guard Extensions ID enclave
%files -n suse-libsgx-ae-id-enclave
%_libdir/libsgx_id_enclave.signed.so.1

%package -n suse-libsgx-ae-le
Summary:        Intel(R) SGX LE
Conflicts:      libsgx-ae-le
Requires:       %name = %version-%release
%description -n suse-libsgx-ae-le
Intel(R) Software Guard Extensions LE
%files -n suse-libsgx-ae-le
%_libdir/libsgx_launch_enclave.signed.so.1

%package -n suse-libsgx-ae-pce
Summary:        Intel(R) SGX PCE
Conflicts:      libsgx-ae-pce
Requires:       %name = %version-%release
%description -n suse-libsgx-ae-pce
Intel(R) Software Guard Extensions PCE
%files -n suse-libsgx-ae-pce
%_libdir/libsgx_pce.signed.so.1

%package -n suse-libsgx-ae-qe3
Summary:        Intel(R) SGX QE3
Conflicts:      libsgx-ae-qe3
Requires:       %name = %version-%release
%description -n suse-libsgx-ae-qe3
Intel(R) Software Guard Extensions QE3
%files -n suse-libsgx-ae-qe3
%_libdir/libsgx_qe3.signed.so.1

%package -n suse-libsgx-ae-qve
Summary:        Intel(R) SGX QVE
Conflicts:      libsgx-ae-qve
Requires:       %name = %version-%release
%description -n suse-libsgx-ae-qve
Intel(R) Software Guard Extensions QVE
%files -n suse-libsgx-ae-qve
%_libdir/libsgx_qve.signed.so.1

%package -n suse-libsgx-ae-tdqe
Summary:        Intel(R) Trust Domain Extensions QE
Conflicts:      libsgx-ae-tdqe
Requires:       %name = %version-%release
%description -n suse-libsgx-ae-tdqe
Intel(R) Trust Domain Extensions QE
%files -n suse-libsgx-ae-tdqe
%_libdir/libsgx_tdqe.signed.so.1

%package -n suse-tee_appraisal_policy
Summary:        Policy file used by quote-verify enclave
Conflicts:      libsgx-dcap-quote-verify
Requires:       %name = %version-%release
%description -n suse-tee_appraisal_policy
Policy file used by quote-verify enclave.
%files -n suse-tee_appraisal_policy
%_datadir/sgx

%prep
%setup -c -T -D

%build
archive_ae='prebuilt_ae_2.25.tar.gz'
archive_dcap='prebuilt_dcap_1.24.tar.gz'
ln -s %{S:0} "${archive_ae}"
ln -s %{S:1} "${archive_dcap}"
tee | sha256sum -c <<__EOC__
1e587deab60eca6976cb9d1df0048acfa53dec597485b198102799886f673124  ${archive_ae}
b1cfde6083dd8700320e4d998751d4eb2b859686ea572ff8fbe9b93a7404dc17  ${archive_dcap}
__EOC__
tar xfva "${archive_ae}"
tar xfva "${archive_dcap}"
for ELF in psw/ae/data/prebuilt/*.signed.so
do
  file "${ELF}"
  chmod -c 444 "${ELF}"
  read SONAME < <(objdump --private-headers "${ELF}" | awk '/^[[:blank:]]+SONAME[[:blank:]]+/{print $2}')
  mv "${ELF}" "${SONAME}"
done
mv prebuilt/opa_bin/policy.wasm tee_appraisal_policy.wasm
chmod -c 444 "${_}"

%install
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_datadir/sgx
mv -t %buildroot%_libdir *.signed.*
mv -t %buildroot%_datadir/sgx *.wasm

%files
%license BSD-3-Clause.txt

%changelog

