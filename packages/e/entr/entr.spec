#
# spec file for package entr
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2016 Daniel Lichtenberger
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


Name:           entr
Version:        5.3
Release:        0
Summary:        A utility for running arbitrary commands when files change
License:        ISC
Group:          Development/Tools/Other
URL:            https://bitbucket.org/eradman/entr
Source:         http://eradman.com/entrproject/code/%{name}-%{version}.tar.gz
Source1:        http://eradman.com/entrproject/code/%{name}-%{version}.tar.gz.asc#/%{name}-%{version}.tar.gz.sig
Source99:       %{name}.keyring

%description
A utility for running arbitrary commands when files change. Uses
inotify(7) to avoid polling.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
# not autotoolsconfigure
./configure
make %{?_smp_mflags}

%install
export PREFIX=%{_prefix}
export MANPREFIX=%{_mandir}
%make_install

%files
%license LICENSE
%doc NEWS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
