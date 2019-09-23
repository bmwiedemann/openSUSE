#
# spec file for package tpm-quote-tools
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


Name:           tpm-quote-tools
Version:        1.0.4
Release:        0
Summary:        Trusted Platform Module (TPM) remote attestation tools
License:        BSD-3-Clause
Group:          Productivity/Security
Url:            https://sourceforge.net/projects/tpmquotetools
Source0:        https://downloads.sourceforge.net/project/tpmquotetools/%{version}/tpm-quote-tools-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  trousers-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Trusted Computing is a set of specifications published by the Trusted
Computing Group (TCG). The Trusted Platform Module (TPM) is the
hardware component for Trusted Computing. The tpm-quote-tools package
provides additional tools that employ the TPM quote command to facilitate
remote attestation. These tools are based on the trousers TPM 1.2 stack.

%prep
%setup -q

%build
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags}

%install
%define docdir %{_defaultdocdir}/%{name}
make DESTDIR=%{buildroot} install %{?_smp_mflags}
mkdir -p %{buildroot}/%{docdir}
cp README COPYING %{buildroot}/%{docdir}

%files
%defattr(-,root,root)
%doc README COPYING
%{_mandir}/man8/tpm_*
%{_bindir}/tpm_*

%changelog
