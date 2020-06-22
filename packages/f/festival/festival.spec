#
# spec file for package festival
#
# Copyright (c) 2020 SUSE LLC
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           festival
Version:        2.5.0
Release:        0
Summary:        The Speech Synthesis System
License:        BSD-3-Clause
Group:          Productivity/Text/Convertors
URL:            http://festvox.org/festival
Source0:        http://festvox.org/packed/%{name}/2.5/%{name}-%{version}-release.tar.gz
Source1:        http://festvox.org/packed/%{name}/2.5/speech_tools-%{version}-release.tar.gz
Source2:        http://festvox.org/packed/%{name}/2.5/festlex_CMU.tar.gz
Source3:        http://festvox.org/packed/%{name}/2.5/voices/festvox_kallpc16k.tar.gz
Source4:        http://festvox.org/packed/%{name}/2.5/festlex_POSLEX.tar.gz
Source5:        sysconfig.%{name}
Source6:        rc%{name}
Source7:        http://festvox.org/packed/%{name}/2.5/voices/festvox_rablpc16k.tar.gz
# systemd unit file
Source8:        %{name}.systemd
# festival patches
Patch2:         %{name}-1.95-examples.patch
Patch3:         %{name}-text2wave-manpage.patch
Patch4:         %{name}-1.95-libdir.patch
Patch7:         %{name}-1.95-audsp.patch
Patch8:         %{name}-1.96-chroot.patch
# PATCH-FIX-UPSTREAM festival-no-LD_LIBRARY_PATH-extension.patch bnc#642507 vuntz@opensuse.org -- Do not change LD_LIBRARY_PATH in binaries, to avoid any risks
Patch9:         %{name}-no-LD_LIBRARY_PATH-extension.patch
# PATCH-FIX-UPSTREAM festival-safe-temp-file.patch bnc#642507 vuntz@opensuse.org -- Create temporary files in a safe way
Patch10:        %{name}-safe-temp-file.patch
# speech-tools patches
# PATCH-FIX-UPSTREAM speech_tools-undefined-operation.patch vuntz@opensuse.org -- Avoid a undefined-operation warning with gcc (sending mail upstream)
Patch11:        speech_tools-undefined-operation.patch
Patch12:        speech_tools-1.2.95-config.patch
# PATCH-FIX-UPSTREAM speech_tools-no-LD_LIBRARY_PATH-extension.patch vuntz@opensuse.org -- Do not change LD_LIBRARY_PATH in binaries, to avoid any risks
Patch17:        speech_tools-no-LD_LIBRARY_PATH-extension.patch
Patch18:        speech_tools-remove-errneous-decl.patch
Patch19:        speech_tools-null-fragile.patch
Patch20:        festival-null-fragile.patch
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
Requires(pre):  insserv-compat
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd

%description
Festival is a multilingual speech synthesis system developed at CSTR.
It offers a full text-to-speech system with various APIs as well as an
environment for development and research of speech synthesis
techniques. It is written in C++ and has a Scheme-based command
interpreter for general control.

%package devel
Summary:        Development Package for Festival
License:        MIT
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
Files needed for developing software that uses Festival.

%prep
%setup -q -b 1 -b 2 -b 3 -b 4 -b 7 -n %{name}
%patch2 -p1
%patch3 -p1
%patch4
%patch7
%patch8
%patch9 -p1
%patch10 -p1
cd ../speech_tools
%patch11 -p1
%patch12
%patch17 -p1
%patch18 -p1
%patch19 -p1
cd ../festival
%patch20 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
# configure festival
%configure
# configure speech tools
cp config.guess config.sub ../speech_tools
cd ../speech_tools
%configure
  # -fPIC 'cause we're building shared libraries and it doesn't hurt
  # -fno-strict-aliasing because of a couple of warnings about code
  #   problems; if $RPM_OPT_FLAGS contains -O2 or above, this puts
  #   it back. Once that problem is gone upstream, remove this for
  #   better optimization.
  make \
    CFLAGS="%{optflags} -fPIC -fno-strict-aliasing" \
    CXXFLAGS="%{optflags} -fPIC -fno-strict-aliasing"
cd ../%{name}
make \
  FTLIBDIR="%{_datadir}/festival" \
  CFLAGS="%{optflags} -fPIC" \
  CXXFLAGS="%{optflags} -fPIC"
make %{?_smp_mflags} doc

