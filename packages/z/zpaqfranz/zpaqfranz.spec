#
# spec file for package zpaqfranz
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


Name:           zpaqfranz
Version:        59.8
Release:        0
Summary:        A journaling, incremental, deduplicating archiver
License:        MIT AND SUSE-Public-Domain
Group:          Productivity/Archiving/Compression
URL:            https://github.com/fcorbelli/zpaqfranz
Source0:        https://github.com/fcorbelli/zpaqfranz/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++

%description
Swiss army knife for backup and disaster recovery, like 7z or RAR on
steroids,with deduplicated "snapshots" (versions). Conceptually similar to Mac
time machine, but much more efficiently.

%prep
%autosetup

%build
g++ %{optflags} \
  %ifarch %ix86
  -Dunix -DHWSHA2 \
  %elifarch s390x  \
  -Dunix -DNOJIT -DBIG \
  %else
  -Dunix -DNOJIT \
  %endif
  zpaqfranz.cpp -o zpaqfranz -pthread -lstdc++ -lm

%install
install -Dpm 0755 zpaqfranz %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE COPYING
%{_bindir}/%{name}

%changelog
