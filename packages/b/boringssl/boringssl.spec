#
# spec file for package boringssl
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover 1
%define libname libboringssl%{sover}
%define src_install_dir %{_prefix}/src/%{name}
Name:           boringssl
Version:        0.20210430
Release:        0
Summary:        An SSL/TLS protocol implementation
License:        OpenSSL
URL:            https://boringssl.googlesource.com/boringssl/
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
Patch2:         0002-crypto-Fix-aead_test-build-on-aarch64.patch
Patch3:         0003-enable-s390x-builds.patch
Patch4:         0004-fix-alignment-for-ppc64le.patch
Patch5:         0005-fix-alignment-for-arm.patch
Patch6:         0006-gcc-disable-werror.patch
Patch7:         0007-fix-go-vendor-embed_test_data.patch
Patch8:         0008-fix-go-vendor-err_data_generate.patch
Patch9:         0009-soname-sover.patch
BuildRequires:  cmake >= 3.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  golang(API) >= 1.13
ExclusiveArch:  %{ix86} x86_64 aarch64 s390x ppc64le %{arm} riscv64

%description
BoringSSL is an implementation of the Secure Sockets Layer (SSL) and
Transport Layer Security (TLS) protocols, derived from OpenSSL.

%package -n %{libname}
Summary:        An SSL/TLS protocol implementation
Recommends:     ca-certificates-mozilla

%description -n %{libname}
BoringSSL is an implementation of the Secure Sockets Layer (SSL) and
Transport Layer Security (TLS) protocols, derived from OpenSSL.

%package devel
Summary:        Development files for BoringSSL
Requires:       %{libname} = %{version}

%description devel
Development files for BoringSSL - an implementation of the Secure
Sockets Layer (SSL) and Transport Layer Security (TLS) protocols,
derived from OpenSSL.

%package source
Summary:        Source code of BoringSSL
BuildArch:      noarch

%description source
Source files for BoringSSL implementation

%prep
%autosetup -a 1 -p 1

%build
# Supress CMake default to include RPATH in binary on platforms which support it.
# Failure to supress rpath fails rpmlint:
# libboringssl1: E: binary-or-shlib-defines-rpath (Badness: 10000) /usr/lib64/libboringssl_ssl.so.1
# (RUNPATH: /home/abuild/rpmbuild/BUILD/boringssl-0.20210430-build/boringssl-0.20210430/build/crypto)
# The binary or shared library defines `RPATH' (or `RUNPATH') that points to a non-system library path.
%cmake \
%ifarch riscv64
  -DOPENSSL_NO_ASM=1 \
%endif
  -DCMAKE_SKIP_RPATH=1 \
  -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now"
%cmake_build

%install
# Install libraries
# Upstream sources build .so in crypto/ and ssl/ subdirs. TBD if package layout needs to preserve that.
install -D -m0755 build/crypto/libboringssl_crypto.so.%{sover} %{buildroot}%{_libdir}/libboringssl_crypto.so.%{sover}
install -D -m0755 build/ssl/libboringssl_ssl.so.%{sover} %{buildroot}%{_libdir}/libboringssl_ssl.so.%{sover}
# Create links from *.so to *.so.SOVER
ln -sf libboringssl_crypto.so.%{sover} %{buildroot}%{_libdir}/libboringssl_crypto.so
ln -sf libboringssl_ssl.so.%{sover} %{buildroot}%{_libdir}/libboringssl_ssl.so

# Install sources
rm -rf build/
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}
# Fix arch-independent-package-contains-binary-or-object
find %{buildroot}%{src_install_dir} -type f \( -name "*.a" -o -name "*.lib" -o -name "*.o" \) -exec rm -f "{}" +

# Fix version-control-internal-file error.
# boringssl-source.noarch: E: version-control-internal-file
# /usr/src/boringssl/vendor/golang.org/x/sys/unix/.gitignore
find %{buildroot}%{src_install_dir} -type f -name ".gitignore" -delete

# Fix script-without-shebang error.
# boringssl-source.noarch: E: script-without-shebang
# /usr/src/boringssl/third_party/googletest/test/gtest_test_utils.py
# /usr/src/boringssl/third_party/googletest/test/gtest_xml_test_utils.py
# /usr/src/boringssl/fuzz/minimise_corpora.sh
# /usr/src/boringssl/util/fipstools/break-tests-android.sh
# /usr/src/boringssl/util/fipstools/break-tests.sh
# /usr/src/boringssl/crypto/fipsmodule/ec/asm/p256_beeu-x86_64-asm.pl
# As built, permissions for these are:
# -rwxr-xr-x third_party/googletest/test/gtest_test_utils.py
# -rwxr-xr-x third_party/googletest/test/gtest_xml_test_utils.py
# -rw-r--r-- fuzz/minimise_corpora.sh
# -rw-r--r-- util/fipstools/break-tests-android.sh
# -rw-r--r-- util/fipstools/break-tests.sh
# -rw-r--r-- crypto/fipsmodule/ec/asm/p256_beeu-x86_64-asm.pl
# Unsetting executable bits on .py files has the intended effect to pass the linter
chmod a-x %{buildroot}%{_prefix}/src/boringssl/third_party/googletest/test/gtest_test_utils.py
chmod a-x %{buildroot}%{_prefix}/src/boringssl/third_party/googletest/test/gtest_xml_test_utils.py
# The .sh files already do not have executable bits set but script-without-shebang linter still fails
# Insert a bash shebang line for script-without-shebang linter
sed -i -e '1i#!/bin/bash' %{buildroot}%{_prefix}/src/boringssl/fuzz/minimise_corpora.sh
sed -i -e '1i#!/bin/bash' %{buildroot}%{_prefix}/src/boringssl/util/fipstools/break-tests-android.sh
sed -i -e '1i#!/bin/bash' %{buildroot}%{_prefix}/src/boringssl/util/fipstools/break-tests.sh
# Insert a perl shebang line for script-without-shebang linter
sed -i -e '1i#!%{_bindir}/perl' %{buildroot}%{_prefix}/src/boringssl/crypto/fipsmodule/ec/asm/p256_beeu-x86_64-asm.pl

