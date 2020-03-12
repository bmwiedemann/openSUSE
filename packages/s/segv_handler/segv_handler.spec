#
# spec file for package segv_handler
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


Name:           segv_handler
Version:        0.0.2
Release:        0
Summary:        System wide segv handler to produces a backtrace
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://samba.org/ftp/unpacked/junkcode/segv_handler/
Source:         https://samba.org/ftp/unpacked/junkcode/segv_handler/backtrace
Source1:        https://samba.org/ftp/unpacked/junkcode/segv_handler/Makefile
Source2:        https://samba.org/ftp/unpacked/junkcode/segv_handler/README
Source3:        https://samba.org/ftp/unpacked/junkcode/segv_handler/segv_handler.c
Source4:        https://samba.org/ftp/unpacked/junkcode/segv_handler/testprog.c

%description
This is a useful utility for installing a system-wide segv handler that
produces a backtrace on any program that gets a SEGV signal. It is
installed as a preload, so you don't need to modify the target
programs.

%prep
export CFLAGS="%{optflags}"
%setup -q -c -T
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} ./

%build
%make_build

%install
install -Dpm 0755 %{SOURCE0} \
  %{buildroot}%{_bindir}/backtrace
install -Dpm 0755 segv_handler.so \
  %{buildroot}%{_libdir}/segv_handler.so

%files
%doc README
%{_bindir}/backtrace
%{_libdir}/segv_handler.so

%changelog
