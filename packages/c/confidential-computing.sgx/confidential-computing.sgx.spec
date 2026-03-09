#
# spec file for package confidential-computing.sgx
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

%define build_flavor @BUILD_FLAVOR@%nil
%define pkg confidential-computing.sgx
%define pkg_suffix %nil

%global _buildshell /bin/bash
%define _lto_cflags %nil
# Both repositories have different versions
# The version of the primary repository is used,
# to avoid rebuilds because build-compare can not cope with
# two different versions in sub-packages from the same src.rpm
%define coco_sgx_version 2.28
%define sgx_dcap_version 2.28
#
%define sgx_ssl_hash 1f99dd73e4a38a0da2b47f74064b28b8da04f794
#
Name:           %pkg%pkg_suffix
Version:        %coco_sgx_version
Release:        0
# The secondary Version tags shadow the primary Version/Release
%define primary_pkg_version %coco_sgx_version-%release
Summary:        Anchor package for confidential-computing.sgx.git
License:        BSD-3-Clause
URL:            https://github.com/intel/confidential-computing.sgx
ExclusiveArch:  x86_64
Source0:        %pkg-%version.tar
Source6:        sgx-ssl-%sgx_ssl_hash.tar
Source123:      %pkg.rpmlintrc
Patch0:         %pkg.patch
Patch6:         sgx-ssl.patch
Obsoletes:      linux-sgx < %version-%release
Provides:       linux-sgx = %version-%release
BuildRequires:  bash
BuildRequires:  cmake
BuildRequires:  gcc%?suse_sgx_gcc_major
BuildRequires:  gcc%?suse_sgx_gcc_major-c++
%if "%build_flavor" == ""
BuildRequires:  libboost_headers-devel
%if 0%?suse_version < 1600
BuildRequires:  libboost_system-devel
%endif
BuildRequires:  libboost_thread-devel
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(libcrypto) >= 3
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl) >= 3
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(tinyxml2)
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
# build_flavor == ""
%endif
%description
This is an anchor package, which every package below requires.
It contains the unique License file for all subpackages.

It makes sure that every binary and library comes from the
same build.

Each subpackage contains a Conflicts tag to make sure the
binary packages provided by Intel(R) will be removed by zypper.

%if "%build_flavor" == ""
%files
%license License.txt
%dir %_datadir/%pkg

%package -n system-user-aesmd
Summary:        System user aesmd
Requires:       %pkg = %primary_pkg_version
%?sysusers_requires
%description -n system-user-aesmd
System user aesmd for Intel(R) Architectural Enclave Service Manager
%pre -n system-user-aesmd -f system-user-aesmd.pre
%post -n system-user-aesmd
%tmpfiles_create %_tmpfilesdir/system-user-aesmd.conf
%files -n system-user-aesmd
%_sysusersdir/system-user-aesmd.conf
%_tmpfilesdir/system-user-aesmd.conf

%package -n system-user-qgsd
Summary:        System user qgsd
Requires:       %pkg = %primary_pkg_version
%?sysusers_requires
%description -n system-user-qgsd
System user qgsd for Intel(R) TD Quoting Generation Service
%pre -n system-user-qgsd -f system-user-qgsd.pre
%post -n system-user-qgsd
%tmpfiles_create %_tmpfilesdir/system-user-qgsd.conf
%files -n system-user-qgsd
%_sysusersdir/system-user-qgsd.conf
%_tmpfilesdir/system-user-qgsd.conf

%package -n suse-sgx_edger8r
Summary:        Code generator for SGX
Requires:       %pkg = %primary_pkg_version
Requires:       gcc
Requires:       suse-libsgx-headers = %primary_pkg_version
Requires:       which
%description -n suse-sgx_edger8r
A code generator for Intel(R) SGX.
%files -n suse-sgx_edger8r
%_includedir/sgx_edger8r.h
%_bindir/sgx_edger8r

