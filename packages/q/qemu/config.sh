#!/bin/bash

# config.sh:

# The next few VARIABLES are to be edited as required:

# Package name. (In multibuild, it's the base package). Used to ref spec file.
PKG=qemu

# Here is the git repo which tracks a separate upstream git based project
# We take this approach so we can have our own tags and branches, and store
# the patches in git for others to access outside of the bundle.
PACKAGE_MAIN_GIT_REPO=https://github.com/openSUSE/qemu.git

# This is the upstream for the PACKAGE_MAIN_GIT_REPO
UPSTREAM_GIT_REPO=https://gitlab.com/qemu-project/qemu.git

# The following specifies the upstream tag or commit upon which our patchqueue
# gets rebased. The special value LATEST may be used to "automatically" track
# the upstream development tree in the master branch
#GIT_UPSTREAM_COMMIT_ISH=v7.0.0
GIT_UPSTREAM_COMMIT_ISH=v7.1.0
# WARNING: If transitioning from using LATEST to not, MANUALLY re-set the
# tarball present. If transitioning TO LATEST, make sure that
# NEXT_RELEASE_IS_MAJOR is set correctly
# This is used to choose the version number when LATEST processing is active
NEXT_RELEASE_IS_MAJOR=1

# Unfortunately, SeaBIOS doesn't always follow an "always increasing" version
# model, so there may be times we should overide the automated version setting.
# We can do so by specifing the value here:
#SEABIOS_VERSION=1.13.0

# In following, use 1 or 0 as needed (representing true or false respectively)
NUMBERED_PATCHES=0

PATCH_RANGE=1000

# For compatibility with old packages, we include this option
OVERRIDE_FIVE_DIGIT_NUMBERING=0

# Path to be used for temporary files, directories, repositories, etc.
# Default is /dev/shm. An alternative could be /tmp (e.g., when building
# in containers, or whatever).
#TMPDIR=/dev/shm
TMPDIR=/tmp

# This array tracks all git submodule paths within the superproject (1st entry)
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
    "meson/"
    "tests/fp/berkeley-softfloat-3/"
    "tests/fp/berkeley-testfloat-3/"
    "tests/lcitool/libvirt-ci"
    "roms/edk2/ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3/"
    "roms/edk2/CryptoPkg/Library/OpensslLib/openssl/boringssl/"
    "roms/edk2/CryptoPkg/Library/OpensslLib/openssl/krb5/"
    "roms/edk2/CryptoPkg/Library/OpensslLib/openssl/pyca-cryptography/"
    "roms/edk2/BaseTools/Source/C/BrotliCompress/brotli/"
    "roms/edk2/MdeModulePkg/Library/BrotliCustomDecompressLib/brotli/"
    "roms/edk2/MdeModulePkg/Universal/RegularExpressionDxe/oniguruma/"
    "roms/edk2/UnitTestFrameworkPkg/Library/CmockaLib/cmocka/"
    "roms/vbootrom/"
    "roms/edk2/RedfishPkg/Library/JsonLib/jansson"
)

# (order and count must correspond to PATCH_PATH_MAP)
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
    ~/git/qemu-meson
    ~/git/qemu-tests-berkeley-softfloat-3
    ~/git/qemu-tests-berkeley-testfloat-3
    ~/git/qemu-tests-lcitool-libvirt-ci
    ~/git/qemu-edk2-berkeley-softfloat-3
    ~/git/qemu-edk2-openssl-boringssl
    ~/git/qemu-edk2-openssl-krb5
    ~/git/qemu-edk2-openssl-pyca-cryptography
    ~/git/qemu-edk2-BrotliCompress-brotli
    ~/git/qemu-edk2-BrotliCustomDecompressLib-brotli
    ~/git/qemu-edk2-oniguruma
    ~/git/qemu-edk2-cmocka
    ~/git/qemu-vbootrom
    ~/git/qemu-edk2-jansson
)
