#
# spec file for package etc-update
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           etc-update
Version:        2.3.31
Release:        0
Summary:        Configuration file update handler
License:        GPL-2.0-only
Group:          System/Base
URL:            https://wiki.gentoo.org/wiki/Handbook:X86/Portage/Tools#etc-update
Source0:        https://github.com/gentoo/portage/archive/portage-%{version}.tar.gz
Patch0:         etc-update-opensuse.patch
Requires:       bash
BuildArch:      noarch

%description
etc-update  is  supposed  to be run after merging a new package to see if there
are updates to the configuration files.  If a new configuration file will
override an old one, etc-update will prompt the user for a decision.

etc-update will check all directories specified on the command line.  If no
paths are given, then the CONFIG_PROTECT variable will be  used.   All  config
files  found  in  CONFIG_PRO‐TECT_MASK will automatically be updated for you by
etc-update.

%prep
%setup -q -n portage-portage-%{version}
%patch0 -p1

%build
:

%install
install -D -m 0755 bin/%{name} %{buildroot}/%{_sbindir}/%{name}
install -D -m 0644 cnf/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf
sed -i -e "s/VERSION/%{version}/" man/%{name}.1
install -D -m 0644 man/%{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/%{name}*

%changelog
