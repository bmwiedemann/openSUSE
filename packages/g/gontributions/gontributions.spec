#
# spec file for package gontributions
#
# Copyright (c) 2023 SUSE LLC
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


Name:           gontributions
Version:        0.7.1
Release:        0
Summary:        Open source contributions lister
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/jubalh/gontributions
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
%ifarch x86_64
BuildRequires:  pandoc
%endif

%description
Open source contributions lister.

%prep
%setup -q -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie
%ifarch x86_64
pandoc -s -t man "doc/%{name}.1.md" -o "doc/%{name}.1"
%endif

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
%ifarch x86_64
install -d %{buildroot}%{_mandir}/man1
install -D -m0644 doc/%{name}.1 %{buildroot}%{_mandir}/man1
%endif

%files
%{_bindir}/%{name}
%ifarch x86_64
%{_mandir}/man1/%{name}.1%{?ext_man}
%endif

%changelog
