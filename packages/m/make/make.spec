#
# spec file for package make
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


Name:           make
Version:        4.2.1
Release:        0
Summary:        GNU make
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Url:            http://www.gnu.org/software/make/make.html
Source:         http://ftp.gnu.org/gnu/make/make-%{version}.tar.bz2
Source1:        http://ftp.gnu.org/gnu/make/make-%{version}.tar.bz2.sig
# keyring downloaded from http://savannah.gnu.org/project/memberlist-gpgkeys.php?group=make
Source2:        %{name}.keyring
Patch1:         make-testcases_timeout.diff
# PATCH-FEATURE-OPENSUSE sort glob https://savannah.gnu.org/bugs/index.php?52076
Patch2:         make-sorted-glob.patch
Patch3:         glob-lstat.patch
Patch4:         glob-interface.patch
Patch5:         test-driver.patch
Patch6:         pselect-non-blocking.patch
Patch64:        make-library-search-path.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Recommends:     %{name}-lang
Provides:       gmake

%description
The GNU make command with extensive documentation.

%lang_package

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
if [ %{_lib} = lib64 ]; then
%patch64 -p1
fi

%build
autoreconf -fi
export CFLAGS="%{optflags}"
%configure
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check || {
  for f in tests/work/*/*.diff; do
    test -f "$f" || continue
    printf "++++++++++++++ %s ++++++++++++++\n" "${f##*/}"
    cat "$f"
  done
}

%install
%make_install
ln -s make %{buildroot}%{_bindir}/gmake
%find_lang %{name}
# gnumake.h was introduced in 4.0, looks useless
rm %{buildroot}%{_includedir}/gnumake.h

%files
%{_bindir}/make
%{_bindir}/gmake
%{_infodir}/make.info-*%{ext_info}
%{_infodir}/make.info%{ext_info}
%{_mandir}/man1/make.1%{ext_man}

%files lang -f %{name}.lang

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%changelog
