#
# spec file for package colordiff
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


Name:           colordiff
Version:        1.0.18
Release:        0
Summary:        Colour-highlighted 'diff' output
License:        GPL-2.0+
Group:          Productivity/Text/Utilities
Url:            http://www.colordiff.org
Source0:        http://www.colordiff.org/%{name}-%{version}.tar.gz
Source1:        http://www.colordiff.org/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Patch0:         colordiff-fix-permission.diff
BuildArch:      noarch

%description
The Perl script colordiff is a wrapper for 'diff' and produces the same
output but with pretty 'syntax' highlighting. Colour schemes can be
customized.

%prep
%setup -q
%patch0

%build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}
make \
  INSTALL_DIR=%{buildroot}/%{_bindir} \
  MAN_DIR=%{buildroot}/%{_mandir}/man1 \
  ETC_DIR=%{buildroot}%{_sysconfdir} install
sed -i -e "s@%{buildroot}@@" %{buildroot}/%{_bindir}/colordiff
chmod a-x %{buildroot}/%{_mandir}/man1/colordiff.*

%files
%doc README COPYING CHANGES BUGS colordiffrc colordiffrc-lightbg
%config %{_sysconfdir}/colordiffrc
%{_bindir}/cdiff
%{_bindir}/colordiff
%{_mandir}/man1/cdiff.1%{?ext_man}
%{_mandir}/man1/colordiff.1%{?ext_man}

%changelog
