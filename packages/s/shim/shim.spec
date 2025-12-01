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
Version:        16.1
Release:        0
Summary:        UEFI shim loader
License:        BSD-2-Clause
Group:          System/Boot
URL:            https://github.com/rhboot/shim
Source:         %{name}-%{version}.tar.bz2
# run "extract_signature.sh shim.efi" where shim.efi is the binary
# with the signature from the UEFI signing service.
# Note: For signature requesting, check SIGNATURE_UPDATE.txt
Source1:	shim-install
Source2:	extract_signature.sh
Source3:	attach_signature.sh
Source4:	show_hash.sh
Source5:	show_signatures.sh
Source6:	timestamp.pl
Source7:	strip_signature.sh
Source8:	generate-vendor-dbx.sh
# Certificates Used to Verify the Shim (DER format)
# SUSE CA is also built-in to the shim via VENDOR_CERT_FILE
# openSUSE Secure Boot CA, 2013-2035
Source11:	openSUSE_Secure_Boot_CA_2013.crt
# SUSE Linux Enterprise Secure Boot CA, 2013-2035
Source12:	SUSE_Linux_Enterprise_Secure_Boot_CA_2013.crt
# Microsoft Corporation UEFI CA 2011, 2011-2026
Source13:	Microsoft_Corporation_UEFI_CA_2011.crt
# Microsoft UEFI CA 2023, 2023-2038
Source14:	Microsoft_UEFI_CA_2023.crt
# Microsoft-signed shim
Source30:	shim-opensuse.x86.efi
Source31:	shim-opensuse.aarch64.efi
Source32:	shim-sles.x86.efi
Source33:	shim-sles.aarch64.efi
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
BuildRequires:  gcc%{gcc_version}
BuildRequires:  dos2unix
BuildRequires:  efitools
BuildRequires:  mozilla-nss-tools
BuildRequires:  openssl >= 0.9.8
BuildRequires:  pesign
BuildRequires:  pesign-obs-integration
# we need xxd in global macro in shim.spec
BuildRequires:  vim
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

# subject hash of openSUSE/SLE/devel certificates for identifying devel project
%global prjissuer_hash %(test -f %{_sourcedir}/_projectcert.crt && openssl x509 -in %{_sourcedir}/_projectcert.crt -inform PEM -noout -issuer_hash 2>/dev/null || echo "PRJ_ISSUER_NOT_FOUND")
%global prjsubjec_hash %(test -f %{_sourcedir}/_projectcert.crt && openssl x509 -in %{_sourcedir}/_projectcert.crt -inform PEM -noout -subject_hash 2>/dev/null || echo "PRJ_SUBJECT_NOT_FOUND")
%global opensusesubject_hash %(openssl x509 -in %{SOURCE11} -inform DER -noout -subject_hash 2>/dev/null)
%global slessubject_hash %(openssl x509 -in %{SOURCE12} -inform DER -noout -subject_hash 2>/dev/null)
# Hex content of certs (DER format) will be used in the TARGET_CERT_HEXES array in pretrans script
%global opensuse_ca_hex %(xxd -p %{SOURCE11} | tr -d '\\n')
%global sles_ca_hex %(xxd -p %{SOURCE12} | tr -d '\\n')
%global microsoft_ca_hex %(xxd -p %{SOURCE13} | tr -d '\\n')
%global microsoft_ca_2023_hex %(xxd -p %{SOURCE14} | tr -d '\\n')
%global prjcert_hex %(test -f %{_sourcedir}/_projectcert.crt && (openssl x509 -in %{_sourcedir}/_projectcert.crt -outform DER -out - | xxd -p | tr -d '\\n') 2>/dev/null)

%description
shim is a trivial EFI application that, when run, attempts to open and
execute another application.

%if 0%{?shim_nx:1}
%package -n shim-nx
Summary:        UEFI shim loader - supports non-executable
Group:          System/Boot
Requires:	shim = %{version}

%description -n shim-nx
shim with NX_COMPAT field (aka. NxCompatible field in DllCharacteristics)
for supporting non-executable
%endif	# 0%{?shim_nx:1}

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
    prjsubject=$(openssl x509 -in %{_sourcedir}/_projectcert.crt -inform PEM -noout -subject_hash)
    prjissuer=$(openssl x509 -in %{_sourcedir}/_projectcert.crt -inform PEM -noout -issuer_hash)
    opensusesubject=$(openssl x509 -in %{SOURCE11} -inform DER -noout -subject_hash)
    slessubject=$(openssl x509 -in %{SOURCE12} -inform DER -noout -subject_hash)
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
	cert=%{SOURCE11}
	cp $cert shim-$suffix.der
	verify='openSUSE Secure Boot CA1'
	vendor_dbx='vendor-dbx-opensuse.esl'
%ifarch x86_64
	ms_shim=%{SOURCE30}
%else
	# opensuse aarch64
	ms_shim=%{SOURCE31}
%endif
    elif test "$suffix" = "sles"; then
	cert=%{SOURCE12}
	cp $cert shim-$suffix.der
	verify='SUSE Linux Enterprise Secure Boot CA1'
	vendor_dbx='vendor-dbx-sles.esl'
