#
# spec file for package emacs-semi
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


Name:           emacs-semi
Version:        1.14.6+239+gb1c245b81715
Release:        0
Summary:        Library to provide MIME feature for GNU Emacs
License:        GPL-2.0-or-later
Group:          Productivity/Editors/Emacs
URL:            https://github.com/wanderlust/semi
Source0:        semi-%{version}.tar.gz
BuildRequires:  emacs-flim
BuildRequires:  emacs-nox
Requires:       emacs
Requires:       emacs-flim
Requires:       emacs_program
Provides:       semi-emacs = %{version}
Obsoletes:      semi-emacs < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
SEMI is a library to provide MIME feature for GNU Emacs.  MIME is a
proposed internet standard for including content and headers other than
(ASCII) plain text in messages

%prep
%setup -q -n semi-%{version}

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

%files
%defattr(-,root,root)
%doc NEWS README* ChangeLog.1 TODO VERSION
%{_datadir}/emacs/site-lisp/semi

%changelog