%package -n suse-sgx_sign
Summary:        Sign enclave objects
Requires:       %pkg = %primary_pkg_version
%description -n suse-sgx_sign
Sign enclave objects.
%files -n suse-sgx_sign
%_bindir/sgx_sign

%package -n libsgx_enclave_common1
Summary:        SUSE build of Intel(R) SGX Enclave Common Loader
Conflicts:      libsgx-enclave-common
Conflicts:      libsgx-enclave-common-debuginfo
Requires:       %pkg = %primary_pkg_version
%description -n libsgx_enclave_common1
Intel(R) Software Guard Extensions Enclave Common Loader
%ldconfig_scriptlets -n libsgx_enclave_common1
%files -n libsgx_enclave_common1
%_libdir/libsgx_enclave_common.so.*
%package -n suse-libsgx-enclave-common-devel
Summary:        SUSE build of Intel(R) SGX Enclave Common Loader for Developers
Conflicts:      libsgx-enclave-common-devel
Requires:       %pkg = %primary_pkg_version
Requires:       libsgx_enclave_common1 = %primary_pkg_version
%description -n suse-libsgx-enclave-common-devel
Intel(R) Software Guard Extensions Enclave Common Loader for Developers
%files -n suse-libsgx-enclave-common-devel
%_includedir/sgx_enclave_common.h
%_libdir/libsgx_enclave_common.so

%package -n suse-libsgx-headers
Summary:        SUSE build of Intel(R) SGX Basic Headers
Requires:       %pkg = %primary_pkg_version
Conflicts:      libsgx-headers
%description -n suse-libsgx-headers
Intel(R) Software Guard Extensions Basic Headers
%files -n suse-libsgx-headers
%_includedir/sgx_attributes.h
%_includedir/sgx_defs.h
%_includedir/sgx_eid.h
%_includedir/sgx_error.h
%_includedir/sgx_key.h
%_includedir/sgx_pce.h
%_includedir/sgx_ql_lib_common.h
%_includedir/sgx_ql_quote.h
%_includedir/sgx_quote.h
%_includedir/sgx_quote_3.h
%_includedir/sgx_quote_4.h
%_includedir/sgx_quote_5.h
%_includedir/sgx_report.h
%_includedir/sgx_report2.h
%_includedir/sgx_urts.h

%package -n libsgx_quote_ex1
Summary:        SUSE build of Intel(R) SGX Unified Quote Service
Requires:       %pkg = %primary_pkg_version
Conflicts:      libsgx-quote-ex
Conflicts:      libsgx-quote-ex-debuginfo
%description -n libsgx_quote_ex1
Intel(R) Software Guard Extensions Unified Quote Service
%files -n libsgx_quote_ex1
%_libdir/libsgx_quote_ex.so.*
%package -n suse-libsgx-quote-ex-devel
Summary:        SUSE build of Intel(R) SGX Unified Quote Service for Developers
Conflicts:      libsgx-quote-ex-devel
Requires:       %pkg = %primary_pkg_version
Requires:       libsgx_quote_ex1 = %primary_pkg_version
%description -n suse-libsgx-quote-ex-devel
Intel(R) Software Guard Extensions Unified Quote Service for Developers
%ldconfig_scriptlets -n libsgx_quote_ex1
%files -n suse-libsgx-quote-ex-devel
%_includedir/sgx_uae_quote_ex.h
%_libdir/libsgx_quote_ex.so

%package -n libtdx_attest1
Summary:        SUSE build of Intel(R) TDX Attestation library
Requires:       %pkg = %primary_pkg_version
Conflicts:      libtdx-attest
Conflicts:      libtdx-attest-debuginfo
%description -n libtdx_attest1
Intel(R) Software Guard Extensions Unified Quote Service
%files -n libtdx_attest1
%_libdir/libtdx_attest.so.*
%package -n suse-libtdx-attest-devel
Summary:        SUSE build of Intel(R) SGX Unified Quote Service for Developers
Conflicts:      libtdx-attest-devel
Requires:       %pkg = %primary_pkg_version
Requires:       libtdx_attest1 = %primary_pkg_version
%description -n suse-libtdx-attest-devel
Intel(R) Software Guard Extensions Unified Quote Service for Developers
%ldconfig_scriptlets -n libtdx_attest1
%files -n suse-libtdx-attest-devel
%_includedir/tdx_attest.h
%_libdir/libtdx_attest.so
%_sbindir/test_tdx_attest

