#
# spec file for package openssl_tpm_engine
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define enginesdir %(pkg-config libcrypto --variable=enginesdir)
Name:           openssl_tpm_engine
Version:        0.4.2
Release:        0
Summary:        OpenSSL TPM interface engine plugin
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            http://sourceforge.net/projects/trousers
Source0:        https://downloads.sourceforge.net/project/trousers/OpenSSL%%20TPM%%20Engine/%{version}/%{name}-%{version}.tar.gz
Patch0:         openssl_tpm_engine-somodule.patch
Patch1:         0000-openssl-1.1-compatibility-preparation-remove-unneede.patch
Patch2:         0001-openssl-1.1-compatibility-preparation-fix-warnings-a.patch
Patch3:         0002-Explicitly-link-create_tpm_key-against-libcrypto.patch
Patch4:         0003-OpenSSL-1.1-compatibility.patch
Patch5:         0004-automake-add-linker-flags-to-explicitly-build-a-plug.patch
Patch6:         0005-autotools-choose-engine-plugin-name-based-on-OpenSSL.patch
Patch7:         0006-autotools-make-engine-plugin-installation-dir-config.patch
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  trousers-devel
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(openssl)

%description
This package contains a plugin a for OpenSSL which connects it with the
Trusted Platform Module found on newer machines and a create_tpm_key
helper binary to create and extract a TPM key.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
mkdir m4
sh ./bootstrap.sh
%configure --libdir=/%{_lib}
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}/%{enginesdir}/tpm.la

%files
%license LICENSE
%doc README openssl.cnf.sample
%{_bindir}/create_tpm_key
%dir %{enginesdir}
%{enginesdir}/tpm.so

%changelog
