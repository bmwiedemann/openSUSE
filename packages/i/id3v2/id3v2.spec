#
# spec file for package id3v2
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           id3v2
Version:        0.1.12
Release:        0
Summary:        A Command Line Editor for ID3 V2 tags
License:        LGPL-2.1+
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://id3v2.sourceforge.net/
Source0:        https://sourceforge.net/projects/id3v2/files/id3v2/%{version}/id3v2-%{version}.tar.gz
Patch0:         id3v2-0.1.11.diff
Patch1:         %{name}-%{version}-bogus-linkage.patch
BuildRequires:  gcc-c++
BuildRequires:  groff
BuildRequires:  id3lib-devel

%description
ID3 tags are found in MP3 files. They can store information about what band
recorded the song, the song name, and more. ID3-V1 tags are seriously
deficient as to the kind of and length of information that they can store.
This is a tool for editing ID3-V2 tags in Linux.

%prep
%setup -q
%patch0
%patch1

%build
rm -f id3v2 create_map core *.o
export CXXFLAGS="%{optflags}"
export LDFLAGS="-L%{_libdir}"
make %{?_smp_mflags}

%install
install -Dp id3v2 \
	%{buildroot}%{_bindir}/id3v2
mkdir -p %{buildroot}%{_mandir}/man1
nroff -man id3v2.1 > %{buildroot}%{_mandir}/man1/id3v2.1

%files
%doc README COPYING
%{_bindir}/id3v2
%{_mandir}/man1/id3v2.1%{ext_man}

%changelog
