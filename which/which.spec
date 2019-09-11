#
# spec file for package which
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


Name:           which
Version:        2.21
Release:        0
Summary:        Displays where a particular program in your path is located
License:        GPL-3.0-or-later
Group:          System/Base
Url:            https://savannah.gnu.org/projects/which/
Source0:        http://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Provides:       util-linux:%{_bindir}/which
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The which command shows the full pathname of a specified program, if
the specified program is in your PATH.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%post
%install_info --info-dir="%{_infodir}" "%{_infodir}/which.info.gz"

%preun
%install_info_delete --info-dir="%{_infodir}" "%{_infodir}/which.info.gz"

%files
%defattr(-,root,root)
%{_bindir}/which
%license COPYING
%doc EXAMPLES README README.alias AUTHORS NEWS
%{_infodir}/which.info*
%{_mandir}/man1/which.1*

%changelog
