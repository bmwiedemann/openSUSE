#
# spec file for package pwgen
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


Name:           pwgen
Version:        2.08
Release:        0
Summary:        Password generator
License:        GPL-2.0+
Group:          Productivity/Security
Url:            http://sourceforge.net/projects/pwgen/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Patch0:         pwgen-2.06-fdleaks.patch
BuildRequires:  autoconf
BuildRequires:  automake

%description
pwgen generates random, meaningless but pronounceable and thus easy to
remember passwords. The also contained makepasswd gives even more
options which are more aimed at security.

%prep
%setup -q
%patch0

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%{_mandir}/man1/%{name}.1%{ext_man}
%{_bindir}/%{name}

%changelog
