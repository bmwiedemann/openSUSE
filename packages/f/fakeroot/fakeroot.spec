#
# spec file for package fakeroot
#
# Copyright (c) 2024 SUSE LLC
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


Name:           fakeroot
Version:        1.35.1
Release:        0
Summary:        Wrapper that gives a fake root environment
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://tracker.debian.org/pkg/fakeroot
Source0:        http://ftp.debian.org/debian/pool/main/f/fakeroot/%{name}_%{version}.orig.tar.gz#/%{name}_%{version}.orig.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM fakeroot-1.21-fix-shell-in-fakeroot.patch (deb#828810)
Patch0:         fakeroot-1.21-fix-shell-in-fakeroot
BuildRequires:  autoconf >= 2.71
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  group(sys)
# user(daemon)/group(sys) is required for t.tar testsuite
BuildRequires:  intltool
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  libcap-progs
BuildRequires:  libtool
BuildRequires:  po4a
BuildRequires:  sharutils
BuildRequires:  user(daemon)
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description
fakeroot runs a command in an environment wherein it appears to have
root privileges for file manipulation. fakeroot works by replacing the
file manipulation library functions (chmod(2), stat(2) etc.) by ones
that simulate the effect the real library functions would have had,
had the user really been root.

%prep
%autosetup -p1

%build
./bootstrap
pushd doc
po4a -k 0 --rm-backups --variable "srcdir=../doc/" po4a/po4a.cfg
popd

for type in sysv tcp; do
  mkdir obj-$type
  cd obj-$type
  cat >> configure << 'EOF'
#! /bin/sh
exec ../configure "$@"
EOF
  chmod +x configure
  %configure \
    --libdir=%{_libdir}/libfakeroot \
    --disable-static \
    --with-ipc=$type \
    --program-suffix=-$type
  %make_build
  cd ..
done

%install
for type in sysv tcp; do
  make -C obj-$type install DESTDIR=%{buildroot}
  mv %{buildroot}%{_libdir}/libfakeroot/libfakeroot-0.so \
     %{buildroot}%{_libdir}/libfakeroot/libfakeroot-$type.so
  rm -f %{buildroot}%{_libdir}/libfakeroot/libfakeroot.so
  rm -f %{buildroot}%{_libdir}/libfakeroot/libfakeroot.*a
done

%fdupes -s %{buildroot}

# Create ghost files for "update-alternatives"
ln -sf faked-sysv %{buildroot}%{_bindir}/faked
ln -sf fakeroot-sysv %{buildroot}%{_bindir}/fakeroot
ln -sf faked-sysv.1.gz %{buildroot}%{_mandir}/man1/faked.1.gz
ln -sf fakeroot-sysv.1.gz %{buildroot}%{_mandir}/man1/fakeroot.1.gz
for i in de es fr nl pt ro sv; do
  ln -sf faked-sysv.1.gz %{buildroot}%{_mandir}/$i/man1/faked.1.gz
  ln -sf fakeroot-sysv.1.gz %{buildroot}%{_mandir}/$i/man1/fakeroot.1.gz
done
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/{faked,fakeroot}{,.1%{ext_man}}

%check
for type in sysv tcp; do
  %make_build -C obj-$type check
done

