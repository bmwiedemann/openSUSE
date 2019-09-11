#
# spec file for package recidivm
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


Name:           recidivm
Version:        0.2
Release:        0
Summary:        Tool for estimating peak virtual memory use
License:        MIT
Group:          Development/Tools/Other
Url:            http://jwilk.net/software/recidivm
Source:         https://github.com/jwilk/recidivm/releases/download/%{version}/recidivm-%{version}.tar.gz
Source1:        https://github.com/jwilk/recidivm/releases/download/%{version}/recidivm-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  gcc

%description
recidivm estimates the target program's peak virtual memory use by running it multiple times with different memory limits.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

%check
make %{?_smp_mflags} test

%files
%doc doc/changelog
%license doc/LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