%install
%make_install
cd ../speech_tools
%make_install
cd ../%{name}
# install binaries
install -D bin/text2wave %{buildroot}%{_bindir}/text2wave
install -m 755 bin/%{name}* %{buildroot}%{_bindir}/
install -m 755 examples/saytime %{buildroot}%{_bindir}/
# install manpages
install -Dm 644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -m 644 doc/%{name}_client.1 %{buildroot}%{_mandir}/man1/
install -m 644 doc/text2wave.1 %{buildroot}%{_mandir}/man1/
# install configs
install -Dm 644 lib/%{name}.scm %{buildroot}%{_sysconfdir}/%{name}.scm
# install dictionarys
install -Dm 644 lib/dicts/cmu/cmudict-0.4.out %{buildroot}%{_datadir}/%{name}/dicts/cmu/cmudict-0.4.out
install -m 644 lib/dicts/cmu/*.scm %{buildroot}%{_datadir}/%{name}/dicts/cmu/
install -m 644 lib/dicts/wsj.wp39.poslexR %{buildroot}%{_datadir}/%{name}/dicts/
install -m 644 lib/dicts/wsj.wp39.tri.ngrambin %{buildroot}%{_datadir}/%{name}/dicts/
# install voices
mkdir -p %{buildroot}%{_datadir}/%{name}/voices/english/{kal_diphone,rab_diphone}/{group,festvox}
cp lib/voices/english/kal_diphone/group/* %{buildroot}%{_datadir}/%{name}/voices/english/kal_diphone/group/
cp lib/voices/english/kal_diphone/festvox/*.scm %{buildroot}%{_datadir}/%{name}/voices/english/kal_diphone/festvox
cp lib/voices/english/rab_diphone/group/* %{buildroot}%{_datadir}/%{name}/voices/english/rab_diphone/group/
cp lib/voices/english/rab_diphone/festvox/*.scm %{buildroot}%{_datadir}/%{name}/voices/english/rab_diphone/festvox
# install data
cp lib/*.scm %{buildroot}%{_datadir}/%{name}/
cp lib/*.ngrambin %{buildroot}%{_datadir}/%{name}/
cp lib/*.gram %{buildroot}%{_datadir}/%{name}/
cp lib/*.el %{buildroot}%{_datadir}/%{name}/
install -D lib%{_sysconfdir}/unknown_Linux/audsp %{buildroot}%{_libexecdir}/%{name}/audsp
# install includes
mkdir -p %{buildroot}%{_includedir}/
install -m 644 src/include/*.h %{buildroot}%{_includedir}/
cd ../speech_tools

mkdir -p %{buildroot}%{_includedir}/{instantiate,ling_class,rxp,sigpr,unix}
install -m 644 include/*h %{buildroot}%{_includedir}
install -m 644 include/instantiate/*h %{buildroot}%{_includedir}/instantiate
install -m 644 include/ling_class/*h %{buildroot}%{_includedir}/ling_class
install -m 644 include/rxp/*h %{buildroot}%{_includedir}/rxp
install -m 644 include/sigpr/*h %{buildroot}%{_includedir}/sigpr
install -m 644 include/unix/*h %{buildroot}%{_includedir}/unix
# install libs
install -Dm 644 ../%{name}/src/lib/libFestival.a  %{buildroot}/%{_libdir}/libFestival.a
install -m 644 lib/lib*.a %{buildroot}%{_libdir}
# install init script
install -m 755 -D %{SOURCE6} %{buildroot}%{_usr}/lib/%{name}/server
install -d %{buildroot}%{_sbindir}
ln -sf /sbin/service %{buildroot}%{_sbindir}/rc%{name}
# install systemd unit file
install -m 644 -D %{SOURCE8} %{buildroot}%{_unitdir}/%{name}.service
# installl sysconfig file
install -m 644 -D %{SOURCE5} %{buildroot}%{_fillupdir}/sysconfig.%{name}

# remove instalation instructions
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL

%pre
getent group %{name} >/dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} >/dev/null || \
	%{_sbindir}/useradd -r -g %{name} -s /bin/false -c "Festival daemon" \
	-d %{_datadir}/%{name}/ %{name}
%service_add_pre %{name}.service

%post
%fillup_only
%service_add_post %{name}.service

%preun
%stop_on_removal %{name}
%service_del_preun %{name}.service

%postun
%restart_on_update %{name}
%insserv_cleanup
%service_del_postun %{name}.service

%files
%license COPYING
%doc examples/*.text examples/ex1.* examples/*.scm examples/*.dtd
%config(noreplace) %{_sysconfdir}/%{name}.scm
%{_bindir}/%{name}
%{_bindir}/%{name}_client
%{_bindir}/%{name}_server
%{_bindir}/%{name}_server_control
%{_bindir}/text2wave
%{_bindir}/saytime
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_fillupdir}/*

%files devel
%{_includedir}/*
%{_libdir}/lib*.a

%changelog
