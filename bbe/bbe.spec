#
# spec file for package bbe
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bbe
Version:        0.2.2
Release:        0
Summary:        Binary Block Editor
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://sourceforge.net/projects/bbe-/
Source0:        https://sourceforge.net/projects/bbe-/files/bbe/%{version}/bbe-%{version}.tar.gz
Requires:       info
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
bbe is a sed-like editor for binary files. Instead of reading input in
lines as sed, bbe reads arbitrary blocks from an input stream and performs
byte-related transformations on found blocks.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc/bbe

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%license COPYING
%doc README AUTHORS ChangeLog
%{_bindir}/%{name}
%{_infodir}/bbe.info%{?ext_info}
%{_mandir}/man1/bbe.1%{?ext_man}

%changelog