%post
%{_sbindir}/update-alternatives --install %{_bindir}/fakeroot fakeroot %{_bindir}/fakeroot-sysv 20 \
 --slave %{_bindir}/faked faked %{_bindir}/faked-sysv \
 --slave %{_mandir}/man1/fakeroot.1.gz fakeroot.1.gz %{_mandir}/man1/fakeroot-sysv.1.gz \
 --slave %{_mandir}/man1/faked.1.gz faked.1.gz %{_mandir}/man1/faked-sysv.1.gz \
 --slave %{_mandir}/de/man1/fakeroot.1.gz fakeroot.de.1.gz %{_mandir}/de/man1/fakeroot-sysv.1.gz \
 --slave %{_mandir}/de/man1/faked.1.gz faked.de.1.gz %{_mandir}/de/man1/faked-sysv.1.gz \
 --slave %{_mandir}/es/man1/fakeroot.1.gz fakeroot.es.1.gz %{_mandir}/es/man1/fakeroot-sysv.1.gz \
 --slave %{_mandir}/es/man1/faked.1.gz faked.es.1.gz %{_mandir}/es/man1/faked-sysv.1.gz \
 --slave %{_mandir}/fr/man1/fakeroot.1.gz fakeroot.fr.1.gz %{_mandir}/fr/man1/fakeroot-sysv.1.gz \
 --slave %{_mandir}/fr/man1/faked.1.gz faked.fr.1.gz %{_mandir}/fr/man1/faked-sysv.1.gz \
 --slave %{_mandir}/nl/man1/fakeroot.1.gz fakeroot.nl.1.gz %{_mandir}/nl/man1/fakeroot-sysv.1.gz \
 --slave %{_mandir}/nl/man1/faked.1.gz faked.nl.1.gz %{_mandir}/nl/man1/faked-sysv.1.gz \
 --slave %{_mandir}/pt/man1/fakeroot.1.gz fakeroot.pt.1.gz %{_mandir}/pt/man1/fakeroot-sysv.1.gz \
 --slave %{_mandir}/pt/man1/faked.1.gz faked.pt.1.gz %{_mandir}/pt/man1/faked-sysv.1.gz \
 --slave %{_mandir}/ro/man1/fakeroot.1.gz fakeroot.ro.1.gz %{_mandir}/ro/man1/fakeroot-sysv.1.gz \
 --slave %{_mandir}/ro/man1/faked.1.gz faked.ro.1.gz %{_mandir}/ro/man1/faked-sysv.1.gz \
 --slave %{_mandir}/sv/man1/fakeroot.1.gz fakeroot.sv.1.gz %{_mandir}/sv/man1/fakeroot-sysv.1.gz \
 --slave %{_mandir}/sv/man1/faked.1.gz faked.sv.1.gz %{_mandir}/sv/man1/faked-sysv.1.gz

%{_sbindir}/update-alternatives --install %{_bindir}/fakeroot fakeroot %{_bindir}/fakeroot-tcp 10 \
 --slave %{_bindir}/faked faked %{_bindir}/faked-tcp \
 --slave %{_mandir}/man1/fakeroot.1.gz fakeroot.1.gz %{_mandir}/man1/fakeroot-tcp.1.gz \
 --slave %{_mandir}/man1/faked.1.gz faked.1.gz %{_mandir}/man1/faked-tcp.1.gz \
 --slave %{_mandir}/de/man1/fakeroot.1.gz fakeroot.de.1.gz %{_mandir}/de/man1/fakeroot-tcp.1.gz \
 --slave %{_mandir}/de/man1/faked.1.gz faked.de.1.gz %{_mandir}/de/man1/faked-tcp.1.gz \
 --slave %{_mandir}/es/man1/fakeroot.1.gz fakeroot.es.1.gz %{_mandir}/es/man1/fakeroot-tcp.1.gz \
 --slave %{_mandir}/es/man1/faked.1.gz faked.es.1.gz %{_mandir}/es/man1/faked-tcp.1.gz \
 --slave %{_mandir}/fr/man1/fakeroot.1.gz fakeroot.fr.1.gz %{_mandir}/fr/man1/fakeroot-tcp.1.gz \
 --slave %{_mandir}/fr/man1/faked.1.gz faked.fr.1.gz %{_mandir}/fr/man1/faked-tcp.1.gz \
 --slave %{_mandir}/nl/man1/fakeroot.1.gz fakeroot.nl.1.gz %{_mandir}/nl/man1/fakeroot-tcp.1.gz \
 --slave %{_mandir}/nl/man1/faked.1.gz faked.nl.1.gz %{_mandir}/nl/man1/faked-tcp.1.gz \
 --slave %{_mandir}/pt/man1/fakeroot.1.gz fakeroot.pt.1.gz %{_mandir}/pt/man1/fakeroot-tcp.1.gz \
 --slave %{_mandir}/pt/man1/faked.1.gz faked.pt.1.gz %{_mandir}/pt/man1/faked-tcp.1.gz \
 --slave %{_mandir}/ro/man1/fakeroot.1.gz fakeroot.ro.1.gz %{_mandir}/ro/man1/fakeroot-tcp.1.gz \
 --slave %{_mandir}/ro/man1/faked.1.gz faked.ro.1.gz %{_mandir}/ro/man1/faked-tcp.1.gz \
 --slave %{_mandir}/sv/man1/fakeroot.1.gz fakeroot.sv.1.gz %{_mandir}/sv/man1/fakeroot-tcp.1.gz \
 --slave %{_mandir}/sv/man1/faked.1.gz faked.sv.1.gz %{_mandir}/sv/man1/faked-tcp.1.gz

