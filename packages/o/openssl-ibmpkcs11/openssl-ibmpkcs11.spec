#
# spec file for package openssl-ibmpkcs11
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           openssl-ibmpkcs11
Url:            http://sourceforge.net/projects/opencryptoki/
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  openssl-devel
Version:        1.0.1
Release:        0
Summary:        OpenSSL Dynamic PKCS #11 Engine
License:        OpenSSL
Group:          Productivity/Networking/Security
Source:         %name-%{version}.tar.bz2
Patch:          openssl-ibmpkcs11_sample_config_file.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
OpenSSL Dynamic PKCS #11 Engine



%prep
%setup
%patch -p1

%build
# The directory where crypto engines are located is owned by the libcrypto package.
# Find out where that is for this version of the distribution.
%define _ENGINE_DIR %(pkg-config --variable=enginesdir libcrypto)

sh bootstrap.sh
%configure --libdir=%{_ENGINE_DIR}
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_ENGINE_DIR}/*.{la,so}

%files
%defattr(-,root,root)
%doc LICENSE ChangeLog README openssl.cnf.sample
%{_ENGINE_DIR}/libibmpkcs11.so.*

%changelog
