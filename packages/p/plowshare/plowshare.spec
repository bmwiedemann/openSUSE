#
# spec file for package plowshare
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


Name:           plowshare
Version:        2.1.7
Release:        0
Summary:        Download and upload files from file-sharing websites
License:        GPL-3.0+
Group:          Productivity/Networking/Web/Utilities
Url:            https://github.com/mcrapet/plowshare
Source0:        https://github.com/mcrapet/plowshare/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         reproducible.patch
BuildRequires:  bash >= 4.1
BuildRequires:  curl >= 7.24
Requires:       bash >= 4.1
Requires:       curl >= 7.24
Requires:       perl
Requires:       perl(HTML::Entities)
Recommends:     bash-completion
Provides:       %{name}-bash-completion = %{version}
Obsoletes:      %{name}-bash-completion < %{version}
BuildArch:      noarch

%description
plowshare is a command-line (CLI) download/upload tool for popular file
sharing websites (aka file hosting provider or One-Click hoster). With
plowshare, you will be able to download or upload files and manage remote
folders and link deletion. It runs on Linux/BSD/Unix operating system. The
basic concept is that files can be downloaded and uploaded though command
line as easily as wget (or curl).

%prep
%setup -q
%patch0 -p1

%build

%install
%make_install
install -D -p -m 0644  scripts/%{name}.completion  %{buildroot}%{_datadir}/bash-completion/completions/%{name}
sed -i 's|/local||g' %{buildroot}%{_datadir}/bash-completion/completions/%{name}
rm -rf  %{buildroot}%{_datadir}/doc/%{name}

%files
%doc COPYING CHANGELOG README.md docs/plowshare.conf.sample
%{_bindir}/plowdel
%{_bindir}/plowdown
%{_bindir}/plowlist
%{_bindir}/plowmod
%{_bindir}/plowprobe
%{_bindir}/plowup
%{_datadir}/plowshare
%{_datadir}/bash-completion
%{_mandir}/man1/plowdel.1%{ext_man}
%{_mandir}/man1/plowdown.1%{ext_man}
%{_mandir}/man1/plowlist.1%{ext_man}
%{_mandir}/man1/plowmod.1%{ext_man}
%{_mandir}/man1/plowprobe.1%{ext_man}
%{_mandir}/man1/plowup.1%{ext_man}
%{_mandir}/man5/%{name}.conf.5%{ext_man}
%ghost %config(noreplace) %{_sysconfdir}/plowshare.conf

%changelog
