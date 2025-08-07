#
# spec file for package shim
#
# Copyright (c) 2021 SUSE LLC
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
# needssslcertforbuild


%undefine _debuginfo_subpackages
%undefine _build_create_debug
%undefine _enable_debug_packages
%ifarch aarch64
%define grubplatform arm64-efi
%else
%define grubplatform %{_target_cpu}-efi
%endif
%if %{defined sle_version} && 0%{?sle_version} <= 150000
%define sysefidir      /usr/lib64/efi
%else
%define sysefibasedir  %{_datadir}/efi
%define sysefidir      %{sysefibasedir}/%{_target_cpu}
%if "%{grubplatform}" == "x86_64-efi" && 0%{?suse_version} < 1600
# provide compatibility sym-link for residual kiwi, etc.
%define shim_lib64_share_compat 1
%endif
%endif
# Set gcc version, the minimum version is gcc-13
%if %gcc_version < 13
%define gcc_version 13
%endif
%global cc_compiler /usr/bin/gcc-%{gcc_version}

%if 0%{?suse_version} >= 1600
%define shim_use_fde_tpm_helper 1
%endif

Name:           shim
Version:        16.0
Release:        0
Summary:        UEFI shim loader
License:        BSD-2-Clause
Group:          System/Boot
URL:            https://github.com/rhboot/shim
Source:         %{name}-%{version}.tar.bz2
# run "extract_signature.sh shim.efi" where shim.efi is the binary
# with the signature from the UEFI signing service.
# Note: For signature requesting, check SIGNATURE_UPDATE.txt
Source1:        signature-opensuse.x86_64.asc
# openSUSE Secure Boot CA, 2013-2035, PEM format
Source2:        openSUSE-UEFI-CA-Certificate.crt
Source3:        shim-install
# SUSE Linux Enterprise Secure Boot CA, 2013-2035, PEM format
Source4:        SLES-UEFI-CA-Certificate.crt
Source5:        extract_signature.sh
Source6:        attach_signature.sh
Source7:        show_hash.sh
Source8:        show_signatures.sh
Source9:        timestamp.pl
Source10:       strip_signature.sh
Source11:       signature-sles.x86_64.asc
Source12:       signature-opensuse.aarch64.asc
Source13:       signature-sles.aarch64.asc
Source14:       generate-vendor-dbx.sh
# signatures for shim.nx
Source20:       signature-opensuse-nx.x86_64.asc
Source21:       signature-sles-nx.x86_64.asc
Source22:       signature-opensuse-nx.aarch64.asc
Source23:       signature-sles-nx.aarch64.asc
# revoked certificates for dbx
Source50:       revoked-openSUSE-UEFI-SIGN-Certificate-2013-01.crt
Source51:       revoked-openSUSE-UEFI-SIGN-Certificate-2013-08.crt
Source52:       revoked-openSUSE-UEFI-SIGN-Certificate-2020-01.crt
Source53:       revoked-openSUSE-UEFI-SIGN-Certificate-2020-07.crt
Source54:       revoked-openSUSE-UEFI-SIGN-Certificate-2021-05.crt
Source55:       revoked-openSUSE-UEFI-SIGN-Certificate-2022-06.crt
Source56:       revoked-SLES-UEFI-SIGN-Certificate-2013-01.crt
Source57:       revoked-SLES-UEFI-SIGN-Certificate-2013-04.crt
Source58:       revoked-SLES-UEFI-SIGN-Certificate-2016-02.crt
Source59:       revoked-SLES-UEFI-SIGN-Certificate-2020-07.crt
Source60:       revoked-SLES-UEFI-SIGN-Certificate-2021-05.crt
Source61:       revoked-SLES-UEFI-SIGN-Certificate-2022-05.crt
###
Source99:       SIGNATURE_UPDATE.txt
# PATCH-FIX-SUSE shim-arch-independent-names.patch glin@suse.com -- Use the Arch-independent names
Patch1:         shim-arch-independent-names.patch
# PATCH-FIX-OPENSUSE shim-change-debug-file-path.patch glin@suse.com -- Change the default debug file path
Patch2:         shim-change-debug-file-path.patch
# PATCH-FIX-SUSE remove_build_id.patch -- Remove the build ID to make the binary reproducible when building with AArch64 container
Patch3:         remove_build_id.patch
# PATCH-FIX-SUSE shim-disable-export-vendor-dbx.patch bsc#1185261 glin@suse.com -- Disable exporting vendor-dbx to MokListXRT
Patch4:         shim-disable-export-vendor-dbx.patch
# PATCH-FIX-UPSTREAM shim-alloc-one-more-byte-for-sprintf.patch dennis.tseng@suse.com
Patch5:         shim-alloc-one-more-byte-for-sprintf.patch
# PATCH-FIX-UPSTREAM shim: change automatically enable MOK_POLICY_REQUIRE_NX (PR #761)(bsc#1205588) - jlee@suse.com
Patch6:         shim-change-automatically-enable-MOK_POLICY_REQUIRE_NX.patch
BuildRequires:  gcc%{gcc_version}
BuildRequires:  dos2unix
BuildRequires:  efitools
BuildRequires:  mozilla-nss-tools
BuildRequires:  openssl >= 0.9.8
BuildRequires:  pesign
BuildRequires:  pesign-obs-integration
%if 0%{?shim_use_fde_tpm_helper:1}
BuildRequires:  fde-tpm-helper-rpm-macros
%endif
%if 0%{?suse_version} > 1320
BuildRequires:  update-bootloader-rpm-macros
%endif
%if 0%{?update_bootloader_requires:1}
%update_bootloader_requires
%else
Requires:       perl-Bootloader
%endif
%if 0%{?fde_tpm_update_requires:1}
%fde_tpm_update_requires
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# For shim-install script grub is needed but we also want to use
# shim for systemd-boot where shim-install is not actually used.
# Requires:       grub2-%{grubplatform}
Requires:       mokutil
ExclusiveArch:  x86_64 aarch64

