#
# spec file for package datamash
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# bypass https://bugzilla.opensuse.org/show_bug.cgi?id=1149348
%ifarch ppc64le ppc64 aarch64
%define _lto_cflags %{nil}
%endif

Name:           datamash
Version:        1.5
Release:        0
Summary:        Statistical, numerical and textual operations in the command line
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.gnu.org/software/datamash/
Source:         https://ftp.gnu.org/gnu/datamash/%{name}-%{version}.tar.gz
Source2:        https://ftp.gnu.org/gnu/datamash/%{name}-%{version}.tar.gz.sig
Source3:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=datamash&download=1#/%{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
GNU datamash is a command-line program which performs basic numeric,
textual and statistical operations on input textual data files.

%prep
%setup -q

%build
%configure \
	--docdir=%{_docdir}/%{name} \
	--with-openssl=yes \
	--with-packager="%{vendor}" \
	--with-packager-version="%{distribution} %{version}-%{release}" \
	--with-packager-bug-reports="%{packager}" \
	--with-bash-completion-dir=no
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}

%check
make %{?_smp_mflags} check

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files -f %{name}.lang
%license COPYING
%doc ChangeLog README AUTHORS THANKS TODO
%{_bindir}/%{name}
%{_mandir}/man1/*.1%{?ext_man}
%{_infodir}/%{name}.info%{?ext_info}
%{_datadir}/%{name}

%changelog
