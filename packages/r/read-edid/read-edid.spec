#
# spec file for package read-edid
#
# Copyright (c) 2024 SUSE LLC
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


Name:           read-edid
Version:        3.0.2
Release:        0
Summary:        Tool for reading EDID information
License:        BSD-3-Clause
Group:          System/X11/Utilities
URL:            http://polypux.org/projects/read-edid/
Source0:        http://polypux.org/projects/read-edid/read-edid-%{version}.tar.gz
Source1:        read-edid-wrapper
Patch0:         read-edid-fix-cmakelists.patch
Patch1:         read-edid-code-cleanup.patch
Patch2:         read-edid-fix-gcc10-build.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  sed
Recommends:     grep
Recommends:     kmod-compat
ExclusiveArch:  %{ix86} x86_64

%description
A pair of tools for reading the Extended Display Identification Data
(EDID) from a monitor. Assuming the video card supports the standard
read commands, the utilities should work with most monitors made
since 1996. 256-byte EDIDs are not supported, though.

- get-edid, which gets the raw edid information from the monitor.
- parse-edid, which turns the raw binary information into an
  xorg-compatible monitor section.

%prep
%setup -q
%autopatch -p1

%build
%cmake -DCLASSICBUILD=OFF
make %{?_smp_mflags}

%install
%cmake_install
mkdir -p %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/get-edid %{buildroot}%{_libexecdir}
install -m 755 %{SOURCE1} %{buildroot}%{_bindir}/get-edid
sed -i -e "s|@LIBEXECDIR@|%{_libexecdir}|" %{buildroot}%{_bindir}/get-edid
rm -f %{buildroot}%{_docdir}/read-edid/LICENSE

%files
%license LICENSE
%doc AUTHORS ChangeLog README
%{_bindir}/get-edid
%{_bindir}/parse-edid
%{_libexecdir}/get-edid
%{_mandir}/man1/get-edid.1%{?ext_man}

%changelog
