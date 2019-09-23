#
# spec file for package tftpboot-installation-common
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


Name:           tftpboot-installation-common
Version:        1.1
Release:        0
Summary:        Contains the needed services for tftpboot-installation
License:        BSD-3-Clause
Group:          System/Base
Source:         %{name}-%{version}.tar.bz2
Requires:       tftp
Requires(pre):  tftp
BuildArch:      noarch

%description
This packages contains all the files and services which are needed to
mount the tftpboot-installation images into the /srv/tftpboot directory.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib
cp -av * %{buildroot}%{_prefix}/lib/

%pre
%service_add_pre srv-tftpboot-suse\\x2dtftp\\x2dinstall.mount

%post
%tmpfiles_create ypserv.conf
%service_add_post srv-tftpboot-suse\\x2dtftp\\x2dinstall.mount

%preun
%service_del_preun srv-tftpboot-suse\\x2dtftp\\x2dinstall.mount

%postun
%service_del_postun srv-tftpboot-suse\\x2dtftp\\x2dinstall.mount

%files
%{_prefix}/lib/tmpfiles.d/*.conf
%{_prefix}/lib/systemd/system/*.mount

%changelog
