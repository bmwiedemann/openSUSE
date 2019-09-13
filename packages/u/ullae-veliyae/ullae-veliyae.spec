#
# spec file for package ullae-veliyae (Version 1.0)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           ullae-veliyae
# List of additional build dependencies
BuildRequires:  ant java-devel
Version:        1.0
Release:        2
License:        GPL-2.0
Source:         ullae-veliyae-1.0.tar
Group:          System/Monitoring
Summary:        UV - Realtime graph of I/O per process
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
UV - Realtime graph of I/O per process.

Signed-off-by: Nikanth Karthikesan <knikanth@suse.de>
Sponsored by Novell, during openSUSE Hackweek, 20-24 July, 2009.

Ullae-veliyae are Tamil words for In-Out.
For Input/Output, it would be Ulleedu/Veliyeedu.

WARNING: Use this tool at your own risk, data accuracy not guaranteed!!

%prep
%setup -q

%build
%ant jar

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
# jars
%__install -d -m 0755 "%{buildroot}%{_datadir}/%{name}"
%__install -m 0644 uv.jar "%{buildroot}%{_datadir}/%{name}/"
# startscript
%__install -d -m 0755 "%{buildroot}%{_bindir}"
cat > "%{buildroot}%{_bindir}/%{name}" << EOF
#!/bin/sh
exec java -jar %{_datadir}/%{name}/uv.jar
EOF
%__chmod 0755 "%{buildroot}%{_bindir}/%{name}"
# Write a proper %%files section and remove these two commands and
# the '-f filelist' option to %%files
echo '%%defattr(-,root,root)' >filelist
find %buildroot -type f -printf '/%%P*\n' >>filelist

%clean
rm -rf %buildroot

%files -f filelist
%defattr(-,root,root)
%doc COPYING 
# AUTHORS CHANGES LICENSE README
%{_bindir}/%{name}
%{_datadir}/%{name}
# This is a place for a proper filelist:
# /usr/bin/ullae-veliyae
# You can also use shell wildcards:
# /usr/share/ullae-veliyae/*
# This installs documentation files from the top build directory
# into /usr/share/doc/...
# %doc README COPYING
# The advantage of using a real filelist instead of the '-f filelist' trick is
# that rpmbuild will detect if the install section forgets to install
# something that is listed here

%changelog
