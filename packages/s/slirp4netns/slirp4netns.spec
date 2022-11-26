#
# spec file for package slirp4netns
#
# Copyright (c) 2022 SUSE LLC
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


Name:           slirp4netns
Version:        1.2.0
Release:        0
Summary:        User-mode networking for unprivileged network namespaces
License:        GPL-2.0-only AND MIT AND BSD-2-Clause
Group:          System/Management
URL:            https://github.com/rootless-containers/slirp4netns
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  go-go-md2man
BuildRequires:  libcap-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libslirp-devel

%description
slirp for network namespaces, without copying buffers across the namespaces.

%prep
%autosetup

%build
./autogen.sh
%configure
%make_build all generate-man

%install
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
install -d %{buildroot}/%{_mandir}/man1
install -m 0644 %{name}.1 %{buildroot}/%{_mandir}/man1

%files
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1%{?ext_man}

%changelog
