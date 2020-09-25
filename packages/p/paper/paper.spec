#
# spec file for package *
#
# Copyright (c) 2020 SUSE LLC
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


Name:           paper
Version:        2.2
Release:        0
Summary:        Enables users to indicate their preferred paper size
License:        GPL-3.0-or-later
URL:            https://github.com/rrthomas/paper
Source:         https://github.com/rrthomas/paper/releases/download/v%{version}/paper-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  perl
BuildRequires:  autoconf
BuildRequires:  help2man

%description
This package enables users to indicate their preferred paper
size, provides the paper(1) utility to find the user's preferred
default paper size and give information about known sizes, and
specifies system-wide and per-user paper size catalogues, which can be
can also be used directly (see paperspecs(5)).

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog 
%config %{_sysconfdir}/paperspecs
%{_bindir}/paper
%dir %{_datadir}/doc/paper
%{_datadir}/doc/paper/README
%{_libexecdir}/localepaper
%{_mandir}/man1/paper.1.gz
%{_mandir}/man5/paperspecs.5.gz


%changelog
