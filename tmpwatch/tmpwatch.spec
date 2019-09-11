#
# spec file for package tmpwatch
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


Name:           tmpwatch
Summary:        Watches file system activity, such as /tmp files
License:        GPL-2.0-only
Group:          Productivity/Security
Version:        2.11
Release:        0
Url:            https://pagure.io/tmpwatch
#Source0:        https://pagure.io/tmpwatch/archive/%{name}-%{version}/%{name}-%{name}-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.daily
BuildRequires:  psmisc
Requires:       cron
Requires:       psmisc

%description
The tmpwatch utility recursively searches through specified directories
and removes files which have not been accessed in a specified period of
time. tmpwatch is normally used to clean up directories which are used
for temporarily holding files (for example, /tmp).

There are multiple tools called "tmpwatch", this package contains the
Fedora/Red Hat version previously available at
https://fedorahosted.org/tmpwatch and now hosted at
https://pagure.io/tmpwatch

%prep
%setup -q

%build
%configure
%{__make}

%install
%makeinstall
%{__install} -D -m755 %{S:1} %{buildroot}%{_sysconfdir}/cron.daily/%{name}

%files
%defattr(-,root,root)
%doc ChangeLog NEWS README COPYING
%config(noreplace) %{_sysconfdir}/cron.daily/%{name}
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
