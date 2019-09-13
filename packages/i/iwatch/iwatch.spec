#
# spec file for package iwatch
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


Name:           iwatch
Version:        0.2.2
Release:        0
Summary:        Realtime filesystem monitoring program
License:        GPL-2.0+
Group:          Productivity/Security
Url:            http://iwatch.sourceforge.net
Source0:        http://sourceforge.net/projects/iwatch/files/iwatch/%{version}/iwatch-%{version}.tgz
Requires:       perl-Event
Requires:       perl-Linux-Inotify2
Requires:       perl-Mail-Sendmail
Requires:       perl-XML-LibXML
Requires:       perl-XML-SimpleObject-LibXML
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
iWatch monitor the filesystem's integrity in realtime and will send
alarm immediately to the system administrator when there is any changes
in the monitored filesystem. iWatch is written in Perl and based on
inotify, a file change notification system, a kernel feature that
allows applications to request the monitoring of a set of files against
a list of events.

Currently it can:

- run in command line mode as well as in daemon mode

- using an easy xml configuration file

- can watch directory recursively and watch new created directory

- can have a list of exceptions

- can use regex to compare the file/directory name

- can execute command if an event occures

- send email

- syslog

- print time stamp

%prep
%setup -q -n %{name}

%build

%install
install -d %{buildroot}%{_sysconfdir}
install -p iwatch.xml %{buildroot}%{_sysconfdir}/iwatch.xml
install -p iwatch.dtd %{buildroot}%{_sysconfdir}/iwatch.dtd
install -d %{buildroot}%{_bindir}
install -p iwatch %{buildroot}%{_bindir}/iwatch

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README iwatch.xml.example
%attr(0644,root,root) %config %{_sysconfdir}/iwatch.xml
%attr(0644,root,root) %config %{_sysconfdir}/iwatch.dtd
%{_bindir}/iwatch

%changelog
