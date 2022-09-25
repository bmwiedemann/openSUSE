#
# spec file for package inchi
#
# Copyright (c) 2022 SUSE LLC
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


%define abiver  1
%define urlver  106
Name:           inchi
Version:        1.06
Release:        0
Summary:        The IUPAC International Chemical Identifier
License:        LGPL-2.0-or-later
URL:            https://www.inchi-trust.org
Source0:        https://www.inchi-trust.org/download/%{urlver}/INCHI-1-SRC.zip
Source1:        https://www.inchi-trust.org/download/%{urlver}/INCHI-1-DOC.zip
Source2:        https://www.inchi-trust.org/download/%{urlver}/INCHI-1-TEST.zip
# PATCH-FIX-UPSTREAM inchi-1.06-optflags.patch -- Pass optflags to compiler and don't require gcc-c++ (picked from Fedora)
Patch0:         inchi-1.06-optflags.patch
# PATCH-FIX-UPSTREAM inchi-1.06-big-endian.patch -- Fix tests on big-endian architectures (rh#1930943)
Patch1:         inchi-1.06-big-endian.patch
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  unzip
Suggests:       inchi-doc

%description
The IUPAC International Chemical Identifier (InChI) is a non-proprietary
identifier for chemical substances that can be used in printed and
electronic data sources thus enabling easier linking of diverse data
compilations. It was developed under IUPAC Project 2000-025-1-800 during
the period 2000-2004. Details of the project and the history of its
progress are available from the project web site.

This package contains the command line conversion utility.

%package -n libinchi%{abiver}
Summary:        The IUPAC International Chemical Identifier library

%description -n libinchi%{abiver}
The IUPAC International Chemical Identifier (InChI) is a non-proprietary
identifier for chemical substances that can be used in printed and
electronic data sources thus enabling easier linking of diverse data
compilations. It was developed under IUPAC Project 2000-025-1-800 during
the period 2000-2004. Details of the project and the history of its
progress are available from the project web site.

This package contains the InChi shared library.

%package devel
Summary:        Development headers for the InChI library
Requires:       libinchi%{abiver} = %{version}
Suggests:       inchi-doc
# openbabel-devel used to ship the headers of its bundled inchi
Conflicts:      openbabel-devel <= 2.4.1

%description devel
This package contains the development files for the InChI library.

%package doc
Summary:        Documentation for the InChI library
BuildArch:      noarch

%description doc
This package contains the user documentation for the InChI software
and InChI library API reference for developers.

%prep
# Extract Source0 then cd into extracted directory then extract Source1 then extract Source2
%setup -q -n INCHI-1-SRC -a 1 -a 2
%autopatch -p1
dos2unix -k readme.txt

# Remove files from INCHI-1-DOC that are already present in ICHI-1-SRC so that they are not listed twice
rm -v INCHI-1-DOC/{LICENCE.pdf,readme.txt}

# Uncompress test datasets and reference test outputs
cd INCHI-1-TEST/test
unzip -d reference -qq -a test-results.zip
unzip -qq -a test-datasets.zip
dos2unix -k reference/*.inc *.sdf

# Test scripts are Windows batch scripts; turn them into shell scripts
for test_script in inchify_{InChI_TestSet,zzp} ; do
    sed -e 's,REM,#,g'                                         \
        -e 's,/,-,g'                                           \
        -e 's,NUL,/dev/null,g'                                 \
        -e 's,inchi-1.exe,../../INCHI_EXE/bin/Linux/inchi-1,g' \
        ${test_script}.cmd > ${test_script}.sh
    dos2unix ${test_script}.sh
done

%build
export OPTFLAGS="%{optflags}"
%make_build -C INCHI_API/demos/inchi_main/gcc
%make_build -C INCHI_EXE/inchi-1/gcc

%install
# Install binary
install -pm 755 INCHI_EXE/bin/Linux/inchi-1 -D -t %{buildroot}%{_bindir}

# Install shared library and do the appropriate links
install -p INCHI_API/bin/Linux/libinchi.so.%{abiver}.*.* -D -t %{buildroot}%{_libdir}
ln -s $(basename %{buildroot}%{_libdir}/libinchi.so.%{abiver}.*.*) %{buildroot}%{_libdir}/libinchi.so.%{abiver}
ln -s libinchi.so.%{abiver} %{buildroot}%{_libdir}/libinchi.so

# Install the headers
install -pm644 INCHI_BASE/src/{ichisize,inchi_api,ixa}.h -D -t %{buildroot}%{_includedir}/inchi

%post -n libinchi%{abiver} -p /sbin/ldconfig
%postun -n libinchi%{abiver} -p /sbin/ldconfig

%check
# Run tests
cd INCHI-1-TEST/test
for test_script in inchify_{InChI_TestSet,zzp} ; do
    sh ./${test_script}.sh
done

# Compare test outputs with reference test outputs
for test_output in its-*.inc zzp-*.inc ; do
    diff -u reference/${test_output} ${test_output}
done

%files
%license LICENCE.pdf
%{_bindir}/inchi-1

%files -n libinchi%{abiver}
%license LICENCE.pdf
%{_libdir}/libinchi.so.%{abiver}*

%files devel
%license LICENCE.pdf
%{_includedir}/inchi
%{_libdir}/libinchi.so

%files doc
%license LICENCE.pdf
%doc readme.txt INCHI-1-DOC/*

%changelog
