#
# spec file for package metamail
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


Name:           metamail
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bdftopcf
BuildRequires:  libpipeline-devel
BuildRequires:  mkfontdir
BuildRequires:  ncurses-devel
Requires:       sharutils
Version:        2.7.19
Release:        0
Summary:        MIME Mail Handler
License:        GPL-2.0-only AND MIT
Group:          Productivity/Networking/Email/Utilities
Source:         metamail-2.7-19.tar.gz
Source1:        mimecheck
Source2:        mimecheck.1
Source3:        mimegrep-0.2.tar.xz
Source4:        mimelang-0.3.tar.gz
Patch0:         metamail-2.7-19-security.dif
Patch1:         metamail-2.7-19.dif
Patch2:         metamail-2.7-19-getline.dif
Patch3:         metamail-2.7-19-binderman.dif
Patch4:         metamail-2.7-19-fix-bashisms.patch
Patch5:         metamail-2.7-19-provide-filenames-for-attachments.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%bcond_with     font

%description
Metamail is required for reading multimedia mail messages (such as
those using the Andrew toolkit) with elm.

%prep
# Workaround for boo#1225862
%global optflags %{optflags} -fpermissive

%setup -n metamail-2.7-19 -b 3 -b 4
%autopatch -p1

%build
    rm -f bin/mailserver
    rm -f bin/sun-message.csh
    make
    make -C fonts
    pushd ../mimegrep-0.2
	sed -i 's/`date/`date -u -r ChangeLog/' configure.ac #https://github.com/bitstreamout/mimegrep/pull/1
	./autogen.sh
	%configure
	make %{?_smp_mflags}
    popd
    pushd ../mimelang-0.3
	make %{?_smp_mflags}
    popd

%install
    mkdir -p %{buildroot}%{_bindir} %{buildroot}%_mandir/man{1,4}
    make INSTROOT=%{buildroot}/usr INSTALL=install install-all
%if %{with font}
    mkdir -p %{buildroot}%{_datadir}/fonts/misc
    install -m 0644 fonts/heb8x13B.pcf %{buildroot}%{_datadir}/fonts/misc/
    gzip -9f %{buildroot}%{_datadir}/fonts/misc/heb8x13B.pcf
%endif
    install -m 755 %{S:1} %{buildroot}%{_bindir}/
    install -m 644 %{S:2} %{buildroot}%{_mandir}/man1/
    ln -sf mimecheck %{buildroot}%{_bindir}/mimezip
    ln -sf mimecheck %{buildroot}%{_bindir}/mimebzip
    ln -sf mimecheck %{buildroot}%{_bindir}/mimegzip
    pushd ../mimegrep-0.2
	make install DESTDIR=%{buildroot}
    popd
    pushd ../mimelang-0.3
	make install DESTDIR=%{buildroot}
    popd

%files
%defattr(-,root,root)
%doc README mailers.txt
%{_bindir}/audiocompose
%{_bindir}/audiosend
%{_bindir}/extcompose
%{_bindir}/getfilename
%{_bindir}/mailto
%{_bindir}/mailto-hebrew
%{_bindir}/metamail
%{_bindir}/metasend
%{_bindir}/mimeit
%{_bindir}/mimencode
%{_bindir}/mimecheck
%{_bindir}/mimelang
%{_bindir}/mimezip
%{_bindir}/mimebzip
%{_bindir}/mimegzip
%{_bindir}/mmencode
%{_bindir}/mgrep
%{_bindir}/patch-metamail
%{_bindir}/rcvAppleSingle
%{_bindir}/richtext
%{_bindir}/richtoatk
%{_bindir}/showaudio
%{_bindir}/showexternal
%{_bindir}/shownonascii
%{_bindir}/showpartial
%{_bindir}/showpicture
%{_bindir}/sndAppleSingle
%{_bindir}/splitmail
%{_bindir}/sun-audio-file
%{_bindir}/sun-message
%{_bindir}/sun-to-mime
%{_bindir}/sun2mime
%{_bindir}/uudepipe
%{_bindir}/uuenpipe
%doc %{_mandir}/man1/audiocompose.1.gz
%doc %{_mandir}/man1/audiosend.1.gz
%doc %{_mandir}/man1/extcompose.1.gz
%doc %{_mandir}/man1/getfilename.1.gz
%doc %{_mandir}/man1/mailto-hebrew.1.gz
%doc %{_mandir}/man1/mailto.1.gz
%doc %{_mandir}/man1/metamail.1.gz
%doc %{_mandir}/man1/metasend.1.gz
%doc %{_mandir}/man1/mgrep.1.gz
%doc %{_mandir}/man1/mime.1.gz
%doc %{_mandir}/man1/mimencode.1.gz
%doc %{_mandir}/man1/mimecheck.1.gz
%doc %{_mandir}/man1/mimelang.1.gz
%doc %{_mandir}/man1/mmencode.1.gz
%doc %{_mandir}/man1/patch-metamail.1.gz
%doc %{_mandir}/man1/richtext.1.gz
%doc %{_mandir}/man1/showaudio.1.gz
%doc %{_mandir}/man1/showexternal.1.gz
%doc %{_mandir}/man1/shownonascii.1.gz
%doc %{_mandir}/man1/showpartial.1.gz
%doc %{_mandir}/man1/showpicture.1.gz
%doc %{_mandir}/man1/splitmail.1.gz
%doc %{_mandir}/man4/mailcap.4.gz
%if %{with font}
%{_datadir}/fonts/misc/heb8x13B.pcf.gz
%endif

%changelog