%description
shim is a trivial EFI application that, when run, attempts to open and
execute another application.

%package -n shim-nx
Summary:        UEFI shim loader - supports non-executable
Group:          System/Boot
Requires:	shim = %{version}

%description -n shim-nx
shim with NX_COMPAT field (aka. NxCompatible field in DllCharacteristics)
for supporting non-executable

%package -n shim-debuginfo
Summary:        UEFI shim loader - debug symbols
Group:          Development/Debug

%description -n shim-debuginfo
The debug symbols of UEFI shim loader

%package -n shim-debugsource
Summary:        UEFI shim loader - debug source
Group:          Development/Debug

%description -n shim-debugsource
The source code of UEFI shim loader

%prep
%autosetup -p1

%build
# generate the vendor SBAT metadata
%if 0%{?is_opensuse} == 1 || 0%{?sle_version} == 0
distro_id="opensuse"
distro_name="The openSUSE project"
%else
distro_id="sle"
distro_name="SUSE Linux Enterprise"
%endif
distro_sbat=1
sbat="shim.${distro_id},${distro_sbat},${distro_name},%{name},%{version},mail:security@suse.de"
echo "${sbat}" > data/sbat.vendor.csv

# generate dbx files based on revoked certs
bash %{_sourcedir}/generate-vendor-dbx.sh %{_sourcedir}/revoked-*.crt
ls -al *.esl

# first, build MokManager and fallback as they don't depend on a
# specific certificate
make CC=%{cc_compiler} RELEASE=0 \
     MMSTEM=MokManager FBSTEM=fallback \
     POST_PROCESS_PE_FLAGS=-n \
     MokManager.efi.debug fallback.efi.debug \
     MokManager.efi fallback.efi
# make sure all object files gets rebuilt
rm -f *.o

