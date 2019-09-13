#
# spec file for package yafc
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           yafc
BuildRequires:  krb5-devel
BuildRequires:  makeinfo
BuildRequires:  openssl-devel
BuildRequires:  readline-devel
Summary:        Yet Another FTP Client
License:        GPL-2.0+
Group:          Productivity/Networking/Ftp/Clients
Version:        1.1.1
Release:        0
Url:            http://yafc.sourceforge.net/
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Prefix:         /usr
PreReq:         %install_info_prereq
Patch:          patch_utils.diff
Patch1:         kerberos_warnings.diff
Patch2:         remove_bsd_code.diff
Patch3:         yafc-krb5.diff
Patch4:         disable_date_time.diff
Patch5:         yafc-texinfo-5.0.patch

%description
Yafc is an OpenSource console mode FTP client. It has support for
Kerberos 4/5 authentication and sftp (ssh2). Other features include tab
completion, directory cache, powerful aliases, recursive file commands
and bookmarks with autologin.



Authors:
--------
    Martin Hedenfalk <mhe@home.se>

%prep
%setup -q
%patch
%patch1
%patch2
%patch3
%patch4 -p1
%patch5 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" ./configure --prefix=%{prefix} --infodir=%{_infodir} --mandir=%{_mandir}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install 

%clean
rm -rf $RPM_BUILD_ROOT

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%defattr(-,root,root)
%doc BUGS COPYING NEWS README THANKS TODO inputrc.sample yafcrc.sample
%doc %{_mandir}/man1/yafc.1.gz
%{_bindir}/yafc
%{_infodir}/yafc.info.gz

%changelog