%ifarch x86_64
	ms_shim=%{SOURCE32}
%else
	# sles aarch64
	ms_shim=%{SOURCE33}
%endif
    elif test "$suffix" = "devel"; then
	cert=%{_sourcedir}/_projectcert.crt
	verify=`openssl x509 -in "$cert" -noout -email`
	vendor_dbx='vendor-dbx.esl'
	ms_shim=''
	test -e "$cert" || continue
	openssl x509 -in $cert -inform PEM -outform DER -out shim-$suffix.der
    else
	echo "invalid suffix"
	false
    fi

    make CC=%{cc_compiler} RELEASE=0 ENABLE_CODESIGN_EKU=1 SHIMSTEM=shim \
         VENDOR_CERT_FILE=shim-$suffix.der ENABLE_HTTPBOOT=1 \
         DEFAULT_LOADER="\\\\\\\\grub.efi" \
         VENDOR_DBX_FILE=$vendor_dbx \
         shim.efi.debug shim.efi
    #
    # assert correct certificate embedded
    grep -q "$verify" shim.efi
    # Use ms-signed shim when the version equals with the version of newly built shim
    # Version mismatch indicates development of a new shim.
    if test -n "$ms_shim"; then
	ms_version=$(strings "$ms_shim" | grep '$Version:' | sed -e 's/^.*: //' -e 's/ \$//')
	dev_version=$(strings shim.efi | grep '$Version:' | sed -e 's/^.*: //' -e 's/ \$//')
	if [ "$ms_version" = "$dev_version" ]; then
		cp $ms_shim shim-$suffix.efi
	else
		cp shim.efi shim-$suffix.efi
	fi
	rm shim.efi
    else
	# devel shim
	mv shim.efi shim-$suffix.efi
    fi
    # FIX: using debug info from devel shim doesn't match with ms-signed shim
    mv shim.efi.debug shim-$suffix.debug
    # remove the build cert if exists
    rm -f shim_cert.h shim.cer shim.crt
    # make sure all object files gets rebuilt
    rm -f *.o

%if 0%{?shim_nx:1}
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
    mv shim.nx.efi shim-$suffix.nx.efi
    mv shim.nx.efi.debug shim-$suffix.nx.debug
    # remove the build cert if exists
    rm -f shim_cert.h shim.cer shim.crt
    # make sure all object files gets rebuilt
    rm -f *.o
%endif  # 0%{?shim_nx:1}
done

ln -s shim-${suffixes[0]}.efi shim.efi
mv shim-${suffixes[0]}.debug shim.debug
%if 0%{?shim_nx:1}
ln -s shim-${suffixes[0]}.nx.efi shim.nx.efi
mv shim-${suffixes[0]}.nx.debug shim.nx.debug
%endif  # 0%{?shim_nx:1}

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
install -m 755 %{SOURCE1} %{buildroot}/%{_sbindir}/
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

%pretrans -p <lua>
-- Using Lua
print("INFO: Current Lua Version: " .. tostring(_VERSION))

-- ==========================================================================================
-- This pretrans script verifies that the UEFI db should have the necessary certificate to
-- allow the shim binary to boot.
-- The installation will be aborted if the db is missing the target certificate. To proceed,
-- the user must enroll the target certificate in the db or disable UEFI Secure Boot.
-- ==========================================================================================

local db_filename = "/sys/firmware/efi/efivars/db-d719b2cb-3d3a-4596-a3bc-dad00e67656f"

-- The db file existence check
local f_check, err_check = io.open(db_filename, "rb")

if not f_check then
    print("WARNING: Attempt to open db EFI variable file failed. Error message: " .. tostring(err_check))
    print("WARNING: This usually means the system is not booted in UEFI mode. Skipping all db check steps.")
    return 0
end
f_check:close()

-- ==========================================================================================
-- This is the hardcoded target certificate content used to check for its existence.
-- HEX_CONTENT=$(xxd -p taget_certificate.der | tr -d '\n') && echo "$HEX_CONTENT"
-- ==========================================================================================

-- Only the DER format is supported
local TARGET_CERT_HEXES = {
    -- Always check Microsoft keys
    -- Certificate #1, Microsoft Corporation UEFI CA 2011
    "%{microsoft_ca_hex}",
    -- Certificate #2, Microsoft UEFI CA 2023
    "%{microsoft_ca_2023_hex}",
%if "%{prjissuer_hash}" == "%{opensusesubject_hash}"
    -- Certificate #3, openSUSE Secure Boot CA 2013
    "%{opensuse_ca_hex}",
%endif
%if "%{prjissuer_hash}" == "%{slessubject_hash}"
    -- Certificate #3, SUSE Linux Enterprise Secure Boot CA 2013
    "%{sles_ca_hex}",
%endif
%if "%{prjissuer_hash}" == "%{prjsubjec_hash}"
    -- We put all keys for testing on devel/staging project
    -- Certificate #3, openSUSE Secure Boot CA 2013
    "%{opensuse_ca_hex}",
    -- Certificate #4, SUSE Linux Enterprise Secure Boot CA 2013
    "%{sles_ca_hex}",
    -- Certificate #5, _projectcert.crt
    "%{prjcert_hex}",
%endif  # prjissuer_hash check
}