%package -n libsgx_uae_service2
Summary:        SUSE build of Intel(R) SGX Untrusted AE Service
Conflicts:      libsgx-uae-service
Conflicts:      libsgx-uae-service-debuginfo
Requires:       %pkg = %primary_pkg_version
Requires:       libsgx_quote_ex1 = %primary_pkg_version
%description -n libsgx_uae_service2
Intel(R) Software Guard Extensions Untrusted Appraisal Enclave Service
%ldconfig_scriptlets -n libsgx_uae_service2
%files -n libsgx_uae_service2
%_libdir/libsgx_uae_service.so
%_libdir/libsgx_uae_service.so.*

%package -n libsgx_urts1
Summary:        SUSE build of Intel(R) SGX uRTS
Conflicts:      libsgx-urts
Conflicts:      libsgx-urts-debuginfo
Requires:       %pkg = %primary_pkg_version
%description -n libsgx_urts1
Intel(R) Software Guard Extensions Untrusted Runtime Service
%ldconfig_scriptlets -n libsgx_urts1
%files -n libsgx_urts1
%_libdir/libsgx_urts.so
%_libdir/libsgx_urts.so.*

%package -n suse-tdx-qgs
Summary:        SUSE build of Intel(R) TD Quoting Generation Service
Conflicts:      tdx-qgs
Requires:       %pkg = %primary_pkg_version
Requires:       system-user-qgsd = %primary_pkg_version
%description -n suse-tdx-qgs
Intel(R) TD Quoting Generation Service
%pre -n suse-tdx-qgs
%service_add_pre qgsd.service
%post -n suse-tdx-qgs
%service_add_post qgsd.service
%preun -n suse-tdx-qgs
%service_del_preun qgsd.service
%postun -n suse-tdx-qgs
%service_del_postun_with_restart qgsd.service
%posttrans -n suse-tdx-qgs
if test -c '/dev/sgx_enclave'
then
	if systemctl --quiet is-enabled qgsd.service
	then
		: already enabled
	else
		echo 'run "systemctl enable --now qgsd.service" to use this service.'
	fi
fi
%files -n suse-tdx-qgs
%_libexecdir/qgs
%_unitdir/qgsd.service
%_unitdir/remount-dev-exec.service

%package -n suse-tee-appraisal-tool
Summary:        SUSE build of Intel(R) SGX DCAP Appraisal Tool
Conflicts:      tee-appraisal-tool
Conflicts:      tee-appraisal-tool-debuginfo
Requires:       %pkg = %primary_pkg_version
%description -n suse-tee-appraisal-tool
Intel(R) Software Guard Extensions Data Center Attestation Primitives Appraisal Tool
%files -n suse-tee-appraisal-tool
%_sbindir/tee_appraisal_tool

%package -n suse-sgx-aesm-service
Summary: Intel(R) Architectural Enclave Service Manager
Requires:       %pkg = %primary_pkg_version
Conflicts:      sgx-aesm-service
Conflicts:      sgx-aesm-service-debuginfo
Requires:       %pkg = %primary_pkg_version
Requires:       suse-libsgx-aesm-ecdsa-plugin = %primary_pkg_version
Requires:       suse-libsgx-aesm-pce-plugin = %primary_pkg_version
Requires:       suse-libsgx-aesm-quote-ex-plugin = %primary_pkg_version
Requires:       system-user-aesmd = %primary_pkg_version
%description -n suse-sgx-aesm-service
Intel(R) Architectural Enclave Service Manager
%pre -n suse-sgx-aesm-service
%service_add_pre aesmd.service
%post -n suse-sgx-aesm-service
%service_add_post aesmd.service
%preun -n suse-sgx-aesm-service
%service_del_preun aesmd.service
%postun -n suse-sgx-aesm-service
%service_del_postun_with_restart aesmd.service
%posttrans -n suse-sgx-aesm-service
if test -c '/dev/sgx_enclave'
then
	if systemctl --quiet is-enabled aesmd.service
	then
		: already enabled
	else
		echo 'run "systemctl enable --now aesmd.service" to use this service.'
	fi
