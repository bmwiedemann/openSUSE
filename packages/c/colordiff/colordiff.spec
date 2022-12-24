#
# spec file for package colordiff
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


Name:           colordiff
Version:        1.0.21
Release:        0
Summary:        Colour-highlighted 'diff' output
License:        GPL-2.0-or-later
URL:            https://www.colordiff.org
Source0:        https://www.colordiff.org/%{name}-%{version}.tar.gz
Source1:        https://www.colordiff.org/%{name}-%{version}.tar.gz.sig
Source2:        https://www.sungate.co.uk/gpgkey_2013.txt#/%{name}.keyring
BuildArch:      noarch

%description
The Perl script colordiff is a wrapper for 'diff' and produces the same
output but with pretty 'syntax' highlighting. Colour schemes can be
customized.

%prep
%autosetup

%build

%install
%make_install INSTALL_DIR=%{_bindir} \
	ETC_DIR=%{_sysconfdir} \
	MAN_DIR=%{_mandir}/man1

%files
%license COPYING
%doc README CHANGES BUGS colordiffrc colordiffrc-lightbg colordiffrc-gitdiff
%config(noreplace) %{_sysconfdir}/colordiffrc
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%changelog
