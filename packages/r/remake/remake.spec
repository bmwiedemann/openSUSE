#
# spec file for package remake
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define base_version 4.2+dbg-1.4
%define pkg_version 4.2.1+dbg-1.4
Name:           remake
Version:        4.2.1_1.4
Release:        0
Summary:        A gnu make version including a debuger
License:        GPL-3.0+
Group:          Development/Tools/Building
Summary(de):    Eine gnu make Version inklusive Debugger
URL:            http://bashdb.sourceforge.net/remake/
Source0:        https://downloads.sourceforge.net/project/bashdb/remake/%{base_version}/remake-%{pkg_version}.tar.bz2
Patch1:         glob-lstat.patch
Patch2:         glob-interface.patch
BuildRequires:  readline-devel
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Recommends:     %{name}-lang = %{version}

%description
remake is a patched and modernized version of GNU make utility that
adds improved error reporting, the ability to trace execution in a
comprehensible way, and a debugger.

%description -l de
remake ist eine gepatchte und modernisierte Version des GNU make
Utilities. Es wurde die Fehlerbenachrichtigung erweitertert, die
Möglichkeit die Ausführung zu tracen ergänzt und ein Debugger
eingebaut.

%lang_package

%prep
%setup -q -n "%{name}-%{pkg_version}"
%patch1 -p1
%patch2 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}/%{_infodir}/make* \
      %{buildroot}/%{_includedir}/gnuremake.h

%find_lang remake

%post
%install_info --info-dir="%{_infodir}" "%{_infodir}"/remake.info*

%preun
%install_info_delete --info-dir="%{_infodir}" "%{_infodir}"/remake.info*

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/remake
%{_mandir}/man1/remake.1%{ext_man}
%{_infodir}/remake.info%{ext_info}

%files lang -f %{name}.lang

%changelog
