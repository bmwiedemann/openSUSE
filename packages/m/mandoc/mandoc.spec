#
# spec file for package mandoc
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


Name:           mandoc
Version:        1.14.5
Release:        0
Summary:        UNIX manpage compiler
License:        ISC
Group:          Productivity/Publishing/Troff
URL:            http://mandoc.bsd.lv/
Source:         http://mandoc.bsd.lv/snapshots/mandoc-%{version}.tar.gz
BuildRequires:  zlib-devel
BuildRequires:  update-alternatives
Provides:       man = %{version}
Conflicts:      man
Conflicts:      groff
Requires(post): update-alternatives
Requires(postun): update-alternatives


%description
The mandoc manpage compiler toolset (formerly called "mdocml")
is a suite of tools compiling mdoc(7), the roff(7) macro language
of choice for BSD manual pages, and man(7), the predominant
historical language for UNIX manuals.

It includes a man(1) manual viewer and additional tools.
For general information, see <http://mandoc.bsd.lv/>.

%prep
%setup -q

%build
%{?!make_build:%define make_build make %{?_smp_mflags} V=1 VERBOSE=1}
export CPPFLAGS="%{optflags}"
export CFLAGS="%optflags"
%configure
%make_build

%install
%make_install MANDIR=%{_mandir} BINDIR=%{_bindir} SBINDIR=%{_sbindir}
cp -fv %{buildroot}%{_bindir}/apropos %{_tmppath}/
mv -fv %{_tmppath}/apropos %{buildroot}%{_sbindir}/makewhatis

# create a dummy target for /etc/alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for cmd in apropos man soelim ; do
    mv %{buildroot}%{_bindir}/$cmd{,.mandoc}
    ln -s -f %{_sysconfdir}/alternatives/$cmd %{buildroot}%{_bindir}/$cmd
done

mv %{buildroot}%{_sbindir}/makewhatis{,.mandoc}
ln -s -f %{_sysconfdir}/alternatives/makewhatis %{buildroot}%{_sbindir}/makewhatis

# sec 1
for man in apropos man soelim whatis ; do
    from=$(ls %{buildroot}%{_mandir}/man1/$man.1*)
    to=$(echo $from|sed -e 's!\.1$!!')-mandoc.1
    mv -v "$from" "$to"
    ln -s -f %{_sysconfdir}/alternatives/$man.1 "$from"
done
# sec 7
for man in eqn man mdoc roff tbl ; do
    from=$(ls %{buildroot}%{_mandir}/man7/$man.7*)
    to=$(echo $from|sed -e 's!\.7$!!')-mandoc.7
    mv -v "$from" "$to"
    ln -s -f %{_sysconfdir}/alternatives/$man.7 "$from"
done

%post
update-alternatives --install \
   %{_bindir}/man man %{_bindir}/man.mandoc 1000 \
   --slave %{_bindir}/apropos apropos %{_bindir}/apropos.mandoc \
   --slave %{_bindir}/soelim soelim %{_bindir}/soelim.mandoc \
   --slave %{_sbindir}/makewhatis makewhatis %{_sbindir}/makewhatis.mandoc \
   --slave %{_mandir}/man1/apropos.1%{?ext_man} apropos.1%{?ext_man} %{_mandir}/man1/apropos-mandoc.1%{?ext_man} \
   --slave %{_mandir}/man1/man.1%{?ext_man} man.1%{?ext_man} %{_mandir}/man1/man-mandoc.1%{?ext_man} \
   --slave %{_mandir}/man1/soelim.1%{?ext_man} soelim.1%{?ext_man} %{_mandir}/man1/soelim-mandoc.1%{?ext_man} \
   --slave %{_mandir}/man1/whatis.1%{?ext_man} whatis.1%{?ext_man} %{_mandir}/man1/whatis-mandoc.1%{?ext_man} \
   --slave %{_mandir}/man7/eqn.7%{?ext_man} eqn.7%{?ext_man} %{_mandir}/man7/eqn-mandoc.7%{?ext_man} \
   --slave %{_mandir}/man7/man.7%{?ext_man} man.7%{?ext_man} %{_mandir}/man7/man-mandoc.7%{?ext_man} \
   --slave %{_mandir}/man7/mdoc.7%{?ext_man} mdoc.7%{?ext_man} %{_mandir}/man7/mdoc-mandoc.7%{?ext_man} \
   --slave %{_mandir}/man7/roff.7%{?ext_man} roff.7%{?ext_man} %{_mandir}/man7/roff-mandoc.7%{?ext_man} \
   --slave %{_mandir}/man7/tbl.7%{?ext_man} tbl.7%{?ext_man} %{_mandir}/man7/tbl-mandoc.7%{?ext_man}


%preun
if [ $1 -eq 0 ] ; then
   update-alternatives --remove man %{_bindir}/man.mandoc
fi

%files
%license LICENSE
%doc NEWS TODO
%{_bindir}/apropos*
%{_bindir}/demandoc
%{_bindir}/man*
%{_bindir}/soelim*
%{_bindir}/whatis
%{_sbindir}/makewhatis*
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}
%{_mandir}/man7/*.7%{?ext_man}
%{_mandir}/man8/*.8%{?ext_man}
%ghost %{_sysconfdir}/alternatives/man
%ghost %{_sysconfdir}/alternatives/apropos
%ghost %{_sysconfdir}/alternatives/soelim
%ghost %{_sysconfdir}/alternatives/makewhatis
%ghost %{_sysconfdir}/alternatives/apropos.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/man.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/soelim.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/whatis.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/eqn.7%{?ext_man}
%ghost %{_sysconfdir}/alternatives/man.7%{?ext_man}
%ghost %{_sysconfdir}/alternatives/mdoc.7%{?ext_man}
%ghost %{_sysconfdir}/alternatives/roff.7%{?ext_man}
%ghost %{_sysconfdir}/alternatives/tbl.7%{?ext_man}

%changelog
