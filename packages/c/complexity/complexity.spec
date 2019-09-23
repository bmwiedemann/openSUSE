#
# spec file for package complexity
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


Name:           complexity
Version:        1.10
Release:        0
Summary:        C source code complexity computation utility
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://www.gnu.org/software/complexity/
Source0:        https://ftp.gnu.org/gnu/complexity/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/complexity/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Patch0:         complexity-1.10-avoid-random-return-in-nonvoid-function.patch
BuildRequires:  autogen
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(autoopts)
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
Complexity is a tool for analyzing the complexity of "C" program functions.
It is very similar to the McCabe scoring, but addresses some issues not considered
in that scoring scheme.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%check
make %{?_smp_mflags} check

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%license COPYING
%doc AUTHORS ChangeLog README NEWS
%{_bindir}/complexity
%{_bindir}/cx-vs-mc
%{_infodir}/complexity.info%{?ext_info}
%{_mandir}/man1/complexity.1%{?ext_man}

%changelog
