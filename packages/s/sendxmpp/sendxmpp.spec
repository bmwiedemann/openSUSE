#
# spec file for package sendxmpp
#
# Copyright (c) 2020 SUSE LLC
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


Name:           sendxmpp
Version:        1.24
Release:        0
Summary:        A perl-script to send xmpp, similar to what mail does for mail
License:        GPL-2.0-only
Group:          Productivity/Networking/Talk/Clients
URL:            https://sendxmpp.hostname.sk/
Source0:        https://github.com/lhost/sendxmpp/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
Requires:       perl(Net::XMPP)
%perl_requires

%description
sendxmpp is a perl-script to send xmpp (jabber), similar to 
what mail(1) does for mail.

%prep
%setup -q

%build
%{__perl} Makefile.PL
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,-)

%changelog
