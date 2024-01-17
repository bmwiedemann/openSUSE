#
# spec file for package paperkey
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           paperkey
Version:        1.6
Release:        0
Summary:        Tool to backup GnuPG secret keys on paper
License:        GPL-3.0-or-later
Group:          Productivity/Security
URL:            http://www.jabberwocky.com/software/paperkey
Source0:        http://www.jabberwocky.com/software/%{name}/%{name}-%{version}.tar.gz
Source1:        http://www.jabberwocky.com/software/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring

%description
A reasonable way to achieve a long term backup of OpenPGP (GnuPG, PGP, etc)
keys is to print them out on paper. Paper and ink have amazingly long retention
qualities - far longer than the magnetic or optical means that are generally
used to back up computer data.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%check
make %{?_smp_mflags} check

%files
%license COPYING
%doc NEWS README AUTHORS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
