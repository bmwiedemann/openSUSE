#
# spec file for package UEFITool
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           UEFITool
Version:        20180624
Release:        0
Summary:        Tools to inspect and work on UEFI BIOSes
License:        BSD-2-Clause
Group:          Development/Tools/Other
URL:            https://github.com/LongSoft/UEFITool
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
UEFITool is a C++/Qt program for parsing, extracting and
modifying UEFI firmware images. It supports parsing of full BIOS images
starting with the flash descriptor or any binary files containing UEFI
volumes.

%prep
%setup -q

%build
%qmake5
%make_jobs
for i in UEFIPatch UEFIReplace; do
  pushd $i
    %qmake5
    %make_jobs
  popd
done

%install
install -Dpm 0755 UEFITool \
  %{buildroot}/%{_bindir}/UEFITool
for i in UEFIPatch UEFIReplace; do
  pushd $i
    install -Dpm 0755 $i %{buildroot}/%{_bindir}/$i
  popd
done

%files
%license LICENSE.md
%doc README.rst
%{_bindir}/UEFITool
%{_bindir}/UEFIPatch
%{_bindir}/UEFIReplace

%changelog
