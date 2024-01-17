#
# spec file for package rpmorphan
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rpmorphan
Version:        1.19
Release:        0
Summary:        Tool to list orphaned RPM packages
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            http://rpmorphan.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Requires:       rpm
Recommends:     logrotate
Recommends:     perl-Curses-UI
Recommends:     perl-RPM2
Recommends:     perl-Tk
Recommends:     perl-URPM
BuildArch:      noarch

%description
This program finds "orphaned" packages on the system. It determines
which packages have no other packages depending on their
installation, and shows a list of these packages.

%prep
%setup -q

# Fix rpmlint warning "non-executable-script"
sed -i '/^#\!/d' locale/en/rpmorphan_trans.pl
sed -i '/^#\!/d' locale/fr_FR/rpmorphan_trans.pl
sed -i '/^#\!/d' rpmorphan-curses-lib.pl
sed -i '/^#\!/d' rpmorphan-lib.pl
sed -i '/^#\!/d' rpmorphan-tk-lib.pl
# Fix rpmlint error "env-script-interpreter"
sed -i 's/^#\!\/usr\/bin\/env\ perl/#\!\/usr\/bin\/perl/' *.pl

%build

%install
%make_install

%files
%doc Authors Changelog NEWS Readme Readme.fr Todo rpmorphan.lsm
%license COPYING
%config(noreplace) %{_sysconfdir}/logrotate.d/rpmorphan
%config(noreplace) %{_sysconfdir}/rpmorphanrc
%{_bindir}/grpmorphan
%{_bindir}/rpmdep
%{_bindir}/rpmdep.pl
%{_bindir}/rpmduplicates
%{_bindir}/rpmduplicates.pl
%{_bindir}/rpmextra
%{_bindir}/rpmextra.pl
%{_bindir}/rpmorphan
%{_bindir}/rpmorphan.pl
%{_bindir}/rpmusage
%{_bindir}/rpmusage.pl
%{_mandir}/man1/rpmdep.1%{?ext_man}
%{_mandir}/man1/rpmduplicates.1%{?ext_man}
%{_mandir}/man1/rpmextra.1%{?ext_man}
%{_mandir}/man1/rpmorphan.1%{?ext_man}
%{_mandir}/man1/rpmusage.1%{?ext_man}
%{_prefix}/lib/rpmorphan/
%dir %{_localstatedir}/lib/rpmorphan
%{_localstatedir}/lib/rpmorphan/keep
%ghost %config(noreplace) %{_localstatedir}/log/rpmorphan.log

%changelog
