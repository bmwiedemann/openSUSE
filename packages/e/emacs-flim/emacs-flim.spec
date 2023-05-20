#
# spec file for package emacs-flim
#
# Copyright (c) 2022 SUSE LLC
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


Name:           emacs-flim
Version:        1.14.9+136+g2cf5a78
Release:        0
Summary:        An Emacs Library for MIME
License:        GPL-2.0-or-later
Group:          Productivity/Editors/Emacs
URL:            https://github.com/wanderlust/flim
Source:         flim-%{version}.tar.gz
Patch:          flim-encoding-fix.diff
BuildRequires:  emacs-apel >= 10.7
BuildRequires:  emacs-nox
Requires:       emacs
Requires:       emacs-apel
Requires:       emacs_program
Provides:       flim = %{version}
Requires:       emacs_program
Obsoletes:      flim <= %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
For coding and decoding MIME messages.

%prep
%setup -q -n flim-%{version}
%patch

%build
make %{?_smp_mflags} EMACS=emacs \
  PREFIX=%{_prefix} \
  PACKAGE_LISPDIR=NONE \
  VERSION_SPECIFIC_LISPDIR=%{_datadir}/emacs/site-lisp/emu

%install
make install EMACS=emacs  \
  PREFIX=%{buildroot}%{_prefix} \
  PACKAGE_LISPDIR=NONE \
  VERSION_SPECIFIC_LISPDIR=%{_datadir}/emacs/site-lisp/emu
# make install.man
# Already part of Emacs
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/flim/smtpmail.el*
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/flim/sha1.el*
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/flim/hex-util.el*
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/flim/md4.el*
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/flim/hmac-def.el*
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/flim/hmac-md5.el*
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/flim/sasl.el*
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/flim/sasl-cram.el*
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/flim/sasl-digest.el*
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/flim/sasl-ntlm.el*
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/flim/ntlm.el*

%files
%defattr(-,root,root)
%doc README.en README.ja ChangeLog.1 NEWS
%{_datadir}/emacs/site-lisp/flim

%changelog