fi
%files -n suse-sgx-aesm-service
%dir %_libexecdir/aesm
%dir %_libexecdir/aesm/bundles
%_libexecdir/aesm/aesm_service
%_libexecdir/aesm/bundles/liblinux_network_service_bundle.so
%_unitdir/aesmd.service

%package -n suse-libsgx-aesm-ecdsa-plugin
Summary:        ECDSA Quote Plugin for AESM Service
Requires:       %pkg = %primary_pkg_version
Conflicts:      libsgx-aesm-ecdsa-plugin
Conflicts:      libsgx-aesm-ecdsa-plugin-debuginfo
%description -n suse-libsgx-aesm-ecdsa-plugin
ECDSA Quote Plugin for Intel(R) Software Guard Extensions AESM Service
%ldconfig_scriptlets -n suse-libsgx-aesm-ecdsa-plugin
%files -n suse-libsgx-aesm-ecdsa-plugin
%dir %_libexecdir/aesm
%dir %_libexecdir/aesm/bundles
%_libexecdir/aesm/bundles/libecdsa_quote_service_bundle.so

%package -n suse-libsgx-aesm-pce-plugin
Summary:        PCE Plugin for AESM Service
Requires:       %pkg = %primary_pkg_version
Conflicts:      libsgx-aesm-pce-plugin
Conflicts:      libsgx-aesm-pce-plugin-debuginfo
%description -n suse-libsgx-aesm-pce-plugin
Provisioning Certification Enclave Plugin for Intel(R) Software Guard Extensions AESM Service
%ldconfig_scriptlets -n suse-libsgx-aesm-pce-plugin
%files -n suse-libsgx-aesm-pce-plugin
%dir %_libexecdir/aesm
%dir %_libexecdir/aesm/bundles
%_libexecdir/aesm/bundles/libpce_service_bundle.so

%package -n suse-libsgx-aesm-quote-ex-plugin
Summary:        Unified Quote Plugin for AESM Service
Requires:       %pkg = %primary_pkg_version
Conflicts:      libsgx-aesm-quote-ex-plugin
Conflicts:      libsgx-aesm-quote-ex-plugin-debuginfo
%description -n suse-libsgx-aesm-quote-ex-plugin
Unified Quote Plugin for Intel(R) Software Guard Extensions AESM Service
%ldconfig_scriptlets -n suse-libsgx-aesm-quote-ex-plugin
%files -n suse-libsgx-aesm-quote-ex-plugin
%dir %_libexecdir/aesm
%dir %_libexecdir/aesm/bundles
%_libexecdir/aesm/bundles/libquote_ex_service_bundle.so

%package -n libCppMicroServices4
Summary:        OSGi-like C++ dynamic module system and service registry
URL:            https://github.com/CppMicroServices/CppMicroServices
Requires:       %pkg = %primary_pkg_version
%description -n libCppMicroServices4
The C++ Micro Services project is a collection of components for building modular and dynamic service-oriented applications. It is based on OSGi, but tailored to support native cross-platform solutions.
Based on commit 29348046dd8b680051de55c4eddee4222e2fae02 2018-10-24 09:08:10 -0400
%ldconfig_scriptlets -n libCppMicroServices4
%files -n libCppMicroServices4
%_libdir/libCppMicroServices.so.4.0.0

