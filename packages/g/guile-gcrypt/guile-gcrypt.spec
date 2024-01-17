#
# spec file for package guile-gcrypt
#
# Copyright (c) 2022 SUSE LLC
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


Name:           guile-gcrypt
Version:        0.4.0
Release:        0
Summary:        Cryptography library for Guile using Libgcrypt
License:        GPL-3.0-or-later
Group:          Development/Libraries/Other
URL:            https://notabug.org/cwebber/guile-gcrypt
Source0:        https://notabug.org/cwebber/%{name}/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  guile-devel >= 2.0.10
BuildRequires:  libgcrypt-devel
BuildRequires:  pkg-config
BuildRequires:  texinfo
Requires:       guile >= 2.0.10
# guile-gcrypt needs /usr/lib64/libgcrypt.so (without version number)
Requires:       libgcrypt-devel
Requires(pre):  %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Guile-Gcrypt provides a Guile 2.x interface to a subset of the GNU
Libgcrypt crytographic library. It provides modules for cryptographic
hash functions, message authentication codes (MAC), public-key cryptography,
strong randomness, and more. It is implemented using the foreign function
interface (FFI) of Guile.

%prep
%setup -q -n %{name}

%build
./bootstrap.sh
%configure
make # non-parallel for boo#1170378

%install
make install %{_smp_mflags} DESTDIR=%{buildroot}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/guile-gcrypt.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/guile-gcrypt.info.gz

%files
%defattr(-,root,root,-)
%doc AUTHORS README
%license COPYING
%{_datadir}/guile
%{_infodir}/guile-gcrypt*
%{_libdir}/guile

%changelog