%preun
if [ $1 -eq 0 ]; then
  %{_sbindir}/update-alternatives --remove fakeroot %{_bindir}/fakeroot-sysv
  %{_sbindir}/update-alternatives --remove fakeroot %{_bindir}/fakeroot-tcp
fi

%files
%license COPYING
%doc AUTHORS BUGS DEBUG README doc/README.saving
%ghost %{_bindir}/faked
%ghost %{_sysconfdir}/alternatives/faked
%ghost %{_bindir}/fakeroot
%ghost %{_sysconfdir}/alternatives/fakeroot
%{_bindir}/faked-sysv
%{_bindir}/faked-tcp
%{_bindir}/fakeroot-sysv
%{_bindir}/fakeroot-tcp
%{_libdir}/libfakeroot/
%ghost %{_mandir}/man1/faked.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/faked.1%{ext_man}
%ghost %{_mandir}/man1/fakeroot.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/fakeroot.1%{ext_man}
%{_mandir}/man1/faked-*.1%{?ext_man}
%{_mandir}/man1/fakeroot-*.1%{?ext_man}
%dir %{_mandir}/nl/
%dir %{_mandir}/nl/man1/
%dir %{_mandir}/pt/
%dir %{_mandir}/pt/man1/
%dir %{_mandir}/ro/
%dir %{_mandir}/ro/man1/
%dir %{_mandir}/sv/
%dir %{_mandir}/sv/man1/
%ghost %lang(de) %{_mandir}/de/man1/faked.1%{ext_man}
%ghost %lang(de) %{_mandir}/de/man1/fakeroot.1%{ext_man}
%lang(de) %{_mandir}/de/man1/faked-*.1%{ext_man}
%lang(de) %{_mandir}/de/man1/fakeroot-*.1%{ext_man}
%ghost %lang(es) %{_mandir}/es/man1/faked.1%{ext_man}
%ghost %lang(es) %{_mandir}/es/man1/fakeroot.1%{ext_man}
%lang(es) %{_mandir}/es/man1/faked-*.1%{ext_man}
%lang(es) %{_mandir}/es/man1/fakeroot-*.1%{ext_man}
%ghost %lang(fr) %{_mandir}/fr/man1/faked.1%{ext_man}
%ghost %lang(fr) %{_mandir}/fr/man1/fakeroot.1%{ext_man}
%lang(fr) %{_mandir}/fr/man1/faked-*.1%{ext_man}
%lang(fr) %{_mandir}/fr/man1/fakeroot-*.1%{ext_man}
%ghost %lang(nl) %{_mandir}/nl/man1/faked.1%{ext_man}
%ghost %lang(nl) %{_mandir}/nl/man1/fakeroot.1%{ext_man}
%lang(nl) %{_mandir}/nl/man1/faked-*.1%{ext_man}
%lang(nl) %{_mandir}/nl/man1/fakeroot-*.1%{ext_man}
%ghost %lang(pt) %{_mandir}/pt/man1/faked.1%{ext_man}
%ghost %lang(pt) %{_mandir}/pt/man1/fakeroot.1%{ext_man}
%lang(pt) %{_mandir}/pt/man1/faked-*.1%{ext_man}
%lang(pt) %{_mandir}/pt/man1/fakeroot-*.1%{ext_man}
%ghost %lang(ro) %{_mandir}/ro/man1/faked.1%{ext_man}
%ghost %lang(ro) %{_mandir}/ro/man1/fakeroot.1%{ext_man}
%lang(ro) %{_mandir}/ro/man1/faked-*.1%{ext_man}
%lang(ro) %{_mandir}/ro/man1/fakeroot-*.1%{ext_man}
%ghost %lang(sv) %{_mandir}/sv/man1/faked.1%{ext_man}
%ghost %lang(sv) %{_mandir}/sv/man1/fakeroot.1%{ext_man}
%lang(sv) %{_mandir}/sv/man1/faked-*.1%{ext_man}
%lang(sv) %{_mandir}/sv/man1/fakeroot-*.1%{ext_man}

%changelog
