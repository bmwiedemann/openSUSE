#
# spec file for package cvs
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


Name:           cvs
Version:        1.12.13
Release:        0
Summary:        Concurrent Versions System
License:        GPL-2.0
Group:          Development/Tools/Version Control
Url:            http://www.nongnu.org/cvs/
Source:         http://ftp.gnu.org/non-gnu/%{name}/source/feature/%{version}/%{name}-%{version}.tar.bz2
Source1:        http://www.does-not-exist.org/roessler/cvslock-0.2.tar.gz
Source3:        cvs.sh
Source4:        cvs.csh
Source5:        cvs@.service
Source6:        cvs.socket
Source7:        cvs.target
Source10:       http://cvsbook.red-bean.com/OpenSourceDevWithCVS_2E.tar.gz
Patch0:         cvs.diff
Patch2:         diff-k.possible.patch
Patch5:         cvs-fix_sigpipe_flowcontrol.diff
Patch8:         cvs-use_vitmp.diff
Patch10:        cvs-new-sort-option.diff
Patch11:        cvs-1.11.9-nocsh.patch
Patch12:        03cvs-client-exploit-fix.diff
Patch16:        cvs_readd_l_option.diff
Patch17:        cvs-silence_option_r_warning.diff
Patch18:        cvs-silence_old_format_strings.diff
Patch19:        cvs-1.12.9-null.patch
Patch20:        cvs-format.patch
Patch21:        cvs-useless-asnprintf.diff
Patch22:        cvs-1.12.12_cvsbug-tmp.diff
Patch23:        cvs-1.12.12-rcsfile-sanity.diff
Patch24:        cvs-1.12.12-type_punning.diff
Patch25:        cvs-no_AM_GETTEXT_VERSION.diff
Patch26:        cvs-request_rcs_installation.diff
Patch27:        cvs-fix_printf_format.diff
Patch28:        cvs-gnulib.diff
Patch29:        cvs-CVE-2012-0804.patch
Patch30:        cvs-Bug-1053364-disallow-dash.patch
BuildRequires:  automake
BuildRequires:  gdbm-devel
BuildRequires:  groff
BuildRequires:  krb5-devel
BuildRequires:  openssh
Requires:       openssh
BuildRequires:  zlib-devel
Requires:       %{_bindir}/csh
Requires:       /bin/mktemp
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
CVS is a front-end to the rcs (Revision Control System) included in the
standard Linux distributions. PCL-CVS, an emacs (Emacs) front-end for
CVS, is also included.

%package doc
Summary:        Info pages and Open Source Development with CVS, 2nd Edition Book
Group:          Development/Tools/Version Control
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description doc
Info pages for cvs, an introduction to cvs
(%{_datadir}/%{name}/contrib/intro.doc) and the complete book "Open Source
Development with CVS, 2nd Edition".

%prep
%setup -q -a 1 -a 10
%patch0
%patch2
%patch5
%patch8 -p1
%patch10
%patch11 -p1
%patch12 -p1
%patch16
%patch17
%patch18
%patch19
%patch20 -p1
%patch21
%patch22 -p1
%patch23
%patch24
%patch25
%patch26
%patch27
%patch28
%patch29
%patch30 -p1

%build
autoreconf -fvi
export CFLAGS="%{optflags} -pipe -D_GNU_SOURCE -std=gnu99"
%configure \
   --with-external-zlib \
   --with-editor=%{_bindir}/vitmp \
   --with-rsh=ssh
cd cvslock-*
%configure
cd -
make %{?_smp_mflags}
cd cvslock-*
make %{?_smp_mflags}
cd -

%install
%make_install install-info
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 0644 %{SOURCE3} %{SOURCE4} %{buildroot}%{_sysconfdir}/profile.d
# hack to avoid csh in requires
chmod 644 %{buildroot}%{_datadir}/cvs/contrib/sccs2rcs
install -p -m 644 -D %{SOURCE5} %{buildroot}%{_unitdir}/cvs\@.service
install -p -m 644 -D %{SOURCE6} %{buildroot}%{_unitdir}/cvs.socket
install -p -m 644 -D %{SOURCE7} %{buildroot}%{_unitdir}/cvs.target
#
# install cvslock
#
cd cvslock-*
%make_install
cd -
#
# documentation
#
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}/
install -m 0644 */OpenSourceDevWithCVS_2E.pdf \
        %{buildroot}/%{_defaultdocdir}/%{name}/
install -m 0644 contrib/rcs2log.1 %{buildroot}/%{_mandir}/man1

%post doc
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}client.info%{ext_info}

%preun doc
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}client.info%{ext_info}

%pre
%service_add_pre cvs.target cvs.socket

%post
%service_add_post cvs.target cvs.socket

%preun
%service_del_preun cvs.target cvs.socket

%postun
%service_del_postun cvs.target cvs.socket

%files
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/contrib
%config(noreplace) %{_sysconfdir}/profile.d/cvs.sh
%config(noreplace) %{_sysconfdir}/profile.d/cvs.csh
%{_unitdir}/*
%{_bindir}/cvs
%{_bindir}/cvsbug
%{_bindir}/rcs2log
%{_bindir}/cvslock
%{_datadir}/%{name}/contrib/clmerge
%{_datadir}/%{name}/contrib/cln_hist
%{_datadir}/%{name}/contrib/commit_prep
%{_datadir}/%{name}/contrib/cvs2vendor
%{_datadir}/%{name}/contrib/cvs_acls
%{_datadir}/%{name}/contrib/debug_check_log
%{_datadir}/%{name}/contrib/log
%{_datadir}/%{name}/contrib/log_accum
%{_datadir}/%{name}/contrib/mfpipe
%{_datadir}/%{name}/contrib/newcvsroot
%{_datadir}/%{name}/contrib/pvcs2rcs
%{_datadir}/%{name}/contrib/rcs2log
%{_datadir}/%{name}/contrib/rcslock
%{_datadir}/%{name}/contrib/rcs-to-cvs
%{_datadir}/%{name}/contrib/README
%{_datadir}/%{name}/contrib/rcs-5.7-commitid.patch
%{_datadir}/%{name}/contrib/sandbox_status
%{_datadir}/%{name}/contrib/validate_repo
%attr(755,root,root) %{_datadir}/%{name}/contrib/sccs2rcs
%{_mandir}/man1/*%{ext_man}
%{_mandir}/man5/*%{ext_man}
%{_mandir}/man8/*%{ext_man}

%files doc
%defattr(-,root,root)
%dir %{_defaultdocdir}/%{name}
%{_infodir}/*.info*
%doc %{_datadir}/%{name}/contrib/intro.doc
%doc %{_defaultdocdir}/%{name}/OpenSourceDevWithCVS_2E.pdf

%changelog
