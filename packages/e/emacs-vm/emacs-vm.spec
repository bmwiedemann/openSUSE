#
# spec file for package emacs-vm
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           emacs-vm
Version:        8.2.0b.1538
Release:        0
Summary:        VM - a mail reader for GNU Emacs
License:        GPL-2.0+
Group:          Productivity/Text/Editors
Url:            http://www.nongnu.org/viewmail/
# This is Launchpad trunk https://launchpad.net/vm/trunk - thus no URI, sorry.
Source:         vm-%{version}.tgz
Source2:        emacs-vm-autoload.el
# PATCH-FIX-UPSTREAM U_rev-1313.patch bsc#939497 eich@suse.com -- Fix Launchpad lp#793541 and lp#907286
Patch0:         vcard-Make-vcard-parser-more-robust-to-invalid-vcards.patch
# For 'trunk':
BuildRequires:  autoconf
BuildRequires:  emacs-nox
BuildRequires:  makeinfo
Requires:       ed
Requires:       emacs
%if 0%{?suse_version} <= 1500
Requires(post): %{install_info_prereq}
Requires(pre):  %{install_info_prereq}
%endif

%description
VM (View Mail) is an Emacs subsystem that allows UNIX mail to be read
and disposed of within Emacs.  Commands exist to do the normal things
expected of a mail user agent, such as generating replies, saving
messages to folders, deleting messages and so on.  There are other more
advanced commands that do tasks like bursting and creating digests,
message forwarding, and organizing message presentation according to
various criteria.

%define _sitedir %{_prefix}/share/emacs/site-lisp
%define _vmdir  %{_sitedir}/vm
%define _infodir %{_prefix}/share/info
%define _vmetcdir %{_prefix}/share/emacs/${emacs_ver}/etc/vm
%define _vmdocdir %{_prefix}/share/doc/packages/%{name}

%prep
%setup -q -n ~vm/vm/trunk
# For trunk
%autopatch -p3

%build
export LC_CTYPE=ISO-8859-1
export EMACS_UNIBYTE=1
EMACS="emacs --no-site"
emacs_ver=$(rpm -q --qf '%%{VERSION}' emacs)
rm -rf lisp/*.elc
# For trunk
autoconf
%configure FLAGS="-batch -q -no-site-file -no-init-file -l \$(srcdir)/vm-build.el" --with-etcdir=%{_vmetcdir} --with-docdir=%{_vmdocdir}
make %{?_smp_mflags} MAKEINFO="makeinfo --force"

%install
mkdir -p %{buildroot}
%make_install
{
  echo ";; %{_datadir}/emacs/site-lisp/suse-start-%{name}.el"
  cat %{SOURCE2}
  echo ";; %{_datadir}/emacs/site-lisp/suse-start-%{name}.el ends here"
} > %{buildroot}%{_sitedir}/suse-start-%{name}.el

%if 0%{?suse_version} <= 1500
%post
%install_info --info-dir=%{_infodir} %{_infodir}/vm.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/vm.info%{ext_info}
%endif

%files
%docdir %{_vmdocdir}
%{_vmdocdir}
%dir %{_sitedir}
%{_sitedir}/*.el
%dir %{_vmdir}
%{_vmdir}/*.el
%{_vmdir}/*.elc
%{_vmdir}/version.txt
%{_bindir}/base64-encode
%{_bindir}/base64-decode
%{_bindir}/qp-decode
%{_bindir}/qp-encode
%{_infodir}/*%{ext_info}
%{_datadir}/emacs/*%{_sysconfdir}/vm/pixmaps
%dir %{_datadir}/emacs/*%{_sysconfdir}/vm
%exclude %{_datadir}/emacs/*%{_sysconfdir}/vm/README
%exclude %{_datadir}/emacs/*%{_sysconfdir}/vm/CHANGES
%exclude %{_datadir}/emacs/*%{_sysconfdir}/vm/COPYING
%exclude %{_datadir}/emacs/*%{_sysconfdir}/vm/NEWS
%exclude %{_datadir}/emacs/*%{_sysconfdir}/vm/TODO

%changelog