# Fix non-executable-script warning.
find %{buildroot}%{src_install_dir} -type f -name "*.sh" -print -exec chmod +x "{}" +
find %{buildroot}%{src_install_dir} -type f -name "*.pl" -print -exec chmod +x "{}" +
# Fix these individually, since we don't want all *.py to all be executable
chmod +x %{buildroot}%{_prefix}/src/boringssl/third_party/googletest/test/googletest-json-outfiles-test.py
chmod +x %{buildroot}%{_prefix}/src/boringssl/third_party/googletest/test/googletest-json-output-unittest.py
chmod +x %{buildroot}%{_prefix}/src/boringssl/third_party/googletest/test/googletest-param-test-invalid-name1-test.py
chmod +x %{buildroot}%{_prefix}/src/boringssl/third_party/googletest/test/googletest-param-test-invalid-name2-test.py
chmod +x %{buildroot}%{_prefix}/src/boringssl/third_party/googletest/test/gtest_list_output_unittest.py
chmod +x %{buildroot}%{_prefix}/src/boringssl/util/bot/update_clang.py
# Fix one bash script to be executable
chmod +x %{buildroot}%{_prefix}/src/boringssl/vendor/golang.org/x/sys/windows/mkerrors.bash

# Fix env-script-interpreter error.
find %{buildroot}%{src_install_dir} -type f -name "*.pl" -exec sed -i 's|#!.*%{_bindir}/env perl|#!%{_bindir}/perl|' "{}" +
# crypto/asn1/charmap.pl /usr/local/bin/perl disallowed perl location
find %{buildroot}%{src_install_dir} -type f -name "*.pl" -exec sed -i 's|#!.*%{_prefix}/local/bin/perl|#!%{_bindir}/perl|' "{}" +

find %{buildroot}%{src_install_dir} -type f -name "*.py" -exec sed -i 's|#!.*%{_bindir}/python$|#!%{_bindir}/python3|' "{}" +
find %{buildroot}%{src_install_dir} -type f -name "*.py" -exec sed -i 's|#!.*%{_bindir}/env python.*|#!%{_bindir}/python3|' "{}" +
find %{buildroot}%{src_install_dir} -type f -name "*.sh" -exec sed -i 's|#!.*%{_bindir}/env bash|#!/bin/bash|' "{}" +

# To avoid conflicts with openssl development files, change all includes from
# openssl to boringssl.
# BoringSSL headers provided by this pachage are installed in
# /usr/include/boringssl for the same reason.
find %{buildroot}%{_prefix}/src/boringssl/include/openssl -type f -exec sed -i 's/openssl/boringssl/' "{}" +

find %{buildroot}%{_prefix}/src/boringssl/include/openssl -type f -execdir install -D -m0644 "{}" "%{buildroot}%{_includedir}/boringssl/{}" \;

# Remove Go build utilities which cause debuginfo error:
# dwz: ./usr/src/boringssl/crypto/err/err_data_generate.debug: Found compressed .debug_abbrev section, not attempting dwz compression
# dwz: ./usr/src/boringssl/embed_test_data.debug: Found compressed .debug_abbrev section, not attempting dwz compression
rm %{buildroot}%{_prefix}/src/boringssl/crypto/err/err_data_generate
rm %{buildroot}%{_prefix}/src/boringssl/embed_test_data

# Relocate doc and license to align with packaging standards
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a %{buildroot}%{_prefix}/src/boringssl/README.md %{buildroot}%{_docdir}/%{name}
cp -a %{buildroot}%{_prefix}/src/boringssl/LICENSE %{buildroot}%{_docdir}/%{name}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc %{_docdir}/%{name}/README.md
%license %{_docdir}/%{name}/LICENSE
%exclude %{_docdir}/%{name}
%{_libdir}/libboringssl_crypto.so.%{sover}
%{_libdir}/libboringssl_ssl.so.%{sover}

%files devel
%{_includedir}/boringssl
%{_libdir}/libboringssl_crypto.so
%{_libdir}/libboringssl_ssl.so

%files source
%{src_install_dir}
%exclude %{_prefix}/src/boringssl/README.md
%exclude %{_prefix}/src/boringssl/LICENSE

%changelog
