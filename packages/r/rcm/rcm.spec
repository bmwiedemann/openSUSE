#
# spec file for package rcm
#
# Copyright (c) 2023 SUSE LLC
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
Name:           rcm
Version:        1.3.6
Release:        0
Summary:        An rc file (dotfile) management tool
License:        BSD-3-Clause
Group:          Productivity/File utilities
URL:            https://thoughtbot.github.io/rcm/
Source0:        https://thoughtbot.github.io/rcm/dist/%{name}-%{version}.tar.gz
Requires:       bash
BuildArch:      noarch

%description
The rcm suite of tools is for managing dotfiles directories. This is a
directory containing all the .*rc files in your home directory (.zshrc,
.vimrc, and so on). These files have gone by many names in history,
such as “rc files” because they typically end in rc or “dotfiles”
because they begin with a period.

%prep
%setup -q

%build
%configure

%install
%make_install

mkdir -p '%{buildroot}/%{_docdir}/%{name}'
cp -a LICENSE README.md NEWS.md '%{buildroot}/%{_docdir}/%{name}'

%files
%{_bindir}/*

%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*

%{_datadir}/rcm/

%{_docdir}/%{name}

%changelog
