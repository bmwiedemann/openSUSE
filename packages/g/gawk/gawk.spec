#
# spec file for package gawk
#
# Copyright (c) 2021 SUSE LLC
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


Name:           gawk
Version:        5.1.0
Release:        0
Summary:        Domain-specific language for text processing
License:        GPL-3.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://www.gnu.org/software/gawk/
Source:         http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source2:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source3:        http://savannah.gnu.org/people/viewgpg.php?user_id=80653#/gawk.keyring
Source4:        gawk.rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  makeinfo
BuildRequires:  update-alternatives
Requires(post): %{install_info_prereq}
Requires(post): update-alternatives
Requires(preun): %{install_info_prereq}
Requires(preun): update-alternatives
Provides:       awk

%description
AWK is a domain-specific language designed for text processing and
typically used as a data extraction and reporting tool.

GNU awk is upwardly compatible with the System V Release 4 awk.  It is
almost completely POSIX 1003.2 compliant.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install

%if !0%{?usrmerged}
install -d %{buildroot}/bin
ln -sf %{_bindir}/gawk %{buildroot}/bin
ln -s %{_sysconfdir}/alternatives/awk %{buildroot}/bin/awk
%endif
rm -f %{buildroot}%{_bindir}/*-%{version} %{buildroot}%{_bindir}/awk

# create symlinks for update-alternatives
%if !0%{?usrmerged}
ln -s %{_sysconfdir}/alternatives/usr-bin-awk %{buildroot}%{_bindir}/awk
%else
ln -s %{_sysconfdir}/alternatives/awk %{buildroot}%{_bindir}/awk
%endif
ln -s %{_sysconfdir}/alternatives/awk.1%{?ext_man} %{buildroot}%{_mandir}/man1/awk.1%{?ext_man}

%find_lang %{name}

%post
%if !0%{?usrmerged}
%{_sbindir}/update-alternatives \
  --install /bin/awk awk %{_bindir}/gawk 20 \
  --slave %{_bindir}/awk usr-bin-awk %{_bindir}/gawk \
  --slave %{_mandir}/man1/awk.1.gz awk.1%{?ext_man} %{_mandir}/man1/gawk.1%{?ext_man}
%else
%{_sbindir}/update-alternatives \
  --install %{_bindir}/awk awk %{_bindir}/gawk 20 \
  --slave %{_mandir}/man1/awk.1.gz awk.1%{?ext_man} %{_mandir}/man1/gawk.1%{?ext_man}
%endif

%postun
if [ ! -f %{_bindir}/gawk ]; then
    %{_sbindir}/update-alternatives --remove awk %{_bindir}/gawk
fi

%files -f %{name}.lang
%config %{_sysconfdir}/profile.d/gawk.csh
%config %{_sysconfdir}/profile.d/gawk.sh
%if !0%{?usrmerged}
#UsrMerge
/bin/awk
/bin/gawk
%ghost %{_sysconfdir}/alternatives/usr-bin-awk
#EndUsrMerge
%endif
%{_bindir}/awk
%{_mandir}/man1/awk.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/awk
%ghost %{_sysconfdir}/alternatives/awk.1%{?ext_man}
%license COPYING*
%doc AUTHORS NEWS POSIX.STD README ChangeLog*
%{_bindir}/gawk
%{_libexecdir}/awk
%{_libdir}/gawk
%{_datadir}/awk
%{_includedir}/gawkapi.h
%{_infodir}/*.info%{?ext_info}
%{_mandir}/man1/gawk.1%{?ext_man}
%{_mandir}/man3/*%{?ext_man}

%changelog
