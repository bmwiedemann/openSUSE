#
# spec file for package jigdo
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


Name:           jigdo
Version:        0.7.3
Release:        0
Summary:        Jigsaw Download
License:        GPL-2.0
Group:          Productivity/Networking/Other
Url:            http://atterer.org/jigdo/
Source:         %{name}-%{version}.tar.bz2
Patch1:         jigdo-0.7.3-makefile-do-not-strip.patch
Patch2:         jigdo-0.7.3-makefile-paths.patch
Patch3:         jigdo-0.7.3-add-includes.patch
Patch4:         jigdo-0.7.3-gcc7.patch
Patch5:         jigdo-0.7.1-debug.patch
BuildRequires:  gcc-c++
BuildRequires:  libbz2-devel
BuildRequires:  zlib-devel
Requires:       wget
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Jigsaw Download, or jigdo, is an intelligent tool that can be used on
the pieces of any chopped-up big file to create a special template file
that makes reassembly of the file very easy for users who only have the
pieces. What makes jigdo special is that there are no restrictions on
what offsets or sizes the individual pieces have in the original big
image. This makes the program very well suited for distributing CD or
DVD images (or large zip or tar archives) because you can put the files
of the CD on an FTP server--when jigdo is presented the files along
with the template you generated, it is able to recreate the CD image.

%prep
%setup -q
%patch1
%patch2
%patch3
%patch4 -p1
%patch5 -p1

%build
%configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--without-libdb \
	--with-gui=no
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%defattr(-, root, root)
%doc changelog COPYING README THANKS doc/*.html doc/*.txt
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/%{name}

%changelog
