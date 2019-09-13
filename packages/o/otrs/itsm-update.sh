#!/bin/bash
# This script creates a new itsm-%version.tar.bz2

URL='ftp://ftp.otrs.org/pub/otrs/itsm'
VERSION=$(grep "%define itsm_ver" otrs.spec | cut -d' ' -f3)
MAJOR=$(echo ${VERSION} | cut -d'.' -f1)
MINOR=$(echo ${VERSION} | cut -d'.' -f2)
PATCH=$(echo ${VERSION} | cut -d'.' -f3)
PPATCH=$((${PATCH} - 1))

if [[ ${MAJOR} -eq 4 ]]; then
    PMINOR='3.3'
    PMINOR_PKG=33
    PREJECT="*3.2.9?.opm,*${PMINOR}.?.opm,*${PMINOR}.9?.opm"
    REJECT="*${PMINOR}.9?.opm,*${MAJOR}.0.?.opm,*${MAJOR}.0.1?.opm"
elif [[ ${MAJOR} -eq 5 ]]; then
    PMINOR=$((${MAJOR} - 1))
    PMINOR_PKG=${PMINOR}
    PREJECT="*3.3.9?.opm,*${PMINOR}.0.?.opm,*${PMINOR}.0.1?.opm,*${PMINOR}.0.9?.opm"
    REJECT="*${PMINOR}.0.9?.opm,*${MAJOR}.0.?.opm,*${MAJOR}.0.1?.opm"
elif [[ ${MAJOR} -ge 6 ]]; then
    PMINOR=$((${MAJOR} - 1))
    PMINOR_PKG=${PMINOR}
    PREJECT="*$((PMINOR - 1)).0.9?.opm,*$((MAJOR - 1)).0.?.opm,*$((MAJOR - 1)).0.1?.opm,*$((MAJOR - 1)).0.2?.opm"
    REJECT="*${PMINOR}.0.9?.opm,*${MAJOR}.0.9?.opm"
fi

if [[ ! -d itsm-${VERSION} ]]; then
    if [[ ! -d itsm-${MAJOR}.${MINOR}.${PPATCH} ]]; then
        if [[ -f itsm-${MAJOR}.${MINOR}.${PPATCH}.tar.bz2 ]]; then
            tar xvfpj itsm-${MAJOR}.${MINOR}.${PPATCH}.tar.bz2
            mv itsm-${MAJOR}.${MINOR}.${PPATCH} itsm-${VERSION}
        else
            mkdir -p itsm-${VERSION}
        fi
    else
        mv itsm-${MAJOR}.${MINOR}.${PPATCH} itsm-${VERSION}
    fi
fi
cd itsm-${VERSION}/ || exit 1

# get INSTALL file
wget -nH --cut-dirs=3 -m \
${URL}/INSTALL-${MAJOR}.ITSM

# convert "ASCII English text, with CRLF line terminators"
#  into "ASCII English text"
perl -p -i -e 's|\r\n|\n|' INSTALL-*

# get packages of current version, exclude RC's
wget -nH --cut-dirs=3 -m \
-R ${REJECT} \
-R *~ \
${URL}/packages${MAJOR}/

# get packages of previous version, exclude RC's
wget -nH --cut-dirs=3 -m \
-R ${PREJECT} \
-R *~ \
${URL}/packages${PMINOR_PKG}/

cd ..
tar cvfj itsm-${VERSION}.tar.bz2 --exclude='.listing' itsm-${VERSION}
