#
# spec file for package logwarn
#
# Copyright (c) 2020 SUSE LLC
# Copyright (C) 2010-2011 Archie L. Cobbs. All rights reserved.
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


Name:           logwarn
Version:        1.0.15
Release:        0
Summary:        Utility for finding interesting messages in log files
License:        Apache-2.0
Group:          System/Monitoring
Source:         https://s3.amazonaws.com/archie-public/%{name}/%{name}-%{version}.tar.gz
URL:            https://github.com/archiecobbs/%{name}/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  nagios-rpm-macros

%description
%{name} searches for interesting messages in log files, where ``interest-
ing'' is defined by an user-supplied list of positive and negative (pre-
ceeded with a ``!'') extended regular expressions provided on the command
line.

Each log message is compared against each pattern in the order given.  If
the log message matches a positive pattern before matching a negative
!pattern then it's printed to standard output.

%{name} keeps track of its position between invocations, so each matching
line is only ever output once.  It also finds messages in log files that
have been rotated (and possibly compressed) since the previous invoca-
tion.

%{name} also includes support for log messages that span multiple lines.

%prep
%setup -q

%build
%{configure}
make

%install
%{makeinstall}
install -d %{buildroot}%{_var}/lib/%{name}
install -d %{buildroot}%{_datadir}/doc/packages/%{name}
install COPYING %{buildroot}%{_datadir}/doc/packages/%{name}/
rm -rf %{buildroot}%{_datadir}/doc/packages/%{name}/INSTALL

%files
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_mandir}/man1/%{name}.1.gz
%defattr(0644,root,root,0755)
%{_var}/lib/%{name}
%doc %{_datadir}/doc/packages/%{name}

%package nagios-plugin
Summary:        Nagios plugin based on the logwarn(1) utility
Group:          System/Monitoring
Requires:       bash
Requires:       logwarn >= %{version}
BuildArch:      noarch

%description nagios-plugin
%{name} searches for interesting messages in log files, where ``interest-
ing'' is defined by an user-supplied list of positive and negative (pre-
ceeded with a ``!'') extended regular expressions provided on the command
line.

This package contains the Nagios plugin that is based on %{name}.

%files nagios-plugin
%defattr(0755,root,root,0755)
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/check_logwarn

%changelog
