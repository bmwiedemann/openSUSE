#
# spec file for package segv_handler
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           segv_handler
Version:        0.0.1
Release:        0
Url:            http://samba.org/ftp/unpacked/junkcode/segv_handler/
Summary:        System wide segv handler to produces a backtrace
License:        GPL-2.0+
Group:          Development/Tools/Other
Source:         http://samba.org/ftp/unpacked/junkcode/segv_handler/backtrace
Source1:        http://samba.org/ftp/unpacked/junkcode/segv_handler/Makefile
Source2:        http://samba.org/ftp/unpacked/junkcode/segv_handler/README
Source3:        http://samba.org/ftp/unpacked/junkcode/segv_handler/segv_handler.c
Source4:        http://samba.org/ftp/unpacked/junkcode/segv_handler/testprog.c
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a useful utility for installing a system-wide segv handler that
produces a backtrace on any program that gets a SEGV signal. It is
installed as a preload, so you don't need to modify the target
programs.



Authors:
--------
    Andrew Tridgell <tridge at Samba dot org>

%prep
cp -p %{S:1} %{S:2} %{S:3} %{S:4} ${RPM_BUILD_DIR}

%build
export CFLAGS=$RPM_OPT_FLAGS
make
rm -f /tmp/segv_testprog.*
%ifnarch %arm
make test
%endif

%install
mkdir -p \
	${RPM_BUILD_ROOT}/%{_bindir} \
	${RPM_BUILD_ROOT}/%{_libdir} \
	${RPM_BUILD_ROOT}/%{_docdir}/%{name}
install -m 0755 %{S:0} ${RPM_BUILD_ROOT}/%{_bindir}
install -m 0755 ${RPM_BUILD_DIR}/segv_handler.so ${RPM_BUILD_ROOT}/%{_libdir}

%files
%defattr(-,root,root)
%{_bindir}/backtrace
%{_libdir}/segv_handler.so
%doc README

%changelog
