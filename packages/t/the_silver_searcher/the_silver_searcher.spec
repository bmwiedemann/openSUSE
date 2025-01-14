#
# spec file for package the_silver_searcher
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


Name:           the_silver_searcher
Version:        2.2.0
Release:        0
Summary:        A code-searching tool similar to ack, but faster
License:        Apache-2.0
Group:          Productivity/File utilities
URL:            https://github.com/ggreer/the_silver_searcher
Source:         http://geoff.greer.fm/ag/releases/%{name}-%{version}.tar.gz
Source2:        http://geoff.greer.fm/ag/releases/%{name}-%{version}.tar.gz.asc
Source3:        %{name}.keyring
Source4:        %{name}.changes
# PATCH-FIX-UPSTREAM the_silver_searcher-2.2.0-portabilityfixes.patch gh#ggreer/the_silver_searcher#1377 -- Fix multiple global symbols definitions
Patch0:         the_silver_searcher-2.2.0-portabilityfixes.patch
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(zlib)

%description
A code searching tool similar to ack, with a focus on speed.

%prep
%autosetup -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}/%{_datadir}/bash-completion/completions/
mv -v %{buildroot}%{_datadir}/%{name}/completions/ag.bashcomp.sh %{buildroot}/%{_datadir}/bash-completion/completions/%{name}

%files
%license LICENSE
%doc NOTICE README.md
%{_bindir}/ag
%{_mandir}/man1/ag.1%{?ext_man}
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_the_silver_searcher

%changelog
