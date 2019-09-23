#
# spec file for package unixbench
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           unixbench
Version:        4.0.1
Release:        0
Summary:        A byte Unix benchmarks
License:        GPL-2.0
Group:          System/Benchmark
Url:            http://ftp.tux.org/pub/benchmarks/System/unixbench/
Source0:        %{name}-%{version}.tar.bz2
Source1:        COPYING
Source2:        LICENSE
Source3:        unixbench-rpmlintrc
Patch0:         unixbench-fix_Run_nomake.diff
Patch1:         unixbench-fix_context_x86_64.diff
Patch2:         unixbench-fix_execl_no_such_file.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#BuildArchitectures: noarch
#ExclusiveArch: %ix86
#Authors:
#--------------
#	David C Niemi

%description
The design flaw was that the benchmarks timed a fixed number of loops;
if there were too few loops, the times were too small to be reliable.
Perhaps we could have increased the number of loops and been safe for
another few years (months?).



Authors:
--------
    David C Niemi

%prep 
%setup
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/qa/unixbench
#mkdir -p $RPM_BUILD_ROOT/usr/share/qa/unixbench/src
mkdir -p $RPM_BUILD_ROOT/usr/share/qa/unixbench/testdir
#mkdir -p $RPM_BUILD_ROOT/usr/share/qa/unixbench/old-doc
mkdir -p $RPM_BUILD_ROOT/usr/share/qa/unixbench/tmp
mkdir -p $RPM_BUILD_ROOT/usr/share/qa/unixbench/results
mkdir -p $RPM_BUILD_ROOT/usr/share/qa/unixbench/pgms
install -m 755 ./Run $RPM_BUILD_ROOT/usr/share/qa/unixbench/Run
#install -m 755 ./COPYING $RPM_BUILD_ROOT/usr/share/qa/unixbench/COPYING
#install -m 755 ./LICENSE $RPM_BUILD_ROOT/usr/share/qa/unixbench/LICENSE
install -m 755 ./pgms/* $RPM_BUILD_ROOT/usr/share/qa/unixbench/pgms/.
#install -m 755 ./src/* $RPM_BUILD_ROOT/usr/share/qa/unixbench/src/.
install -m 755 ./testdir/* $RPM_BUILD_ROOT/usr/share/qa/unixbench/testdir/.
#install -m 755 ./old-doc/* $RPM_BUILD_ROOT/usr/share/qa/unixbench/old-doc/.
#install -m 755 ./tmp $RPM_BUILD_ROOT/usr/share/qa/unixbench/tmp/.
#install -m 755 ./results $RPM_BUILD_ROOT/usr/share/qa/unixbench/results/.
#if [ ! -d $RPM_BUILD_ROOT/usr/bin ];
#then
#	mkdir -p $RPM_BUILD_ROOT/usr/bin
#fi
#ln -sf  $RPM_BUILD_ROOT/usr/share/qa/unixbench/Run  $RPM_BUILD_ROOT/usr/bin/unixbench-run 

%clean
rm -rf $RPM_BUILD_ROOT/usr/share/qa/unixbench
#rm -rf $RPM_BUILD_ROOT/usr/share/qa/unixbench-run

%files
%defattr(-,root,root)   
%doc COPYING LICENSE
%dir /usr/share/qa
/usr/share/qa/unixbench
#

%changelog
