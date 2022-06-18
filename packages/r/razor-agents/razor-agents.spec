#
# spec file for package razor-agents
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


%define src_name Razor2-Client-Agent
Name:           razor-agents
Version:        2.86
Release:        0
Summary:        SPAM catalogue inquiry and update tool
License:        Artistic-2.0
Group:          Productivity/Networking/Email/Utilities
URL:            http://razor.sourceforge.net/
Source:         https://github.com/toddr/%{src_name}/archive/refs/tags/v%{version}.tar.gz#/%{src_name}-%{version}.tar.gz
Source1:        README.SUSE
Requires:       perl-razor-agents
%{perl_requires}

%description
Vipul's Razor is a distributed, collaborative, spam detection and
filtering network. Razor establishes a distributed and constantly
updating catalogue of spam in propagation. This catalogue is used by
clients to filter out known spam. On receiving a spam, a Razor
Reporting Agent (run by an end-user or a troll box) calculates and
submits a 20-character unique identification of the spam (a SHA Digest)
to its closest Razor Catalogue Server. The Catalogue Server echos this
signature to other trusted servers after storing it in its database.
Prior to manual processing or transport-level reception, Razor
Filtering Agents (end-users and MTAs) check their incoming mail against
a Catalogue Server and filter out or deny transport in case of a
signature match. Catalogued spam, once identified and reported by a
Reporting Agent, can be blocked out by the rest of the Filtering Agents
on the network.

Can be used as one of the spamassassin rules.

%package -n perl-razor-agents
Summary:        The required perl modules for razor-agents
License:        Artistic-1.0
Group:          Development/Languages/Perl
Requires:       perl-Digest-SHA1
Requires:       perl-URI

%description -n perl-razor-agents
razor-agents are little programs to retrieve or update information
from the razor <http://razor.sourceforge.net/> network to exchange
signatures of SPAM. This package contains the required perl modules.

%prep
%setup -q -n %{src_name}-%{version}
cp %{SOURCE1} .

%build
perl Makefile.PL OPTIMIZE="%{optflags} -Wall"
make

%check
make test

%install
make DESTDIR=%{buildroot} INSTALLMAN5DIR=%{buildroot}/%{_mandir}/man5 install_vendor
%perl_process_packlist

%files -n perl-razor-agents
%doc BUGS CREDITS Changes FAQ README.SUSE
%license LICENSE
%{_mandir}/man3/Razor*
%{_mandir}/man5/razor*
%{perl_vendorarch}/Razor2
%{perl_vendorarch}/auto/Razor2

%files
%{_mandir}/man1/razor*
%{_bindir}/razor*

%changelog
