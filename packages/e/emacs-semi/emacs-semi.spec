#
# spec file for package emacs-semi
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


Name:           emacs-semi
BuildRequires:  emacs-nox
BuildRequires:  flim
Requires:       emacs
Requires:       flim
Version:        1.14.6
Release:        0
Url:            http://git.chise.org/elisp/semi/
Source0:        semi-%{version}.tar.bz2
Patch0:         autoloads.patch
Patch1:         mime-hide-buttons-in-reply.diff
Summary:        Library to provide MIME feature for GNU Emacs
License:        GPL-2.0-or-later
Group:          Productivity/Editors/Emacs
Provides:       semi-emacs
Obsoletes:      semi-emacs
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
SEMI is a library to provide MIME feature for GNU Emacs.  MIME is a
proposed internet standard for including content and headers other than
(ASCII) plain text in messages

%prep
%setup -q -n semi-%{version}
%patch0 -p1
%patch1 -p1
# necessary to generate the auto-autoloads.el file:
touch *.el

%build
%define emacs_package_dir /usr/share/emacs/site-lisp/
make LISPDIR=%{emacs_package_dir}

%install
mkdir -p $RPM_BUILD_ROOT%{emacs_package_dir}/semi
make install LISPDIR=$RPM_BUILD_ROOT%{emacs_package_dir}

%files 
%defattr(-,root,root)
%doc NEWS README* ChangeLog SEMI* TODO VERSION
%{emacs_package_dir}/*

%changelog
