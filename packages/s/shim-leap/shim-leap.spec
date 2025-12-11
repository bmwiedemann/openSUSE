#
# spec file for package shim-leap
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


# Move 'efi'-executables to '/usr/share/efi' (FATE#326960, bsc#1166523)
%define sysefibasedir  %{_datadir}/efi
%define sysefidir      %{sysefibasedir}/%{_target_cpu}
%if 0%{?suse_version} < 1600
# provide compatibility sym-link for residual kiwi, etc.
%define shim_lib64_share_compat 1
%endif

Name:           shim-leap
Version:        16.1
Release:        0
Summary:        UEFI shim loader
License:        BSD-2-Clause
Group:          System/Boot
Source0:        shim-16.1-lp156.4.1.x86_64.rpm
Source1:        shim-16.1-lp156.4.1.aarch64.rpm
Source2:        README
Source3:        shim-install
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
BuildRequires:  fde-tpm-helper-rpm-macros
BuildRequires:  update-bootloader-rpm-macros
BuildRequires:  openssl >= 0.9.8
# we need xxd in global macro in shim.spec
BuildRequires:  vim
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
does not exist

%package -n shim
Summary:        UEFI shim loader
Group:          System/Boot
Requires:       perl-Bootloader
%if 0%{?fde_tpm_update_requires:1}
%fde_tpm_update_requires
%endif

%description -n shim
shim is a trivial EFI application that, when run, attempts to open and
execute another application.

%prep
%ifarch         x86_64
shim_rpm=%{SOURCE0}
%else
shim_rpm=%{SOURCE1}
%endif
rpm2cpio $shim_rpm | cpio --extract --unconditional --preserve-modification-time --make-directories

%build

%install
# purely repackaged
cp -a etc usr %{buildroot}
cp %{S:2} .

# Override shim-install
install -m 755 %{S:3} %{buildroot}/%{_sbindir}/shim-install

%if %{undefined shim_lib64_share_compat}
# Remove the sym-links in /usr/lib64/efi
rm -rf %{buildroot}/usr/lib64/efi
%endif

# This pretrans Lua script is directly copied from shim.spec
# Please remember to sync this script if it be modified
%pretrans -n shim -p <lua>
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
    -- Certificate #3, openSUSE Secure Boot CA 2013
    "%{opensuse_ca_hex}",
%if "%{prjissuer_hash}" == "%{slessubject_hash}"
    -- Certificate #4, SUSE Linux Enterprise Secure Boot CA 2013
    "%{sles_ca_hex}",
%endif
%if "%{prjissuer_hash}" == "%{prjsubjec_hash}"
    -- We put all keys for testing on devel/staging project
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

%post -n shim
%if 0%{?fde_tpm_update_post:1}
%fde_tpm_update_post shim
%endif

%if 0%{?update_bootloader_check_type_reinit_post:1}
%update_bootloader_check_type_reinit_post grub2-efi
%else
/sbin/update-bootloader --reinit || true
%endif

%posttrans -n shim
%{?update_bootloader_posttrans}
%{?fde_tpm_update_posttrans}

%files -n shim
%doc README
%dir %{?sysefibasedir}
%dir %{sysefidir}
%{sysefidir}/shim.efi
%{sysefidir}/shim-*.efi
%{sysefidir}/shim-*.der
%{sysefidir}/MokManager.efi
%{sysefidir}/fallback.efi
%if %{defined shim_lib64_share_compat}
# provide compatibility sym-link for previous kiwi, etc.
%dir /usr/lib64/efi
/usr/lib64/efi/*.efi
%endif
/etc/uefi
%{_sbindir}/shim-install
/usr/share/doc/packages/shim

%changelog