# now build variants of shim that embed different certificates
default=''
suffixes=(opensuse sles)
# check whether the project cert is a known one. If it is we build
# just one shim that embeds this specific cert. If it's a devel
# project we build all variants to simplify testing.
if test -e %{_sourcedir}/_projectcert.crt ; then
    prjsubject=$(openssl x509 -in %{_sourcedir}/_projectcert.crt -noout -subject_hash)
    prjissuer=$(openssl x509 -in %{_sourcedir}/_projectcert.crt -noout -issuer_hash)
    opensusesubject=$(openssl x509 -in %{SOURCE2} -noout -subject_hash)
    slessubject=$(openssl x509 -in %{SOURCE4} -noout -subject_hash)
    if test "$prjissuer" = "$opensusesubject" ; then
	suffixes=(opensuse)
    elif test "$prjissuer" = "$slessubject" ; then
	suffixes=(sles)
    elif test "$prjsubject" = "$prjissuer" ; then
	suffixes=(devel opensuse sles)
    fi
fi

for suffix in "${suffixes[@]}"; do
    if test "$suffix" = "opensuse"; then
	cert=%{SOURCE2}
	verify='openSUSE Secure Boot CA1'
	vendor_dbx='vendor-dbx-opensuse.esl'
%ifarch x86_64
	signature=%{SOURCE1}
	signature_nx=%{SOURCE20}
%else
	# AArch64 signature
	# Disable AArch64 signature attachment temporarily
	# until we get a real one.
        # Now, we got a real one. So enable it again.
	signature=%{SOURCE12}
	signature_nx=%{SOURCE22}
%endif
    elif test "$suffix" = "sles"; then
	cert=%{SOURCE4}
	verify='SUSE Linux Enterprise Secure Boot CA1'
	vendor_dbx='vendor-dbx-opensuse.esl'
%ifarch x86_64
	signature=%{SOURCE11}
	signature_nx=%{SOURCE21}
%else
	# AArch64 signature
	signature=%{SOURCE13}
	signature_nx=%{SOURCE23}
%endif
    elif test "$suffix" = "devel"; then
	cert=%{_sourcedir}/_projectcert.crt
	verify=`openssl x509 -in "$cert" -noout -email`
	vendor_dbx='vendor-dbx.esl'
	signature=''
	signature_nx=''
	test -e "$cert" || continue
    else
	echo "invalid suffix"
	false
    fi

    openssl x509 -in $cert -outform DER -out shim-$suffix.der
    make CC=%{cc_compiler} RELEASE=0 ENABLE_CODESIGN_EKU=1 SHIMSTEM=shim \
         VENDOR_CERT_FILE=shim-$suffix.der ENABLE_HTTPBOOT=1 \
         DEFAULT_LOADER="\\\\\\\\grub.efi" \
         VENDOR_DBX_FILE=$vendor_dbx \
         shim.efi.debug shim.efi
    #
    # assert correct certificate embedded
    grep -q "$verify" shim.efi
    # make VENDOR_CERT_FILE=cert.der VENDOR_DBX_FILE=dbx
    chmod 755 %{SOURCE9}
    # alternative: verify signature
    #sbverify --cert MicCorThiParMarRoo_2010-10-05.pem shim-signed.efi
    if test -n "$signature"; then
	head -1 "$signature" > hash1
	cp shim.efi shim.efi.bak
	# pe header contains timestamp and checksum. we need to
	# restore that
	%{SOURCE9} --set-from-file "$signature" shim.efi
	pesign -h -P -i shim.efi > hash2
	cat hash1 hash2
	if ! cmp -s hash1 hash2; then
		echo "ERROR: $suffix binary changed, need to request new signature!"
%if %{defined shim_enforce_ms_signature} && 0%{?shim_enforce_ms_signature} > 0
		# compare suffix (sles, opensuse) with distro_id (sle, opensuse)
		# when hash mismatch and distro_id match with suffix, stop building 
		if test "$suffix" = "$distro_id" || test "$suffix" = "${distro_id}s"; then
			false
		fi
