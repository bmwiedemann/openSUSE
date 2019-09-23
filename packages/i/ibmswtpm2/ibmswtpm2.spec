#
# spec file for package ibmswtpm2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define suite ibmtss

%ifarch    ppc ppc64 s390 s390x
%define extra_ccflags -DBIG_ENDIAN_TPM=1
%else
%define extra_ccflags ""
%endif

Name:           ibmswtpm2
Version:        1332
Release:        0
Summary:        IBM's Software TPM 2.0
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://sourceforge.net/projects/ibmswtpm2
Source:         https://sourceforge.net/projects/ibmswtpm2/files/ibmtpm%{version}.tar.gz
Patch1:         makefile.patch
Patch2:         ibmswtpm2-fix-uninitialized.patch
BuildRequires:  libopenssl-devel >= 1.0

%description
An implementation of the TCG TPM 2.0 specification. It is based on
the TPM specification Parts 3 and 4 source code donated by Microsoft,
with additional files to complete the implementation.

This TPM emulator listens on TCP ports (default 2321 and 2322) and
saves state to the file "NVChip" in the current directory.

It is probably not of much use other than testing the IBM TSS
implementation because of this specific interface.

%prep
%setup -q -c
%autopatch -p 1

%build
cd src
CCFLAGS="%{optflags} "%{extra_ccflags} make %{?_smp_mflags}

%install
cd src
install -m 755 -D -t %{buildroot}/%{_libexecdir}/%{suite} tpm_server

%files
%dir %{_libexecdir}/%{suite}
%{_libexecdir}/%{suite}/tpm_server
%doc ibmtpm.doc

%changelog