# The packages below come from a different git repository.
# This git repository has its own versioned tags.
# The packages need to be grouped at the end to get a different version.
%package -n libsgx_dcap_gl1
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) SGX DCAP
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-dcap-ql
Conflicts:      libsgx-dcap-ql-debuginfo
Requires:       %pkg = %primary_pkg_version
%description -n libsgx_dcap_gl1
Intel(R) Software Guard Extensions Data Center Attestation Primitives
%ldconfig_scriptlets -n libsgx_dcap_gl1
%files -n libsgx_dcap_gl1
%_libdir/libsgx_dcap_gl.so.*
%package -n suse-libsgx-dcap-ql-devel
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) SGX DCAP for Developers
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-dcap-ql-devel
Requires:       %pkg = %primary_pkg_version
Requires:       libsgx_dcap_gl1 = %sgx_dcap_version-%release
%description -n suse-libsgx-dcap-ql-devel
Intel(R) Software Guard Extensions Data Center Attestation Primitives for Developers
%files -n suse-libsgx-dcap-ql-devel
%_includedir/sgx_dcap_ql_wrapper.h
%_libdir/libsgx_dcap_gl.so

%package -n suse-libsgx-pce-logic
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) SGX PCE Logic
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-pce-logic
Conflicts:      libsgx-pce-logic-debuginfo
Requires:       %pkg = %primary_pkg_version
%description -n suse-libsgx-pce-logic
Intel(R) Software Guard Extensions Provisioning Certification Enclave Logic
%ldconfig_scriptlets -n suse-libsgx-pce-logic
%files -n suse-libsgx-pce-logic
%_libdir/libsgx_pce_logic.so
%_libdir/libsgx_pce_logic.so.*

%package -n suse-libsgx-qe3-logic
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) SGX QE3 Logic
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-qe3-logic
Conflicts:      libsgx-qe3-logic-debuginfo
Requires:       %pkg = %primary_pkg_version
Requires:       suse-libsgx-ae-id-enclave
Requires:       suse-libsgx-ae-qe3
%description -n suse-libsgx-qe3-logic
Intel(R) Software Guard Extensions QE3 Logic
%ldconfig_scriptlets -n suse-libsgx-qe3-logic
%files -n suse-libsgx-qe3-logic
%_libdir/libsgx_qe3_logic.so

%dir %_datadir/%pkg
%package -n libmpa_network1
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) SGX Registration Agent Network Library
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-ra-network
Conflicts:      libsgx-ra-network-debuginfo
Requires:       %pkg = %primary_pkg_version
%description -n libmpa_network1
Intel(R) Software Guard Extensions Registration Agent Network Library
%ldconfig_scriptlets -n libmpa_network1
%files -n libmpa_network1
%_libdir/libmpa_network.so.*
%package -n suse-libsgx-ra-network-devel
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) SGX Registration Agent Network Library for Developers
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-ra-network-devel
Requires:       %pkg = %primary_pkg_version
Requires:       libmpa_network1 = %sgx_dcap_version-%release
%description -n suse-libsgx-ra-network-devel
Intel(R) Software Guard Extensions Registration Agent Network Library for Developers
%files -n suse-libsgx-ra-network-devel
%_includedir/MPNetwork.h
%_includedir/MPNetworkDefs.h
%_includedir/mp_network.h
%_libdir/libmpa_network.so

%package -n suse-sgx-ra-service
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) SGX Registration Agent Service
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      sgx-ra-service
Conflicts:      sgx-ra-service-debuginfo
Requires:       %pkg = %primary_pkg_version
%systemd_requires
%systemd_ordering
%description -n suse-sgx-ra-service
Intel(R) Software Guard Extensions Registration Agent Service
%pre -n suse-sgx-ra-service
%service_add_pre mpa_registration_tool.service
%post -n suse-sgx-ra-service
%service_add_post mpa_registration_tool.service
%preun -n suse-sgx-ra-service
%service_del_preun mpa_registration_tool.service
%postun -n suse-sgx-ra-service
%service_del_postun_with_restart mpa_registration_tool.service
%posttrans -n suse-sgx-ra-service
if test -c '/dev/sgx_enclave'
then
	if systemctl --quiet is-enabled mpa_registration_tool.service
	then
		: already enabled
	else
		echo 'run "systemctl enable --now mpa_registration_tool.service" to use this service.'
	fi