%endif
		mv shim.efi.bak shim-$suffix.efi
		rm shim.efi
	else
		# attach signature
		pesign -m "$signature" -i shim.efi -o shim-$suffix.efi
		rm -f shim.efi
	fi
    else
        mv shim.efi shim-$suffix.efi
    fi
    mv shim.efi.debug shim-$suffix.debug
    # remove the build cert if exists
    rm -f shim_cert.h shim.cer shim.crt
    # make sure all object files gets rebuilt
    rm -f *.o

    # building shim.nx.efi
    make CC=%{cc_compiler} RELEASE=0 ENABLE_CODESIGN_EKU=1 SHIMSTEM=shim.nx \
         VENDOR_CERT_FILE=shim-$suffix.der ENABLE_HTTPBOOT=1 \
         DEFAULT_LOADER="\\\\\\\\grub.efi" \
         VENDOR_DBX_FILE=$vendor_dbx \
	 POST_PROCESS_PE_FLAGS=-n \
         shim.nx.efi.debug shim.nx.efi
    #
    # assert correct certificate embedded
    grep -q "$verify" shim.nx.efi
    # make VENDOR_CERT_FILE=cert.der VENDOR_DBX_FILE=dbx
    chmod 755 %{SOURCE9}
    # alternative: verify signature
    #sbverify --cert MicCorThiParMarRoo_2010-10-05.pem shim-signed.efi
    if test -n "$signature_nx"; then
	head -1 "$signature_nx" > hash1
	cp shim.nx.efi shim.nx.efi.bak
	# pe header contains timestamp and checksum. we need to
	# restore that
	%{SOURCE9} --set-from-file "$signature_nx" shim.nx.efi
	pesign -h -P -i shim.nx.efi > hash2
	cat hash1 hash2
	if ! cmp -s hash1 hash2; then
		echo "ERROR: $suffix nx binary changed, need to request new signature!"
%if %{defined shim_enforce_ms_signature} && 0%{?shim_enforce_ms_signature} > 0
		# compare suffix (sles, opensuse) with distro_id (sle, opensuse)
		# when hash mismatch and distro_id match with suffix, stop building 
		if test "$suffix" = "$distro_id" || test "$suffix" = "${distro_id}s"; then
			false
		fi
%endif
		mv shim.nx.efi.bak shim-$suffix.nx.efi
		rm shim.nx.efi
	else
		# attach signature
		pesign -m "$signature" -i shim.nx.efi -o shim-$suffix.nx.efi
		rm -f shim.nx.efi
	fi
    else
        mv shim.nx.efi shim-$suffix.nx.efi
    fi
    mv shim.nx.efi.debug shim-$suffix.nx.debug
    # remove the build cert if exists
    rm -f shim_cert.h shim.cer shim.crt
    # make sure all object files gets rebuilt
    rm -f *.o
done

ln -s shim-${suffixes[0]}.efi shim.efi
mv shim-${suffixes[0]}.debug shim.debug
ln -s shim-${suffixes[0]}.nx.efi shim.nx.efi
mv shim-${suffixes[0]}.nx.debug shim.nx.debug

# Collect the source for debugsource
mkdir ../source
find . \( -name "*.c" -o -name "*.h" \) -type f -exec cp --parents -a {} ../source/ \;
mv ../source .

%install
export BRP_PESIGN_FILES='%{sysefidir}/shim*.efi %{sysefidir}/MokManager.efi %{sysefidir}/fallback.efi'
install -d %{buildroot}/%{sysefidir}
cp -a shim*.efi %{buildroot}/%{sysefidir}
install -m 444 shim-*.der %{buildroot}/%{sysefidir}
install -m 644 MokManager.efi %{buildroot}/%{sysefidir}/MokManager.efi
install -m 644 fallback.efi %{buildroot}/%{sysefidir}/fallback.efi
install -d %{buildroot}/%{_sbindir}
install -m 755 %{SOURCE3} %{buildroot}/%{_sbindir}/
# install SUSE certificate
install -d %{buildroot}/%{_sysconfdir}/uefi/certs/
for file in shim-*.der; do
    filename=$(echo "$file" | cut -f 1 -d '.')
    fpr=$(openssl x509 -sha1 -fingerprint -inform DER -noout -in $file | cut -c 18- | cut -d ":" -f 1,2,3,4 | sed 's/://g')
    install -m 644 $file %{buildroot}/%{_sysconfdir}/uefi/certs/${fpr}-${filename}.crt
