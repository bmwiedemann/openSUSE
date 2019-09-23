#
# spec file for package simh
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


Name:           simh
BuildRequires:  libpcap-devel
BuildRequires:  unzip
Url:            http://simh.trailing-edge.com/
Version:        3.9_0
Release:        0
Summary:        A collection of simulators of historically significant data processing systems
License:        BSD-3-Clause
Group:          System/Emulators/Other
Source:         http://simh.trailing-edge.com/sources/simhv39-0.zip
Source1:        uv7swre.tar.bz2
# Preparation of interim patches...
# DFORMAT=$(date +"%Y%m%d")
# export DFORMAT
# wget -q -nH -m -np http://simh.trailing-edge.com/interim/ &&  mv interim/ interim-${DFORMAT} && mv interim-${DFORMAT} && rm interim-${DFORMAT}/index*
# tar zvcf interim-${DFORMAT}.tar.gz interim-${DFORMAT}
Source2:        interim-20130422.tar.gz
# PATCH-FIX-UPSTREAM -- obsolete not used any more...
Patch0:         simhv37-3.dif
# PATCH-FIX-UPSTREAM  interim-20130422.patch fix for interim source as it has typo error 
Patch1:         interim-20130422.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  help2man

%description
This package contains simulators of the following systems:
Data General Nova
Data General Eclipse
Digital Equipment Corporation PDP-1
Digital Equipment Corporation PDP-4
Digital Equipment Corporation PDP-7
Digital Equipment Corporation PDP-8
Digital Equipment Corporation PDP-9
Digital Equipment Corporation PDP-10
Digital Equipment Corporation PDP-11
Digital Equipment Corporation PDP-15
Digital Equipment Corporation PDP-18B
IBM 1401
IBM System 3
Hewlett-Packard HP 2100
Honeywell H316
MITS Altair 8800

A disk image with UNIX V7 for the PDP-11 is included, instructions on
how to make it work can be found in the file
/usr/share/doc/packages/simh/simh_swre.txt in chapter 2.1.3.

A selection of software for other systems can be found at The Computer
History Simulation Project at http://simh.trailing-edge.com/


%prep
%setup -c -T -a 1
unzip -a %SOURCE0
tar zxvf %SOURCE2
# obsolete patch
#%%patch
%patch1
#for i in `find -name "*.[ch]"` makefile
#do
#	recode ibmpc..lat1 $i || true
#done

# replace files with interim fixed ones...
for i in interim-20130422/* ; do
	FLOCATION=$(find . -name $(basename $i)|grep -v interim)
	cp -v $i $FLOCATION
done

%build
mkdir -p BIN
USE_NETWORK=1 make
for i in $(cd BIN; ls *) ; do 
	mv -v BIN/${i} BIN/simh-${i}
done

cp sim_rev.h CHANGELOG_sim_rev_h.txt

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 BIN/* $RPM_BUILD_ROOT/usr/bin
chmod 644 *.txt SDS/*.txt Interdata/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc *.txt Disks */*txt
%{_bindir}/simh-altair
%{_bindir}/simh-altairz80
%{_bindir}/simh-eclipse
%{_bindir}/simh-gri
%{_bindir}/simh-h316
%{_bindir}/simh-hp2100
%{_bindir}/simh-i1401
%{_bindir}/simh-i1620
%{_bindir}/simh-i7094
%{_bindir}/simh-ibm1130
%{_bindir}/simh-id16
%{_bindir}/simh-id32
%{_bindir}/simh-lgp
%{_bindir}/simh-nova
%{_bindir}/simh-pdp1
%{_bindir}/simh-pdp10
%{_bindir}/simh-pdp11
%{_bindir}/simh-pdp15
%{_bindir}/simh-pdp4
%{_bindir}/simh-pdp7
%{_bindir}/simh-pdp8
%{_bindir}/simh-pdp9
%{_bindir}/simh-s3
%{_bindir}/simh-sds
%{_bindir}/simh-vax
%{_bindir}/simh-vax780
%{_bindir}/simh-eclipse
%{_bindir}/simh-swtp6800mp-a
%{_bindir}/simh-swtp6800mp-a2

%changelog
