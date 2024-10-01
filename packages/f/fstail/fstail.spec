#
# spec file for package fstail
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           fstail
Version:        0.1.0
Release:        0
Summary:        Scan a directory for changed files and tail them
License:        MIT
URL:            https://github.com/alexellis/fstail
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.19

# ZODB also contains a fstail binary
Conflicts:      python310-ZODB
Conflicts:      python311-ZODB
Conflicts:      python312-ZODB

%description
fstail - scan a directory for changed files and tail them

When you need to see the output from all changed files within a directory.
Why doesn't tail -f /var/logs/* work?

Unfortunately, tail -f /logs/* may not do what you want it to do. Bash will
expand * to all existing files within /logs/ and then show the extra lines
added to each of them.

It also will not recurse down, any levels deeper than the current directory.
How is fstail different then?

fstail uses the gopkg.in/fsnotify to detect both new files, and existing files
that are changed. It then starts concatenting their contents to the terminal.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/%{name}

%install
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
