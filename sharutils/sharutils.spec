#
# spec file for package sharutils
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           sharutils
Version:        4.15.2
Release:        0
Summary:        GNU shar utilities
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Compression
Url:            http://www.gnu.org/software/sharutils
Source0:        ftp://ftp.gnu.org/gnu/sharutils/sharutils-%{version}.tar.xz
Source1:        ftp://ftp.gnu.org/gnu/sharutils/sharutils-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Patch0:         sharutils-testsuite.diff
Patch1:         sharutils-CVE-2018-1000097-fix_buffer_overflow.patch
Patch2:         gnulib-libio.patch
BuildRequires:  libopenssl-devel
BuildRequires:  mailx
BuildRequires:  xz
Requires(pre):  %{install_info_prereq}
Requires(pre):  coreutils
Recommends:     %{name}-lang = %{version}
Provides:       sharutil = %{version}
Obsoletes:      sharutil < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is the set of GNU shar utilities.

shar makes shell archives out of many files, preparing them for
transmission by electronic mail services.  Use unshar to unpack shell
archives after reception.

uuencode prepares a file for transmission over an electronic channel
which ignores or otherwise mangles the eight bit (high order bit) of
bytes.	uudecode does the converse transformation.

remsync allows for remote synchronization of directory trees, using
e-mail.  This part of sharutils is still alpha.

%{?lang_package}

%prep
%setup -q
%patch0
%patch1
%patch2 -p1
chmod +w src/scripts.x

%build
mkdir -p ../bin
ln -snf /bin/true ../bin/compress
PATH=$PWD/../bin:$PATH
%configure \
	--with-openssl

make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files lang -f %{name}.lang
%defattr(-, root, root)

%files
%defattr(-, root, root)
%doc README NEWS THANKS
%license COPYING
%{_bindir}/*
%{_infodir}/*.gz
%{_mandir}/*/*.gz

%changelog