-- Check if the TARGET_CERT_HEXES array is empty
if #TARGET_CERT_HEXES == 0 then
    print("INFO: certificate list is empty. Skipping certificate check.")
    -- Exiting safely as the certificate list is empty.
    return 0
else
    -- Check if the Hex string for certificate is valid
    for i, cert_hex in ipairs(TARGET_CERT_HEXES) do
        if #cert_hex % 2 ~= 0 then
            print("Error: The length of hard-coded hex string for certificate #" .. i .. " must be an even number.")
            error("The Hex string is invalid. The transaction is being aborted in the pretrans script.")
        end
    end
end

-- =========================================================================
-- Helper functions
-- =========================================================================

-- Convert hexadecimal string to original binary string
local function hex_to_binary(hex)
    local binary = ""
    for i = 1, #hex, 2 do
        local byte_hex = hex:sub(i, i + 1)
        binary = binary .. string.char(tonumber(byte_hex, 16))
    end
    return binary
end

-- =========================================================================
-- Main logic for checking if the db has any target certificate
-- =========================================================================

-- Read existing db contents
local db_content = ""
do
    -- The db file is now confirmed to exist, open it again to read the contents
    local f_db, err_db = io.open(db_filename, "rb")

    if f_db then
        local chunks = {}
        local CHUNK_SIZE = 4096
        local raw_content = ""
        local chunk = f_db:read(CHUNK_SIZE)

        while chunk do
	    -- If an empty string is read, it means EOF has been reached and the loop is exited.
            if chunk == "" then
                break
            end
            table.insert(chunks, chunk)
            chunk = f_db:read(CHUNK_SIZE)
        end

        raw_content = table.concat(chunks)

        f_db:close()

	-- Skip the first 4 bytes (EFI attributes)
        if #raw_content > 4 then
	    -- Truncate from the 5th byte to the end
            db_content = string.sub(raw_content, 5)
	    print("INFO: Successfully read existing db content")
        else
	    -- The file is too small or only has attributes, so it is considered blank.
            db_content = ""
            print("WARNING: db file content length is abnormal (<= 4 bytes). Treated as blank.")
        end
    end
end

-- Check all target certificates
for i, cert_hex in ipairs(TARGET_CERT_HEXES) do

    local target_binary_content = hex_to_binary(cert_hex)

    -- Perform binary string matching
    local start_pos, end_pos = db_content:find(target_binary_content, 1, true)

    if start_pos then
        -- Success: Certificate exist in db
        -- Return 0 to allow the RPM transaction to continue
        print("Target certificate #" .. i .. " was found in the db variable. Proceed with install.")
        return 0
    end
end

-- Certificate not present in db
print("WARNING: The target certificate binary was not found in the db variable.")
print("Please add the appropriate certificate to the db or disable UEFI secure boot.")

-- Secure Boot status check: We only proceed with installation if the certificate is not present in the db and Secure Boot is disabled.
local sb_filename = "/sys/firmware/efi/efivars/SecureBoot-8be4df61-93ca-11d2-aa0d-00e098032b8c"

local f_sb, err_sb = io.open(sb_filename, "rb")

if not f_sb then
    -- If the file is missing, it typically means the system is not UEFI, or Secure Boot is disabled/the variable is absent.
    print("WARNING: SecureBoot EFI variable file does not exist. Proceed with install.")
else
    local raw_content_sb = ""
    local sb_status = 0

    -- Read file contents
    local chunk_sb = f_sb:read(4096)
    while chunk_sb do
        if chunk_sb == "" then break end
        raw_content_sb = raw_content_sb .. chunk_sb
        chunk_sb = f_sb:read(4096)
    end
    f_sb:close()

    -- SecureBoot status check
    if #raw_content_sb >= 5 then
	-- Skip the first 4-byte attribute header and read the 5th byte (status byte)
        sb_status = string.byte(raw_content_sb, 5)

        if sb_status == 0x00 then
            print("INFO: Since Secure Boot is DISABLED, proceed with install.")
            return 0
        elseif sb_status == 0x01 then
	    error("Fatal error: Secure Boot is ENABLED (status = 0x01), but the target certificate was not found in the db. Aborting installation.")
        else
            error("Fatal error: Secure Boot status is unrecognized (0x" .. string.format("%02x", sb_status) .. "). Aborting installation.")
        end
    else
	error("Fatal error: SecureBoot variable content is too short to determine status. Aborting installation.")
    end
end

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
%if 0%{?shim_nx:1}
%exclude %{sysefidir}/shim-*.nx.efi
%endif  # 0%{?shim_nx:1}
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

%if 0%{?shim_nx:1}
%files -n shim-nx
%defattr(-,root,root)
%{sysefidir}/shim.nx.efi
%{sysefidir}/shim-*.nx.efi 
%endif  # 0%{?shim_nx:1}

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
