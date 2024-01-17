#
# spec file for package rrep
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


Name:           rrep
Version:        1.3.7
Release:        1%{?dist}
Summary:        Recursive pattern replacement utility
License:        GPL-3.0-or-later
Group:          Productivity/Text/Utilities
URL:            http://sourceforge.net/projects/%{name}/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  libacl-devel
BuildRequires:  texinfo
Requires(post): info
Requires(preun): info

%description
rrep is a pattern replacement utility.  It comes with support for regular
expressions, recursive directory processing, backup, simulation and prompting.
The replacement string may contain special characters to refer to portions of
the matched pattern.

%prep
%autosetup

%build
%configure
%make_build

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
/sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_datadir}/doc/%{name}/COPYING
rm -f %{buildroot}%{_datadir}/doc/%{name}/README
%find_lang %{name}

%files -f %{name}.lang
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_infodir}/%{name}.info%{?ext_info}
%{_bindir}/%{name}
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README THANKS
%license COPYING

%changelog