fi
%files -n suse-sgx-ra-service
%doc external/dcap_source/tools/SGXPlatformRegistration/installer/common/sgx-ra-service/config/mpa_registration.conf
%_libexecdir/mpa_registration
%_sbindir/mpa_manage
%_unitdir/mpa_registration_tool.service

%package -n libmpa_uefi1
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) SGX Registration Agent UEFI Library
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-ra-uefi
Conflicts:      libsgx-ra-uefi-debuginfo
Requires:       %pkg = %primary_pkg_version
%description -n libmpa_uefi1
Intel(R) Software Guard Extensions Registration Agent UEFI Library
%ldconfig_scriptlets -n libmpa_uefi1
%files -n libmpa_uefi1
%_libdir/libmpa_uefi.so.*
%package -n suse-libsgx-ra-uefi-devel
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) SGX Registration Agent UEFI Library for Developers
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-ra-uefi-devel
Requires:       %pkg = %primary_pkg_version
Requires:       libmpa_uefi1 = %sgx_dcap_version-%release
%description -n suse-libsgx-ra-uefi-devel
Intel(R) Software Guard Extensions Registration Agent UEFI Library for Developers
%files -n suse-libsgx-ra-uefi-devel
%_includedir/MPUefi.h
%_includedir/MultiPackageDefs.h
%_includedir/mp_uefi.h
%_libdir/libmpa_uefi.so

%package -n libsgx_tdx_logic1
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) Trust Domain Extensions QE logic library
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-tdx-logic
Conflicts:      libsgx-tdx-logic-debuginfo
Requires:       %pkg = %primary_pkg_version
Requires:       suse-libsgx-ae-id-enclave
Requires:       suse-libsgx-ae-tdqe
%description -n libsgx_tdx_logic1
Intel(R) Trust Domain Extensions QE logic library
%ldconfig_scriptlets -n libsgx_tdx_logic1
%files -n libsgx_tdx_logic1
%_libdir/libsgx_tdx_logic.so
%_libdir/libsgx_tdx_logic.so.*
%package -n suse-libsgx-tdx-logic-devel
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) Trust Domain Extensions QE logic library For Developers
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-tdx-logic-devel
Requires:       %pkg = %primary_pkg_version
Requires:       libsgx_quote_ex1 = %primary_pkg_version
Requires:       libsgx_tdx_logic1 = %sgx_dcap_version-%release
%description -n suse-libsgx-tdx-logic-devel
Intel(R) Trust Domain Extensions QE logic library For Developers
%files -n suse-libsgx-tdx-logic-devel
%_includedir/td_ql_wrapper.h

%package -n libsgx_dcap_quote_verify1
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) SGX DCAP library
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-dcap-quote-verify
Conflicts:      libsgx-dcap-quote-verify-debuginfo
Requires:       %pkg = %primary_pkg_version
Requires:       suse-tee_appraisal_policy
%description -n libsgx_dcap_quote_verify1
SUSE build of Intel(R) SGX DCAP library
%ldconfig_scriptlets -n libsgx_dcap_quote_verify1
%files -n libsgx_dcap_quote_verify1
%_libdir/libsgx_dcap_quoteverify.so.*
%package -n suse-libsgx-dcap-quote-verify-devel
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) Trust Domain Extensions QE logic library For Developers
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-dcap-quote-verify-devel
Requires:       %pkg = %primary_pkg_version
Requires:       libsgx_dcap_quote_verify1 = %sgx_dcap_version-%release
%description -n suse-libsgx-dcap-quote-verify-devel
Intel(R) Trust Domain Extensions QE logic library For Developers
%files -n suse-libsgx-dcap-quote-verify-devel
%_includedir/sgx_dcap_qal.h
%_includedir/sgx_dcap_quoteverify.h
%_includedir/sgx_qve_header.h
%_libdir/libsgx_dcap_quoteverify.so

