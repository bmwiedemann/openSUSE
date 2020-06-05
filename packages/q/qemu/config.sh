#!/bin/bash

# config.sh:

# The next few VARIABLES are to be edited as required:

# The following specifies the upstream tag or commit upon which our patchqueue
# gets rebased. The special value LATEST may be used to "automatically" track
# the upstream development tree in the master branch
GIT_UPSTREAM_COMMIT_ISH=v5.0.0
# WARNING: If transitioning from using LATEST to not, MANUALLY re-set the
# tarball present. If transitioning TO LATEST, make sure that
# NEXT_RELEASE_IS_MAJOR is set correctly
# This is used to choose the version number when LATEST processing is active
NEXT_RELEASE_IS_MAJOR=0

# Unfortunately, SeaBIOS doesn't always follow an "always increasing" version
# model, so there may be times we should overide the automated version setting.
# We can do so by specifing the value here:
#SEABIOS_VERSION=1.13.0

# Temporary directories used by this script
GIT_DIR=/dev/shm/qemu-factory-git-dir
CMP_DIR=/dev/shm/qemu-factory-cmp-dir
BUNDLE_DIR=/dev/shm/qemu-factory-bundle-dir

# For the following, use 1 or 0 as needed
NUMBERED_PATCHES=0

PATCH_RANGE=1000
REPO_COUNT=26

# Perhaps we need to instead use the terminal local dirname as the index
# and store the ~/git/ as a separate VARIABLE
# This way, we only have one big array instead of two
# BUT STILL WE NEED TO START WITH THE DATA STORED SOMEWHERE!!!!!!
LOCAL_REPO_MAP=(
    ~/git/qemu-opensuse
    ~/git/qemu-seabios
    ~/git/qemu-ipxe
    ~/git/qemu-sgabios
    ~/git/qemu-edk2
    ~/git/qemu-skiboot
    ~/git/qemu-SLOF
    ~/git/qemu-openbios
    ~/git/qemu-keycodemapdb
    ~/git/qemu-slirp
    ~/git/qemu-u-boot
    ~/git/qemu-qboot
    ~/git/qemu-dtc
    ~/git/qemu-opensbi
    ~/git/qemu-edk2-openssl
    ~/git/qemu-capstone
    ~/git/qemu-qemu-palcode
    ~/git/qemu-seabios-hppa
    ~/git/qemu-u-boot-sam460ex
    ~/git/qemu-QemuMacDrivers
    ~/git/qemu-tests-berkeley-softfloat-3
    ~/git/qemu-tests-berkeley-testfloat-3
    ~/git/qemu-edk2-berkeley-softfloat-3
    ~/git/qemu-edk2-openssl-boringssl
    ~/git/qemu-edk2-openssl-krb5
    ~/git/qemu-edk2-openssl-pyca-cryptography
)

# TEMPORARY! FOR NOW WE REQUIRE THESE LOCALLY TO DO WORK ON PACKAGE
REQUIRED_LOCAL_REPO_MAP=(
    ~/git/qemu-opensuse
    ~/git/qemu-seabios
    ~/git/qemu-ipxe
    ~/git/qemu-sgabios
    ~/git/qemu-keycodemapdb
    ~/git/qemu-qboot
)

PATCH_PATH_MAP=(
    ""
    "roms/seabios/"
    "roms/ipxe/"
    "roms/sgabios/"
    "roms/edk2/"
    "roms/skiboot/"
    "roms/SLOF/"
    "roms/openbios/"
    "ui/keycodemapdb/"
    "slirp/"
    "roms/u-boot/"
    "roms/qboot/"
    "dtc/"
    "roms/opensbi/"
    "roms/edk2/CryptoPkg/Library/OpensslLib/openssl/"
    "capstone/"
    "roms/qemu-palcode/"
    "roms/seabios-hppa/"
    "roms/u-boot-sam460ex/"
    "roms/QemuMacDrivers/"
    "tests/fp/berkeley-softfloat-3/"
    "tests/fp/berkeley-testfloat-3/"
    "roms/edk2/ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3/"
    "roms/edk2/CryptoPkg/Library/OpensslLib/openssl/boringssl/"
    "roms/edk2/CryptoPkg/Library/OpensslLib/openssl/krb5/"
    "roms/edk2/CryptoPkg/Library/OpensslLib/openssl/pyca-cryptography/"
)

# Zero based numbering, so we subtract 1 here:
if (( (REPO_COUNT * PATCH_RANGE) - 1 > 9999 )); then
    FIVE_DIGIT_POTENTIAL=1
else
    FIVE_DIGIT_POTENTIAL=0
fi
