#
# spec file for package simh
#
# Copyright (c) 2023 SUSE LLC
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


Name:           simh
BuildRequires:  dos2unix
BuildRequires:  libpcap-devel
BuildRequires:  libvdeplug-devel
BuildRequires:  unzip
URL:            http://simh.trailing-edge.com/
Version:        3.12_4
Release:        0
Summary:        A collection of simulators of historically significant data processing systems
License:        BSD-3-Clause
Group:          System/Emulators/Other
Source:         http://simh.trailing-edge.com/sources/simhv312-4.zip
Patch1:         0001-declare-don-t-define-uc15_memsize-in-include-file.patch
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
%setup -c -T
unzip -a %SOURCE0
cd sim
%patch1 -p1

%build
cd sim
mkdir -p BIN
make
for i in $(cd BIN; ls * | grep -v buildtools) ; do
	mv -v BIN/${i} BIN/simh-${i}
done

cp sim_rev.h CHANGELOG_sim_rev_h.txt

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 sim/BIN/simh-* $RPM_BUILD_ROOT/usr/bin
chmod 644 sim/*.txt sim/SDS/*.txt sim/Interdata/*.txt
for i in sim/*.txt sim/*/*.txt ; do
  dos2unix ${i}
done

%files
%defattr(-,root,root)
%doc sim/*.txt sim/*/*txt
%{_bindir}/simh-*

%changelog
