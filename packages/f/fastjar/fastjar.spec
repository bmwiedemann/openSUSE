#
# spec file for package fastjar
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


Name:           fastjar
Version:        0.98
Release:        0
Summary:        Java package archiver
License:        GPL-2.0+
Group:          Development/Languages/Java
Url:            http://savannah.nongnu.org/projects/fastjar/
Source0:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
# Current signing key has expired
#Source1:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz.sig
#Source2:        http://savannah.nongnu.org/project/memberlist-gpgkeys.php?group=%{name}&download=1#/%{name}.keyring
Patch2:         fix-update-mode.diff
Patch3:         jartool.diff
BuildRequires:  zlib-devel
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Fastjar is an implementation of Sun's jar utility that comes with the
JDK, written entirely in C, and runs in a fraction of the time while
being 100% feature compatible.

%prep
%setup -q
%autopatch -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%defattr(-,root,root)
%doc AUTHORS README NEWS ChangeLog
%{_mandir}/man1/fastjar.1%{ext_man}
%{_mandir}/man1/grepjar.1%{ext_man}
%{_infodir}/fastjar.info%{ext_info}
%{_bindir}/fastjar
%{_bindir}/grepjar

%changelog
