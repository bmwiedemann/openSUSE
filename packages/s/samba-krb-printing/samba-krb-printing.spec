#
# spec file for package samba-krb-printing
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           samba-krb-printing
Summary:        Wrapper binary for kerberized printing
License:        GPL-3.0+
Version:        3.7.0
Release:        0
Group:          Productivity/Networking/Samba
Source:         get_printing_ticket.c
PreReq:         coreutils
Provides:       samba-gplv3-krb-printing = %{version}
Obsoletes:      samba-gplv3-krb-printing < %{version}
Requires:       cups
Requires:       samba-client
%if 0%{?suse_version} == 0 || 0%{?suse_version} > 1120
%define cups_lib_dir %{_prefix}/lib/cups
%else
%define cups_lib_dir %{_libdir}/cups
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A wrapper binary to run smbspool with the original calling UID.

%prep
%setup -c -T

%build
gcc %optflags -fPIE -pie -o get_printing_ticket %{SOURCE0}

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0700 get_printing_ticket %{buildroot}/%{_bindir}/
# cups SMB support
mkdir -p %{buildroot}/%{cups_lib_dir}/backend/
touch %{buildroot}/%{cups_lib_dir}/backend/smb

%post
if test ${1:-0} -eq 1 -a -d %{cups_lib_dir}/backend; then
	ln -fs %{_bindir}/get_printing_ticket %{cups_lib_dir}/backend/smb
fi

%postun
if test ${1:-0} -eq 0 -a -e %{_bindir}/smbspool -a -d %{cups_lib_dir}/backend; then
	ln -fs %{_bindir}/smbspool %{cups_lib_dir}/backend/smb
fi

%files
%defattr(-,root,root)
%if 0%{?suse_version} == 0 || 0%{?suse_version} > 1120
%attr(0700,root,lp) %{_bindir}/get_printing_ticket
%else
%attr(-,root,lp) %{_bindir}/get_printing_ticket
%endif
%dir %{cups_lib_dir}
%dir %{cups_lib_dir}/backend
%ghost %{cups_lib_dir}/backend/smb

%changelog
