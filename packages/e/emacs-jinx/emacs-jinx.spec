#
# spec file for package emacs-jinx
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2023 Björn Bidar
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


%global _name    jinx

Name:           emacs-%{_name}
Version:        1.8
Release:        0
Summary:        Enchanted Spell Checker for Emacs
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://github.com/minad/jinx
Source0:        %{_name}-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM Only export necessary sumbols in dynamic mod PR 106
Patch1:         0001-Only-export-necessary-symbols.-Fixes-105.patch
# PATCH-FEATURE-UPSTREAM install targets PR 102
Patch2:         0002-Add-makefile-to-build-and-install-jinx.patch
BuildRequires:  emacs-compat
BuildRequires:  emacs-devel
BuildRequires:  emacs-nox
BuildRequires:  make
BuildRequires:  pkgconfig(enchant-2)
Requires:       emacs
Requires:       emacs-compat
Supplements:    emacs

%description
Jinx is a fast just-in-time spell-checker for Emacs.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%make_build

%install
%make_install DYNMODDRIR=%{_emacs_archsitelispdir}

%files
%doc README.org CHANGELOG.org
%license LICENSE
%{_emacs_sitelispdir}/%{_name}.el*
%{_emacs_sitelispdir}/%{_name}-autoloads.el
%dir %{_libdir}/emacs
%dir %{_libdir}/emacs/site-lisp/
%{_emacs_archsitelispdir}/%{_name}-mod.so

%changelog
