#
# spec file for package kup
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 John 'Warthog9' Hawley <warthog9@kernel.org>
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


Name:           kup
Summary:        Kernel.org Uploader
License:        GPL-2.0+
Group:          Development/Tools/Other
Version:        0.3.6
Release:        0
Url:            https://www.kernel.org/pub/software/network/kup/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  xz

# Upstream First - Policy:
# Never add any patches to this package without the upstream commit id
# in the patch. Any patches added here without a very good reason to make
# an exception will be silently removed with the next version update.

%description
Kernel.org Uploader - meta package.

%package client
Summary:        Kernel.org Uploader - client
Group:          Development/Tools/Other
Requires:       perl
Requires:       perl(Config::Simple)
Requires:       perl(Encode)
Requires:       perl(File::Spec)

%description client
Kup is a file upload utility for kernel.org. It is designed to only accept
cryptographically verified uploads from pre-authorized, trusted members.

%package server
Summary:        Kernel.org Uploader - server
Group:          Development/Tools/Other
Requires:       perl
Requires:       perl(BSD::Resource)
Requires:       perl(Config::Simple)
Requires:       perl(Digest::SHA)
Requires:       perl(Encode)
Requires:       perl(Fcntl)
Requires:       perl(File::Path)
Requires:       perl(File::Temp)
Requires:       perl(Git)
Requires:       perl(IO::Handle)
Requires:       perl(IPC::Open2)
Requires:       perl(POSIX)
Requires:       perl(Sys::Syslog)

%description server
Kup is a file upload utility for kernel.org. It is designed to only accept
cryptographically verified uploads from pre-authorized, trusted members.

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m 755 kup gpg-sign-all kup-server %{buildroot}%{_bindir}
install -m 644 kup.1 kup-server.1 %{buildroot}%{_mandir}/man1/

%files client
%defattr(-,root,root,-)
%doc README COPYING
%{_bindir}/kup
%{_mandir}/man1/kup.1*

%files server
%defattr(-,root,root,-)
%doc README COPYING
%{_bindir}/gpg-sign-all
%{_bindir}/kup-server
%{_mandir}/man1/kup-server.1*

%changelog