%package -n suse-libsgx-dcap-default-qpl
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) SGX Default Quote Provider Library
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Requires:       %pkg = %primary_pkg_version
Requires:       libdcap_quoteprov1 = %sgx_dcap_version-%release
Requires:       libsgx_default_qcnl_wrapper1 = %sgx_dcap_version-%release
%description -n suse-libsgx-dcap-default-qpl
Intel(R) Software Guard Extensions Default Quote Provider Library
%files -n suse-libsgx-dcap-default-qpl
%doc external/dcap_source/QuoteGeneration/qcnl/linux/sgx_default_qcnl.conf
%dir %_datadir/%pkg
%package -n libdcap_quoteprov1
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) SGX Default Quote Provider Library
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-dcap-default-qpl
Conflicts:      libsgx-dcap-default-qpl-debuginfo
Requires:       %pkg = %primary_pkg_version
%description -n libdcap_quoteprov1
Intel(R) Software Guard Extensions Default Quote Provider Library
%ldconfig_scriptlets -n libdcap_quoteprov1
%files -n libdcap_quoteprov1
%_libdir/libdcap_quoteprov.so.*
%package -n libsgx_default_qcnl_wrapper1
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) SGX Default Quote Provider Library
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-dcap-default-qpl
Conflicts:      libsgx-dcap-default-qpl-debuginfo
Requires:       %pkg = %primary_pkg_version
%description -n libsgx_default_qcnl_wrapper1
Intel(R) Software Guard Extensions Default Quote Provider Library
%ldconfig_scriptlets -n libsgx_default_qcnl_wrapper1
%files -n libsgx_default_qcnl_wrapper1
%_libdir/libsgx_default_qcnl_wrapper.so.*
%package -n suse-libsgx-dcap-default-qpl-devel
Version:        %sgx_dcap_version
Summary:        SUSE build of Intel(R) SGX Default Quote Provider Library for Developers
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      libsgx-dcap-default-qpl-devel
Requires:       %pkg = %primary_pkg_version
Requires:       suse-libsgx-dcap-default-qpl = %sgx_dcap_version-%release
%description -n suse-libsgx-dcap-default-qpl-devel
Intel(R) Software Guard Extensions Default Quote Provider Library for Developers
%files -n suse-libsgx-dcap-default-qpl-devel
%_includedir/sgx_default_quote_provider.h
%_libdir/libdcap_quoteprov.so
%_libdir/libsgx_default_qcnl_wrapper.so

%package -n suse-sgx-pck-id-retrieval-tool
Version:        %sgx_dcap_version
Summary:        SUSE build of a tool which collects PCK certs
URL:            https://github.com/intel/SGXDataCenterAttestationPrimitives
Conflicts:      sgx-pck-id-retrieval-tool
Conflicts:      sgx-pck-id-retrieval-tool-debuginfo
Requires:       %pkg = %primary_pkg_version
Requires:       libmpa_uefi1 = %sgx_dcap_version-%release
Requires:       libsgx_urts1 = %primary_pkg_version
Requires:       suse-libsgx-ae-id-enclave
Requires:       suse-libsgx-ae-pce
%description -n suse-sgx-pck-id-retrieval-tool
Intel(R) Software Guard Extensions:this tool is used to collect the platform information to retrieve the PCK certs from PCS(Provisioning Certification Server)
%files -n suse-sgx-pck-id-retrieval-tool
%doc external/dcap_source/tools/PCKRetrievalTool/network_setting.conf
%_sbindir/PCKIDRetrievalTool
# build_flavor == ""
%endif
#
%prep
%setup -q -a 6 -n %pkg-%coco_sgx_version
%patch -P 0 -p1

