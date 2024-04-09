#
# spec file for package bb
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


%define src_ver 1.3rc1
Name:           bb
Version:        1.3~rc1
Release:        0
Summary:        Audio-Visual Demonstration for Text Terminal
License:        GPL-2.0-or-later
Group:          Amusements/Toys/Graphics
URL:            https://aa-project.sourceforge.net/bb/
Source:         https://downloads.sourceforge.net/aa-project/bb-%{src_ver}.tar.gz
Patch0:         bb-1.3.0.diff
Patch1:         bb-1.3.0-timer.diff
Patch2:         warn.patch
Patch3:         undefined-operation.diff
Patch4:         bb-1.3.0-no-minilzo-or-builddates.patch
Patch5:         bb-fix-linking.patch
BuildRequires:  aalib-devel
BuildRequires:  automake
BuildRequires:  libmikmod-devel
BuildRequires:  lzo-devel

%description
BB is a high quality audio-visual demonstration for your text terminal.
It is a portable demo, so you can run it on plenty of operating
systems and DOS.

%prep
%autosetup -p0 -n %{name}-1.3.0

%build
autoreconf -fiv
CFLAGS="%{optflags} -DDATADIR='\"%{_datadir}/bb/\"'" \
%configure
%make_build

%install
%make_install

%files
%doc README
%{_bindir}/bb
%{_mandir}/man1/bb.1%{?ext_man}
%dir %{_datadir}/bb
%{_datadir}/bb/*.s3m

%changelog
