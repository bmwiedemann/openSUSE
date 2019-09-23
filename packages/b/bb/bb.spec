#
# spec file for package bb
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


Name:           bb
BuildRequires:  aalib-devel
BuildRequires:  automake
BuildRequires:  libmikmod-devel
BuildRequires:  lzo-devel
Url:            http://aa-project.sourceforge.net/bb/
Summary:        Audio-Visual Demonstration for Text Terminal
License:        GPL-2.0+
Group:          Amusements/Toys/Graphics
Version:        1.3
Release:        0
Source:         bb-1.3rc1.tar.bz2
Patch:          bb-1.3.0.diff
Patch1:         bb-1.3.0-timer.diff
Patch2:         warn.patch
Patch3:         undefined-operation.diff
Patch4:         bb-1.3.0-no-minilzo-or-builddates.patch
Patch5:         bb-fix-linking.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
BB is a high quality audio-visual demonstration for your text terminal.
 It is a portable demo, so you can run it on plenty of operating
systems and DOS.

%prep
%setup -q -n %{name}-1.3.0
%patch
%patch1
%patch2
%patch3
%patch4
%patch5

%build
autoreconf -fiv
CFLAGS="$RPM_OPT_FLAGS -DDATADIR='\"/usr/share/bb/\"'" \
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/usr/bin/bb
%{_mandir}/man1/bb.1.gz
%dir /usr/share/bb
/usr/share/bb/*.s3m

%changelog
