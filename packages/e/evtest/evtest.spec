#
# spec file for package evtest
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           evtest
Version:        1.33
Release:        0
Summary:        Input device event monitor and query tool
License:        GPL-2.0+
Group:          Hardware/Other
Url:            http://cgit.freedesktop.org/evtest
# Full url is http://cgit.freedesktop.org/evtest/snapshot/%%{name}-%%{version}.tar.gz
# Every time source package is downloaded, there is different timestamp in the gzip header.
# This makes the factory-auto decline SR, because of "Source URLs are not valid".
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libxslt-tools
BuildRequires:  xmlto

# splitted in 13.2
Provides:       input-utils:/usr/bin/evtest = 2007.06.22
Obsoletes:      input-utils <= 2007.06.22

%description
evtest displays information on the input device specified on the command line,
including all the events supported by the device. It then monitors the device
and displays all the events layer events generated.

%prep
%setup -q

%build
autoreconf --install
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/evtest
%doc %{_mandir}/man1/evtest*

%changelog
