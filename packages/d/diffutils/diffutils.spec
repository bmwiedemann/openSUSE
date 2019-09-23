#
# spec file for package diffutils
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


Name:           diffutils
Version:        3.7
Release:        0
Summary:        GNU diff Utilities
License:        GFDL-1.2-only AND GPL-3.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://www.gnu.org/software/diffutils/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Requires(pre):  %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Recommends:     %{name}-lang = %{version}
Provides:       diff = %{version}
Obsoletes:      diff < %{version}

%description
The GNU diff utilities find differences between files. diff is used to
make source code patches, for instance.

%lang_package

%prep
%setup -q

%build
%configure \
  --with-packager="openSUSE" \
  --with-packager-bug-reports="http://bugs.opensuse.org/"
make %{?_smp_mflags} V=1

%check
%ifarch ppc64le ppc64
make %{?_smp_mflags} check || echo 'Warning: ignore error https://debbugs.gnu.org/cgi/bugreport.cgi?bug=36488'
%else
make %{?_smp_mflags} check
%endif

%install
%make_install
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%license COPYING
%doc AUTHORS NEWS README THANKS
%{_bindir}/cmp
%{_bindir}/diff
%{_bindir}/diff3
%{_bindir}/sdiff
%{_infodir}/diffutils.info%{?ext_info}
%{_mandir}/man1/cmp.1%{?ext_man}
%{_mandir}/man1/diff.1%{?ext_man}
%{_mandir}/man1/diff3.1%{?ext_man}
%{_mandir}/man1/sdiff.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
