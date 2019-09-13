#
# spec file for package pbuilder
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Frank Lichtenheld <frank@lichtenheld.de>
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


Name:           pbuilder
Version:        0.215
Release:        0
Summary:        Personal package builder for .deb packages
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            http://pbuilder.alioth.debian.org
Source0:        http://ftp.de.debian.org/debian/pool/main/p/pbuilder/%{name}_%{version}.tar.gz
Patch0:         Makefile.patch
Patch1:         pbuilderrc.patch
Patch2:         pdebuild-double-checkbuilddeps.patch
Patch3:         bash-completion-have.patch
Patch4:         bash-completion-extglob.patch
Patch5:         test-suite.patch
Patch6:         pbuilder-ppc.patch
Requires:       debootstrap
Requires:       dpkg
Requires:       wget
%if 0%{?suse_version}
Recommends:     deb fakeroot sudo
%endif
BuildRequires:  dpkg
BuildRequires:  man
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
pbuilder constructs a chroot system, and builds a package inside the
chroot. It uses apt extensively, and a local mirror, or a fast
connection to a Debian/Ubuntu mirror is ideal, but not necessary.

"pbuilder create" uses debootstrap to create a chroot image.

"pbuilder update" updates the image to the current state of
testing/unstable/whatever

"pbuilder build" takes a *.dsc file and builds a binary in the chroot
image.

pdebuild is a wrapper for developers, to allow running pbuilder
just like "debuild", as a normal user.

Authors:
--------
    Junichi Uekawa

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__make} %{?jobs:-j%jobs}

%install
%{__make} install DESTDIR=%{?buildroot}

mv %{buildroot}/etc/bash_completion.d/pbuilder{,.sh}

for man in debuild-pbuilder.1 pbuilder.8 pbuilderrc.5 pbuilder-uml.conf.5 pbuilder-user-mode-linux.1 pdebuild.1 pdebuild-user-mode-linux.1; do
  category=${man: -1}
  install -D -m644 $man %{buildroot}%{_mandir}/man$category/$man
  gzip -9 %{buildroot}%{_mandir}/man$category/$man
done

for doc in ChangeLog README COPYING AUTHORS THANKS; do
  install -D -m644 $doc %{buildroot}%{_defaultdocdir}/%{name}/$doc
done

if [ "%{buildroot}/usr/share/doc/pbuilder" != "%{buildroot}%{_defaultdocdir}/%{name}" ]; then
  mv %{buildroot}/usr/share/doc/pbuilder/* %{buildroot}%{_defaultdocdir}/%{name}/
fi

for dir in build result aptcache ccache; do
  install -d %buildroot/var/cache/pbuilder/$dir
done

%clean
rm -rf $RPM_BUILD_ROOT

%check
%{__make} check

%files
%defattr(-,root,root,0755)
%doc %{_defaultdocdir}/%{name}/
%config /etc/bash_completion.d/pbuilder.sh
%config /etc/pbuilder
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
/usr/sbin/*
/usr/bin/*
/usr/lib/pbuilder
/usr/share/pbuilder
/var/cache/pbuilder

%changelog