rm -rf 'sgx-ssl'
mv 'sgx-ssl-%sgx_ssl_hash' "$_"
pushd "$_"
%patch -P 6 -p1
popd

%build
test -x "$(type -p gcc)"    && ASM="$_"
test -x "$(type -p gcc)"    && CC="$_"
test -x "$(type -p g++)"    && CXX="$_"
if test -n '%?suse_sgx_gcc_major'
then
	test -x "$(type -p gcc-%?suse_sgx_gcc_major)" && ASM="$_"
	test -x "$(type -p gcc-%?suse_sgx_gcc_major)" && CC="$_"
	test -x "$(type -p g++-%?suse_sgx_gcc_major)" && CXX="$_"
fi
export ASM="$(readlink -f ${ASM})"
export CC="$(readlink -f ${CC})"
export CXX="$(readlink -f ${CXX})"
#
%if "%build_flavor" == ""
CFLAGS='%optflags -Wno-misleading-indentation'
CXXFLAGS='%optflags -Wno-misleading-indentation'
USi="$PWD/USi"
USi_cmake="${USi}/share/cppmicroservices4/cmake"
tee .env.txt <<_EOF_
__builddir='%__builddir'
USi="${USi}"
_EOF_
(
# This needs to be separated.
# Using ExternalProject_Add lacks the capability
# to include the generated cmake files.
%global o__sourcedir %__sourcedir
%global o__builddir  %__builddir
%global __sourcedir  external/CppMicroServices
%global __builddir   USb
pushd .
%cmake \
	"-DCMAKE_INSTALL_PREFIX:PATH=${USi}" \
	%nil
%cmake_build
popd
%cmake_install DESTDIR=/
%global __sourcedir %o__sourcedir
%global __builddir  %o__builddir
)
%cmake \
	"-DUSi_cmake:PATH=${USi_cmake}" \
	'-DCMAKE_INSTALL_SBINDIR:PATH=sbin' \
	'-DSHARE_INSTALL_PREFIX:PATH=%_datadir' \
	'-DINSTALL_UNITDIR:PATH=%_unitdir' \
	'-DVERSION_LINUX_SGX=%coco_sgx_version' \
	'-DVERSION_SGX_DCAP=%sgx_dcap_version' \
	%nil
%cmake_build
# build_flavor == ""
%endif

%install
. .env.txt
%if "%build_flavor" == ""
%cmake_install
mkdir -p '%buildroot%_datadir/%pkg'
mkdir -p '%buildroot%_tmpfilesdir' '%buildroot%_sysusersdir'
#
suc='system-user-aesmd.conf'
tee "${suc}" <<'_EOC_'
u aesmd - "Architectural Enclave Service Manager" %_localstatedir/lib/aesmd %_sbindir/nologin
_EOC_
%sysusers_generate_pre "${suc}" system-user-aesmd
mv -vt '%buildroot%_sysusersdir' "${suc}"
tee "${suc}" <<'_EOC_'
d %_localstatedir/lib/aesmd 0700 aesmd aesmd - -
d %_rundir/aesmd 0755 aesmd aesmd - -
_EOC_
mv -vt '%buildroot%_tmpfilesdir' "${suc}"
#
suc='system-user-qgsd.conf'
tee "${suc}" <<'_EOC_'
u qgsd - "TD Quoting Generation Service" %_localstatedir/lib/qgsd %_sbindir/nologin
_EOC_
%sysusers_generate_pre "${suc}" system-user-qgsd
mv -vt '%buildroot%_sysusersdir' "${suc}"
tee "${suc}" <<'_EOC_'
d %_localstatedir/lib/qgsd 0700 qgsd qgsd - -
d %_rundir/tdx-qgs 0755 qgsd qgsd - -
_EOC_
mv -vt '%buildroot%_tmpfilesdir' "${suc}"
#
mkdir -p '%buildroot%_libdir'
mv -t '%buildroot%_libdir' "${USi}/lib/libCppMicroServices.so.4.0.0"
# build_flavor == ""
%endif

%changelog