done
%if %{defined shim_lib64_share_compat}
    [ "%{sysefidir}" != "/usr/lib64/efi" ] || exit 1
    # provide compatibility sym-link for residual "consumers"
    install -d %{buildroot}/usr/lib64/efi
    ln -srf %{buildroot}/%{sysefidir}/*.efi %{buildroot}/usr/lib64/efi/
%endif

# install the debug symbols
install -d %{buildroot}/usr/lib/debug/%{sysefidir}
install -m 644 shim.debug %{buildroot}/usr/lib/debug/%{sysefidir}
install -m 644 MokManager.efi.debug %{buildroot}/usr/lib/debug/%{sysefidir}/MokManager.debug
install -m 644 fallback.efi.debug %{buildroot}/usr/lib/debug/%{sysefidir}/fallback.debug

# install the debug source
install -d %{buildroot}/usr/src/debug/%{name}-%{version}
cp -r source/* %{buildroot}/usr/src/debug/%{name}-%{version}

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%post
%if 0%{?fde_tpm_update_post:1}
%fde_tpm_update_post shim
%endif

%if 0%{?update_bootloader_check_type_reinit_post:1}
%update_bootloader_check_type_reinit_post grub2-efi
%else
/sbin/update-bootloader --reinit || true
%endif

# copy from kernel-scriptlets/cert-script
is_efi () {
    local msg rc=0
# The below statement fails if mokutil isn't installed or UEFI is unsupported.
# It doesn't fail if UEFI is available but secure boot is off.
    msg="$(mokutil --sb-state 2>&1)" || rc=$?
    return $rc
}
# run mokutil for setting sbat policy to latest mode
EFIVARFS=/sys/firmware/efi/efivars
SBAT_POLICY="$EFIVARFS/SbatPolicy-605dab50-e046-4300-abb6-3dd810dd8b23"
if is_efi; then
        if [ -w $EFIVARFS ] && \
           [ ! -f "$SBAT_POLICY" ] && \
           mokutil -h | grep -q "set-sbat-policy"; \
        then
        # Only apply CA check on the kernel package certs (bsc#1173115)
                mokutil --set-sbat-policy latest
        fi
fi

%if %{defined update_bootloader_posttrans}
%posttrans
%{?update_bootloader_posttrans}
%{?fde_tpm_update_posttrans}
%endif

%files
%defattr(-,root,root)
%doc COPYRIGHT
%dir %{?sysefibasedir}
%dir %{sysefidir}
%{sysefidir}/shim.efi
%{sysefidir}/shim-*.efi
%exclude %{sysefidir}/shim-*.nx.efi
%{sysefidir}/shim-*.der
%{sysefidir}/MokManager.efi
%{sysefidir}/fallback.efi
%{_sbindir}/shim-install
%dir %{_sysconfdir}/uefi/
%dir %{_sysconfdir}/uefi/certs/
%{_sysconfdir}/uefi/certs/*.crt
%if %{defined shim_lib64_share_compat}
# provide compatibility sym-link for previous kiwi, etc.
%dir /usr/lib64/efi
/usr/lib64/efi/*.efi
%endif

%files -n shim-nx
%defattr(-,root,root)
%{sysefidir}/shim.nx.efi
%{sysefidir}/shim-*.nx.efi 

%files -n shim-debuginfo
%defattr(-,root,root,-)
/usr/lib/debug%{sysefidir}/shim.debug
/usr/lib/debug%{sysefidir}/MokManager.debug
/usr/lib/debug%{sysefidir}/fallback.debug

%files -n shim-debugsource
%defattr(-,root,root,-)
%dir /usr/src/debug/%{name}-%{version}
/usr/src/debug/%{name}-%{version}/*

%changelog
