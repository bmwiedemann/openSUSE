#
# spec file for package openssl-ibmca
#
# Copyright (c) 2018-2020 SUSE LLC
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


Name:           openssl-ibmca
Version:        2.1.1
Release:        0
Summary:        The IBMCA OpenSSL dynamic engine
License:        Apache-2.0
Group:          Hardware/Other
URL:            https://github.com/opencryptoki/openssl-ibmca
Source:         https://github.com/opencryptoki/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libica-devel >= 3.1.1
BuildRequires:  libica-tools >= 2.4.0
BuildRequires:  libtool
BuildRequires:  openssl-devel
Requires:       libica3
Requires:       openssl
ExclusiveArch:  s390x

%description
This package contains a shared object OpenSSL dynamic engine for the
IBM eServer Cryptographic Accelerator (ICA).

%prep
%autosetup
./bootstrap.sh

%build
# The directory where crypto engines are located is owned by the libcrypto package.
# Find out where that is for this version of the distribution.
%define _ENGINE_DIR %(pkg-config --variable=enginesdir libcrypto)

autoreconf --force --install
export CFLAGS="%{optflags}"
export CPPFLAGS="%{optflags}"
%configure \
  --libdir=%{_ENGINE_DIR}
make %{?_smp_mflags}

%install
# Update the sample config file so that the dynamic path points
# to the correct version of the engines directory.
sed -i -e "/^dynamic_path/s, = .*/, = %{_ENGINE_DIR}/," src/openssl.cnf.sample

%make_install
rm %{buildroot}/%{_ENGINE_DIR}/ibmca.la

%post
#Original fix for bsc#942839 was to update on first install
#For bsc#966139 update if openssl_def not found
SSLCNF=%{_sysconfdir}/ssl/openssl.cnf
SSLSMP=%{_docdir}/%{name}/openssl.cnf.sample

if [ -f ${SSLCNF} -a -f ${SSLSMP} ]; then
  if grep '^openssl_conf[[:space:]]*=[[:space:]]*openssl_def$' ${SSLCNF} >/dev/null 2>&1; then
    # Config already installed. Update library path if necessary
    SECTSTART=$(grep -n '\[ibmca_section\]' ${SSLCNF} | head -n1 | cut -d':' -f1)
    REPLINE=""
    if [ "z${SECTSTART}" != "z" ]; then
      REPLINE=$((SECTSTART - 1 + $(tail -n+${SECTSTART} ${SSLCNF} | grep -n 'dynamic_path' | head -n1 | cut -d':' -f1) ))
    fi
    if [ "z${REPLINE}" != "z" ]; then
      head -n$((REPLINE - 1)) ${SSLCNF} > ${SSLCNF}.temp
      grep 'dynamic_path' ${SSLSMP} >> ${SSLCNF}.temp
      tail -n+$((REPLINE + 1)) ${SSLCNF} >> ${SSLCNF}.temp
      mv ${SSLCNF}.temp ${SSLCNF}
    fi
  else
    CNFSZE=350 # Size in lines of original openssl.cnf
    SMPSZE=52  # Size in lines of original sample config file
    CNFINS=9   # Line number in openssl.cnf to insert new line
    SMPUSE=11  # Line number in sample to copy from
    if [ $(wc -l ${SSLCNF} | cut -d ' ' -f 1) -ne ${CNFSZE} ]; then
      echo Original ${SSLCNF} incorrect size. Please manually update from ${SSLSMP}
    elif [ $(wc -l ${SSLSMP} | cut -d ' ' -f 1) -ne ${SMPSZE} ]; then
      echo Original ${SSLSMP} incorrect size. Please manually update to ${SSLCNF}
    else
      mv ${SSLCNF} ${SSLCNF}.orig
      head -n ${CNFINS} ${SSLCNF}.orig > ${SSLCNF}
      head -n ${SMPUSE} ${SSLSMP} | tail -n 1 >> ${SSLCNF}
      tail -n $((CNFSZE - CNFINS)) ${SSLCNF}.orig >> ${SSLCNF}
      head -n $((SMPUSE - 1)) ${SSLSMP} >> ${SSLCNF}
      tail -n $((SMPSZE - SMPUSE)) ${SSLSMP} >> ${SSLCNF}
    fi
  fi
fi

%postun
if [ $1 -eq 0 ]; then # last uninstall, modify %%{_sysconfdir}/openssl.cnf (bsc#942839)
  SSLCNF=%{_sysconfdir}/ssl/openssl.cnf
  if [ -f ${SSLCNF}.orig ]; then
    mv ${SSLCNF}.orig ${SSLCNF}
  fi
fi

%files
%license LICENSE
%doc README.md
%doc src/openssl.cnf.sample
%{_ENGINE_DIR}/ibmca.*
%{_mandir}/man5/ibmca.5%{?ext_man}

%changelog
