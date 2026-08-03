#
# spec file for package suse-libsgx-prebuilt-signed
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


%global  _buildshell /bin/bash
Name:           suse-libsgx-prebuilt-signed
Version:        1
Release:        0
Summary:        SGX enclaves built and signed by Intel
License:        BSD-3-Clause
URL:            https://download.01.org/intel-sgx/sgx-dcap/1.24/linux/
ExclusiveArch:  x86_64
Source0:        prebuilt_ae_2.25.tar.gz
Source1:        prebuilt_dcap_1.24.tar.gz
Source123:      suse-libsgx-prebuilt-signed.rpmlintrc
Conflicts:      libsgx-ae-epid
Conflicts:      libsgx-ae-id-enclave
Conflicts:      libsgx-ae-le
Conflicts:      libsgx-ae-pce
Conflicts:      libsgx-ae-qe3
Conflicts:      libsgx-ae-qve
Conflicts:      libsgx-ae-tdqe
Conflicts:      libsgx-dcap-quote-verify
Conflicts:       suse-libsgx-ae-epid
Conflicts:       suse-libsgx-ae-id-enclave
Conflicts:       suse-libsgx-ae-le
Conflicts:       suse-libsgx-ae-pce
Conflicts:       suse-libsgx-ae-qe3
Conflicts:       suse-libsgx-ae-qve
Conflicts:       suse-libsgx-ae-tdqe
Conflicts:       suse-tee_appraisal_policy

%description
Signed SGX Enclaves which will be verified and loaded at application runtime.
Intel(R) SGX ID enclave
Intel(R) SGX LE
Intel(R) SGX PCE
Intel(R) SGX QE and PvE
Intel(R) SGX QE3
Intel(R) SGX QVE
Intel(R) Trust Domain Extensions QE

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

%install
mkdir -p %buildroot%_libdir
mv -t %buildroot%_libdir *.signed.*

%files
%license BSD-3-Clause.txt
%_libdir/libsgx_id_enclave.signed.so.1
%_libdir/libsgx_launch_enclave.signed.so.1
%_libdir/libsgx_pce.signed.so.1
%_libdir/libsgx_provision_enclave.signed.so.1
%_libdir/libsgx_qe.signed.so.1
%_libdir/libsgx_qe3.signed.so.1
%_libdir/libsgx_qve.signed.so.1
%_libdir/libsgx_tdqe.signed.so.1

%changelog

